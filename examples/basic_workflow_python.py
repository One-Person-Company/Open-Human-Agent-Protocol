"""
OHAP Python SDK - Complete workflow example

This example demonstrates the full OHAP workflow:
1. Create a task
2. Submit a proposal
3. Accept proposal and create contract
4. Submit deliverable
5. Review deliverable
"""
import asyncio
from ohap import OHAPClient, OHAPClientSync


# ============= Async Example =============

async def create_task_async(client: OHAPClient):
    """Create a design task asynchronously."""
    task = await client.create_task({
        "title": "Design company logo with AI-human collaboration",
        "objective": "Create a modern, memorable logo for a tech startup",
        "initiator": {
            "id": "agent-alpha-001",
            "type": "agent",
            "name": "Design Coordinator AI",
        },
        "inputs": [
            {
                "type": "text",
                "reference": "Company name: NexaBridge",
                "description": "Company name to incorporate",
            },
            {
                "type": "url",
                "reference": "https://example.com/brand-guidelines.pdf",
                "description": "Brand guidelines and color palette",
            },
        ],
        "constraints": {
            "budget": {"amount": 500, "currency": "USD"},
            "timeline": {
                "deadline": "2026-02-20T23:59:59Z",
                "estimated_hours": 8,
                "timezone": "America/Los_Angeles",
            },
            "tools": ["Adobe Illustrator", "Figma"],
            "policies": ["Original work only", "Provide source files"],
        },
        "acceptance": {
            "criteria": [
                {
                    "description": "Logo works at sizes from 16px to 2000px",
                    "test_method": "Visual inspection at multiple scales",
                    "priority": "required",
                },
                {
                    "description": "Includes both icon-only and text versions",
                    "priority": "required",
                },
            ],
            "review_process": "Joint review by initiator and design expert",
        },
        "evidence": {
            "required": ["artifact", "worklog", "citation"],
            "specifications": "Include process sketches and design rationale",
        },
        "collaboration": {
            "shared_context": "Logo for tech startup emphasizing human-AI collaboration",
            "communication_channel": "https://chat.example.com/channels/logo-project",
            "update_frequency": "Daily progress updates",
        },
    })
    
    print(f"✅ Task created: {task['id']}")
    return task


async def submit_proposal_async(client: OHAPClient, task_id: str):
    """Submit a proposal asynchronously."""
    proposal = await client.submit_proposal({
        "task_id": task_id,
        "proposer": {
            "id": "human-sarah-chen",
            "type": "human",
            "name": "Sarah Chen",
            "credentials": [
                {
                    "type": "Portfolio",
                    "issuer": "Behance",
                    "verification_url": "https://behance.net/sarahchen",
                },
            ],
            "reputation": {"score": 4.8, "completed_tasks": 127},
        },
        "approach": "I will create 3-5 concept directions blending geometric precision with organic elements.",
        "timeline": {
            "estimated_completion": "2026-02-18T17:00:00Z",
            "milestones": [
                {
                    "name": "Concept sketches",
                    "date": "2026-02-10T17:00:00Z",
                    "deliverable": "3-5 rough concepts",
                },
                {
                    "name": "Refined designs",
                    "date": "2026-02-14T17:00:00Z",
                    "deliverable": "2 polished directions",
                },
            ],
        },
        "cost": {
            "amount": 450,
            "currency": "USD",
            "breakdown": [
                {"category": "Concept development", "amount": 150},
                {"category": "Design refinement", "amount": 200},
                {"category": "File preparation", "amount": 100},
            ],
        },
        "negotiable": {"scope": True, "cost": True, "timeline": False},
    })
    
    print(f"✅ Proposal submitted: {proposal['id']}")
    return proposal


async def accept_proposal_async(client: OHAPClient, proposal_id: str):
    """Accept proposal and create contract."""
    contract = await client.accept_proposal(proposal_id)
    print(f"✅ Contract created: {contract['id']}")
    return contract


async def submit_deliverable_async(client: OHAPClient, task_id: str, contract_id: str):
    """Submit deliverable with evidence."""
    deliverable = await client.submit_deliverable({
        "task_id": task_id,
        "contract_id": contract_id,
        "submitter": {"id": "human-sarah-chen", "name": "Sarah Chen"},
        "artifacts": [
            {
                "type": "file",
                "reference": "https://storage.example.com/logo-package.zip",
                "description": "Complete logo package",
                "checksum": "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a",
                "mime_type": "application/zip",
                "size": 2458624,
            },
            {
                "type": "document",
                "reference": "https://storage.example.com/usage-guidelines.pdf",
                "description": "Logo usage guidelines",
                "mime_type": "application/pdf",
                "size": 1024000,
            },
        ],
        "evidence": {
            "items": [
                {
                    "type": "worklog",
                    "reference": "https://storage.example.com/process-log.md",
                    "description": "Daily work log with design decisions",
                    "timestamp": "2026-02-18T16:45:00Z",
                },
                {
                    "type": "screenshot",
                    "reference": "https://storage.example.com/process-sketches.png",
                    "description": "Initial concept sketches",
                    "timestamp": "2026-02-10T18:30:00Z",
                },
            ],
            "provenance": {
                "sources": [
                    {
                        "type": "AI Tool",
                        "reference": "Midjourney v6 - concept exploration",
                        "accessed": "2026-02-08T14:00:00Z",
                    },
                ],
                "tools": ["Adobe Illustrator CC 2026", "Midjourney v6", "Figma"],
                "contributors": [
                    {"id": "agent-alpha-001", "role": "Feedback coordination"},
                ],
            },
        },
        "completion_notes": "Completed 2 days ahead of schedule. High-quality deliverables.",
        "acceptance_met": [
            {
                "criteria_id": "crit-001",
                "status": "met",
                "notes": "Tested at all required sizes",
            },
            {
                "criteria_id": "crit-002",
                "status": "met",
                "notes": "All variants provided",
            },
        ],
    })
    
    print(f"✅ Deliverable submitted: {deliverable['id']}")
    return deliverable


