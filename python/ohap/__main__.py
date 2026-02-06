"""
OHAP Python SDK - Package demo and CLI interface
"""
import asyncio
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from ohap import OHAPClient, OHAPClientSync


async def demo_async():
    """Run async demo"""
    print("=" * 60)
    print("OHAP Python SDK - Async Demo")
    print("=" * 60)
    print()

    # Note: This demo uses mock responses. In production,
    # replace with real OHAP server URL
    async with OHAPClient(
        base_url="http://localhost:3000",
        validate_schemas=False,
    ) as client:
        print("✅ OHAPClient initialized (async)")
        print(f"   Base URL: {client.base_url}")
        print(f"   Support: task, proposal, contract, deliverable, review")
        print()

        # Example data structures
        task_data = {
            "title": "Design company logo",
            "objective": "Create a modern, memorable logo",
            "initiator": {
                "id": "agent-design-001",
                "type": "agent",
                "name": "Design Coordinator",
            },
            "constraints": {
                "budget": {"amount": 500, "currency": "USD"},
                "timeline": {"deadline": "2026-02-20T23:59:59Z"},
            },
        }

        print("📋 Example Task Data:")
        print(f"   Title: {task_data['title']}")
        print(f"   Budget: {task_data['constraints']['budget']['amount']} {task_data['constraints']['budget']['currency']}")
        print()

        proposal_data = {
            "task_id": "task-001",
            "proposer": {
                "id": "human-sarah-chen",
                "type": "human",
                "name": "Sarah Chen",
            },
            "approach": "I will create 3-5 concept directions.",
            "timeline": {"estimated_completion": "2026-02-18T17:00:00Z"},
            "cost": {"amount": 450, "currency": "USD"},
        }

        print("📋 Example Proposal Data:")
        print(f"   Proposer: {proposal_data['proposer']['name']}")
        print(f"   Cost: {proposal_data['cost']['amount']} {proposal_data['cost']['currency']}")
        print()

        print("🔄 Workflow Steps:")
        print("   1. Create Task")
        print("   2. Submit Proposal")
        print("   3. Accept Proposal (Create Contract)")
        print("   4. Submit Deliverable")
        print("   5. Submit Review")
        print()

        print("📚 SDK Features:")
        print("   ✓ Async/await support")
        print("   ✓ Type hints with TypedDict")
        print("   ✓ Schema validation (optional)")
        print("   ✓ Synchronous wrapper (OHAPClientSync)")
        print("   ✓ Context manager support")
        print()

        print("🚀 Get Started:")
        print("   from ohap import OHAPClient")
        print()
        print("   async with OHAPClient(base_url='...') as client:")
        print("       task = await client.create_task({...})")
        print()


def demo_sync():
    """Run sync demo"""
    print("=" * 60)
    print("OHAP Python SDK - Sync Demo")
    print("=" * 60)
    print()

    with OHAPClientSync(
        base_url="http://localhost:3000",
        validate_schemas=False,
    ) as client:
        print("✅ OHAPClientSync initialized (synchronous)")
        print(f"   Base URL: {client.base_url}")
        print(f"   Methods: Same as OHAPClient but without await")
        print()

        print("🚀 Get Started (Sync):")
        print("   from ohap import OHAPClientSync")
        print()
        print("   with OHAPClientSync(base_url='...') as client:")
        print("       task = client.create_task({...})  # No await")
        print()


def main():
    """Main entry point"""
    if len(sys.argv) > 1 and sys.argv[1] == "sync":
        demo_sync()
    else:
        asyncio.run(demo_async())


if __name__ == "__main__":
    main()
