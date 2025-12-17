# 🏛️ Codex Veritas - DevOps CI/CD Project

![CI](https://github.com/TON-USERNAME/devops-ci-cd-project/workflows/CI%20-%20Intégration%20Continue/badge.svg)
![CD](https://github.com/TON-USERNAME/devops-ci-cd-project/workflows/CD%20-%20Déploiement%20Continu/badge.svg)
[![Docker Hub](https://img.shields.io/docker/v/vickydvsh99/flask-app?label=Docker%20Hub)](https://hub.docker.com/r/vickydvsh99/flask-app)

## 📝 Description

Application Flask avec pipeline CI/CD complet utilisant GitHub Actions pour l'automatisation des tests, du build et du déploiement.

## 🚀 Utilisation

### Avec Docker Hub
```bash
docker pull vickydvsh99/flask-app:latest
docker run -p 5000:5000 vickydvsh99/flask-app:latest
```

Accéder à l'application : http://localhost:5000

## 🔧 Technologies utilisées

- **Backend** : Python, Flask
- **Conteneurisation** : Docker
- **CI/CD** : GitHub Actions
- **Tests** : pytest
- **Registry** : Docker Hub, GitHub Container Registry

## 📊 Pipeline CI/CD

### CI - Intégration Continue
- ✅ Tests unitaires automatisés
- ✅ Vérification de la qualité du code (linting)
- ✅ Build de l'application
- ✅ Construction et test de l'image Docker

### CD - Déploiement Continu
- ✅ Publication automatique sur Docker Hub
- ✅ Publication sur GitHub Container Registry
- ✅ Déploiement sur GitHub Pages
- ✅ Notifications de déploiement

## 🏗️ Structure du projet
```
devops-ci-cd-project/
├── .github/
│   └── workflows/
│       ├── ci.yml          # Pipeline d'intégration continue
│       └── cd.yml          # Pipeline de déploiement continu
├── app/                    # Code de l'application Flask
├── docker/
│   └── Dockerfile          # Configuration Docker
├── tests/                  # Tests unitaires
├── requirements.txt        # Dépendances Python
└── README.md
```

## 👨‍💻 Auteur

Développé dans le cadre du TP DevOps CI/CD