# Python SDK

Official Python SDK for the Open Human Agent Protocol (OHAP).

## Installation

```bash
pip install ohap-sdk
```

## Quick Start (Async)

```python
import asyncio
from ohap import OHAPClient

async def main():
    async with OHAPClient(
        base_url='https://api.ohap.org',
        api_key='your-api-key',
    ) as client:
        # Create a task
        task = await client.create_task({
            'title': 'Design company logo',
            'objective': 'Create modern brand identity',
            'initiator': {'id': 'agent-001', 'type': 'agent'},
        })
        
        print(f'Task created: {task["id"]}')
        
        # Submit a proposal
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {'id': 'designer-01', 'type': 'human'},
            'approach': 'I will create 3-5 design directions...',
        })
        
        print(f'Proposal submitted: {proposal["id"]}')

asyncio.run(main())
```

## Quick Start (Sync)

```python
from ohap import OHAPClientSync

with OHAPClientSync(
    base_url='https://api.ohap.org',
    api_key='your-api-key',
) as client:
    # Create a task
    task = client.create_task({
        'title': 'Design company logo',
        'objective': 'Create modern brand identity',
        'initiator': {'id': 'agent-001', 'type': 'agent'},
    })
    
    print(f'Task created: {task["id"]}')
    
    # Submit a proposal
    proposal = client.submit_proposal({
        'task_id': task['id'],
        'proposer': {'id': 'designer-01', 'type': 'human'},
        'approach': 'I will create 3-5 design directions...',
    })
    
    print(f'Proposal submitted: {proposal["id"]}')
```

## Features

- ✅ **Async & Sync** - Both async/await and synchronous APIs
- ✅ **Full Type Hints** - Complete Python type annotations
- ✅ **Schema Validation** - Built-in validation
- ✅ **Lightweight** - Minimal dependencies (httpx only)
- ✅ **Python 3.8+** - Modern Python support
- ✅ **LangChain Integration** - Use OHAP as tools in LangChain agents

## LangChain Integration

### Install

```bash
pip install langchain langchain-openai
```

### Example

```python
from ohap import OHAPClientSync
from langchain_openai import ChatOpenAI

with OHAPClientSync(
    base_url='https://api.ohap.org',
    api_key='your-api-key',
) as client:
    tools = client.to_langchain_tools()

    model = ChatOpenAI(model='gpt-4o-mini')
    model_with_tools = model.bind_tools(tools)

    response = model_with_tools.invoke(
        'Create a task for designing a minimal logo for a fintech startup.'
    )
    print(response)
```

## Core API

### OHAPClient (Async) / OHAPClientSync (Sync)

#### Task Management
- `create_task(data)` - Create a new task
- `get_task(task_id)` - Get task details
- `update_task(task_id, data)` - Update task
- `list_tasks(status=None, domain=None)` - List tasks with filtering

#### Proposal Management
- `submit_proposal(data)` - Submit a proposal
- `get_proposals(task_id)` - Get proposals for task
- `accept_proposal(proposal_id)` - Accept proposal (creates contract)

#### Contract Management
- `get_contract(contract_id)` - Get contract details
- `update_contract(contract_id, data)` - Update contract

#### Deliverable Management
- `submit_deliverable(data)` - Submit work with evidence
- `get_deliverable(deliverable_id)` - Get deliverable details

#### Review Management
- `submit_review(data)` - Submit review and decision
- `get_review(review_id)` - Get review details

## Complete Workflow Example (Async)

