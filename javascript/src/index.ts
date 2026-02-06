import type {
  Task,
  TaskStatus,
  Proposal,
  ProposalStatus,
  Contract,
  ContractStatus,
  Deliverable,
  DeliverableStatus,
  Review,
  ReviewDecision,
} from './types'
import { validateTask, validateProposal, validateDeliverable, validateReview } from './validator'

export interface OHAPClientOptions {
  baseUrl?: string
  apiKey?: string
  validateSchemas?: boolean
}

export interface LangChainToolFactory {
  <TInput = unknown, TOutput = unknown>(
    fn: (input: TInput) => Promise<TOutput> | TOutput,
    config: {
      name: string
      description: string
      schema?: unknown
    }
  ): unknown
}

export interface LangChainToolOptions {
  initiatorId?: string
  initiatorType?: 'human' | 'agent' | 'system' | 'broker'
  schema?: {
    createTask?: unknown
    submitProposal?: unknown
    submitDeliverable?: unknown
    submitReview?: unknown
  }
}

/**
 * OHAP SDK Client for Human-AI Fusion Workflows
 * 
 * This client provides a programmatic interface for creating, managing,
 * and coordinating human-AI collaborative tasks following the OHAP protocol.
 */
export class OHAPClient {
  private baseUrl: string
  private apiKey?: string
  private validateSchemas: boolean

  constructor(options: OHAPClientOptions = {}) {
    this.baseUrl = options.baseUrl || 'https://api.ohap.org'
    this.apiKey = options.apiKey
    this.validateSchemas = options.validateSchemas ?? true
  }

  /**
   * Create LangChain tools bound to this client.
   */
  toLangChainTools(
    toolFactory: LangChainToolFactory,
    options: LangChainToolOptions = {}
  ): unknown[] {
    const initiatorId = options.initiatorId || 'agent-001'
    const initiatorType = options.initiatorType || 'agent'

    const createTaskTool = toolFactory(
      async ({ title, objective }: { title: string; objective: string }) => {
        const task = await this.createTask({
          title,
          objective,
          initiator: { id: initiatorId, type: initiatorType },
        })
        return { id: task.id, title: task.title }
      },
      {
        name: 'ohap_create_task',
        description: 'Create an OHAP task',
        schema: options.schema?.createTask,
      }
    )

    const submitProposalTool = toolFactory(
      async (
        input: {
          taskId: string
          proposerId: string
          proposerType: 'human' | 'agent' | 'system' | 'broker'
          approach: string
        }
      ) => {
        const proposal = await this.submitProposal({
          taskId: input.taskId,
          proposer: { id: input.proposerId, type: input.proposerType },
          approach: input.approach,
        })
        return { id: proposal.id, taskId: proposal.taskId }
      },
      {
        name: 'ohap_submit_proposal',
        description: 'Submit an OHAP proposal for a task',
        schema: options.schema?.submitProposal,
      }
    )

    const submitDeliverableTool = toolFactory(
      async (
        input: {
          taskId: string
          contractId: string
          submitterId: string
          artifactReference: string
        }
      ) => {
        const deliverable = await this.submitDeliverable({
          taskId: input.taskId,
          contractId: input.contractId,
          submitter: { id: input.submitterId },
          artifacts: [
            { type: 'url', reference: input.artifactReference },
          ],
        })
        return { id: deliverable.id, taskId: deliverable.taskId }
      },
      {
        name: 'ohap_submit_deliverable',
        description: 'Submit an OHAP deliverable for a contract',
        schema: options.schema?.submitDeliverable,
      }
    )

    const submitReviewTool = toolFactory(
      async (
        input: {
          deliverableId: string
          taskId: string
          reviewerId: string
          decision: ReviewDecision
        }
      ) => {
        const review = await this.submitReview({
          deliverableId: input.deliverableId,
          taskId: input.taskId,
          reviewer: { id: input.reviewerId, type: 'initiator' },
          decision: input.decision,
        })
        return { id: review.id, decision: review.decision }
      },
      {
        name: 'ohap_submit_review',
        description: 'Submit an OHAP review for a deliverable',
        schema: options.schema?.submitReview,
      }
    )

    return [
      createTaskTool,
      submitProposalTool,
      submitDeliverableTool,
      submitReviewTool,
    ]
  }

  // ========== Task Management ==========

  /**
   * Create a new collaborative task
   */
  async createTask(task: Partial<Task>): Promise<Task> {
    const fullTask: Task = {
      id: task.id || this.generateId('task'),
      version: '0.1',
      status: 'draft',
      createdAt: new Date().toISOString(),
      ...task,
    } as Task

    if (this.validateSchemas) {
      validateTask(fullTask)
    }

    return this.request<Task>('POST', '/tasks', fullTask)
  }

