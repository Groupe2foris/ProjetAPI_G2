
# ProjetAPI - Documentation Complète

Une **API REST complète** pour gérer les soumissions de projets étudiants pour un cours. Développée avec **FastAPI** et **Pydantic**, ce projet démontre les meilleures pratiques de développement logiciel en équipe : Git Flow, Pull Requests, Revues de code, CI/CD, et Automatisation.

---

## 📖 Table des Matières

1. [Vue d'Ensemble](#vue-densemble)
2. [Architecture](#architecture)
3. [Installation](#installation)
4. [Démarrage Rapide](#démarrage-rapide)
5. [Endpoints de l'API](#endpoints-de-lapi)
6. [Tests Détaillés](#tests-détaillés)
7. [Modèles de Données](#modèles-de-données)
8. [Gestion des Erreurs](#gestion-des-erreurs)
9. [Outils de Qualité](#outils-de-qualité)
10. [Git Flow](#git-flow)
11. [CI/CD et Automatisation](#cicd-et-automatisation)
12. [FAQ et Dépannage](#faq-et-dépannage)

---

## Vue d'Ensemble

### 🎯 Objectif

ProjetAPI est une API REST simple conçue pour :
- Gérer les soumissions de projets étudiants
- Permettre aux professeurs de noter les projets
- Filtrer les projets par cours
- Démontrer les bonnes pratiques de développement en équipe

### 🏆 Caractéristiques Principales

- **6 Endpoints REST** pour les opérations CRUD
- **Validation des données** avec Pydantic
- **Stockage simple** en fichier JSON
- **Documentation interactive** (Swagger UI et ReDoc)
- **Linting automatique** (Black, Flake8, isort)
- **Git Hooks** pour la qualité du code
- **CI/CD Pipeline** avec GitHub Actions
- **Revue de code automatisée** par LLM (Gemini)
- **Notifications par email** pour les Pull Requests

### 📊 Stack Technologique

| Composant | Technologie | Version |
| :--- | :--- | :--- |
| Framework | FastAPI | 0.104.1 |
| Validation | Pydantic | 2.5.0 |
| Serveur | Uvicorn | 0.24.0 |
| Linting | Flake8 | 6.1.0 |
| Formatage | Black | 23.12.0 |
| Imports | isort | 5.13.2 |
| Hooks | pre-commit | 3.5.0 |
| Python | Python | 3.8+ |

---

## Architecture

### 📁 Structure du Projet

```
ProjetAPI/
├── main.py                          # Fichier principal de l'API
├── db.json                          # Base de données (fichier JSON)
├── requirements.txt                 # Dépendances Python
├── .pre-commit-config.yaml          # Configuration des Git Hooks
├── .gitignore                       # Fichiers à ignorer
├── README.md                        # Documentation courte
├── README_COMPLET.md                # Cette documentation
├── CHANGELOG.md                     # Historique des versions
├── .github/
│   └── workflows/
│       ├── ci.yml                   # Pipeline CI (linting, tests)
│       └── llm-review.yml           # Workflow LLM Review + Email
└── venv/                            # Environnement virtuel Python
```

### 🔄 Flux de Données

```
Client HTTP
    ↓
FastAPI (main.py)
    ↓
Pydantic (Validation)
    ↓
Logique Métier
    ↓
Fichier db.json (Stockage)
    ↓
Réponse JSON
    ↓
Client HTTP
```

### 📋 Modèle de Données

```
Project {
  id: string (UUID)                 # Identifiant unique
  studentName: string               # Nom de l'étudiant
  course: string                    # Nom du cours
  githubUrl: string                 # URL du dépôt GitHub
  grade: float | null               # Note (0-20) ou null
  createdAt: string (ISO 8601)      # Date de création
  updatedAt: string (ISO 8601)      # Date de dernière mise à jour
}
```

---

## Installation

### 📋 Prérequis

- **Python** : 3.8 ou supérieur
- **pip** : Gestionnaire de paquets Python
- **Git** : Pour le contrôle de version
- **curl** ou **Postman** : Pour tester l'API

### 🔧 Étapes d'Installation

#### 1. Cloner le Dépôt

```bash
git clone https://github.com/VOTRE_USERNAME/ProjetAPI.git
cd ProjetAPI
```

#### 2. Créer un Environnement Virtuel

```bash
# Créer l'environnement virtuel
python3 -m venv venv

# Activer l'environnement virtuel
# Sur Linux/Mac :
source venv/bin/activate

# Sur Windows :
venv\Scripts\activate
```

**Vérification :** Vous devriez voir `(venv)` au début de votre ligne de commande.

#### 3. Installer les Dépendances

```bash
pip install -r requirements.txt
```

**Dépendances installées :**
- fastapi==0.104.1
- uvicorn==0.24.0
- pydantic==2.5.0
- flake8==6.1.0
- black==23.12.0
- pre-commit==3.5.0
- pytest==7.4.3
- httpx==0.25.2

#### 4. Installer les Git Hooks

```bash
pre-commit install
```

**Résultat attendu :**
```
pre-commit installed at .git/hooks/pre-commit
```

#### 5. Vérifier l'Installation

```bash
# Vérifier que FastAPI est installé
python -c "import fastapi; print(f'FastAPI {fastapi.__version__}')"

# Vérifier que Pydantic est installé
python -c "import pydantic; print(f'Pydantic {pydantic.__version__}')"
```

---

## Démarrage Rapide

### 🚀 Lancer le Serveur

```bash
# Assurez-vous que l'environnement virtuel est activé
source venv/bin/activate

# Lancer le serveur
python main.py
```

**Résultat attendu :**
```
INFO:     Started server process [12345]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 📚 Accéder à la Documentation

Une fois le serveur lancé, accédez à :

| Documentation | URL |
| :--- | :--- |
| **Swagger UI** | http://localhost:8000/docs |
| **ReDoc** | http://localhost:8000/redoc |
| **OpenAPI JSON** | http://localhost:8000/openapi.json |

### 🧪 Tester l'API

```bash
# Vérifier que l'API fonctionne
curl http://localhost:8000/health
```

**Réponse attendue :**
```json
{
  "status": "ok",
  "message": "ProjetAPI is running"
}
```

---

## Endpoints de l'API

### 📌 Vue d'Ensemble

| Méthode | Endpoint | Description | Code HTTP |
| :--- | :--- | :--- | :--- |
| `GET` | `/health` | Vérifier l'état de l'API | 200 |
| `POST` | `/projects` | Créer un nouveau projet | 201 |
| `GET` | `/projects` | Lister tous les projets | 200 |
| `GET` | `/projects/{id}` | Obtenir un projet par ID | 200 / 404 |
| `PUT` | `/projects/{id}/grade` | Noter un projet | 200 / 404 |
| `DELETE` | `/projects/{id}` | Supprimer un projet | 204 / 404 |
| `GET` | `/projects/course/{name}` | Filtrer par cours | 200 / 404 |

---

## Tests Détaillés

### 🧪 Test 1 : Health Check

**Endpoint :** `GET /health`

**Description :** Vérifier que l'API fonctionne correctement.

**Commande :**
```bash
curl -X GET "http://localhost:8000/health" \
  -H "Content-Type: application/json"
```

**Réponse (200 OK) :**
```json
{
  "status": "ok",
  "message": "ProjetAPI is running"
}
```

**Cas d'Usage :**
- Vérifier que le serveur est en ligne
- Monitoring et health checks automatisés

---

### 🧪 Test 2 : POST /projects - Créer un Projet

**Endpoint :** `POST /projects`

**Description :** Créer une nouvelle soumission de projet.

**Paramètres (Body JSON) :**
```json
{
  "studentName": "string",    // Nom de l'étudiant (requis)
  "course": "string",         // Nom du cours (requis)
  "githubUrl": "string"       // URL du dépôt GitHub (requis)
}
```

#### Test 2.1 : Créer un Projet Valide

**Commande :**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Alice Dupont",
    "course": "Python Avancé",
    "githubUrl": "https://github.com/alice/projet-python"
  }'
```

**Réponse (201 Created) :**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "studentName": "Alice Dupont",
  "course": "Python Avancé",
  "githubUrl": "https://github.com/alice/projet-python",
  "grade": null,
  "createdAt": "2024-01-15T10:30:00.123456",
  "updatedAt": "2024-01-15T10:30:00.123456"
}
```

**Points à Vérifier :**
- ✓ Code HTTP : 201 Created
- ✓ `id` : UUID généré automatiquement
- ✓ `grade` : null (pas encore noté)
- ✓ `createdAt` et `updatedAt` : timestamps ISO 8601

#### Test 2.2 : Créer Plusieurs Projets

**Commande 1 :**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Bob Martin",
    "course": "FastAPI Basics",
    "githubUrl": "https://github.com/bob/projet-fastapi"
  }'
```

**Commande 2 :**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Charlie Brown",
    "course": "Python Avancé",
    "githubUrl": "https://github.com/charlie/projet-python"
  }'
```

**Commande 3 :**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Diana Prince",
    "course": "Web Development",
    "githubUrl": "https://github.com/diana/projet-web"
  }'
```

#### Test 2.3 : Validation - Champ Manquant

**Commande :**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "Eve Smith",
    "course": "Python Avancé"
  }'
```

**Réponse (422 Unprocessable Entity) :**
```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "githubUrl"],
      "msg": "Field required",
      "input": {...}
    }
  ]
}
```

#### Test 2.4 : Validation - Champ Vide

**Commande :**
```bash
curl -X POST "http://localhost:8000/projects" \
  -H "Content-Type: application/json" \
  -d '{
    "studentName": "",
    "course": "Python Avancé",
    "githubUrl": "https://github.com/frank/projet"
  }'
```

**Réponse (422 Unprocessable Entity) :**
```json
{
  "detail": [
    {
      "type": "string_too_short",
      "loc": ["body", "studentName"],
      "msg": "String should have at least 1 character",
      "input": ""
    }
  ]
}
```

---

### 🧪 Test 3 : GET /projects - Lister Tous les Projets

**Endpoint :** `GET /projects`

**Description :** Récupérer la liste complète de tous les projets.

**Commande :**
```bash
curl -X GET "http://localhost:8000/projects" \
  -H "Content-Type: application/json"
```

**Réponse (200 OK) :**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "studentName": "Alice Dupont",
    "course": "Python Avancé",
    "githubUrl": "https://github.com/alice/projet-python",
    "grade": null,
    "createdAt": "2024-01-15T10:30:00.123456",
    "updatedAt": "2024-01-15T10:30:00.123456"
  },
  {
    "id": "550e8400-e29b-41d4-a716-446655440001",
    "studentName": "Bob Martin",
    "course": "FastAPI Basics",
    "githubUrl": "https://github.com/bob/projet-fastapi",
    "grade": null,
    "createdAt": "2024-01-15T10:31:00.123456",
    "updatedAt": "2024-01-15T10:31:00.123456"
  }
]
```

**Points à Vérifier :**
- ✓ Code HTTP : 200 OK
- ✓ Retour : Array de Project objects
- ✓ Chaque projet a tous les champs

#### Test 3.1 : Lister Quand Aucun Projet n'Existe

**Commande (après suppression de tous les projets) :**
```bash
curl -X GET "http://localhost:8000/projects"
```

**Réponse (200 OK) :**
```json
[]
```

---

### 🧪 Test 4 : GET /projects/:id - Obtenir un Projet par ID

**Endpoint :** `GET /projects/{project_id}`

**Description :** Récupérer les informations complètes d'un projet spécifique.

**Paramètres :**
- `project_id` (URL path) : ID unique du projet

#### Test 4.1 : Obtenir un Projet Existant

**Commande :**
```bash
# Remplacez l'ID par un ID réel
curl -X GET "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440000" \
  -H "Content-Type: application/json"
```

**Réponse (200 OK) :**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "studentName": "Alice Dupont",
  "course": "Python Avancé",
  "githubUrl": "https://github.com/alice/projet-python",
  "grade": null,
  "createdAt": "2024-01-15T10:30:00.123456",
  "updatedAt": "2024-01-15T10:30:00.123456"
}
```

#### Test 4.2 : Obtenir un Projet Inexistant

**Commande :**
```bash
curl -X GET "http://localhost:8000/projects/invalid-id" \
  -H "Content-Type: application/json"
```

**Réponse (404 Not Found) :**
```json
{
  "detail": "Projet avec l'ID invalid-id non trouvé"
}
```

---

### 🧪 Test 5 : PUT /projects/:id/grade - Noter un Projet

**Endpoint :** `PUT /projects/{project_id}/grade`

**Description :** Attribuer une note à un projet (rôle professeur).

**Paramètres :**
- `project_id` (URL path) : ID unique du projet
- `grade` (Body JSON) : Note entre 0 et 20

#### Test 5.1 : Noter un Projet Valide

**Commande :**
```bash
curl -X PUT "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440000/grade" \
  -H "Content-Type: application/json" \
  -d '{
    "grade": 18.5
  }'
```

**Réponse (200 OK) :**
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "studentName": "Alice Dupont",
  "course": "Python Avancé",
  "githubUrl": "https://github.com/alice/projet-python",
  "grade": 18.5,
  "createdAt": "2024-01-15T10:30:00.123456",
  "updatedAt": "2024-01-15T10:35:00.123456"
}
```

**Points à Vérifier :**
- ✓ `grade` : 18.5 (mis à jour)
- ✓ `updatedAt` : timestamp actualisé
- ✓ Autres champs : inchangés

#### Test 5.2 : Noter avec une Valeur Invalide (> 20)

**Commande :**
```bash
curl -X PUT "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440000/grade" \
  -H "Content-Type: application/json" \
  -d '{
    "grade": 25
  }'
```

**Réponse (422 Unprocessable Entity) :**
```json
{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": ["body", "grade"],
      "msg": "Input should be less than or equal to 20",
      "input": 25
    }
  ]
}
```

#### Test 5.3 : Noter avec une Valeur Invalide (< 0)

**Commande :**
```bash
curl -X PUT "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440000/grade" \
  -H "Content-Type: application/json" \
  -d '{
    "grade": -5
  }'
```

**Réponse (422 Unprocessable Entity) :**
```json
{
  "detail": [
    {
      "type": "greater_than_equal",
      "loc": ["body", "grade"],
      "msg": "Input should be greater than or equal to 0",
      "input": -5
    }
  ]
}
```

#### Test 5.4 : Noter un Projet Inexistant

**Commande :**
```bash
curl -X PUT "http://localhost:8000/projects/invalid-id/grade" \
  -H "Content-Type: application/json" \
  -d '{
    "grade": 15
  }'
```

**Réponse (404 Not Found) :**
```json
{
  "detail": "Projet avec l'ID invalid-id non trouvé"
}
```

#### Test 5.5 : Noter Plusieurs Projets

**Commande 1 :**
```bash
curl -X PUT "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440001/grade" \
  -H "Content-Type: application/json" \
  -d '{"grade": 16.0}'
```

**Commande 2 :**
```bash
curl -X PUT "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440002/grade" \
  -H "Content-Type: application/json" \
  -d '{"grade": 19.5}'
```

---

### 🧪 Test 6 : DELETE /projects/:id - Supprimer un Projet

**Endpoint :** `DELETE /projects/{project_id}`

**Description :** Supprimer une soumission de projet de la base de données.

**Paramètres :**
- `project_id` (URL path) : ID unique du projet à supprimer

#### Test 6.1 : Supprimer un Projet Existant

**Commande :**
```bash
curl -X DELETE "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440000" \
  -H "Content-Type: application/json"
```

**Réponse (204 No Content) :**
```
(Pas de corps de réponse)
```

**Points à Vérifier :**
- ✓ Code HTTP : 204 No Content
- ✓ Pas de corps de réponse

#### Test 6.2 : Vérifier que le Projet est Supprimé

**Commande :**
```bash
curl -X GET "http://localhost:8000/projects/550e8400-e29b-41d4-a716-446655440000"
```

**Réponse (404 Not Found) :**
```json
{
  "detail": "Projet avec l'ID 550e8400-e29b-41d4-a716-446655440000 non trouvé"
}
```

#### Test 6.3 : Supprimer un Projet Inexistant

**Commande :**
```bash
curl -X DELETE "http://localhost:8000/projects/invalid-id"
```

**Réponse (404 Not Found) :**
```json
{
  "detail": "Projet avec l'ID invalid-id non trouvé"
}
```

---

### 🧪 Test 7 : GET /projects/course/:courseName - Filtrer par Cours

**Endpoint :** `GET /projects/course/{course_name}`

**Description :** Récupérer tous les projets d'un cours spécifique.

**Paramètres :**
- `course_name` (URL path) : Nom du cours

#### Test 7.1 : Filtrer par Cours Existant

**Commande :**
```bash
# URL-encode l'espace : "Python Avancé" → "Python%20Avancé"
curl -X GET "http://localhost:8000/projects/course/Python%20Avancé" \
  -H "Content-Type: application/json"
```

**Réponse (200 OK) :**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440002",
    "studentName": "Charlie Brown",
    "course": "Python Avancé",
    "githubUrl": "https://github.com/charlie/projet-python",
    "grade": 19.5,
    "createdAt": "2024-01-15T10:32:00.123456",
    "updatedAt": "2024-01-15T10:35:00.123456"
  }
]
```

#### Test 7.2 : Filtrer avec Casse Différente (Case-Insensitive)

**Commande :**
```bash
curl -X GET "http://localhost:8000/projects/course/python%20avancé" \
  -H "Content-Type: application/json"
