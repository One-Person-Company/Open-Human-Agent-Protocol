# 开放人类代理协议（OHAP）提案

[English](README.md) | [中文](README.zh.md)


### 使用 JavaScript SDK

```bash
# 安装 SDK
npm install @ohap/sdk
```

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  apiKey: 'your-api-key',
})

// 创建任务
const task = await client.createTask({
  title: '设计公司Logo',
  objective: '创建现代化的品牌标识',
  initiator: { id: 'agent-001', type: 'agent' },
})

// 提交提案
const proposal = await client.submitProposal({
  taskId: task.id,
  proposer: { id: 'designer-01', type: 'human' },
  approach: '我将创建3-5个设计方向...',
})
```

详见 [SDK.md](SDK.md) 获取完整 JavaScript SDK 文档。

### 使用 Python SDK

```bash
# 安装 SDK
pip install ohap-sdk
```

```python
import asyncio
from ohap import OHAPClient

async def main():
    async with OHAPClient(
        base_url='https://api.ohap.org',
        api_key='your-api-key',
    ) as client:
        # 创建任务
        task = await client.create_task({
            'title': '设计公司Logo',
            'objective': '创建现代化的品牌标识',
            'initiator': {'id': 'agent-001', 'type': 'agent'},
        })
        
        # 提交提案
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {'id': 'designer-01', 'type': 'human'},
            'approach': '我将创建3-5个设计方向...',
        })

asyncio.run(main())
```

详见 [PYTHON-SDK.md](PYTHON-SDK.md) 获取完整 Python SDK 文档。

## 摘要
开放人类代理协议（OHAP）定义了一种协作式协议，让人类与 AI 形成融合体的生产系统。OHAP 将人类的能力融合进工作流程，把共同意图、上下文与责任写入协作流程，AI负责协调异步工作。该协议规定角色、消息格式、任务生命周期与证据要求，使协作能够被发现、签约、交付并审计。OHAP 面向 OPC（One Person Company，一人公司）时代，帮助个人与小团队把AI与人类专长融合为一个可互操作的能力。

## 问题陈述
AI 擅长速度与规模，人类擅长判断、创造与上下文理解。但现实中的人机协作仍是临时性的：邮件、聊天、零散外包流程，缺乏清晰意图、可追踪性与可审计性。这限制了人类在协作中的参与深度，也阻碍了可靠的人机融合工作流。

## 目标
- 以共同意图与主体性为中心，实现人机共创。
- 标准化一种最小且可组合的协作协议。
- 支持异步协作，并具备清晰的状态流转与责任边界。
- 通过证据与审查产物实现可验证的结果。
- 支持跨平台、跨供应商的市场互操作。

## 非目标
- 替代现有招聘平台或支付体系。
- 直接定义法律合同；OHAP 仅提供技术原语。
- 强制单一 UX；多种客户端与市场均可实现。

## 核心原则
- 主体性：人类作为共创者主动参与决策与执行。
- 清晰：每个任务都有明确范围、约束与验收标准。
- 共担：贡献、上下文与责任可见且可追溯。
- 异步：人类按自己的节奏响应，AI基于阶段性更新推进。
- 可验证：交付物包含证据、溯源与审查元数据。
- 关怀：保护人类福祉、隐私与选择权。

## 角色与责任
- 发起方（代理或人类）：定义共同意图、提供上下文、承担责任。
- 人类伙伴：完成工作，提交交付物与证据，并可协商范围。
- 经纪人（可选）：匹配任务与人类，管理政策与定价。
- 审计者（可选）：审查证据、处理争议、评价质量。

## 协议概览
### 实体
- Task：包含元数据、输入、约束与输出的共享工作单元。
- Proposal：人类或经纪人的执行报价。
- Contract：被接受的提案与条款。
- Deliverable：输出工件、证据与完成元数据。
- Review：验证报告、通过/拒绝及理由。

### 任务生命周期
1. Draft：发起方编写任务范围与验收标准。
2. Offer：人类或经纪人提交报价（成本、周期、方法）。
3. Contract：发起方接受提案，条款生效。
4. In-Progress：执行中，提交状态更新与阶段性成果。
5. Delivered：提交最终交付物与证据。
6. Reviewed：通过、拒绝或要求修改，并给出理由。
7. Closed：归档任务与审计日志及评分。

## 最小任务结构（概念）
- id：任务唯一标识。
- title：简短名称。
- objective：目标描述。
- inputs：文件、链接或数据引用。
- constraints：预算、时间、工具与政策限制。
- acceptance：明确的验收标准与测试方法。
- evidence：所需证据类型（截图、日志、引用、校验和）。
- timeline：截止时间、里程碑、时区。
- privacy：数据处理与脱敏要求。

### JSON Schema 定义
完整的 JSON Schema 定义位于 [schema/](schema/) 目录，包括：
- [task.schema.json](schema/task.schema.json) - 任务定义
- [proposal.schema.json](schema/proposal.schema.json) - 提案定义
- [contract.schema.json](schema/contract.schema.json) - 合约定义
- [deliverable.schema.json](schema/deliverable.schema.json) - 交付物定义
- [review.schema.json](schema/review.schema.json) - 审查定义

详见 [schema/README.md](schema/README.md) 了解使用方法、验证和代码生成。

## 证据与验证
OHAP 要求对影响正确性或安全性的声明提供证据，包括：
- 工作日志或时间片记录。
- 工件哈希或签名文件。
- 可追溯引用与快照。
- 审查者签名与结构化反馈。

## 安全、隐私与伦理
- 敏感数据应最小化、脱敏或托管。
- 涉及个人数据的任务需明确同意与政策。
- 高风险或有害任务需额外审查与保护。
- 人类伙伴享有任务选择权与协商权。

## 治理与扩展
OHAP 定义核心规范与扩展点：
- 领域任务类型（设计、法律、研究、QA）。
- 市场政策（定价、托管、声誉）。
- 安全配置（加密、访问控制、审计深度）。

## 采用路径
1. ✅ 发布开放 JSON Schema 与参考文档（已完成，见 [schema/](schema/)）。
2. ✅ 提供代理与市场的 SDK（已完成，见 [SDK.md](SDK.md)、[PYTHON-SDK.md](PYTHON-SDK.md) 和 [src/](src/)）。
3. 发布参考经纪人并提供示例任务。
4. 组建社区评审委员会管理规范演进。

## 路线图（简版）
- v0.1：最小结构、任务生命周期与证据要求。
- v0.2：审查/审计扩展与争议处理。
- v0.3：互操作测试套件与认证清单。

## 行动呼吁
欢迎开发者、研究者与协作者贡献示例、提出扩展并试点集成。OHAP 旨在建立人机融合的协作基础设施，让人类关键领域发挥核心价值。
