# OHAP Python SDK - Complete Guide

## Overview

The OHAP Python SDK provides a modern, type-safe interface for building human-AI collaborative workflows with the Open Human Agent Protocol.

### Key Features

- **Full Async/Await Support** - Native Python asyncio integration
- **Type Safety** - Complete type hints with dataclasses
- **Schema Validation** - Automatic validation against OHAP schemas
- **Synchronous Wrapper** - Optional OHAPClientSync for traditional code
- **Lightweight** - Minimal dependencies (httpx only)
- **Human-Centric** - Designed for human-AI fusion workflows

## Installation

### From PyPI

```bash
pip install ohap-sdk
```

### From Source

```bash
git clone https://github.com/your-org/Open-Human-Agent-Protocol.git
cd Open-Human-Agent-Protocol
pip install -e .
```

### Development Installation

```bash
pip install -e ".[dev]"
```

## Quick Start

### Basic Async Usage

```python
import asyncio
from ohap import OHAPClient

async def main():
    async with OHAPClient(
        base_url="https://api.ohap.org",
        api_key="sk_live_xxxxx",
    ) as client:
        # Create a task
        task = await client.create_task({
            "title": "Logo Design",
            "objective": "Design a company logo",
            "initiator": {
                "id": "agent-001",
                "type": "agent",
                "name": "Design Coordinator",
            },
        })
        
        print(f"✅ Task created: {task['id']}")

asyncio.run(main())
```

### Basic Sync Usage

```python
from ohap import OHAPClientSync

with OHAPClientSync(
    base_url="https://api.ohap.org",
    api_key="sk_live_xxxxx",
) as client:
    # Create a task
    task = client.create_task({
        "title": "Logo Design",
        "objective": "Design a company logo",
        "initiator": {
            "id": "agent-001",
            "type": "agent",
            "name": "Design Coordinator",
        },
    })
    
    print(f"✅ Task created: {task['id']}")
```

## Core Concepts

### OHAP Workflow Phases

1. **Task Creation** - Define work and requirements
2. **Proposal Submission** - Accept offers from agents/humans
3. **Contract Acceptance** - Bind on accepted proposal
4. **Deliverable Submission** - Provide work with evidence
5. **Review & Acceptance** - Verify and accept work

### Entity Types

All OHAP entities are represented as TypedDict in Python:

```python
from ohap import Task, Proposal, Contract, Deliverable, Review

task: Task = {
    "id": "task-001",
    "title": "Design logo",
    "objective": "Create modern logo",
    # ...
}

proposal: Proposal = {
    "id": "prop-001",
    "task_id": "task-001",
    "proposer": {"id": "human-001", "type": "human"},
    # ...
}
```

### Dataclass Types

For type validation and IDE support, use the dataclass versions:

```python
from dataclasses import asdict
from ohap.types import Task as TaskDataclass

# Create from dict
task_dict = {"title": "Logo", "objective": "...", ...}
task = asdict(TaskDataclass(**task_dict))
```

## API Reference

### OHAPClient (Async)

#### Initialization

```python
client = OHAPClient(
    base_url: str = "https://api.ohap.org",
    api_key: str = "",
    timeout: float = 30.0,
    validate_schemas: bool = True,
)
```

**Parameters:**
- `base_url` - OHAP server URL
- `api_key` - API authentication key
- `timeout` - HTTP request timeout in seconds
- `validate_schemas` - Enable schema validation (disabled by default for performance)

#### Context Manager

```python
async with OHAPClient(...) as client:
    # Use client
    task = await client.create_task({...})
```

#### Task Methods

```python
# Create task
task: Task = await client.create_task(data: Dict)

# Get task by ID
task: Task = await client.get_task(task_id: str)

# Update task
task: Task = await client.update_task(task_id: str, data: Dict)

# List tasks
tasks: List[Task] = await client.list_tasks(
    status: str = None,
    domain: str = None,
    initiator_id: str = None,
)
```

#### Proposal Methods

```python
# Submit proposal
proposal: Proposal = await client.submit_proposal(data: Dict)

# Get proposals for task
proposals: List[Proposal] = await client.get_proposals(task_id: str)

# Get single proposal
proposal: Proposal = await client.get_proposal(proposal_id: str)

# Accept proposal (creates contract)
contract: Contract = await client.accept_proposal(proposal_id: str)

# Reject proposal
result: Dict = await client.reject_proposal(proposal_id: str)

# Update proposal status
proposal: Proposal = await client.update_proposal_status(
    proposal_id: str,
    status: ProposalStatus
)
```

