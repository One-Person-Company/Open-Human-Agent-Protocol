# JavaScript/TypeScript SDK

Official JavaScript SDK for the Open Human Agent Protocol (OHAP).

## Installation

```bash
npm install @ohap/sdk
```

## Quick Start

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
  initiator: { id: 'agent-001', type: 'agent' },
})

console.log(`Task created: ${task.id}`)

// Submit a proposal
const proposal = await client.submitProposal({
  taskId: task.id,
  proposer: { id: 'designer-01', type: 'human' },
  approach: 'I will create 3-5 design directions...',
})

console.log(`Proposal submitted: ${proposal.id}`)
```

## Features

- ✅ **Full TypeScript Support** - Complete type definitions
- ✅ **Async/Await** - Native Promise-based API
- ✅ **Schema Validation** - Built-in validation
- ✅ **Multiple Runtimes** - Node.js, Bun, Deno, browsers
- ✅ **Browser Compatible** - UMD bundle included
- ✅ **LangChain Ready** - Wrap OHAP operations as tools for agent workflows

## LangChain Integration

### Install

```bash
npm install @langchain/core @langchain/openai zod
```

### Example

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
  'Create a task for designing a minimal logo for a fintech startup.'
)

console.log(response)
```

## Core API

### OHAPClient Methods

#### Task Management
- `createTask(data)` - Create a new task
- `getTask(taskId)` - Get task details
- `updateTask(taskId, data)` - Update task
- `listTasks(filters)` - List tasks with filtering

#### Proposal Management
- `submitProposal(data)` - Submit a proposal
- `getProposals(taskId)` - Get proposals for task
- `acceptProposal(proposalId)` - Accept proposal (creates contract)

#### Contract Management
- `getContract(contractId)` - Get contract details
- `updateContract(contractId, data)` - Update contract

#### Deliverable Management
- `submitDeliverable(data)` - Submit work with evidence
- `getDeliverable(deliverableId)` - Get deliverable details

#### Review Management
- `submitReview(data)` - Submit review and decision
- `getReview(reviewId)` - Get review details

## Complete Workflow Example

```typescript
import { OHAPClient } from '@ohap/sdk'

async function logoDesignWorkflow() {
  const client = new OHAPClient({
    baseUrl: 'https://api.ohap.org',
    apiKey: process.env.OHAP_API_KEY,
  })

  // 1. Create a task
  const task = await client.createTask({
    title: 'Design company logo with AI-human collaboration',
    objective: 'Create a modern, memorable logo for a tech startup',
    initiator: {
      id: 'agent-alpha-001',
      type: 'agent',
      name: 'Design Coordinator AI',
    },
    inputs: [
      {
        type: 'text',
        reference: 'Company name: NexaBridge',
        description: 'Company name to incorporate',
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
          description: 'Logo works at sizes from 16px to 2000px',
          priority: 'required',
        },
      ],
    },
  })

  console.log(`✅ Task created: ${task.id}`)

  // 2. Submit proposal
  const proposal = await client.submitProposal({
    taskId: task.id,
    proposer: {
      id: 'human-sarah-chen',
      type: 'human',
      name: 'Sarah Chen',
    },
    approach: 'I will create 3-5 concept directions blending geometric precision with organic elements.',
    timeline: {
      estimated_completion: '2026-02-18T17:00:00Z',
    },
    cost: {
      amount: 450,
      currency: 'USD',
    },
  })

  console.log(`✅ Proposal submitted: ${proposal.id}`)

  // 3. Accept proposal (creates contract)
  const contract = await client.acceptProposal(proposal.id)

  console.log(`✅ Contract created: ${contract.id}`)

  // 4. Submit deliverable with evidence
  const deliverable = await client.submitDeliverable({
    taskId: task.id,
    contractId: contract.id,
    submitter: { id: 'human-sarah-chen', name: 'Sarah Chen' },
    artifacts: [
      {
        type: 'file',
        reference: 'https://storage.example.com/logo-package.zip',
        description: 'Complete logo package',
      },
    ],
    evidence: {
      items: [
        {
          type: 'worklog',
          reference: 'https://storage.example.com/process-log.md',
          description: 'Daily work log with design decisions',
        },
      ],
      provenance: {
        tools: ['Adobe Illustrator CC 2026', 'Midjourney v6'],
      },
    },
  })

  console.log(`✅ Deliverable submitted: ${deliverable.id}`)

  // 5. Submit review
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

  console.log(`✅ Review submitted: ${review.id}`)
  console.log('✅ Complete workflow finished!')

  return { task, proposal, contract, deliverable, review }
}

// Run workflow
logoDesignWorkflow().catch(console.error)
```

## Browser Usage

The SDK is available as UMD for browser usage:

```html
<!DOCTYPE html>
<html>
<head>
  <script src="https://unpkg.com/@ohap/sdk@0.1.0/dist/ohap.umd.js"></script>
</head>
<body>
  <button onclick="runWorkflow()">Start Workflow</button>
  
  <script>
    async function runWorkflow() {
      const client = new OHAP.OHAPClient({
        baseUrl: 'https://api.ohap.org',
        apiKey: 'your-api-key',
      })
      
      const task = await client.createTask({
        title: 'Design logo',
        objective: 'Create modern logo',
        initiator: { id: 'agent-001', type: 'agent' },
      })
      
      console.log('Task created:', task.id)
    }
  </script>
</body>
</html>
```

## Type Definitions

Full TypeScript support with detailed type definitions:

```typescript
import {
  Task, Proposal, Contract, Deliverable, Review,
  Entity, Input, Constraints, Acceptance, Evidence,
  TaskStatus, ProposalStatus, ContractStatus,
} from '@ohap/sdk'

function processTask(task: Task): void {
  console.log(`Processing: ${task.title}`)
}
```

## Error Handling

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
})

try {
  const task = await client.createTask({
    title: 'Design logo',
    objective: 'Create modern logo',
    initiator: { id: 'agent-001', type: 'agent' },
  })
} catch (error) {
  if (error instanceof ValidationError) {
    console.error('Invalid data:', error.message)
  } else {
    console.error('Network error:', error)
  }
}
```

## Schema Validation

Enable or disable validation:

```typescript
// With validation (default)
const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  validateSchemas: true,
})

// Disable for performance
const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  validateSchemas: false,
})
```

## Advanced Usage

### Custom HTTP Client Configuration

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  apiKey: 'your-api-key',
  timeout: 30000, // 30 seconds
})
```

### Concurrent Operations

```typescript
const [task1, task2, task3] = await Promise.all([
  client.createTask(taskData1),
  client.createTask(taskData2),
  client.createTask(taskData3),
])
```

## Source Code

- [GitHub Repository](https://github.com/your-org/Open-Human-Agent-Protocol)
- [NPM Package](https://www.npmjs.com/package/@ohap/sdk)

## License

MIT License - see LICENSE file in repository

## Support

- 📖 [Full Documentation](/sdk)
- 💬 [GitHub Discussions](https://github.com/your-org/Open-Human-Agent-Protocol/discussions)
- 🐛 [Issue Tracker](https://github.com/your-org/Open-Human-Agent-Protocol/issues)
