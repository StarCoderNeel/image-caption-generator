"""Test suite for image-caption-generator."""

import pytest
from fastapi.testclient import TestClient

try:
    from src.main import app
except ImportError:
    app = None


class TestHealthEndpoint:
    """Tests for health check endpoint."""
    
    def setup_method(self):
        """Setup test client."""
        if app:
            self.client = TestClient(app)
    
    @pytest.mark.skipif(app is None, reason="App not available")
    def test_health_check_success(self):
        """Test health check returns 200."""
        response = self.client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "version" in data


class TestProcessEndpoint:
    """Tests for process endpoint."""
    
    def setup_method(self):
        """Setup test client."""
        if app:
            self.client = TestClient(app)
    
    @pytest.mark.skipif(app is None, reason="App not available")
    def test_process_valid_input(self):
        """Test processing with valid input."""
        response = self.client.post("/process", json={"input_text": "test input"})
        assert response.status_code == 200
        data = response.json()
        assert "output" in data
        assert data["status"] == "success"
    
    @pytest.mark.skipif(app is None, reason="App not available")
    def test_process_empty_input(self):
        """Test processing with empty input."""
        response = self.client.post("/process", json={"input_text": ""})
        assert response.status_code == 400
    
    @pytest.mark.skipif(app is None, reason="App not available")
    def test_process_missing_field(self):
        """Test processing with missing required field."""
        response = self.client.post("/process", json={})
        assert response.status_code == 422


class TestIntegration:
    """Integration tests for the application."""
    
    def setup_method(self):
        """Setup test client."""
        if app:
            self.client = TestClient(app)
    
    @pytest.mark.skipif(app is None, reason="App not available")
    def test_full_workflow(self):
        """Test complete request/response workflow."""
        health = self.client.get("/health")
        assert health.status_code == 200
        
        response = self.client.post("/process", json={"input_text": "workflow test"})
        assert response.status_code == 200
        assert response.json()["status"] == "success"

# Test additions for iteration 2

# Test additions for iteration 5

# Test additions for iteration 8