```

**Réponse (200 OK) :**
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440002",
    "studentName": "Charlie Brown",
    "course": "Python Avancé",
    "githubUrl": "https://github.com/charlie/projet-python",
    "grade": 19.5,
    "createdAt": "2024-01-15T10:32:00.123456",
    "updatedAt": "2024-01-15T10:35:00.123456"
  }
]
```

**Points à Vérifier :**
- ✓ La recherche est insensible à la casse

#### Test 7.3 : Filtrer par Cours Inexistant

**Commande :**
```bash
curl -X GET "http://localhost:8000/projects/course/Cours%20Inexistant"
```

**Réponse (404 Not Found) :**
```json
{
  "detail": "Aucun projet trouvé pour le cours 'Cours Inexistant'"
}
```

---

## Modèles de Données

### 📊 Modèle Project

**Structure complète :**

```python
class Project(BaseModel):
    """Modèle complet d'un projet"""
    id: str                    # UUID unique
    studentName: str           # Nom de l'étudiant (1+ caractères)
    course: str                # Nom du cours (1+ caractères)
    githubUrl: str             # URL du dépôt GitHub (1+ caractères)
    grade: Optional[float]     # Note (0-20) ou None
    createdAt: str             # Timestamp ISO 8601
    updatedAt: str             # Timestamp ISO 8601
```

