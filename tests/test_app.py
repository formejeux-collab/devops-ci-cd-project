"""
Codex Veritas - Tests Unitaires
Tests pour l'application Flask
"""

import pytest
import json
from app.app import app


@pytest.fixture
def client():
    """Fixture pour créer un client de test Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test de la page d'accueil"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Codex Veritas' in response.data


def test_health_endpoint(client):
    """Test de l'endpoint de santé"""
    response = client.get('/health')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['status'] == 'healthy'
    assert data['service'] == 'codex-veritas-app'
    assert 'timestamp' in data


def test_team_info_endpoint(client):
    """Test de l'endpoint des informations de l'équipe"""
    response = client.get('/api/team-info')
    assert response.status_code == 200
    
    data = json.loads(response.data)
    assert data['name'] == 'Codex Veritas'
    assert data['tagline'] == 'Du code fiable et maîtrisé'
    assert 'technologies' in data
    assert 'Flask' in data['technologies']
    assert 'Docker' in data['technologies']
    assert data['deployment_status'] == 'automated'


def test_404_error(client):
    """Test de la gestion des erreurs 404"""
    response = client.get('/page-inexistante')
    assert response.status_code == 404


def test_api_response_format(client):
    """Test du format de réponse JSON"""
    response = client.get('/api/team-info')
    assert response.content_type == 'application/json'
    
    data = json.loads(response.data)
    assert isinstance(data, dict)
    assert 'name' in data
    assert 'tagline' in data


def test_health_check_structure(client):
    """Test de la structure complète du health check"""
    response = client.get('/health')
    data = json.loads(response.data)
    
    required_fields = ['status', 'service', 'timestamp']
    for field in required_fields:
        assert field in data, f"Le champ '{field}' est manquant"


def test_team_technologies(client):
    """Test de la liste des technologies"""
    response = client.get('/api/team-info')
    data = json.loads(response.data)
    
    expected_technologies = ['Flask', 'Docker', 'GitHub Actions', 'Kubernetes']
    for tech in expected_technologies:
        assert tech in data['technologies'], f"La technologie '{tech}' est manquante"


def test_response_time(client):
    """Test du temps de réponse"""
    import time
    start = time.time()
    response = client.get('/')
    end = time.time()
    
    assert response.status_code == 200
    assert (end - start) < 1.0, "La réponse est trop lente (> 1s)"


def test_multiple_requests(client):
    """Test de la stabilité avec plusieurs requêtes"""
    for _ in range(10):
        response = client.get('/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'