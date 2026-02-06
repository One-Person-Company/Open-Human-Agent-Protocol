# JavaScript/TypeScript SDK

Open Human Agent Protocol 官方 JavaScript SDK。

## 安装

```bash
npm install @ohap/sdk
```

## 快速开始

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  apiKey: 'your-api-key',
})

// 创建任务
const task = await client.createTask({
  title: '设计公司 Logo',
  objective: '创建现代化品牌标识',
  initiator: { id: 'agent-001', type: 'agent' },
})

console.log(`任务已创建: ${task.id}`)

// 提交提案
const proposal = await client.submitProposal({
  taskId: task.id,
  proposer: { id: 'designer-01', type: 'human' },
  approach: '我将创建 3-5 个设计方向...',
})

console.log(`提案已提交: ${proposal.id}`)
```

## 特性

- ✅ **完整 TypeScript 支持** - 完整的类型定义
- ✅ **Async/Await** - 原生 Promise API
- ✅ **Schema 验证** - 内置验证
- ✅ **多运行时** - Node.js、Bun、Deno、浏览器
- ✅ **浏览器兼容** - 包含 UMD 构建
- ✅ **LangChain 集成** - 将 OHAP 封装为工具接入智能体工作流

## LangChain 集成

### 安装

```bash
npm install @langchain/core @langchain/openai zod
```

### 示例

```typescript
import { OHAPClient } from '@ohap/sdk'
import { ChatOpenAI } from '@langchain/openai'
import { tool } from '@langchain/core/tools'
import { z } from 'zod'

const ohap = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  apiKey: process.env.OHAP_API_KEY,
})

const tools = ohap.toLangChainTools(tool, {
  schema: {
    createTask: z.object({
      title: z.string(),
      objective: z.string(),
    }),
  },
})

const model = new ChatOpenAI({ model: 'gpt-4o-mini' })
const modelWithTools = model.bindTools(tools)

const response = await modelWithTools.invoke(
  '为金融科技创业公司创建一个极简风格的 Logo 设计任务。'
)

console.log(response)
```

## 核心 API

### OHAPClient 方法

#### 任务管理
- `createTask(data)` - 创建新任务
- `getTask(taskId)` - 获取任务详情
- `updateTask(taskId, data)` - 更新任务
- `listTasks(filters)` - 列表查询任务

#### 提案管理
- `submitProposal(data)` - 提交提案
- `getProposals(taskId)` - 获取任务的提案列表
- `acceptProposal(proposalId)` - 接受提案（创建合约）

#### 合约管理
- `getContract(contractId)` - 获取合约详情
- `updateContract(contractId, data)` - 更新合约

#### 交付物管理
- `submitDeliverable(data)` - 提交交付物及证据
- `getDeliverable(deliverableId)` - 获取交付物详情

#### 审查管理
- `submitReview(data)` - 提交审查与决议
- `getReview(reviewId)` - 获取审查详情

## 完整工作流示例

```typescript
import { OHAPClient } from '@ohap/sdk'