  /**
   * Get task by ID
   */
  async getTask(taskId: string): Promise<Task> {
    return this.request<Task>('GET', `/tasks/${taskId}`)
  }

  /**
   * Update task status or details
   */
  async updateTask(taskId: string, updates: Partial<Task>): Promise<Task> {
    return this.request<Task>('PATCH', `/tasks/${taskId}`, updates)
  }

  /**
   * List tasks with optional filters
   */
  async listTasks(filters?: {
    status?: TaskStatus
    domain?: string
    initiatorId?: string
  }): Promise<Task[]> {
    const params = new URLSearchParams(filters as Record<string, string>)
    return this.request<Task[]>('GET', `/tasks?${params}`)
  }

  // ========== Proposal Management ==========

  /**
   * Submit a proposal for a task
   */
  async submitProposal(proposal: Partial<Proposal>): Promise<Proposal> {
    const fullProposal: Proposal = {
      id: proposal.id || this.generateId('prop'),
      status: 'submitted',
      createdAt: new Date().toISOString(),
      ...proposal,
    } as Proposal

    if (this.validateSchemas) {
      validateProposal(fullProposal)
    }

    return this.request<Proposal>('POST', '/proposals', fullProposal)
  }

  /**
   * Get proposals for a task
   */
  async getProposals(taskId: string): Promise<Proposal[]> {
    return this.request<Proposal[]>('GET', `/tasks/${taskId}/proposals`)
  }

  /**
   * Accept a proposal and create a contract
   */
  async acceptProposal(proposalId: string): Promise<Contract> {
    return this.request<Contract>('POST', `/proposals/${proposalId}/accept`)
  }

  /**
   * Withdraw or reject a proposal
   */
  async updateProposalStatus(
    proposalId: string,
    status: ProposalStatus
  ): Promise<Proposal> {
    return this.request<Proposal>('PATCH', `/proposals/${proposalId}`, { status })
  }

  // ========== Contract Management ==========

  /**
   * Get contract by ID
   */
  async getContract(contractId: string): Promise<Contract> {
    return this.request<Contract>('GET', `/contracts/${contractId}`)
  }

  /**
   * Update contract status
   */
  async updateContract(
    contractId: string,
    updates: Partial<Contract>
  ): Promise<Contract> {
    return this.request<Contract>('PATCH', `/contracts/${contractId}`, updates)
  }

  // ========== Deliverable Management ==========

  /**
   * Submit deliverable for a contract
   */
  async submitDeliverable(deliverable: Partial<Deliverable>): Promise<Deliverable> {
    const fullDeliverable: Deliverable = {
      id: deliverable.id || this.generateId('deliv'),
      status: 'submitted',
      submittedAt: new Date().toISOString(),
      ...deliverable,
    } as Deliverable

    if (this.validateSchemas) {
      validateDeliverable(fullDeliverable)
    }

    return this.request<Deliverable>('POST', '/deliverables', fullDeliverable)
  }

  /**
   * Get deliverable by ID
   */
  async getDeliverable(deliverableId: string): Promise<Deliverable> {
    return this.request<Deliverable>('GET', `/deliverables/${deliverableId}`)
  }

  // ========== Review Management ==========

  /**
   * Submit a review for a deliverable
   */
  async submitReview(review: Partial<Review>): Promise<Review> {
    const fullReview: Review = {
      id: review.id || this.generateId('rev'),
      reviewedAt: new Date().toISOString(),
      ...review,
    } as Review

    if (this.validateSchemas) {
      validateReview(fullReview)
    }

    return this.request<Review>('POST', '/reviews', fullReview)
  }

  /**
   * Get review by ID
   */
  async getReview(reviewId: string): Promise<Review> {
    return this.request<Review>('GET', `/reviews/${reviewId}`)
  }

  // ========== Utility Methods ==========

  /**
   * Generate a unique ID with prefix
   */
  private generateId(prefix: string): string {
    return `${prefix}-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`
  }

  /**
   * Make HTTP request to OHAP API
   */
  private async request<T>(
    method: string,
    path: string,
    body?: unknown
  ): Promise<T> {
    const url = `${this.baseUrl}${path}`
    const headers: HeadersInit = {
      'Content-Type': 'application/json',
    }

    if (this.apiKey) {
      headers['Authorization'] = `Bearer ${this.apiKey}`
    }

    const response = await fetch(url, {
      method,
      headers,
      body: body ? JSON.stringify(body) : undefined,
    })

    if (!response.ok) {
      throw new Error(`OHAP API error: ${response.status} ${response.statusText}`)
    }

    return response.json()
  }
}

// Export types for convenience
export type {
  Task,
  TaskStatus,
  Proposal,
  ProposalStatus,
  Contract,
  ContractStatus,
  Deliverable,
  DeliverableStatus,
  Review,
  ReviewDecision,
  LangChainToolFactory,
  LangChainToolOptions,
}
