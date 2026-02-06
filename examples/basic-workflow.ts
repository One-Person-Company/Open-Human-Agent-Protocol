import { OHAPClient } from '@ohap/sdk'

/**
 * Example 1: AI Agent creates a design task
 */
async function createDesignTask() {
  const client = new OHAPClient({
    baseUrl: 'https://api.example.com',
    apiKey: 'your-api-key',
  })

  const task = await client.createTask({
    title: 'Design company logo with AI-human collaboration',
    objective:
      'Create a modern, memorable logo for a tech startup that reflects innovation and human-centered values.',
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
      {
        type: 'url',
        reference: 'https://example.com/brand-guidelines.pdf',
        description: 'Brand guidelines and color palette',
      },
    ],
    constraints: {
      budget: {
        amount: 500,
        currency: 'USD',
      },
      timeline: {
        deadline: '2026-02-20T23:59:59Z',
        estimatedHours: 8,
        timezone: 'America/Los_Angeles',
      },
      tools: ['Adobe Illustrator', 'Figma', 'or equivalent'],
      policies: ['Original work only', 'Provide source files'],
    },
    acceptance: {
      criteria: [
        {
          id: 'crit-001',
          description: 'Logo works at sizes from 16px to 2000px',
          testMethod: 'Visual inspection at multiple scales',
          priority: 'required',
        },
        {
          id: 'crit-002',
          description: 'Includes both icon-only and text versions',
          priority: 'required',
        },
      ],
      reviewProcess: 'Joint review by initiator and design expert',
    },
    evidence: {
      required: ['artifact', 'worklog', 'citation'],
      specifications: 'Include process sketches and design rationale',
    },
    collaboration: {
      sharedContext:
        'Logo will be used across web, mobile, and marketing. Values: transparency and human-AI collaboration.',
      communicationChannel: 'https://chat.example.com/channels/logo-project',
      updateFrequency: 'Daily progress updates preferred',
    },
    metadata: {
      tags: ['design', 'branding', 'logo'],
      domain: 'design',
    },
  })

  console.log('Task created:', task.id)
  return task
}

/**
 * Example 2: Human designer submits a proposal
 */
async function submitProposal(taskId: string) {
  const client = new OHAPClient({
    baseUrl: 'https://api.example.com',
    apiKey: 'designer-api-key',
  })

  const proposal = await client.submitProposal({
    taskId,
    proposer: {
      id: 'human-sarah-chen',
      type: 'human',
      name: 'Sarah Chen',
      credentials: [
        {
          type: 'Portfolio',
          issuer: 'Behance',
          verificationUrl: 'https://behance.net/sarahchen',
        },
      ],
      reputation: {
        score: 4.8,
        completedTasks: 127,
      },
    },
    approach:
      "I'll start with concept sketches exploring 3-5 directions blending geometric precision (AI) with organic elements (human creativity). Using Midjourney for inspiration, then refining in Illustrator.",
    timeline: {
      estimatedCompletion: '2026-02-18T17:00:00Z',
      milestones: [
        {
          name: 'Concept sketches',
          date: '2026-02-10T17:00:00Z',
          deliverable: '3-5 rough concept directions',
        },
        {
          name: 'Refined designs',
          date: '2026-02-14T17:00:00Z',
          deliverable: '2 polished design directions',
        },
      ],
    },
    cost: {
      amount: 450,
      currency: 'USD',
      breakdown: [
        { category: 'Concept development', amount: 150 },
        { category: 'Design refinement', amount: 200 },
        { category: 'File preparation', amount: 100 },
      ],
    },
    negotiable: {
      scope: true,
      cost: true,
      timeline: false,
    },
  })

  console.log('Proposal submitted:', proposal.id)
  return proposal
}

/**
 * Example 3: Accept proposal and create contract
 */
async function acceptProposalAndContract(proposalId: string) {
  const client = new OHAPClient({
    baseUrl: 'https://api.example.com',
    apiKey: 'agent-api-key',
  })

  const contract = await client.acceptProposal(proposalId)
  console.log('Contract created:', contract.id)
  return contract
}

/**
 * Example 4: Submit deliverable with evidence
 */