### 📊 Modèle ProjectCreate

**Utilisé pour créer un projet :**

```python
class ProjectCreate(BaseModel):
    """Modèle pour créer un projet"""
    studentName: str           # Requis, min 1 caractère
    course: str                # Requis, min 1 caractère
    githubUrl: str             # Requis, min 1 caractère
```

### 📊 Modèle ProjectGrade

**Utilisé pour noter un projet :**

```python
class ProjectGrade(BaseModel):
    """Modèle pour noter un projet"""
    grade: float               # Requis, entre 0 et 20
```

### 📊 Exemple de db.json

```json
{
  "projects": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "studentName": "Alice Dupont",
      "course": "Python Avancé",
      "githubUrl": "https://github.com/alice/projet-python",
      "grade": 18.5,
      "createdAt": "2024-01-15T10:30:00.123456",
      "updatedAt": "2024-01-15T10:35:00.123456"
    },
    {
      "id": "550e8400-e29b-41d4-a716-446655440001",
      "studentName": "Bob Martin",
      "course": "FastAPI Basics",
      "githubUrl": "https://github.com/bob/projet-fastapi",
      "grade": null,
      "createdAt": "2024-01-15T10:31:00.123456",
      "updatedAt": "2024-01-15T10:31:00.123456"
    }
  ]
}
```

