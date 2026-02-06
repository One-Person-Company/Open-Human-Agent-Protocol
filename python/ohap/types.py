"""
OHAP Python SDK - Type definitions for the Open Human Agent Protocol
"""
from typing import Any, List, Optional, Dict, Literal
from dataclasses import dataclass, field
from datetime import datetime


# Status types
TaskStatus = Literal[
    "draft", "open", "offered", "contracted", "in-progress",
    "delivered", "reviewed", "closed", "cancelled"
]
ProposalStatus = Literal["submitted", "under-review", "accepted", "rejected", "withdrawn"]
ContractStatus = Literal["active", "completed", "cancelled", "disputed"]
DeliverableStatus = Literal[
    "submitted", "under-review", "accepted", "rejected", "revision-requested"
]
ReviewDecision = Literal["accepted", "rejected", "revision-requested", "escalated"]
EntityType = Literal["human", "agent", "system", "broker"]


@dataclass
class Entity:
    """Base entity with id and type"""
    id: str
    type: EntityType
    name: Optional[str] = None
    contact: Optional[str] = None


@dataclass
class Input:
    """Task input - file, link, or data reference"""
    type: Literal["file", "url", "text", "data", "reference"]
    reference: str
    description: Optional[str] = None
    checksum: Optional[str] = None


@dataclass
class Budget:
    """Budget constraint"""
    amount: float
    currency: str


@dataclass
class Timeline:
    """Timeline constraint"""
    deadline: Optional[str] = None
    estimated_hours: Optional[float] = None
    timezone: Optional[str] = None


@dataclass
class Constraints:
    """Work constraints - budget, time, tools, policies"""
    budget: Optional[Budget] = None
    timeline: Optional[Timeline] = None
    tools: Optional[List[str]] = None
    policies: Optional[List[str]] = None


@dataclass
class AcceptanceCriterion:
    """Single acceptance criterion"""
    description: str
    id: Optional[str] = None
    test_method: Optional[str] = None
    priority: Literal["required", "preferred", "optional"] = "required"


@dataclass
class Acceptance:
    """Acceptance criteria and review process"""
    criteria: List[AcceptanceCriterion]
    review_process: Optional[str] = None


@dataclass
class Evidence:
    """Required and optional evidence types"""
    required: Optional[List[str]] = None
    optional: Optional[List[str]] = None
    specifications: Optional[str] = None


@dataclass
class Privacy:
    """Data handling and privacy rules"""
    data_classification: Optional[str] = None
    consent_required: bool = False
    redaction_rules: Optional[List[str]] = None
    retention: Optional[str] = None


@dataclass
class Collaboration:
    """Collaboration context and expectations"""
    shared_context: Optional[str] = None
    communication_channel: Optional[str] = None
    update_frequency: Optional[str] = None


@dataclass
class TaskMetadata:
    """Task metadata"""
    created_at: str
    updated_at: Optional[str] = None
    tags: Optional[List[str]] = None
    domain: Optional[str] = None


@dataclass
class Task:
    """Shared unit of work in OHAP"""
    id: str
    version: str
    title: str
    objective: str
    status: TaskStatus
    initiator: Entity
    created_at: str
    inputs: Optional[List[Input]] = None
    constraints: Optional[Constraints] = None
    acceptance: Optional[Acceptance] = None
    evidence: Optional[Evidence] = None
    privacy: Optional[Privacy] = None
    collaboration: Optional[Collaboration] = None
    metadata: Optional[TaskMetadata] = None


@dataclass
class Credential:
    """Credential or certification"""
    type: str
    issuer: str
    verification_url: Optional[str] = None


@dataclass
class Reputation:
    """Reputation score and history"""
    score: Optional[float] = None
    completed_tasks: Optional[int] = None


@dataclass
class Proposer(Entity):
    """Entity submitting a proposal"""
    credentials: Optional[List[Credential]] = None
    reputation: Optional[Reputation] = None


@dataclass
class Milestone:
    """Project milestone"""
    name: str
    date: str
    deliverable: Optional[str] = None


@dataclass
class ProposalTimeline:
    """Proposed timeline with milestones"""
    estimated_completion: str
    milestones: Optional[List[Milestone]] = None


@dataclass
class Cost:
    """Cost structure"""
    amount: float
    currency: str
    breakdown: Optional[List[Dict[str, Any]]] = None
    payment_schedule: Optional[str] = None


@dataclass
class Negotiable:
    """What aspects are negotiable"""
    scope: bool = False
    timeline: bool = False
    cost: bool = False


