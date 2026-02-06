"""
OHAP Python SDK - Main client for human-AI fusion workflows
"""
import json
from typing import Optional, Dict, Any, List
from urllib.parse import urlencode

try:
    import httpx
except ImportError:
    httpx = None

from .types import (
    Task, Proposal, Contract, Deliverable, Review,
    TaskStatus, ProposalStatus, ContractStatus, DeliverableStatus, ReviewDecision
)
from .validator import validate_task, validate_proposal, validate_deliverable, validate_review


class OHAPClient:
    """
    OHAP Client for Human-AI Fusion Workflows
    
    This client provides a programmatic interface for creating, managing,
    and coordinating human-AI collaborative tasks following the OHAP protocol.
    """
    
    def __init__(
        self,
        base_url: str = "https://api.ohap.org",
        api_key: Optional[str] = None,
        validate_schemas: bool = True,
    ):
        """
        Initialize OHAP client.
        
        Args:
            base_url: OHAP API endpoint
            api_key: Optional API key for authentication
            validate_schemas: Enable/disable schema validation
        """
        if httpx is None:
            raise ImportError(
                "httpx is required. Install with: pip install httpx"
            )
        
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.validate_schemas = validate_schemas
        self.client = httpx.AsyncClient()
    
    # ========== Task Management ==========
    
    async def create_task(self, task: Dict[str, Any]) -> Task:
        """Create a new collaborative task."""
        from .types import Task as TaskModel
        
        # Generate ID if not provided
        if "id" not in task:
            task["id"] = self._generate_id("task")
        
        # Set defaults
        if "version" not in task:
            task["version"] = "0.1"
        if "status" not in task:
            task["status"] = "draft"
        if "created_at" not in task:
            task["created_at"] = self._now()
        
        # Validate
        if self.validate_schemas:
            validate_task(task)
        
        return await self._request("POST", "/tasks", task, TaskModel)
    
    async def get_task(self, task_id: str) -> Task:
        """Get task by ID."""
        from .types import Task as TaskModel
        return await self._request("GET", f"/tasks/{task_id}", model=TaskModel)
    
    async def update_task(self, task_id: str, updates: Dict[str, Any]) -> Task:
        """Update task details."""
        from .types import Task as TaskModel
        return await self._request(
            "PATCH", f"/tasks/{task_id}", updates, TaskModel
        )
    
    async def list_tasks(
        self,
        status: Optional[TaskStatus] = None,
        domain: Optional[str] = None,
        initiator_id: Optional[str] = None,
    ) -> List[Task]:
        """List tasks with optional filters."""
        from .types import Task as TaskModel
        
        filters = {}
        if status:
            filters["status"] = status
        if domain:
            filters["domain"] = domain
        if initiator_id:
            filters["initiator_id"] = initiator_id
        
        query = f"?{urlencode(filters)}" if filters else ""
        return await self._request(
            "GET", f"/tasks{query}", model=List[TaskModel]
        )
    
    # ========== Proposal Management ==========
    
    async def submit_proposal(self, proposal: Dict[str, Any]) -> Proposal:
        """Submit a proposal for a task."""
        from .types import Proposal as ProposalModel
        
        # Generate ID if not provided
        if "id" not in proposal:
            proposal["id"] = self._generate_id("prop")
        
        # Set defaults
        if "status" not in proposal:
            proposal["status"] = "submitted"
        if "created_at" not in proposal:
            proposal["created_at"] = self._now()
        
        # Validate
        if self.validate_schemas:
            validate_proposal(proposal)
        
        return await self._request("POST", "/proposals", proposal, ProposalModel)
    
    async def get_proposals(self, task_id: str) -> List[Proposal]:
        """Get proposals for a task."""
        from .types import Proposal as ProposalModel
        return await self._request(
            "GET", f"/tasks/{task_id}/proposals", model=List[ProposalModel]
        )
    
    async def accept_proposal(self, proposal_id: str) -> Contract:
        """Accept a proposal and create a contract."""
        from .types import Contract as ContractModel
        return await self._request(
            "POST", f"/proposals/{proposal_id}/accept", model=ContractModel
        )
    
    async def update_proposal_status(
        self, proposal_id: str, status: ProposalStatus
    ) -> Proposal:
        """Update proposal status."""
        from .types import Proposal as ProposalModel
        return await self._request(
            "PATCH", f"/proposals/{proposal_id}",
            {"status": status}, ProposalModel
        )
    
    # ========== Contract Management ==========
    
    async def get_contract(self, contract_id: str) -> Contract:
        """Get contract by ID."""
        from .types import Contract as ContractModel
        return await self._request(
            "GET", f"/contracts/{contract_id}", model=ContractModel
        )
    
    async def update_contract(
        self, contract_id: str, updates: Dict[str, Any]
    ) -> Contract:
        """Update contract details."""
        from .types import Contract as ContractModel
        return await self._request(
            "PATCH", f"/contracts/{contract_id}", updates, ContractModel
        )
    
    # ========== Deliverable Management ==========
    
    async def submit_deliverable(
        self, deliverable: Dict[str, Any]
    ) -> Deliverable:
        """Submit deliverable for a contract."""
        from .types import Deliverable as DeliverableModel
        
        # Generate ID if not provided
        if "id" not in deliverable:
            deliverable["id"] = self._generate_id("deliv")
        
        # Set defaults
        if "status" not in deliverable:
            deliverable["status"] = "submitted"
        if "submitted_at" not in deliverable:
            deliverable["submitted_at"] = self._now()
        
        # Validate
        if self.validate_schemas:
            validate_deliverable(deliverable)
        
        return await self._request(
            "POST", "/deliverables", deliverable, DeliverableModel
        )
    
    async def get_deliverable(self, deliverable_id: str) -> Deliverable:
        """Get deliverable by ID."""
        from .types import Deliverable as DeliverableModel
        return await self._request(
            "GET", f"/deliverables/{deliverable_id}", model=DeliverableModel
        )
    
    # ========== Review Management ==========
    
    async def submit_review(self, review: Dict[str, Any]) -> Review:
        """Submit a review for a deliverable."""
        from .types import Review as ReviewModel
        
        # Generate ID if not provided
        if "id" not in review:
            review["id"] = self._generate_id("rev")
        
        # Set default
        if "reviewed_at" not in review:
            review["reviewed_at"] = self._now()
        
        # Validate
        if self.validate_schemas:
            validate_review(review)
        
        return await self._request("POST", "/reviews", review, ReviewModel)
    
    async def get_review(self, review_id: str) -> Review:
        """Get review by ID."""
        from .types import Review as ReviewModel
        return await self._request(
            "GET", f"/reviews/{review_id}", model=ReviewModel
        )

    def to_langchain_tools(
        self,
        initiator_id: str = "agent-001",
        initiator_type: str = "agent",
    ):
        """Create LangChain tools bound to this client."""
        try:
            from langchain.tools import tool
        except ImportError as exc:
            raise ImportError(
                "LangChain is required. Install with: pip install langchain langchain-openai"
            ) from exc

        @tool("ohap_create_task")
        async def ohap_create_task(title: str, objective: str) -> str:
            task = await self.create_task({
                "title": title,
                "objective": objective,
                "initiator": {"id": initiator_id, "type": initiator_type},
            })
            return json.dumps({"id": task["id"], "title": task.get("title")})

        @tool("ohap_submit_proposal")
        async def ohap_submit_proposal(
            task_id: str,
            proposer_id: str,
            proposer_type: str,
            approach: str,
        ) -> str:
            proposal = await self.submit_proposal({
                "task_id": task_id,
                "proposer": {"id": proposer_id, "type": proposer_type},
                "approach": approach,
            })
            return json.dumps({"id": proposal["id"], "task_id": proposal["task_id"]})

        @tool("ohap_submit_deliverable")
        async def ohap_submit_deliverable(
            task_id: str,
            contract_id: str,
            submitter_id: str,
            artifact_reference: str,
        ) -> str:
            deliverable = await self.submit_deliverable({
                "task_id": task_id,
                "contract_id": contract_id,
                "submitter": {"id": submitter_id},
                "artifacts": [
                    {"type": "url", "reference": artifact_reference},
                ],
            })
            return json.dumps({"id": deliverable["id"], "task_id": deliverable["task_id"]})

        @tool("ohap_submit_review")
        async def ohap_submit_review(
            deliverable_id: str,
            task_id: str,
            reviewer_id: str,
            decision: str,
        ) -> str:
            review = await self.submit_review({
                "deliverable_id": deliverable_id,
                "task_id": task_id,
                "reviewer": {"id": reviewer_id, "type": "initiator"},
                "decision": decision,
            })
            return json.dumps({"id": review["id"], "decision": review.get("decision")})

        return [
            ohap_create_task,
            ohap_submit_proposal,
            ohap_submit_deliverable,
            ohap_submit_review,
        ]
    
    # ========== Utility Methods ==========
    
    def _generate_id(self, prefix: str) -> str:
        """Generate a unique ID with prefix."""
        import time
        import random
        import string
        
        timestamp = int(time.time() * 1000)
        random_part = ''.join(random.choices(string.ascii_lowercase + string.digits, k=9))
        return f"{prefix}-{timestamp}-{random_part}"
    
    def _now(self) -> str:
        """Get current ISO timestamp."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
    
    async def _request(
        self,
        method: str,
        path: str,
        body: Optional[Dict[str, Any]] = None,
        model: Optional[type] = None,
    ) -> Any:
        """Make HTTP request to OHAP API."""
        url = f"{self.base_url}{path}"
        headers = {"Content-Type": "application/json"}
        
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        # Make request
        if method.upper() == "GET":
            response = await self.client.get(url, headers=headers)
        elif method.upper() == "POST":
            response = await self.client.post(
                url, headers=headers,
                content=json.dumps(body) if body else None
            )
        elif method.upper() == "PATCH":
            response = await self.client.patch(
                url, headers=headers,
                content=json.dumps(body) if body else None
            )
        else:
            raise ValueError(f"Unsupported method: {method}")
        
        # Handle response
        if response.status_code >= 400:
            raise Exception(
                f"OHAP API error: {response.status_code} {response.text}"
            )
        
        data = response.json()
        return data
    
    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


# Synchronous wrapper
class OHAPClientSync:
    """Synchronous wrapper around async OHAPClient."""
    
    def __init__(
        self,
        base_url: str = "https://api.ohap.org",
        api_key: Optional[str] = None,
        validate_schemas: bool = True,
    ):
        """Initialize synchronous OHAP client."""
        self._client = OHAPClient(base_url, api_key, validate_schemas)
        self._loop = None
    
    def _get_event_loop(self):
        """Get or create event loop."""
        import asyncio
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        return loop
    
    def create_task(self, task: Dict[str, Any]) -> Task:
        """Create a new collaborative task."""
        return self._get_event_loop().run_until_complete(
            self._client.create_task(task)
        )
    
    def get_task(self, task_id: str) -> Task:
        """Get task by ID."""
        return self._get_event_loop().run_until_complete(
            self._client.get_task(task_id)
        )
    
    def update_task(self, task_id: str, updates: Dict[str, Any]) -> Task:
        """Update task details."""
        return self._get_event_loop().run_until_complete(
            self._client.update_task(task_id, updates)
        )
    
    def list_tasks(
        self,
        status: Optional[TaskStatus] = None,
        domain: Optional[str] = None,
        initiator_id: Optional[str] = None,
    ) -> List[Task]:
        """List tasks with optional filters."""
        return self._get_event_loop().run_until_complete(
            self._client.list_tasks(status, domain, initiator_id)
        )
    
    def submit_proposal(self, proposal: Dict[str, Any]) -> Proposal:
        """Submit a proposal for a task."""
        return self._get_event_loop().run_until_complete(
            self._client.submit_proposal(proposal)
        )
    
    def get_proposals(self, task_id: str) -> List[Proposal]:
        """Get proposals for a task."""
        return self._get_event_loop().run_until_complete(
            self._client.get_proposals(task_id)
        )
    
    def accept_proposal(self, proposal_id: str) -> Contract:
        """Accept a proposal and create a contract."""
        return self._get_event_loop().run_until_complete(
            self._client.accept_proposal(proposal_id)
        )
    
    def update_proposal_status(
        self, proposal_id: str, status: ProposalStatus
    ) -> Proposal:
        """Update proposal status."""
        return self._get_event_loop().run_until_complete(
            self._client.update_proposal_status(proposal_id, status)
        )
    
    def get_contract(self, contract_id: str) -> Contract:
        """Get contract by ID."""
        return self._get_event_loop().run_until_complete(
            self._client.get_contract(contract_id)
        )
    
    def update_contract(
        self, contract_id: str, updates: Dict[str, Any]
    ) -> Contract:
        """Update contract details."""
        return self._get_event_loop().run_until_complete(
            self._client.update_contract(contract_id, updates)
        )
    
    def submit_deliverable(self, deliverable: Dict[str, Any]) -> Deliverable:
        """Submit deliverable for a contract."""
        return self._get_event_loop().run_until_complete(
            self._client.submit_deliverable(deliverable)
        )
    
    def get_deliverable(self, deliverable_id: str) -> Deliverable:
        """Get deliverable by ID."""
        return self._get_event_loop().run_until_complete(
            self._client.get_deliverable(deliverable_id)
        )
    
    def submit_review(self, review: Dict[str, Any]) -> Review:
        """Submit a review for a deliverable."""
        return self._get_event_loop().run_until_complete(
            self._client.submit_review(review)
        )
    
    def get_review(self, review_id: str) -> Review:
        """Get review by ID."""
        return self._get_event_loop().run_until_complete(
            self._client.get_review(review_id)
        )

    def to_langchain_tools(
        self,
        initiator_id: str = "agent-001",
        initiator_type: str = "agent",
    ):
        """Create LangChain tools bound to this client."""
        try:
            from langchain.tools import tool
        except ImportError as exc:
            raise ImportError(
                "LangChain is required. Install with: pip install langchain langchain-openai"
            ) from exc

        @tool("ohap_create_task")
        def ohap_create_task(title: str, objective: str) -> str:
            task = self.create_task({
                "title": title,
                "objective": objective,
                "initiator": {"id": initiator_id, "type": initiator_type},
            })
            return json.dumps({"id": task["id"], "title": task.get("title")})

        @tool("ohap_submit_proposal")
        def ohap_submit_proposal(
            task_id: str,
            proposer_id: str,
            proposer_type: str,
            approach: str,
        ) -> str:
            proposal = self.submit_proposal({
                "task_id": task_id,
                "proposer": {"id": proposer_id, "type": proposer_type},
                "approach": approach,
            })
            return json.dumps({"id": proposal["id"], "task_id": proposal["task_id"]})

        @tool("ohap_submit_deliverable")
        def ohap_submit_deliverable(
            task_id: str,
            contract_id: str,
            submitter_id: str,
            artifact_reference: str,
        ) -> str:
            deliverable = self.submit_deliverable({
                "task_id": task_id,
                "contract_id": contract_id,
                "submitter": {"id": submitter_id},
                "artifacts": [
                    {"type": "url", "reference": artifact_reference},
                ],
            })
            return json.dumps({"id": deliverable["id"], "task_id": deliverable["task_id"]})

        @tool("ohap_submit_review")
        def ohap_submit_review(
            deliverable_id: str,
            task_id: str,
            reviewer_id: str,
            decision: str,
        ) -> str:
            review = self.submit_review({
                "deliverable_id": deliverable_id,
                "task_id": task_id,
                "reviewer": {"id": reviewer_id, "type": "initiator"},
                "decision": decision,
            })
            return json.dumps({"id": review["id"], "decision": review.get("decision")})

        return [
            ohap_create_task,
            ohap_submit_proposal,
            ohap_submit_deliverable,
            ohap_submit_review,
        ]
    
    def close(self):
        """Close the HTTP client."""
        self._get_event_loop().run_until_complete(self._client.close())
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