---

## Gestion des Erreurs

### 📊 Codes HTTP Utilisés

| Code | Signification | Exemple |
| :--- | :--- | :--- |
| **200 OK** | Requête réussie | GET /projects |
| **201 Created** | Ressource créée | POST /projects |
| **204 No Content** | Suppression réussie | DELETE /projects/:id |
| **400 Bad Request** | Erreur de syntaxe | JSON invalide |
| **404 Not Found** | Ressource non trouvée | GET /projects/invalid-id |
| **422 Unprocessable Entity** | Validation échouée | POST avec champ manquant |
| **500 Internal Server Error** | Erreur serveur | Erreur interne |

### 📊 Réponses d'Erreur

#### Erreur 404 - Ressource Non Trouvée

```json
{
  "detail": "Projet avec l'ID invalid-id non trouvé"
}
```

#### Erreur 422 - Validation Échouée

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "githubUrl"],
      "msg": "Field required",
      "input": {...}
    }
  ]
}
```

#### Erreur 422 - Valeur Invalide

```json
{
  "detail": [
    {
      "type": "less_than_equal",
      "loc": ["body", "grade"],
      "msg": "Input should be less than or equal to 20",
      "input": 25
    }
  ]
}
```

---

## Outils de Qualité

### 🔍 Black - Formatage du Code

**Qu'est-ce que c'est ?**
Black formate automatiquement le code Python selon les standards PEP 8.

**Utilisation :**
```bash
# Formater le code
black main.py

