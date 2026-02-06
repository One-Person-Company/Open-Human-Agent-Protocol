# OHAP SDK Examples

Examples demonstrating how to use the OHAP JavaScript/TypeScript SDK.

## Prerequisites

```bash
npm install @ohap/sdk
```

## Examples

### Basic Workflow

[basic-workflow.ts](basic-workflow.ts) - Complete end-to-end workflow demonstrating:

1. **Create Task** - AI agent creates a collaborative design task
2. **Submit Proposal** - Human designer proposes approach and pricing
3. **Accept & Contract** - Initiator accepts proposal, creating a binding contract
4. **Submit Deliverable** - Human submits completed work with evidence
5. **Review** - Initiator reviews and accepts the deliverable

Run the complete workflow:

```bash
npm install
npx tsx examples/basic-workflow.ts
```

### Quick Start: Create a Task

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.example.com',
  apiKey: 'your-api-key',
})

const task = await client.createTask({
  title: 'Research market trends in AI collaboration',
  objective: 'Analyze current trends and provide actionable insights',
  initiator: {
    id: 'agent-001',
    type: 'agent',
    name: 'Research Coordinator',
  },
  constraints: {
    budget: { amount: 200, currency: 'USD' },
    timeline: { deadline: '2026-03-01T00:00:00Z' },
  },
  acceptance: {
    criteria: [
      {
        description: 'Comprehensive report with data sources',
        priority: 'required',
      },
    ],
  },
})

console.log('Task created:', task.id)
```

### Quick Start: Submit Proposal

```typescript
const proposal = await client.submitProposal({
  taskId: task.id,
  proposer: {
    id: 'human-researcher-01',
    type: 'human',
    name: 'Emma Wilson',
  },
  approach: 'I will conduct primary research across 3 market segments...',
  timeline: {
    estimatedCompletion: '2026-02-28T17:00:00Z',
  },
  cost: {
    amount: 180,
    currency: 'USD',
  },
})
```

### Quick Start: Submit Deliverable

```typescript
const deliverable = await client.submitDeliverable({
  taskId: task.id,
  contractId: contract.id,
  submitter: { id: 'human-researcher-01', name: 'Emma Wilson' },
  artifacts: [
    {
      type: 'document',
      reference: 'https://storage.example.com/research-report.pdf',
      description: 'Market trends analysis report',
    },
  ],
  evidence: {
    items: [
      {
        type: 'citation',
        reference: 'https://storage.example.com/sources.md',
        description: 'All data sources with citations',
      },
    ],
  },
})
```

## Key Concepts

### Human-AI Fusion

OHAP emphasizes collaboration as a fusion system:

- **Shared Intent**: Both humans and AI contribute to defining goals
- **Mutual Responsibility**: Clear accountability on both sides
- **Verifiable Outcomes**: Evidence and provenance for trust

### Asynchronous Coordination

Humans work at their own pace while AI coordinates:

```typescript
// AI monitors progress
const task = await client.getTask(taskId)
console.log('Current status:', task.status)

// Human submits partial update
await client.updateTask(taskId, {
  status: 'in-progress',
  // Partial results can be attached
})
```

### Evidence & Provenance

All deliverables require evidence:

```typescript
evidence: {
  items: [
    { type: 'worklog', reference: 'daily-notes.md' },
    { type: 'citation', reference: 'sources.bib' },
  ],
  provenance: {
    tools: ['GPT-4 for research', 'Manual analysis'],
    contributors: [{ id: 'ai-assistant', role: 'Data gathering' }],
  },
}
```

## More Examples Coming Soon

- Multi-step research collaboration
- Code review workflow
- Content creation with fact-checking
- Legal document analysis

## Contributing

Have a great use case? Submit a PR with your example!

See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.
