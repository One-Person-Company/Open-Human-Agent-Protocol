---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "Open Human Agent Protocol"
  text: "The foundational protocol for the OPC era. Standardizing how AI and humans collaborate asynchronously, structurally, and verifiably through fusion workflows."
  tagline: "Building collaborative infrastructure for human-AI fusion"
  actions:
    - theme: brand
      text: Get Started
      link: /markdown-examples
    - theme: alt
      text: API Reference
      link: /api-examples

features:
  - title: Human-AI Fusion
    details: Centered on shared intent and agency, enabling humans and AI to operate as a fused production system.
  - title: Verifiable Delivery
    details: Evidence and review mechanisms ensure trustworthy and traceable outcomes.
  - title: Cross-Platform Interoperability
    details: Standardized interfaces enable collaboration across markets, agents, and tools.
  - title: JavaScript/TypeScript SDK
    details: Build OHAP workflows with Node.js, browsers, and TypeScript with full type safety.
  - title: Python SDK
    details: Async and sync Python bindings for seamless integration into Python applications.
  - title: Open JSON Schemas
    details: Complete protocol definitions in JSON Schema Draft-07 for validation and code generation.
---

## Quick SDK Examples

### JavaScript (Async/Await)

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  apiKey: 'your-api-key',
})

// Create a task
const task = await client.createTask({
  title: 'Design company logo',
  objective: 'Create modern brand identity',
  initiator: { id: 'ai-design-001', type: 'agent' },
})

// Submit a proposal
const proposal = await client.submitProposal({
  taskId: task.id,
  proposer: { id: 'designer-01', type: 'human' },
  approach: 'I will create 3-5 design directions...',
})
```

### Python (Async)

```python
import asyncio
from ohap import OHAPClient

async def main():
    async with OHAPClient(
        base_url='https://api.ohap.org',
        api_key='your-api-key',
    ) as client:
        # Create a task
        task = await client.create_task({
            'title': 'Design company logo',
            'objective': 'Create modern brand identity',
            'initiator': {'id': 'ai-design-001', 'type': 'agent'},
        })
        
        # Submit a proposal
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {'id': 'designer-01', 'type': 'human'},
            'approach': 'I will create 3-5 design directions...',
        })

asyncio.run(main())
```
