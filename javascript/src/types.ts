// Core entity types based on OHAP JSON Schemas

export type TaskStatus =
  | 'draft'
  | 'open'
  | 'offered'
  | 'contracted'
  | 'in-progress'
  | 'delivered'
  | 'reviewed'
  | 'closed'
  | 'cancelled'

export type ProposalStatus =
  | 'submitted'
  | 'under-review'
  | 'accepted'
  | 'rejected'
  | 'withdrawn'

export type ContractStatus = 'active' | 'completed' | 'cancelled' | 'disputed'

export type DeliverableStatus =
  | 'submitted'
  | 'under-review'
  | 'accepted'
  | 'rejected'
  | 'revision-requested'

export type ReviewDecision = 'accepted' | 'rejected' | 'revision-requested' | 'escalated'

export type EntityType = 'human' | 'agent' | 'system' | 'broker'

export interface Entity {
  id: string
  type: EntityType
  name?: string
  contact?: string
}

export interface Input {
  type: 'file' | 'url' | 'text' | 'data' | 'reference'
  reference: string
  description?: string
  checksum?: string
}

export interface Constraints {
  budget?: {
    amount: number
    currency: string
  }
  timeline?: {
    deadline?: string
    estimatedHours?: number
    timezone?: string
  }
  tools?: string[]
  policies?: string[]
}

export interface AcceptanceCriterion {
  id?: string
  description: string
  testMethod?: string
  priority?: 'required' | 'preferred' | 'optional'
}

export interface Acceptance {
  criteria: AcceptanceCriterion[]
  reviewProcess?: string
}

export interface Evidence {
  required?: Array<'worklog' | 'screenshot' | 'recording' | 'artifact' | 'citation' | 'signature' | 'checksum' | 'other'>
  optional?: string[]
  specifications?: string
}

export interface Privacy {
  dataClassification?: 'public' | 'internal' | 'confidential' | 'restricted'
  consentRequired?: boolean
  redactionRules?: string[]
  retention?: string
}

export interface Collaboration {
  sharedContext?: string
  communicationChannel?: string
  updateFrequency?: string
}

export interface Task {
  id: string
  version: string
  title: string
  objective: string
  status: TaskStatus
  initiator: Entity
  inputs?: Input[]
  constraints?: Constraints
  acceptance?: Acceptance
  evidence?: Evidence
  privacy?: Privacy
  collaboration?: Collaboration
  metadata?: {
    createdAt: string
    updatedAt?: string
    tags?: string[]
    domain?: string
  }
  createdAt: string
}

export interface Credential {
  type: string
  issuer: string
  verificationUrl?: string
}

export interface Reputation {
  score?: number
  completedTasks?: number
}

export interface Proposer extends Entity {
  credentials?: Credential[]
  reputation?: Reputation
}

export interface Milestone {
  name: string
  date: string
  deliverable?: string
}

export interface Timeline {
  estimatedCompletion: string
  milestones?: Milestone[]
}

export interface Cost {
  amount: number
  currency: string
  breakdown?: Array<{
    category: string
    amount: number
  }>
}

export interface Proposal {
  id: string
  taskId: string
  proposer: Proposer
  approach: string
  timeline: Timeline
  cost?: Cost
  negotiable?: {
    scope?: boolean
    timeline?: boolean
    cost?: boolean
  }
  status: ProposalStatus
  createdAt: string
  expiresAt?: string
}

export interface Contract {
  id: string
  taskId: string
  proposalId: string
  initiator: Entity & { signature?: string }
  humanPartner: Entity & { signature?: string }
  terms: {
    scope: string
    timeline: {
      startDate?: string
      deadline: string
      milestones?: Milestone[]
    }
    compensation?: Cost & { paymentSchedule?: string }
    acceptanceCriteria?: AcceptanceCriterion[]
    evidenceRequirements?: string[]
  }
  sharedResponsibilities?: {
    initiatorCommits?: string[]
    humanPartnerCommits?: string[]
    communicationProtocol?: string
  }
  disputeResolution?: {
    method?: 'negotiation' | 'mediation' | 'arbitration' | 'escalation'
    arbitrator?: string
  }
  amendments?: Array<{
    date: string
    description: string
    agreedBy?: string[]
  }>
  status: ContractStatus
  createdAt: string
  completedAt?: string
}

export interface Artifact {
  type: 'file' | 'url' | 'text' | 'code' | 'document' | 'media' | 'other'
  reference: string
  description?: string
  checksum?: string
  mimeType?: string
  size?: number
}

export interface EvidenceItem {
  type: 'worklog' | 'screenshot' | 'recording' | 'citation' | 'signature' | 'checksum' | 'other'
  reference: string
  description?: string
  timestamp?: string
}

export interface Provenance {
  sources?: Array<{
    type: string
    reference: string
    accessed?: string
  }>
  tools?: string[]
  contributors?: Array<{
    id: string
    role: string
  }>
}

export interface Deliverable {
  id: string
  taskId: string
  contractId: string
  submitter: Entity
  artifacts: Artifact[]
  evidence: {
    items: EvidenceItem[]
    provenance?: Provenance
  }
  completionNotes?: string
  acceptanceMet?: Array<{
    criteriaId: string
    status: 'met' | 'partially-met' | 'not-met' | 'not-applicable'
    notes?: string
  }>
  submittedAt: string
  status: DeliverableStatus
}

export interface Review {
  id: string
  deliverableId: string
  taskId?: string
  reviewer: Entity
  decision: ReviewDecision
  acceptanceCriteria?: Array<{
    criteriaId: string
    assessment: 'pass' | 'fail' | 'partial' | 'not-evaluated'
    notes?: string
    evidence?: string[]
  }>
  qualityScore?: {
    overall?: number
    dimensions?: {
      completeness?: number
      accuracy?: number
      clarity?: number
      timeliness?: number
    }
  }
  feedback?: {
    strengths?: string[]
    improvements?: string[]
    revisionRequests?: Array<{
      area: string
      description: string
      priority?: 'required' | 'preferred' | 'optional'
    }>
  }
  evidenceVerification?: {
    checksumVerified?: boolean
    sourcesVerified?: boolean
    notes?: string
  }
  reviewedAt: string
  signature?: {
    algorithm: string
    value: string
    publicKey: string
  }
}