# Vérifier sans modifier
black --check main.py
```

### 🔍 Flake8 - Linting

**Qu'est-ce que c'est ?**
Flake8 vérifie le style et la qualité du code.

**Utilisation :**
```bash
# Vérifier le code
flake8 main.py

# Afficher les statistiques
flake8 main.py --statistics
```

### 🔍 isort - Tri des Imports

**Qu'est-ce que c'est ?**
isort trie automatiquement les imports Python.

**Utilisation :**
```bash
# Trier les imports
isort main.py

# Vérifier sans modifier
isort --check-only main.py
```

### 🔍 pre-commit - Git Hooks

**Qu'est-ce que c'est ?**
pre-commit exécute automatiquement les outils de qualité avant chaque commit.

**Installation :**
```bash
pre-commit install
```

**Utilisation :**
```bash
# Exécuter les hooks manuellement
pre-commit run --all-files

# Les hooks s'exécutent automatiquement lors du commit
git commit -m "Message"
```

**Résultat :**
```
black....................................................................Passed
flake8...................................................................Passed
isort....................................................................Passed
```

---

## Git Flow

### 🌳 Structure des Branches

```
main (production)
  ↑
  └─── develop (développement)
         ↑
         ├─── feature/add-post-project
         ├─── feature/add-get-projects
         ├─── feature/add-get-project-by-id
         ├─── feature/add-grade-project
         ├─── feature/add-delete-project
         └─── feature/add-filter-by-course