async def submit_review_async(client: OHAPClient, deliverable_id: str, task_id: str):
    """Submit review for deliverable."""
    review = await client.submit_review({
        "deliverable_id": deliverable_id,
        "task_id": task_id,
        "reviewer": {"id": "agent-alpha-001", "type": "initiator", "name": "Design Coordinator AI"},
        "decision": "accepted",
        "acceptance_criteria": [
            {
                "criteria_id": "crit-001",
                "assessment": "pass",
                "notes": "Scalability verified",
            },
            {
                "criteria_id": "crit-002",
                "assessment": "pass",
                "notes": "All variants provided",
            },
        ],
        "quality_score": {
            "overall": 4.9,
            "completeness": 5.0,
            "accuracy": 4.8,
            "clarity": 5.0,
            "timeliness": 5.0,
        },
        "feedback": {
            "strengths": [
                "Exceptional attention to scalability",
                "Clear documentation",
                "Initiative shown with bonus variants",
            ],
            "improvements": [],
        },
    })
    
    print(f"✅ Review submitted: {review['id']}")
    return review


async def run_async_workflow():
    """Run complete async workflow."""
    print("🚀 Starting OHAP async workflow demo...\n")
    
    async with OHAPClient(
        base_url="https://api.example.com",
        api_key="your-api-key",
        validate_schemas=False,  # Disable for demo
    ) as client:
        # 1. Create task
        task = await create_task_async(client)
        await asyncio.sleep(0.5)
        
        # 2. Submit proposal
        proposal = await submit_proposal_async(client, task["id"])
        await asyncio.sleep(0.5)
        
        # 3. Accept proposal
        contract = await accept_proposal_async(client, proposal["id"])
        await asyncio.sleep(0.5)
        
        # 4. Submit deliverable
        deliverable = await submit_deliverable_async(client, task["id"], contract["id"])
        await asyncio.sleep(0.5)
        
        # 5. Submit review
        review = await submit_review_async(client, deliverable["id"], task["id"])
        
        print("\n✅ Async workflow completed successfully!")
        return review


# ============= Sync Example =============

def run_sync_workflow():
    """Run complete synchronous workflow."""
    print("🚀 Starting OHAP sync workflow demo...\n")
    
    with OHAPClientSync(
        base_url="https://api.example.com",
        api_key="your-api-key",
        validate_schemas=False,  # Disable for demo
    ) as client:
        # 1. Create task
        task = await create_task_async(client)
        
        # 2. Submit proposal
        proposal = client.submit_proposal({
            "task_id": task["id"],
            "proposer": {
                "id": "human-sarah-chen",
                "type": "human",
                "name": "Sarah Chen",
            },
            "approach": "I will create 3-5 concept directions...",
            "timeline": {"estimated_completion": "2026-02-18T17:00:00Z"},
            "cost": {"amount": 450, "currency": "USD"},
        })
        
        print(f"✅ Proposal submitted: {proposal['id']}")
        
        # 3. Accept proposal
        contract = client.accept_proposal(proposal["id"])
        print(f"✅ Contract created: {contract['id']}")
        
        # 4. Submit deliverable
        deliverable = client.submit_deliverable({
            "task_id": task["id"],
            "contract_id": contract["id"],
            "submitter": {"id": "human-sarah-chen"},
            "artifacts": [
                {
                    "type": "file",
                    "reference": "https://storage.example.com/logo-package.zip",
                    "description": "Complete logo package",
                },
            ],
            "evidence": {
                "items": [
                    {"type": "worklog", "reference": "process-log.md"},
                ],
            },
        })
        
        print(f"✅ Deliverable submitted: {deliverable['id']}")
        
        # 5. Submit review
        review = client.submit_review({
            "deliverable_id": deliverable["id"],
            "task_id": task["id"],
            "reviewer": {"id": "agent-alpha-001", "type": "initiator"},
            "decision": "accepted",
            "quality_score": {"overall": 4.9},
        })
        
        print(f"✅ Review submitted: {review['id']}")
        print("\n✅ Sync workflow completed successfully!")
        return review


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "sync":
        # Run sync example
        run_sync_workflow()
    else:
        # Run async example (default)
        asyncio.run(run_async_workflow())
