---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "开放人类代理协议"
  text: "面向 OPC 时代的基础协议，标准化 AI 与人类以异步、结构化、可验证的方式融合协作。"
  tagline: "建立人机融合的协作基础设施"
  actions:
    - theme: brand
      text: 快速开始
      link: /zh/markdown-examples
    - theme: alt
      text: API 参考
      link: /zh/api-examples

features:
  - title: 人机融合
    details: 以共同意图与主体性为中心，让人类与 AI 形成融合体的生产系统。
  - title: 可验证交付
    details: 通过证据与审查机制提升结果的可信度与可追溯性。
  - title: 跨平台互操作
    details: 标准化接口让不同市场、代理与工具协同工作。
  - title: JavaScript/TypeScript SDK
    details: 使用 Node.js、浏览器和 TypeScript 构建 OHAP 工作流，具有完整类型安全。
  - title: Python SDK
    details: 异步和同步 Python 绑定，无缝集成到 Python 应用。
  - title: 开放 JSON Schemas
    details: JSON Schema Draft-07 完整协议定义，支持验证和代码生成。
---

## SDK 快速示例

### JavaScript (异步)

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
  initiator: { id: 'ai-design-001', type: 'agent' },
})

// 提交提案
const proposal = await client.submitProposal({
  taskId: task.id,
  proposer: { id: 'designer-01', type: 'human' },
  approach: '我将创建 3-5 个设计方向...',
})
```

### Python (异步)

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
            'initiator': {'id': 'ai-design-001', 'type': 'agent'},
        })
        
        # 提交提案
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {'id': 'designer-01', 'type': 'human'},
            'approach': '我将创建 3-5 个设计方向...',
        })

asyncio.run(main())
```
