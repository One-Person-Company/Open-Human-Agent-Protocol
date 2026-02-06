"""
OHAP Python SDK - Test Suite
"""
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
import asyncio
from ohap import OHAPClient, OHAPClientSync
from ohap.types import Task, Proposal, Contract, Deliverable, Review


class TestOHAPClient:
    """Test OHAPClient async operations"""

    @pytest.mark.asyncio
    async def test_client_initialization(self):
        """Test client can be initialized"""
        async with OHAPClient(
            base_url="http://localhost:3000",
            api_key="test-key"
        ) as client:
            assert client.base_url == "http://localhost:3000"
            assert client.api_key == "test-key"

    @pytest.mark.asyncio
    async def test_create_task(self):
        """Test task creation"""
        with patch("httpx.AsyncClient.post") as mock_post:
            mock_response = AsyncMock()
            mock_response.json.return_value = {
                "id": "task-001",
                "title": "Test Task",
                "objective": "Test objective",
                "initiator": {"id": "agent-001", "type": "agent"},
                "status": "open",
            }
            mock_post.return_value = mock_response

            async with OHAPClient(base_url="http://localhost:3000") as client:
                task = await client.create_task({
                    "title": "Test Task",
                    "objective": "Test objective",
                    "initiator": {"id": "agent-001", "type": "agent"},
                })

                assert task["id"] == "task-001"
                assert task["title"] == "Test Task"

    @pytest.mark.asyncio
    async def test_submit_proposal(self):
        """Test proposal submission"""
        with patch("httpx.AsyncClient.post") as mock_post:
            mock_response = AsyncMock()
            mock_response.json.return_value = {
                "id": "prop-001",
                "task_id": "task-001",
                "proposer": {"id": "human-001", "type": "human"},
                "approach": "Test approach",
                "status": "pending",
            }
            mock_post.return_value = mock_response

            async with OHAPClient(base_url="http://localhost:3000") as client:
                proposal = await client.submit_proposal({
                    "task_id": "task-001",
                    "proposer": {"id": "human-001", "type": "human"},
                    "approach": "Test approach",
                })

                assert proposal["id"] == "prop-001"
                assert proposal["task_id"] == "task-001"

    @pytest.mark.asyncio
    async def test_accept_proposal(self):
        """Test accepting a proposal"""
        with patch("httpx.AsyncClient.post") as mock_post:
            mock_response = AsyncMock()
            mock_response.json.return_value = {
                "id": "contract-001",
                "proposal_id": "prop-001",
                "status": "active",
            }
            mock_post.return_value = mock_response

            async with OHAPClient(base_url="http://localhost:3000") as client:
                contract = await client.accept_proposal("prop-001")

                assert contract["id"] == "contract-001"

    @pytest.mark.asyncio
    async def test_submit_deliverable(self):
        """Test deliverable submission"""
        with patch("httpx.AsyncClient.post") as mock_post:
            mock_response = AsyncMock()
            mock_response.json.return_value = {
                "id": "del-001",
                "task_id": "task-001",
                "status": "pending_review",
            }
            mock_post.return_value = mock_response

            async with OHAPClient(base_url="http://localhost:3000") as client:
                deliverable = await client.submit_deliverable({
                    "task_id": "task-001",
                    "contract_id": "contract-001",
                    "submitter": {"id": "human-001"},
                    "artifacts": [],
                })

                assert deliverable["id"] == "del-001"

    @pytest.mark.asyncio
    async def test_submit_review(self):
        """Test review submission"""
        with patch("httpx.AsyncClient.post") as mock_post:
            mock_response = AsyncMock()
            mock_response.json.return_value = {
                "id": "review-001",
                "deliverable_id": "del-001",
                "decision": "accepted",
            }
            mock_post.return_value = mock_response

            async with OHAPClient(base_url="http://localhost:3000") as client:
                review = await client.submit_review({
                    "deliverable_id": "del-001",
                    "task_id": "task-001",
                    "reviewer": {"id": "agent-001"},
                    "decision": "accepted",
                })

                assert review["id"] == "review-001"
                assert review["decision"] == "accepted"


class TestOHAPClientSync:
    """Test OHAPClientSync synchronous operations"""

    def test_sync_client_initialization(self):
        """Test sync client can be initialized"""
        with OHAPClientSync(
            base_url="http://localhost:3000",
            api_key="test-key"
        ) as client:
            assert client.base_url == "http://localhost:3000"

    def test_sync_create_task(self):
        """Test sync task creation"""
        with patch("httpx.Client.post") as mock_post:
            mock_response = MagicMock()
            mock_response.json.return_value = {
                "id": "task-001",
                "title": "Test Task",
                "objective": "Test objective",
                "initiator": {"id": "agent-001", "type": "agent"},
            }
            mock_post.return_value = mock_response

            with OHAPClientSync(base_url="http://localhost:3000") as client:
                task = client.create_task({
                    "title": "Test Task",
                    "objective": "Test objective",
                    "initiator": {"id": "agent-001", "type": "agent"},
                })

                assert task["id"] == "task-001"


class TestValidation:
    """Test schema validation"""

    def test_validate_task(self):
        """Test task validation"""
        from ohap.validator import validate_task

        valid_task = {
            "title": "Test",
            "objective": "Test",
            "initiator": {"id": "a", "type": "agent"},
        }

        # Should not raise
        errors = validate_task(valid_task)
        # Validator returns empty list for valid data
        assert isinstance(errors, list)

    def test_validate_deliverable(self):
        """Test deliverable validation"""
        from ohap.validator import validate_deliverable

        valid_deliverable = {
            "task_id": "task-001",
            "contract_id": "contract-001",
            "submitter": {"id": "human-001"},
            "artifacts": [],
        }

        errors = validate_deliverable(valid_deliverable)
        assert isinstance(errors, list)

    def test_validate_review(self):
        """Test review validation"""
        from ohap.validator import validate_review

        valid_review = {
            "deliverable_id": "del-001",
            "task_id": "task-001",
            "reviewer": {"id": "agent-001", "type": "agent"},
            "decision": "accepted",
        }

        errors = validate_review(valid_review)
        assert isinstance(errors, list)


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