async function logoDesignWorkflow() {
  const client = new OHAPClient({
    baseUrl: 'https://api.ohap.org',
    apiKey: process.env.OHAP_API_KEY,
  })

  // 1. 创建任务
  const task = await client.createTask({
    title: '设计公司 Logo（人机协作）',
    objective: '为科技创业公司创建现代、易记的 Logo',
    initiator: {
      id: 'agent-alpha-001',
      type: 'agent',
      name: 'Design Coordinator AI',
    },
    inputs: [
      {
        type: 'text',
        reference: '公司名: NexaBridge',
        description: '需要融入 Logo 的公司名',
      },
    ],
    constraints: {
      budget: { amount: 500, currency: 'USD' },
      timeline: {
        deadline: '2026-02-20T23:59:59Z',
        estimated_hours: 8,
      },
    },
    acceptance: {
      criteria: [
        {
          description: 'Logo 在 16px 到 2000px 的各个尺寸都能正常显示',
          priority: 'required',
        },
      ],
    },
  })

  console.log(`✅ 任务已创建: ${task.id}`)

  // 2. 提交提案
  const proposal = await client.submitProposal({
    taskId: task.id,
    proposer: {
      id: 'human-sarah-chen',
      type: 'human',
      name: 'Sarah Chen',
    },
    approach: '我将创建 3-5 个概念设计，融合几何精确性与有机元素。',
    timeline: {
      estimated_completion: '2026-02-18T17:00:00Z',
    },
    cost: {
      amount: 450,
      currency: 'USD',
    },
  })

  console.log(`✅ 提案已提交: ${proposal.id}`)

  // 3. 接受提案（创建合约）
  const contract = await client.acceptProposal(proposal.id)

  console.log(`✅ 合约已创建: ${contract.id}`)

  // 4. 提交交付物及证据
  const deliverable = await client.submitDeliverable({
    taskId: task.id,
    contractId: contract.id,
    submitter: { id: 'human-sarah-chen', name: 'Sarah Chen' },
    artifacts: [
      {
        type: 'file',
        reference: 'https://storage.example.com/logo-package.zip',
        description: '完整的 Logo 包',
      },
    ],
    evidence: {
      items: [
        {
          type: 'worklog',
          reference: 'https://storage.example.com/process-log.md',
          description: '包含设计决策的日工作记录',
        },
      ],
      provenance: {
        tools: ['Adobe Illustrator CC 2026', 'Midjourney v6'],
      },
    },
  })

  console.log(`✅ 交付物已提交: ${deliverable.id}`)

  // 5. 提交审查
  const review = await client.submitReview({
    deliverableId: deliverable.id,
    taskId: task.id,
    reviewer: { id: 'agent-alpha-001', type: 'initiator' },
    decision: 'accepted',
    quality_score: {
      overall: 4.9,
      completeness: 5.0,
    },
  })

  console.log(`✅ 审查已提交: ${review.id}`)
  console.log('✅ 完整工作流已完成！')

  return { task, proposal, contract, deliverable, review }
}

// 运行工作流
logoDesignWorkflow().catch(console.error)
```

## 浏览器使用

SDK 可作为 UMD 用于浏览器：

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/@ohap/sdk@0.1.0/dist/ohap.umd.js"></script>
</head>
<body>
  <button onclick="runWorkflow()">启动工作流</button>
  
  <script>
    async function runWorkflow() {
      const client = new OHAP.OHAPClient({
        baseUrl: 'https://api.ohap.org',
        apiKey: 'your-api-key',
      })
      
      const task = await client.createTask({
        title: '设计 Logo',
        objective: '创建现代 Logo',
        initiator: { id: 'agent-001', type: 'agent' },
      })
      
      console.log('任务已创建:', task.id)
    }
  </script>
</body>
</html>
```

## 类型定义

完整的 TypeScript 支持和详细的类型定义：

```typescript
import {
  Task, Proposal, Contract, Deliverable, Review,
  Entity, Input, Constraints, Acceptance, Evidence,
  TaskStatus, ProposalStatus, ContractStatus,
} from '@ohap/sdk'

function processTask(task: Task): void {
  console.log(`处理: ${task.title}`)
}
```

## 错误处理

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
})

try {
  const task = await client.createTask({
    title: '设计 Logo',
    objective: '创建现代 Logo',
    initiator: { id: 'agent-001', type: 'agent' },
  })
} catch (error) {
  if (error instanceof ValidationError) {
    console.error('数据无效:', error.message)
  } else {
    console.error('网络错误:', error)
  }
}
```

## Schema 验证

启用或禁用验证：

```typescript
// 启用验证（默认）
const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  validateSchemas: true,
})

// 禁用以提高性能
const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  validateSchemas: false,
})
```

## 高级用法

### 自定义 HTTP 客户端配置

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  apiKey: 'your-api-key',
  timeout: 30000, // 30 秒
})
```

### 并发操作

```typescript
const [task1, task2, task3] = await Promise.all([
  client.createTask(taskData1),
  client.createTask(taskData2),
  client.createTask(taskData3),
])
```

## 源代码

- [GitHub 仓库](https://github.com/your-org/Open-Human-Agent-Protocol)
- [NPM 包](https://www.npmjs.com/package/@ohap/sdk)

## 许可证

MIT License - 见仓库中的 LICENSE 文件

## 支持

- 📖 [完整文档](../../SDK.md)
- 💬 [GitHub 讨论](https://github.com/your-org/Open-Human-Agent-Protocol/discussions)
- 🐛 [问题跟踪](https://github.com/your-org/Open-Human-Agent-Protocol/issues)
