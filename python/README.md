# OHAP Python SDK

Official Python SDK for the Open Human Agent Protocol (OHAP).

[![PyPI](https://img.shields.io/pypi/v/ohap-sdk.svg)](https://pypi.org/project/ohap-sdk/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Installation

```bash
pip install ohap-sdk
```

## Quick Start

### Async Example

```python
import asyncio
from ohap import OHAPClient

async def main():
    # Initialize client
    async with OHAPClient(
        base_url="https://api.ohap.org",
        api_key="your-api-key",
    ) as client:
        # Create a task
        task = await client.create_task({
            "title": "Design company logo",
            "objective": "Create a modern logo",
            "initiator": {
                "id": "agent-001",
                "type": "agent",
                "name": "Design Coordinator",
            },
            "constraints": {
                "budget": {"amount": 500, "currency": "USD"},
                "timeline": {"deadline": "2026-02-20T23:59:59Z"},
            },
        })
        
        print(f"Task created: {task['id']}")
        
        # Submit proposal
        proposal = await client.submit_proposal({
            "task_id": task["id"],
            "proposer": {
                "id": "designer-01",
                "type": "human",
                "name": "Sarah Chen",
            },
            "approach": "I will create 3-5 design directions...",
            "timeline": {"estimated_completion": "2026-02-18T17:00:00Z"},
        })
        
        print(f"Proposal submitted: {proposal['id']}")

asyncio.run(main())
```

### Sync Example

```python
from ohap import OHAPClientSync

# Initialize synchronous client
with OHAPClientSync(
    base_url="https://api.ohap.org",
    api_key="your-api-key",
) as client:
    # Create task
    task = client.create_task({
        "title": "Design company logo",
        "objective": "Create a modern logo",
        "initiator": {
            "id": "agent-001",
            "type": "agent",
            "name": "Design Coordinator",
        },
    })
    
    print(f"Task created: {task['id']}")
    
    # Submit proposal
    proposal = client.submit_proposal({
        "task_id": task["id"],
        "proposer": {
            "id": "designer-01",
            "type": "human",
            "name": "Sarah Chen",
        },
        "approach": "I will create designs...",
        "timeline": {"estimated_completion": "2026-02-18T17:00:00Z"},
    })
```

## Features

✅ **Async & Sync** - Both async/await and synchronous APIs  
✅ **Type Hints** - Full Python type annotations  
✅ **Schema Validation** - Built-in validation against OHAP JSON schemas  
✅ **Human-AI Fusion** - Designed for collaborative workflows  
✅ **Lightweight** - Minimal dependencies (only httpx)  
✅ **Production Ready** - Comprehensive error handling

## API Overview

### Client Initialization

```python
from ohap import OHAPClient, OHAPClientSync

# Async client
client = OHAPClient(
    base_url="https://api.ohap.org",
    api_key="your-api-key",
    validate_schemas=True,
)

# Sync client
client = OHAPClientSync(
    base_url="https://api.ohap.org",
    api_key="your-api-key",
    validate_schemas=True,
)
```

### Task Management

```python
# Create task
task = await client.create_task({...})

# Get task
task = await client.get_task(task_id)

# Update task
task = await client.update_task(task_id, {"status": "in-progress"})

# List tasks
tasks = await client.list_tasks(status="open", domain="design")
```

### Proposal Management

```python
# Submit proposal
proposal = await client.submit_proposal({...})

# Get proposals for task
proposals = await client.get_proposals(task_id)

# Accept proposal (creates contract)
contract = await client.accept_proposal(proposal_id)

# Update proposal status
proposal = await client.update_proposal_status(proposal_id, "rejected")
```

### Contract Management

```python
# Get contract
contract = await client.get_contract(contract_id)

# Update contract
contract = await client.update_contract(contract_id, {"status": "active"})
```

### Deliverable Management

```python
# Submit deliverable
deliverable = await client.submit_deliverable({...})

# Get deliverable
deliverable = await client.get_deliverable(deliverable_id)
```

### Review Management

```python
# Submit review
review = await client.submit_review({...})

# Get review
review = await client.get_review(review_id)
```

## Type Definitions

Full type definitions available:

```python
from ohap import (
    Task, Proposal, Contract, Deliverable, Review,
    Entity, Input, Constraints, Acceptance, Evidence, Privacy,
    TaskStatus, ProposalStatus, ContractStatus,
    DeliverableStatus, ReviewDecision,
)

# Use types for type hints and IDE support
def process_task(task: Task) -> None:
    print(f"Processing task: {task['title']}")
```

## Examples

See [examples/basic_workflow_python.py](../../examples/basic_workflow_python.py) for a complete end-to-end workflow.

## Configuration

### Disable Schema Validation

For performance in production, disable validation:

```python
client = OHAPClient(validate_schemas=False)
```

### Custom Base URL

```python
client = OHAPClient(base_url="https://custom-api.example.com")
```

### API Authentication

```python
client = OHAPClient(api_key="your-secret-api-key")
```

## Testing

Run the test suite:

```bash
pip install -e ".[dev]"
pytest
```

## Contributing

Contributions welcome! See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.

## Dependencies

- **httpx** >=0.24.0 - Async HTTP client
- **Python** >=3.8 - Type hints and modern async/await

Optional dev dependencies:
- pytest, pytest-asyncio, pytest-cov
- mypy, black, isort, flake8

## License

MIT License - see [LICENSE](../../LICENSE)

## Links

- [OHAP Documentation](https://ohap.org)
- [GitHub Repository](https://github.com/your-org/Open-Human-Agent-Protocol)
- [JSON Schemas](../../schema/)
- [JavaScript SDK](../../SDK.md)

---

Built with ❤️ for human-AI fusion workflows
