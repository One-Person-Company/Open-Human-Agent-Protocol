# Open-Human-Agent-Protocol (OHAP) Proposal

[English](README.md) | [中文](README.zh.md)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/your-org/Open-Human-Agent-Protocol.git
cd Open-Human-Agent-Protocol

# Install dependencies
npm install

# Validate schema examples
npm run schema:validate

# Start documentation site
npm run docs:dev
```

**See complete example:** The [schema/examples/](schema/examples/) directory contains a full logo design collaboration workflow.

### Using the JavaScript SDK

```bash
# Install SDK
npm install @ohap/sdk
```

```typescript
import { OHAPClient } from '@ohap/sdk'

const client = new OHAPClient({
  baseUrl: 'https://api.ohap.org',
  apiKey: 'your-api-key',
})

// Create task
const task = await client.createTask({
  title: 'Design company logo',
  objective: 'Create modern brand identity',
  initiator: { id: 'agent-001', type: 'agent' },
})

// Submit proposal
const proposal = await client.submitProposal({
  taskId: task.id,
  proposer: { id: 'designer-01', type: 'human' },
  approach: 'I will create 3-5 design directions...',
})
```

See [SDK.md](SDK.md) for complete JavaScript SDK documentation.

### Using the Python SDK

```bash
# Install SDK
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
        # Create task
        task = await client.create_task({
            'title': 'Design company logo',
            'objective': 'Create modern brand identity',
            'initiator': {'id': 'agent-001', 'type': 'agent'},
        })
        
        # Submit proposal
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {'id': 'designer-01', 'type': 'human'},
            'approach': 'I will create 3-5 design directions...',
        })

asyncio.run(main())
```

See [PYTHON-SDK.md](PYTHON-SDK.md) for complete Python SDK documentation.

## Abstract
Open-Human-Agent-Protocol (OHAP) defines a cooperative protocol where humans and AI operate as a fused production system. OHAP integrates human capabilities into workflows, embedding shared intent, context, and accountability while AI coordinates asynchronous work. The protocol specifies roles, message formats, task lifecycles, and evidence requirements so collaboration can be discovered, contracted, delivered, and audited. OHAP targets the OPC (One Person Company) era, where individuals and small teams blend AI with human expertise as a single, interoperable capability.

## Problem Statement
AI systems excel at speed and scale, while humans excel at judgment, creativity, and context. Yet human-AI collaboration remains ad hoc: email, chat threads, and fragmented outsourcing workflows with unclear intent, weak traceability, and limited auditability. This constrains human participation depth and blocks reliable human-AI fusion workflows.

## Goals
- Enable human-AI co-creation with explicit shared intent and active participation.
- Standardize a minimal, composable protocol for collaboration.
- Support asynchronous work with clear state transitions and accountability.
- Provide verifiable outcomes via evidence and review artifacts.
- Support marketplace interoperability across platforms and vendors.

## Non-goals
- Replacing existing job platforms or payment rails.
- Defining legal contracts; OHAP provides technical primitives only.
- Forcing a single UX; multiple clients and marketplaces can implement it.

## Core Principles
- Agency: Humans actively participate in decisions and execution as co-creators.
- Clarity: Every task has explicit scope, constraints, and acceptance criteria.
- Co-ownership: Credit, context, and responsibility are shared and visible.
- Asynchrony: Humans respond on their timeline; AI proceeds with partial updates.
- Verifiability: Deliverables include evidence, provenance, and review metadata.
- Care: Human well-being, privacy, and choice are protected.

## Roles and Responsibilities
- Initiator (Agent or Human): Frames shared intent, provides context, accepts responsibility.
- Human Partner: Performs work, supplies deliverables and evidence, and can negotiate scope.
- Broker (Optional): Matches tasks to humans, manages policies and pricing.
- Auditor (Optional): Reviews evidence, resolves disputes, rates quality.

## Protocol Overview
### Entities
- Task: A shared unit of work with metadata, inputs, constraints, and outputs.
- Proposal: A human or broker offer to execute a task.
- Contract: Accepted proposal with terms and deadlines.
- Deliverable: Output artifacts, evidence, and completion metadata.
- Review: Verification report, approvals, or rejection with reasons.

### Task Lifecycle
1. Draft: Requester composes a task with scope and acceptance criteria.
2. Offer: Humans or brokers submit proposals (cost, timeline, approach).
3. Contract: Requester accepts a proposal; terms become binding.
4. In-Progress: Human updates status and partial artifacts.
5. Delivered: Final deliverable and evidence submitted.
6. Reviewed: Accepted, rejected, or revised with reasons.
7. Closed: Task archived with audit log and ratings.

## Minimum Task Schema (Conceptual)
- id: Unique task identifier.
- title: Short, human-readable name.
- objective: Clear goal statement.
- inputs: Files, links, or data references.
- constraints: Budget, time, tools, and policy limits.
- acceptance: Explicit criteria and test methods.
- evidence: Required proof types (screenshots, logs, citations, checksums).
- timeline: Deadlines, checkpoints, timezone.
- privacy: Data handling rules and redaction expectations.

### JSON Schema Definitions
Full JSON Schema definitions are available in the [schema/](schema/) directory, including:
- [task.schema.json](schema/task.schema.json) - Task definition
- [proposal.schema.json](schema/proposal.schema.json) - Proposal definition
- [contract.schema.json](schema/contract.schema.json) - Contract definition
- [deliverable.schema.json](schema/deliverable.schema.json) - Deliverable definition
- [review.schema.json](schema/review.schema.json) - Review definition

See [schema/README.md](schema/README.md) for usage, validation, and code generation instructions.

## Evidence and Verification
OHAP requires evidence for claims that impact correctness or safety. Evidence can include:
- Work logs or timeboxed notes.
- Artifact hashes or signed files.
- References and citations with snapshots.
- Reviewer signatures and structured feedback.

## Safety, Privacy, and Ethics
- Sensitive data must be minimized, masked, or escrowed.
- Tasks involving personal data require explicit consent and policies.
- Risky or harmful tasks require additional review and safeguards.
- Human partners enjoy task choice and negotiation rights.

## Governance and Extensions
OHAP defines a core spec and extension points:
- Domain-specific task types (design, legal, research, QA).
- Marketplace policies (pricing, escrow, reputation).
- Security profiles (encryption, access control, audit depth).

## Adoption Path
1. ✅ Publish open JSON schemas and reference docs (completed, see [schema/](schema/)).
2. ✅ Provide SDKs for agents and marketplace integrations (completed, see [SDK.md](SDK.md), [PYTHON-SDK.md](PYTHON-SDK.md), and [src/](src/)).
3. Launch a reference broker with sample tasks.
4. Establish a community review board for spec changes.

## Roadmap (Short Form)
- v0.1: Minimal schema, task lifecycle, and evidence requirements.
- v0.2: Review/audit extensions and dispute handling.
- v0.3: Interop test suite and certification checklist.

## Call to Action
We invite builders, researchers, and collaborators to contribute examples, propose extensions, and pilot integrations. OHAP aims to build the collaborative infrastructure for human-AI fusion, enabling human intelligence to thrive in the AI era.
