# Python SDK

Open Human Agent Protocol 官方 Python SDK。

## 安装

```bash
pip install ohap-sdk
```

## 快速开始（异步）

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
            'title': '设计公司 Logo',
            'objective': '创建现代化品牌标识',
            'initiator': {'id': 'agent-001', 'type': 'agent'},
        })
        
        print(f'任务已创建: {task["id"]}')
        
        # 提交提案
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {'id': 'designer-01', 'type': 'human'},
            'approach': '我将创建 3-5 个设计方向...',
        })
        
        print(f'提案已提交: {proposal["id"]}')

asyncio.run(main())
```

## 快速开始（同步）

```python
from ohap import OHAPClientSync

with OHAPClientSync(
    base_url='https://api.ohap.org',
    api_key='your-api-key',
) as client:
    # 创建任务
    task = client.create_task({
        'title': '设计公司 Logo',
        'objective': '创建现代化品牌标识',
        'initiator': {'id': 'agent-001', 'type': 'agent'},
    })
    
    print(f'任务已创建: {task["id"]}')
    
    # 提交提案
    proposal = client.submit_proposal({
        'task_id': task['id'],
        'proposer': {'id': 'designer-01', 'type': 'human'},
        'approach': '我将创建 3-5 个设计方向...',
    })
    
    print(f'提案已提交: {proposal["id"]}')
```

## 特性

- ✅ **异步与同步** - 同时支持 async/await 和同步 API
- ✅ **完整类型提示** - 完整的 Python 类型注解
- ✅ **Schema 验证** - 内置验证
- ✅ **轻量级** - 最小依赖（仅 httpx）
- ✅ **Python 3.8+** - 现代 Python 支持
- ✅ **LangChain 集成** - 将 OHAP 作为工具接入 LangChain 智能体

## LangChain 集成

### 安装

```bash
pip install langchain langchain-openai
```

### 示例

```python
from ohap import OHAPClientSync
from langchain_openai import ChatOpenAI

with OHAPClientSync(
    base_url='https://api.ohap.org',
    api_key='your-api-key',
) as client:
    tools = client.to_langchain_tools()

    model = ChatOpenAI(model='gpt-4o-mini')
    model_with_tools = model.bind_tools(tools)

    response = model_with_tools.invoke(
        '为金融科技创业公司创建一个极简风格的 Logo 设计任务。'
    )
    print(response)
```

## 核心 API

### OHAPClient（异步）/ OHAPClientSync（同步）

#### 任务管理
- `create_task(data)` - 创建新任务
- `get_task(task_id)` - 获取任务详情
- `update_task(task_id, data)` - 更新任务
- `list_tasks(status=None, domain=None)` - 列表查询任务

#### 提案管理
- `submit_proposal(data)` - 提交提案
- `get_proposals(task_id)` - 获取任务的提案列表
- `accept_proposal(proposal_id)` - 接受提案（创建合约）

#### 合约管理
- `get_contract(contract_id)` - 获取合约详情
- `update_contract(contract_id, data)` - 更新合约

#### 交付物管理
- `submit_deliverable(data)` - 提交交付物及证据
- `get_deliverable(deliverable_id)` - 获取交付物详情

#### 审查管理
- `submit_review(data)` - 提交审查与决议
- `get_review(review_id)` - 获取审查详情

## 完整工作流示例（异步）

```python
import asyncio
from ohap import OHAPClient

async def logo_design_workflow():
    async with OHAPClient(
        base_url='https://api.ohap.org',
        api_key='your-api-key',
    ) as client:
        # 1. 创建任务
        task = await client.create_task({
            'title': '设计公司 Logo（人机协作）',
            'objective': '为科技创业公司创建现代、易记的 Logo',
            'initiator': {
                'id': 'agent-alpha-001',
                'type': 'agent',
                'name': 'Design Coordinator AI',
            },
            'inputs': [
                {
                    'type': 'text',
                    'reference': '公司名: NexaBridge',
                    'description': '需要融入 Logo 的公司名',
                },
            ],
            'constraints': {
                'budget': {'amount': 500, 'currency': 'USD'},
                'timeline': {
                    'deadline': '2026-02-20T23:59:59Z',
                    'estimated_hours': 8,
                },
            },
            'acceptance': {
                'criteria': [
                    {
                        'description': 'Logo 在 16px 到 2000px 的各个尺寸都能正常显示',
                        'priority': 'required',
                    },
                ],
            },
        })
        
        print(f'✅ 任务已创建: {task["id"]}')
        
        # 2. 提交提案
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {
                'id': 'human-sarah-chen',
                'type': 'human',
                'name': 'Sarah Chen',
            },
            'approach': '我将创建 3-5 个概念设计，融合几何精确性与有机元素。',
            'timeline': {
                'estimated_completion': '2026-02-18T17:00:00Z',
            },
            'cost': {
                'amount': 450,
                'currency': 'USD',
            },
        })
        
        print(f'✅ 提案已提交: {proposal["id"]}')
        
        # 3. 接受提案（创建合约）
        contract = await client.accept_proposal(proposal['id'])
        
        print(f'✅ 合约已创建: {contract["id"]}')
        
        # 4. 提交交付物及证据
        deliverable = await client.submit_deliverable({
            'task_id': task['id'],
            'contract_id': contract['id'],
            'submitter': {'id': 'human-sarah-chen', 'name': 'Sarah Chen'},
            'artifacts': [
                {
                    'type': 'file',
                    'reference': 'https://storage.example.com/logo-package.zip',
                    'description': '完整的 Logo 包',
                },
            ],
            'evidence': {
                'items': [
                    {
                        'type': 'worklog',
                        'reference': 'https://storage.example.com/process-log.md',
                        'description': '包含设计决策的日工作记录',
                    },
                ],
                'provenance': {
                    'tools': ['Adobe Illustrator CC 2026', 'Midjourney v6'],
                },
            },
        })
        
        print(f'✅ 交付物已提交: {deliverable["id"]}')
        
        # 5. 提交审查
        review = await client.submit_review({
            'deliverable_id': deliverable['id'],
            'task_id': task['id'],
            'reviewer': {'id': 'agent-alpha-001', 'type': 'initiator'},
            'decision': 'accepted',
            'quality_score': {
                'overall': 4.9,
                'completeness': 5.0,
            },
        })
        
        print(f'✅ 审查已提交: {review["id"]}')
        print('✅ 完整工作流已完成！')
        
        return {'task': task, 'proposal': proposal, 'contract': contract, 'deliverable': deliverable, 'review': review}

# 运行工作流
asyncio.run(logo_design_workflow())
```

## 类型提示

使用类型提示获得更好的 IDE 支持：

```python
from typing import List
from ohap import OHAPClient
from ohap.types import Task, Proposal

async def process_tasks(client: OHAPClient) -> List[Task]:
    tasks = await client.list_tasks(status='open')
    return tasks

async def submit_proposals(
    client: OHAPClient,
    task: Task,
    proposer_id: str,
) -> Proposal:
    return await client.submit_proposal({
        'task_id': task['id'],
        'proposer': {'id': proposer_id, 'type': 'human'},
        'approach': '我的提案...',
    })
```

## 错误处理

```python
import asyncio
from ohap import OHAPClient
import httpx

async def safe_operation():
    async with OHAPClient(base_url='https://api.ohap.org') as client:
        try:
            task = await client.create_task({
                'title': '任务',
                'objective': '做工作',
                'initiator': {'id': 'agent-001', 'type': 'agent'},
            })
        except httpx.ConnectError:
            print('连接到 OHAP 服务器失败')
        except httpx.TimeoutException:
            print('请求超时')
        except ValueError as e:
            print(f'数据无效: {e}')

asyncio.run(safe_operation())
```

## Schema 验证

启用或禁用验证：

```python
# 启用验证（默认用于离线使用）
client = OHAPClient(
    base_url='https://api.ohap.org',
    validate_schemas=True,
)

# 禁用以提高性能
client = OHAPClient(
    base_url='https://api.ohap.org',
    validate_schemas=False,
)
```

### 手动验证

```python
from ohap.validator import validate_task, validate_proposal

task_data = {'title': '任务', ...}
errors = validate_task(task_data)
if errors:
    print(f'验证错误: {errors}')
```

## 并发操作

```python
import asyncio
from ohap import OHAPClient

async def create_multiple_tasks():
    async with OHAPClient(base_url='https://api.ohap.org') as client:
        # 并发创建 3 个任务
        tasks = await asyncio.gather(
            client.create_task({'title': '任务 1', 'objective': '...', 'initiator': {...}}),
            client.create_task({'title': '任务 2', 'objective': '...', 'initiator': {...}}),
            client.create_task({'title': '任务 3', 'objective': '...', 'initiator': {...}}),
        )
        return tasks
```

## 测试

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest python/tests/

# 运行覆盖率测试
pytest --cov=ohap python/tests/
```

## 源代码

- [GitHub 仓库](https://github.com/your-org/Open-Human-Agent-Protocol)
- [PyPI 包](https://pypi.org/project/ohap-sdk/)

## 许可证

MIT License - 见仓库中的 LICENSE 文件

## 支持

- 📖 [完整文档](/zh/sdk-python)
- 💬 [GitHub 讨论](https://github.com/your-org/Open-Human-Agent-Protocol/discussions)
- 🐛 [问题跟踪](https://github.com/your-org/Open-Human-Agent-Protocol/issues)