#### Contract Methods

```python
# Get contract
contract: Contract = await client.get_contract(contract_id: str)

# List contracts
contracts: List[Contract] = await client.list_contracts(task_id: str = None)

# Update contract
contract: Contract = await client.update_contract(contract_id: str, data: Dict)
```

#### Deliverable Methods

```python
# Submit deliverable
deliverable: Deliverable = await client.submit_deliverable(data: Dict)

# Get deliverable
deliverable: Deliverable = await client.get_deliverable(deliverable_id: str)

# List deliverables
deliverables: List[Deliverable] = await client.list_deliverables(task_id: str)
```

#### Review Methods

```python
# Submit review
review: Review = await client.submit_review(data: Dict)

# Get review
review: Review = await client.get_review(review_id: str)

# List reviews
reviews: List[Review] = await client.list_reviews(task_id: str = None)
```

### OHAPClientSync (Synchronous Wrapper)

Identical API to OHAPClient but for synchronous code:

```python
with OHAPClientSync(...) as client:
    task = client.create_task({...})  # No await
    proposal = client.submit_proposal({...})
```

## Complete Examples

### Example 1: Create and Track a Task

```python
import asyncio
from ohap import OHAPClient

async def track_task():
    async with OHAPClient(base_url="https://api.ohap.org") as client:
        # Create task
        task = await client.create_task({
            "title": "Develop REST API",
            "objective": "Build authentication endpoints",
            "initiator": {
                "id": "agent-backend",
                "type": "agent",
                "name": "Backend Coordinator",
            },
            "constraints": {
                "budget": {"amount": 2000, "currency": "USD"},
                "timeline": {
                    "deadline": "2026-03-15T23:59:59Z",
                    "estimated_hours": 20,
                },
            },
        })
        
        task_id = task["id"]
        print(f"Created task: {task_id}")
        
        # Monitor task
        while True:
            current_task = await client.get_task(task_id)
            print(f"Status: {current_task['status']}")
            
            if current_task["status"] == "closed":
                break
            
            await asyncio.sleep(60)

asyncio.run(track_task())
```

### Example 2: Submit and Accept Proposal

```python
import asyncio
from ohap import OHAPClient

async def manage_proposal():
    async with OHAPClient(base_url="https://api.ohap.org") as client:
        task_id = "task-001"
        
        # Submit proposal
        proposal = await client.submit_proposal({
            "task_id": task_id,
            "proposer": {
                "id": "dev-alice",
                "type": "human",
                "name": "Alice Chen",
                "credentials": [
                    {
                        "type": "GitHub",
                        "verification_url": "https://github.com/alice",
                    }
                ],
            },
            "approach": "I'll use FastAPI with JWT authentication...",
            "timeline": {
                "estimated_completion": "2026-03-10T17:00:00Z",
            },
            "cost": {
                "amount": 1800,
                "currency": "USD",
            },
        })
        
        print(f"Submitted proposal: {proposal['id']}")
        
        # Accept proposal
        contract = await client.accept_proposal(proposal["id"])
        print(f"Contract created: {contract['id']}")

asyncio.run(manage_proposal())
```

### Example 3: Deliverable with Evidence

```python
import asyncio
from ohap import OHAPClient

async def submit_with_evidence():
    async with OHAPClient(base_url="https://api.ohap.org") as client:
        # Submit deliverable with proof of work
        deliverable = await client.submit_deliverable({
            "task_id": "task-001",
            "contract_id": "contract-001",
            "submitter": {"id": "dev-alice", "name": "Alice Chen"},
            "artifacts": [
                {
                    "type": "url",
                    "reference": "https://github.com/myorg/auth-api/releases/v1.0",
                    "description": "GitHub release with API and tests",
                },
                {
                    "type": "file",
                    "reference": "https://storage.example.com/auth-api.zip",
                    "description": "Complete source code",
                    "mime_type": "application/zip",
                },
            ],
            "evidence": {
                "items": [
                    {
                        "type": "worklog",
                        "reference": "https://storage.example.com/worklog.md",
                        "description": "Daily progress notes",
                    },
                    {
                        "type": "test-results",
                        "reference": "https://ci.example.com/build/123",
                        "description": "CI/CD test report (100% pass)",
                    },
                ],
                "provenance": {
                    "sources": [
                        {
                            "type": "Python Library",
                            "reference": "FastAPI 0.104.1",
                        }
                    ],
                    "tools": ["Python 3.11", "FastAPI", "SQLAlchemy"],
                    "contributors": [
                        {"id": "dev-bob", "role": "Code review"}
                    ],
                },
            },
        })
        
        print(f"Deliverable submitted: {deliverable['id']}")

asyncio.run(submit_with_evidence())
```