```python
import asyncio
from ohap import OHAPClient

async def logo_design_workflow():
    async with OHAPClient(
        base_url='https://api.ohap.org',
        api_key='your-api-key',
    ) as client:
        # 1. Create a task
        task = await client.create_task({
            'title': 'Design company logo with AI-human collaboration',
            'objective': 'Create a modern, memorable logo for a tech startup',
            'initiator': {
                'id': 'agent-alpha-001',
                'type': 'agent',
                'name': 'Design Coordinator AI',
            },
            'inputs': [
                {
                    'type': 'text',
                    'reference': 'Company name: NexaBridge',
                    'description': 'Company name to incorporate',
                },
            ],
            'constraints': {
                'budget': {'amount': 500, 'currency': 'USD'},
                'timeline': {
                    'deadline': '2026-02-20T23:59:59Z',
                    'estimated_hours': 8,
                },
            },
            'acceptance': {
                'criteria': [
                    {
                        'description': 'Logo works at sizes from 16px to 2000px',
                        'priority': 'required',
                    },
                ],
            },
        })
        
        print(f'✅ Task created: {task["id"]}')
        
        # 2. Submit proposal
        proposal = await client.submit_proposal({
            'task_id': task['id'],
            'proposer': {
                'id': 'human-sarah-chen',
                'type': 'human',
                'name': 'Sarah Chen',
            },
            'approach': 'I will create 3-5 concept directions blending geometric precision with organic elements.',
            'timeline': {
                'estimated_completion': '2026-02-18T17:00:00Z',
            },
            'cost': {
                'amount': 450,
                'currency': 'USD',
            },
        })
        
        print(f'✅ Proposal submitted: {proposal["id"]}')
        
        # 3. Accept proposal (creates contract)
        contract = await client.accept_proposal(proposal['id'])
        
        print(f'✅ Contract created: {contract["id"]}')
        
        # 4. Submit deliverable with evidence
        deliverable = await client.submit_deliverable({
            'task_id': task['id'],
            'contract_id': contract['id'],
            'submitter': {'id': 'human-sarah-chen', 'name': 'Sarah Chen'},
            'artifacts': [
                {
                    'type': 'file',
                    'reference': 'https://storage.example.com/logo-package.zip',
                    'description': 'Complete logo package',
                },
            ],
            'evidence': {
                'items': [
                    {
                        'type': 'worklog',
                        'reference': 'https://storage.example.com/process-log.md',
                        'description': 'Daily work log with design decisions',
                    },
                ],
                'provenance': {
                    'tools': ['Adobe Illustrator CC 2026', 'Midjourney v6'],
                },
            },
        })
        
        print(f'✅ Deliverable submitted: {deliverable["id"]}')
        
        # 5. Submit review
        review = await client.submit_review({
            'deliverable_id': deliverable['id'],
            'task_id': task['id'],
            'reviewer': {'id': 'agent-alpha-001', 'type': 'initiator'},
            'decision': 'accepted',
            'quality_score': {
                'overall': 4.9,
                'completeness': 5.0,
            },
        })
        
        print(f'✅ Review submitted: {review["id"]}')
        print('✅ Complete workflow finished!')
        
        return {'task': task, 'proposal': proposal, 'contract': contract, 'deliverable': deliverable, 'review': review}

# Run workflow
asyncio.run(logo_design_workflow())
```

## Type Hints

Use type hints for better IDE support:

```python
from typing import List
from ohap import OHAPClient
from ohap.types import Task, Proposal

async def process_tasks(client: OHAPClient) -> List[Task]:
    tasks = await client.list_tasks(status='open')
    return tasks

async def submit_proposals(
    client: OHAPClient,
    task: Task,
    proposer_id: str,
) -> Proposal:
    return await client.submit_proposal({
        'task_id': task['id'],
        'proposer': {'id': proposer_id, 'type': 'human'},
        'approach': 'My proposal...',
    })
```

## Error Handling

```python
import asyncio
from ohap import OHAPClient
import httpx

async def safe_operation():
    async with OHAPClient(base_url='https://api.ohap.org') as client:
        try:
            task = await client.create_task({
                'title': 'Task',
                'objective': 'Do work',
                'initiator': {'id': 'agent-001', 'type': 'agent'},
            })
        except httpx.ConnectError:
            print('Failed to connect to OHAP server')
        except httpx.TimeoutException:
            print('Request timed out')
        except ValueError as e:
            print(f'Invalid data: {e}')

asyncio.run(safe_operation())
```

## Schema Validation

Enable or disable validation:

```python
# With validation (default for offline use)
client = OHAPClient(
    base_url='https://api.ohap.org',
    validate_schemas=True,
)

# Disable for performance
client = OHAPClient(
    base_url='https://api.ohap.org',
    validate_schemas=False,
)
```

### Manual Validation

```python
from ohap.validator import validate_task, validate_proposal

task_data = {'title': 'Task', ...}
errors = validate_task(task_data)
if errors:
    print(f'Validation errors: {errors}')
```

## Concurrent Operations

```python
import asyncio
from ohap import OHAPClient

async def create_multiple_tasks():
    async with OHAPClient(base_url='https://api.ohap.org') as client:
        # Create 3 tasks concurrently
        tasks = await asyncio.gather(
            client.create_task({'title': 'Task 1', 'objective': '...', 'initiator': {...}}),
            client.create_task({'title': 'Task 2', 'objective': '...', 'initiator': {...}}),
            client.create_task({'title': 'Task 3', 'objective': '...', 'initiator': {...}}),
        )
        return tasks
```

## Testing

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest python/tests/

# Run with coverage
pytest --cov=ohap python/tests/
```

## Source Code

- [GitHub Repository](https://github.com/your-org/Open-Human-Agent-Protocol)
- [PyPI Package](https://pypi.org/project/ohap-sdk/)

## License

MIT License - see LICENSE file in repository

## Support

- 📖 [Full Documentation](/sdk-python)
- 💬 [GitHub Discussions](https://github.com/your-org/Open-Human-Agent-Protocol/discussions)
- 🐛 [Issue Tracker](https://github.com/your-org/Open-Human-Agent-Protocol/issues)
