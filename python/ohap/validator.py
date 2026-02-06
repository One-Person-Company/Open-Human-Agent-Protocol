"""
OHAP Python SDK - Schema validation utilities
"""
from typing import Dict, Any


def validate_task(task: Dict[str, Any]) -> None:
    """Validate task against OHAP schema."""
    if not isinstance(task.get("id"), str) or not task.get("id"):
        raise ValueError("Task must have a valid id")
    
    if not isinstance(task.get("title"), str) or len(task.get("title", "")) < 3:
        raise ValueError("Task title must be at least 3 characters")
    
    if not isinstance(task.get("objective"), str) or len(task.get("objective", "")) < 10:
        raise ValueError("Task objective must be at least 10 characters")
    
    initiator = task.get("initiator")
    if not isinstance(initiator, dict) or not initiator.get("id"):
        raise ValueError("Task must have a valid initiator")


def validate_proposal(proposal: Dict[str, Any]) -> None:
    """Validate proposal against OHAP schema."""
    if not isinstance(proposal.get("id"), str) or not proposal.get("id"):
        raise ValueError("Proposal must have a valid id")
    
    if not proposal.get("task_id") and not proposal.get("taskId"):
        raise ValueError("Proposal must reference a task")
    
    proposer = proposal.get("proposer")
    if not isinstance(proposer, dict) or not proposer.get("id"):
        raise ValueError("Proposal must have a valid proposer")
    
    approach = proposal.get("approach", "")
    if not isinstance(approach, str) or len(approach) < 20:
        raise ValueError("Proposal approach must be at least 20 characters")
    
    timeline = proposal.get("timeline")
    if not isinstance(timeline, dict) or not timeline.get("estimated_completion"):
        raise ValueError("Proposal must have an estimated completion date")


def validate_deliverable(deliverable: Dict[str, Any]) -> None:
    """Validate deliverable against OHAP schema."""
    if not isinstance(deliverable.get("id"), str) or not deliverable.get("id"):
        raise ValueError("Deliverable must have a valid id")
    
    if not deliverable.get("task_id"):
        raise ValueError("Deliverable must reference a task")
    
    if not deliverable.get("contract_id"):
        raise ValueError("Deliverable must reference a contract")
    
    submitter = deliverable.get("submitter")
    if not isinstance(submitter, dict) or not submitter.get("id"):
        raise ValueError("Deliverable must have a valid submitter")
    
    artifacts = deliverable.get("artifacts", [])
    if not isinstance(artifacts, list) or len(artifacts) == 0:
        raise ValueError("Deliverable must have at least one artifact")
    
    evidence = deliverable.get("evidence")
    if not isinstance(evidence, dict):
        raise ValueError("Deliverable must have evidence data")
    
    evidence_items = evidence.get("items", [])
    if not isinstance(evidence_items, list) or len(evidence_items) == 0:
        raise ValueError("Deliverable must have at least one evidence item")


def validate_review(review: Dict[str, Any]) -> None:
    """Validate review against OHAP schema."""
    if not isinstance(review.get("id"), str) or not review.get("id"):
        raise ValueError("Review must have a valid id")
    
    if not review.get("deliverable_id"):
        raise ValueError("Review must reference a deliverable")
    
    reviewer = review.get("reviewer")
    if not isinstance(reviewer, dict) or not reviewer.get("id"):
        raise ValueError("Review must have a valid reviewer")
    
    if not review.get("decision"):
        raise ValueError("Review must have a decision")