## Error Handling

```python
import asyncio
from ohap import OHAPClient
import httpx

async def safe_operation():
    async with OHAPClient(base_url="https://api.ohap.org") as client:
        try:
            task = await client.create_task({
                "title": "Task",
                "objective": "Do work",
                "initiator": {"id": "agent-001", "type": "agent"},
            })
        except httpx.ConnectError:
            print("Failed to connect to OHAP server")
        except httpx.TimeoutException:
            print("Request timed out")
        except ValueError as e:
            print(f"Invalid data: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

asyncio.run(safe_operation())
```

## Schema Validation

### Enable Validation

```python
client = OHAPClient(validate_schemas=True)
```

### Manual Validation

```python
from ohap.validator import validate_task, validate_proposal

task_data = {...}
errors = validate_task(task_data)
if errors:
    print(f"Validation errors: {errors}")
```

## Performance Tips

1. **Disable Schema Validation in Production**
   ```python
   client = OHAPClient(validate_schemas=False)
   ```

2. **Batch Operations**
   ```python
   tasks = []
   for data in task_list:
       task = await client.create_task(data)
       tasks.append(task)
   ```

3. **Connection Pooling** - httpx automatically pools connections

4. **Async Concurrency**
   ```python
   tasks = await asyncio.gather(
       client.create_task(data1),
       client.create_task(data2),
       client.create_task(data3),
   )
   ```

## Type Hints

### Full Type Support

```python
from typing import TypedDict, List, Optional
from ohap.types import Task, Proposal, Deliverable

def process_tasks(tasks: List[Task]) -> None:
    for task in tasks:
        print(f"Task: {task['title']}")

async def submit_proposal(
    client: OHAPClient,
    task: Task,
    proposer_id: str,
) -> Proposal:
    return await client.submit_proposal({
        "task_id": task["id"],
        "proposer": {"id": proposer_id, "type": "human"},
        "approach": "...",
    })
```

## Testing

### Unit Tests

```python
import pytest
import pytest_asyncio
from unittest.mock import AsyncMock, patch
from ohap import OHAPClient

@pytest_asyncio.fixture
async def mock_client():
    with patch("ohap.client.httpx.AsyncClient"):
        async with OHAPClient(base_url="http://localhost") as client:
            yield client

@pytest.mark.asyncio
async def test_create_task(mock_client):
    mock_client._client.post = AsyncMock(return_value=mock_response)
    task = await mock_client.create_task({"title": "Test", ...})
    assert task["title"] == "Test"
```

### Running Tests

```bash
pytest
pytest -v
pytest --cov=ohap
```

## Debugging

### Enable Verbose Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("httpx")
logger.setLevel(logging.DEBUG)

client = OHAPClient(base_url="https://api.ohap.org")
```

## Migration from JavaScript SDK

If you're familiar with the JavaScript SDK, note these Python-specific differences:

| JavaScript | Python |
|---|---|
| `new OHAPClient()` | `OHAPClient()` |
| `client.createTask()` | `client.create_task()` |
| `await promise` | `await coroutine` |
| `{ ... }` | `{ ... }` (same dict syntax) |
| `interface Task` | `Task: TypedDict` |

API signatures are otherwise identical.

## Troubleshooting

### Connection Issues

```python
client = OHAPClient(
    base_url="https://api.ohap.org",
    timeout=60.0  # Increase timeout
)
```

### Validation Errors

```python
from ohap.validator import validate_task

errors = validate_task(task_data)
for error in errors:
    print(error)
```

### Async Issues

Got "RuntimeError: Event loop is closed"?

```python
# Use asyncio.run() for top-level async
asyncio.run(main())
```

## Contributing

Contributions welcome! See [CONTRIBUTING.md](../../CONTRIBUTING.md) for development guidelines.

## License

MIT License - see LICENSE file

## Support

- 📖 [Documentation](https://ohap.org)
- 💬 [GitHub Discussions](https://github.com/your-org/Open-Human-Agent-Protocol/discussions)
- 🐛 [Issue Tracker](https://github.com/your-org/Open-Human-Agent-Protocol/issues)
- 📧 Email: support@ohap.org

---

Built with ❤️ for human-AI collaborative workflows