```

### 🔄 Workflow de Développement

#### 1. Créer une Branche de Fonctionnalité

```bash
# Se placer sur develop
git switch develop

# Récupérer les dernières modifications
git pull origin develop

# Créer une branche de fonctionnalité
git switch -c feature/add-post-project
```

#### 2. Développer et Commiter

```bash
# Faire des modifications
# ...

# Ajouter les fichiers
git add main.py

# Commiter avec un message clair
git commit -m "Feat: Add POST /projects endpoint (fixes #1)"
```

**Format du message :**
```
<Type>: <Description> (fixes #<Issue>)
```

**Types :**
- `Feat:` Nouvelle fonctionnalité
- `Fix:` Correction de bug
- `Docs:` Documentation
- `Refactor:` Refactorisation
- `Test:` Tests

#### 3. Pousser la Branche

```bash
git push origin feature/add-post-project
```

#### 4. Créer une Pull Request

Sur GitHub :
1. Cliquez sur **Compare & pull request**
2. Remplissez le titre et la description
3. Demandez 2 reviewers
4. Cliquez sur **Create pull request**

#### 5. Revue de Code

Les reviewers :
1. Lisent le code
2. Posent des questions
3. Approuvent ou demandent des modifications

#### 6. Merger la PR

Une fois approuvée :
1. Cliquez sur **Squash and merge**
2. Cliquez sur **Confirm squash and merge**

---

## CI/CD et Automatisation

### 🔧 Pipeline CI (.github/workflows/ci.yml)

**Déclenché sur :** Pull Requests vers `develop`

**Étapes :**
1. Checkout du code
2. Installation de Python et des dépendances
3. Vérification du formatage (Black)
4. Vérification du style (Flake8)
5. Vérification des imports (isort)
6. Test des endpoints API

**Résultat :**
- ✅ Vert : CI réussie
- ❌ Rouge : CI échouée (bloque le merge)

### 🤖 Workflow LLM Review (.github/workflows/llm-review.yml)

**Déclenché sur :** Pull Requests ouvertes ou synchronisées vers `develop`

**Étapes :**
1. Extraction du diff de la PR
2. Appel à l'API Gemini pour la revue
3. Commentaire sur la PR avec la revue
4. Envoi d'un email à l'équipe
5. Ajout de labels à la PR

**Résultat :**
- 💬 Commentaire LLM sur la PR
- 📧 Email reçu par l'équipe
- 🏷️ Labels ajoutés à la PR

---

## FAQ et Dépannage

### ❓ Le serveur ne démarre pas

**Problème :** `ModuleNotFoundError: No module named 'fastapi'`

**Solution :**
```bash
# Vérifier que l'environnement virtuel est activé
source venv/bin/activate

# Réinstaller les dépendances
pip install -r requirements.txt
```

### ❓ Port 8000 déjà utilisé

**Problème :** `Address already in use`

**Solution :**
```bash
# Trouver le processus qui utilise le port
lsof -i :8000

# Tuer le processus
kill -9 <PID>

# Ou lancer sur un autre port
python main.py --port 8001
```

### ❓ Git Hooks ne se déclenchent pas

**Problème :** Les hooks pre-commit ne s'exécutent pas

**Solution :**
```bash
# Réinstaller les hooks
pre-commit install

# Vérifier que les hooks sont installés
ls -la .git/hooks/pre-commit
```

### ❓ Erreur de validation Pydantic

**Problème :** `422 Unprocessable Entity`

**Solution :**
- Vérifiez que tous les champs requis sont présents
- Vérifiez les types de données (string, float, etc.)
- Vérifiez les contraintes (min_length, ge, le, etc.)

### ❓ Comment réinitialiser la base de données ?

**Solution :**
```bash
# Supprimer le fichier db.json
rm db.json

# Le fichier sera recréé automatiquement au prochain POST
curl -X POST "http://localhost:8000/projects" \
  -H "Content-Type: application/json" \
  -d '{"studentName":"Test","course":"Test","githubUrl":"https://github.com/test/test"}'
```

### ❓ Comment tester l'API avec Postman ?

**Étapes :**
1. Téléchargez [Postman](https://www.postman.com/downloads/)
2. Créez une nouvelle collection "ProjetAPI"
3. Ajoutez les endpoints :
   - GET http://localhost:8000/health
   - POST http://localhost:8000/projects
   - GET http://localhost:8000/projects
   - etc.
4. Testez chaque endpoint

---

## 📞 Support et Ressources

### 📚 Documentation Officielle

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)

### 🔗 Liens Utiles

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)

### 💬 Besoin d'Aide ?

Consultez les guides détaillés :
- GUIDE_TESTS_ENDPOINTS.md
- GUIDE_ISSUES_ET_PRS.md
- GUIDE_SECRETS_ET_ACTIONS.md
- GUIDE_FINALISATION_RELEASE.md

---

## 📄 Licence

Ce projet est fourni à titre éducatif.

---

## 🎉 Conclusion

ProjetAPI démontre les meilleures pratiques de développement logiciel en équipe :

✅ **Qualité du code** : Linting, formatage, validation
✅ **Collaboration** : Issues, Pull Requests, Revues de code
✅ **Automatisation** : CI/CD, LLM Review, Notifications
✅ **Documentation** : API complètement documentée
✅ **Versionning** : Git Flow et Semantic Versioning

Bravo d'avoir complété ce projet ! 🚀