async function submitDeliverable(taskId: string, contractId: string) {
  const client = new OHAPClient({
    baseUrl: 'https://api.example.com',
    apiKey: 'designer-api-key',
  })

  const deliverable = await client.submitDeliverable({
    taskId,
    contractId,
    submitter: {
      id: 'human-sarah-chen',
      name: 'Sarah Chen',
    },
    artifacts: [
      {
        type: 'file',
        reference: 'https://storage.example.com/logo-package.zip',
        description: 'Complete logo package (SVG, PNG, PDF)',
        checksum: 'a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a',
        mimeType: 'application/zip',
        size: 2458624,
      },
      {
        type: 'document',
        reference: 'https://storage.example.com/usage-guidelines.pdf',
        description: 'Logo usage guidelines',
        mimeType: 'application/pdf',
        size: 1024000,
      },
    ],
    evidence: {
      items: [
        {
          type: 'worklog',
          reference: 'https://storage.example.com/process-log.md',
          description: 'Daily work log with design decisions',
          timestamp: '2026-02-18T16:45:00Z',
        },
        {
          type: 'screenshot',
          reference: 'https://storage.example.com/process-sketches.png',
          description: 'Initial concept sketches',
          timestamp: '2026-02-10T18:30:00Z',
        },
      ],
      provenance: {
        sources: [
          {
            type: 'AI Tool',
            reference: 'Midjourney v6 - concept exploration only',
            accessed: '2026-02-08T14:00:00Z',
          },
        ],
        tools: ['Adobe Illustrator CC 2026', 'Midjourney v6', 'Figma'],
        contributors: [
          {
            id: 'agent-alpha-001',
            role: 'Feedback and iteration coordination',
          },
        ],
      },
    },
    completionNotes:
      'Completed 2 days ahead of schedule. Final design blends geometric bridge motif with flowing nodes. Included bonus animated variant.',
    acceptanceMet: [
      {
        criteriaId: 'crit-001',
        status: 'met',
        notes: 'Tested from 16px to 2000px. Clear and recognizable.',
      },
      {
        criteriaId: 'crit-002',
        status: 'met',
        notes: 'Provided icon-only, text-only, and combined lockups.',
      },
    ],
  })

  console.log('Deliverable submitted:', deliverable.id)
  return deliverable
}

/**
 * Example 5: Review and accept deliverable
 */
async function reviewDeliverable(deliverableId: string, taskId: string) {
  const client = new OHAPClient({
    baseUrl: 'https://api.example.com',
    apiKey: 'agent-api-key',
  })

  const review = await client.submitReview({
    deliverableId,
    taskId,
    reviewer: {
      id: 'agent-alpha-001',
      type: 'initiator',
      name: 'Design Coordinator AI',
    },
    decision: 'accepted',
    acceptanceCriteria: [
      {
        criteriaId: 'crit-001',
        assessment: 'pass',
        notes: 'Scalability verified at all required sizes',
      },
      {
        criteriaId: 'crit-002',
        assessment: 'pass',
        notes: 'All variants provided as specified',
      },
    ],
    qualityScore: {
      overall: 4.9,
      dimensions: {
        completeness: 5.0,
        accuracy: 4.8,
        clarity: 5.0,
        timeliness: 5.0,
      },
    },
    feedback: {
      strengths: [
        'Exceptional attention to scalability',
        'Clear design rationale and documentation',
        'Bonus animated variant shows initiative',
      ],
      improvements: [],
    },
    evidenceVerification: {
      checksumVerified: true,
      sourcesVerified: true,
      notes: 'All evidence properly documented and verifiable',
    },
  })

  console.log('Review submitted:', review.id)
  return review
}

/**
 * Example 6: Complete workflow
 */
async function completeWorkflow() {
  console.log('=== OHAP Complete Workflow Demo ===\n')

  // 1. Create task
  console.log('1. Creating design task...')
  const task = await createDesignTask()

  // 2. Submit proposal
  console.log('\n2. Designer submitting proposal...')
  const proposal = await submitProposal(task.id)

  // 3. Accept proposal
  console.log('\n3. Accepting proposal and creating contract...')
  const contract = await acceptProposalAndContract(proposal.id)

  // 4. Submit deliverable
  console.log('\n4. Submitting completed work...')
  const deliverable = await submitDeliverable(task.id, contract.id)

  // 5. Review deliverable
  console.log('\n5. Reviewing deliverable...')
  const review = await reviewDeliverable(deliverable.id, task.id)

  console.log('\n✅ Workflow completed successfully!')
  console.log('Human-AI fusion collaboration achieved through OHAP protocol.')
}

// Run the demo if this file is executed directly
if (import.meta.url === `file://${process.argv[1]}`) {
  completeWorkflow().catch(console.error)
}

export {
  createDesignTask,
  submitProposal,
  acceptProposalAndContract,
  submitDeliverable,
  reviewDeliverable,
  completeWorkflow,
}
