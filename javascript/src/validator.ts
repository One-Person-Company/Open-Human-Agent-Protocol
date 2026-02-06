import type { Task, Proposal, Deliverable, Review } from './types'

/**
 * Basic JSON Schema validation
 * In production, use a proper JSON Schema validator like Ajv
 */

export function validateTask(task: Task): void {
  if (!task.id || typeof task.id !== 'string') {
    throw new Error('Task must have a valid id')
  }
  if (!task.title || task.title.length < 3) {
    throw new Error('Task title must be at least 3 characters')
  }
  if (!task.objective || task.objective.length < 10) {
    throw new Error('Task objective must be at least 10 characters')
  }
  if (!task.initiator || !task.initiator.id) {
    throw new Error('Task must have a valid initiator')
  }
}

export function validateProposal(proposal: Proposal): void {
  if (!proposal.id || typeof proposal.id !== 'string') {
    throw new Error('Proposal must have a valid id')
  }
  if (!proposal.taskId) {
    throw new Error('Proposal must reference a task')
  }
  if (!proposal.proposer || !proposal.proposer.id) {
    throw new Error('Proposal must have a valid proposer')
  }
  if (!proposal.approach || proposal.approach.length < 20) {
    throw new Error('Proposal approach must be at least 20 characters')
  }
  if (!proposal.timeline || !proposal.timeline.estimatedCompletion) {
    throw new Error('Proposal must have an estimated completion date')
  }
}

export function validateDeliverable(deliverable: Deliverable): void {
  if (!deliverable.id || typeof deliverable.id !== 'string') {
    throw new Error('Deliverable must have a valid id')
  }
  if (!deliverable.taskId) {
    throw new Error('Deliverable must reference a task')
  }
  if (!deliverable.contractId) {
    throw new Error('Deliverable must reference a contract')
  }
  if (!deliverable.submitter || !deliverable.submitter.id) {
    throw new Error('Deliverable must have a valid submitter')
  }
  if (!deliverable.artifacts || deliverable.artifacts.length === 0) {
    throw new Error('Deliverable must have at least one artifact')
  }
  if (!deliverable.evidence || !deliverable.evidence.items || deliverable.evidence.items.length === 0) {
    throw new Error('Deliverable must have at least one evidence item')
  }
}

export function validateReview(review: Review): void {
  if (!review.id || typeof review.id !== 'string') {
    throw new Error('Review must have a valid id')
  }
  if (!review.deliverableId) {
    throw new Error('Review must reference a deliverable')
  }
  if (!review.reviewer || !review.reviewer.id) {
    throw new Error('Review must have a valid reviewer')
  }
  if (!review.decision) {
    throw new Error('Review must have a decision')
  }
}