@dataclass
class Proposal:
    """Human or broker offer to execute a task"""
    id: str
    task_id: str
    proposer: Proposer
    approach: str
    timeline: ProposalTimeline
    status: ProposalStatus
    created_at: str
    cost: Optional[Cost] = None
    negotiable: Optional[Negotiable] = None
    expires_at: Optional[str] = None


@dataclass
class ContractTerms:
    """Contract terms and conditions"""
    scope: str
    timeline: ProposalTimeline
    compensation: Optional[Cost] = None
    acceptance_criteria: Optional[List[AcceptanceCriterion]] = None
    evidence_requirements: Optional[List[str]] = None


@dataclass
class SharedResponsibilities:
    """Mutual responsibilities between parties"""
    initiator_commits: Optional[List[str]] = None
    human_partner_commits: Optional[List[str]] = None
    communication_protocol: Optional[str] = None


@dataclass
class DisputeResolution:
    """Dispute resolution mechanism"""
    method: Optional[str] = None
    arbitrator: Optional[str] = None


@dataclass
class Amendment:
    """Contract amendment"""
    date: str
    description: str
    agreed_by: Optional[List[str]] = None


@dataclass
class Contract:
    """Accepted proposal with binding terms"""
    id: str
    task_id: str
    proposal_id: str
    initiator: Entity
    human_partner: Entity
    terms: ContractTerms
    status: ContractStatus
    created_at: str
    shared_responsibilities: Optional[SharedResponsibilities] = None
    dispute_resolution: Optional[DisputeResolution] = None
    amendments: Optional[List[Amendment]] = None
    completed_at: Optional[str] = None


@dataclass
class Artifact:
    """Output artifact"""
    type: str
    reference: str
    description: Optional[str] = None
    checksum: Optional[str] = None
    mime_type: Optional[str] = None
    size: Optional[int] = None


@dataclass
class EvidenceItem:
    """Evidence of work"""
    type: str
    reference: str
    description: Optional[str] = None
    timestamp: Optional[str] = None


@dataclass
class Source:
    """Evidence source"""
    type: str
    reference: str
    accessed: Optional[str] = None


@dataclass
class Contributor:
    """Work contributor"""
    id: str
    role: str


@dataclass
class Provenance:
    """Provenance and audit trail"""
    sources: Optional[List[Source]] = None
    tools: Optional[List[str]] = None
    contributors: Optional[List[Contributor]] = None


@dataclass
class EvidenceData:
    """Complete evidence data"""
    items: List[EvidenceItem]
    provenance: Optional[Provenance] = None


@dataclass
class AcceptanceMet:
    """Acceptance criterion fulfillment"""
    criteria_id: str
    status: Literal["met", "partially-met", "not-met", "not-applicable"]
    notes: Optional[str] = None


@dataclass
class Deliverable:
    """Output artifacts, evidence, and completion metadata"""
    id: str
    task_id: str
    contract_id: str
    submitter: Entity
    artifacts: List[Artifact]
    evidence: EvidenceData
    submitted_at: str
    status: DeliverableStatus
    completion_notes: Optional[str] = None
    acceptance_met: Optional[List[AcceptanceMet]] = None


@dataclass
class ReviewAcceptanceCriterion:
    """Assessment of acceptance criterion"""
    criteria_id: str
    assessment: Literal["pass", "fail", "partial", "not-evaluated"]
    notes: Optional[str] = None
    evidence: Optional[List[str]] = None


@dataclass
class QualityScore:
    """Quality assessment dimensions"""
    overall: Optional[float] = None
    completeness: Optional[float] = None
    accuracy: Optional[float] = None
    clarity: Optional[float] = None
    timeliness: Optional[float] = None


@dataclass
class ReviewFeedback:
    """Structured feedback on deliverable"""
    strengths: Optional[List[str]] = None
    improvements: Optional[List[str]] = None
    revision_requests: Optional[List[Dict[str, Any]]] = None


@dataclass
class EvidenceVerification:
    """Verification of submitted evidence"""
    checksum_verified: Optional[bool] = None
    sources_verified: Optional[bool] = None
    notes: Optional[str] = None


@dataclass
class Signature:
    """Cryptographic signature"""
    algorithm: str
    value: str
    public_key: str


@dataclass
class Review:
    """Verification report and decision"""
    id: str
    deliverable_id: str
    reviewer: Entity
    decision: ReviewDecision
    reviewed_at: str
    task_id: Optional[str] = None
    acceptance_criteria: Optional[List[ReviewAcceptanceCriterion]] = None
    quality_score: Optional[QualityScore] = None
    feedback: Optional[ReviewFeedback] = None
    evidence_verification: Optional[EvidenceVerification] = None
    signature: Optional[Signature] = None
