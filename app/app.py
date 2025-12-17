"""
Codex Veritas - Application Flask
Application web vitrine avec CI/CD automatisé
"""

from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'codex-veritas-dev-key')
app.config['ENV'] = os.environ.get('FLASK_ENV', 'production')

# Route principale
@app.route('/')
def index():
    """Page d'accueil de Codex Veritas"""
    return render_template('index.html')

# API pour les informations de l'équipe
@app.route('/api/team-info')
def team_info():
    """Endpoint API pour récupérer les infos de l'équipe"""
    return jsonify({
        'name': 'Codex Veritas',
        'tagline': 'Du code fiable et maîtrisé',
        'description': 'Équipe DevOps spécialisée en CI/CD et conteneurisation',
        'technologies': ['Flask', 'Docker', 'GitHub Actions', 'Kubernetes'],
        'deployment_status': 'automated',
        'timestamp': datetime.now().isoformat()
    })

# API Health Check (pour monitoring)
@app.route('/health')
def health():
    """Endpoint de santé pour le monitoring"""
    return jsonify({
        'status': 'healthy',
        'service': 'codex-veritas-app',
        'timestamp': datetime.now().isoformat()
    }), 200

# Gestion des erreurs 404
@app.errorhandler(404)
def page_not_found(e):
    """Page 404 personnalisée"""
    return render_template('index.html'), 404

# Gestion des erreurs 500
@app.errorhandler(500)
def internal_server_error(e):
    """Page 500 personnalisée"""
    return jsonify({
        'error': 'Internal Server Error',
        'message': 'Une erreur s\'est produite sur le serveur'
    }), 500

if __name__ == '__main__':
    # Configuration pour développement local
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )