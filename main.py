"""
ProjetAPI - API REST pour gérer les soumissions de projets étudiants
Utilise FastAPI et Pydantic pour la validation des données
Les données sont stockées dans un fichier db.json
"""

import json
import os
import uuid
from datetime import datetime
from typing import List, Optional

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

# Initialiser FastAPI
app = FastAPI(
    title="ProjetAPI",
    description="API REST pour gérer les soumissions de projets étudiants",
    version="1.0.0",
)

# Chemin du fichier de base de données
DB_FILE = "db.json"


# ============================================================================
# Modèles Pydantic pour la validation des données
# ============================================================================


class ProjectBase(BaseModel):
    """Modèle de base pour un projet"""

    studentName: str = Field(..., min_length=1, description="Nom de l'étudiant")
    course: str = Field(..., min_length=1, description="Nom du cours")
    githubUrl: str = Field(..., min_length=1, description="URL du dépôt GitHub")


class ProjectCreate(ProjectBase):
    """Modèle pour créer un nouveau projet"""

    pass


class ProjectGrade(BaseModel):
    """Modèle pour noter un projet"""

    grade: float = Field(..., ge=0, le=20, description="Note du projet (0-20)")


class Project(ProjectBase):
    """Modèle complet d'un projet avec ID et grade"""

    id: str = Field(..., description="ID unique du projet")
    grade: Optional[float] = Field(None, description="Note du projet")
    createdAt: str = Field(..., description="Date de création")
    updatedAt: str = Field(..., description="Date de dernière mise à jour")


# ============================================================================
# Fonctions utilitaires pour la gestion de la base de données
# ============================================================================


def load_db() -> dict:
    """Charger les données depuis db.json"""
    if not os.path.exists(DB_FILE):
        return {"projects": []}
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"projects": []}


def save_db(data: dict) -> None:
    """Sauvegarder les données dans db.json"""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)


# ============================================================================
# Endpoints de l'API
# ============================================================================


@app.post(
    "/projects",
    response_model=Project,
    status_code=status.HTTP_201_CREATED,
    tags=["Projects"],
    summary="Créer un nouveau projet",
    description="Soumettre un nouveau projet étudiant",
)
def create_project(project: ProjectCreate) -> Project:
    """
    **Issue #1 :** Créer un nouveau projet
    """
    db = load_db()

    # Générer un ID unique
    project_id = str(uuid.uuid4())

    # Créer le nouveau projet
    now = datetime.now().isoformat()
    new_project = {
        "id": project_id,
        "studentName": project.studentName,
        "course": project.course,
        "githubUrl": project.githubUrl,
        "grade": None,
        "createdAt": now,
        "updatedAt": now,
    }

    # Ajouter à la base de données
    db["projects"].append(new_project)
    save_db(db)

    return Project(**new_project)


@app.get(
    "/projects",
    response_model=List[Project],
    tags=["Projects"],
    summary="Lister tous les projets",
    description="Récupérer la liste complète de tous les projets soumis",
)
def list_projects() -> List[Project]:
    db = load_db()
    return [Project(**project) for project in db["projects"]]


@app.get(
    "/projects/{project_id}",
    response_model=Project,
    tags=["Projects"],
    summary="Obtenir les détails d'un projet",
    description="Récupérer les informations complètes d'un projet spécifique",
)
def get_project(project_id: str) -> Project:
    db = load_db()

    for project in db["projects"]:
        if project["id"] == project_id:
            return Project(**project)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Projet avec l'ID {project_id} non trouvé",
    )


@app.put(
    "/projects/{project_id}/grade",
    response_model=Project,
    tags=["Projects"],
    summary="Noter un projet",
    description="Attribuer une note à un projet (rôle professeur)",
)
def grade_project(project_id: str, grade_data: ProjectGrade) -> Project:
    db = load_db()

    for project in db["projects"]:
        if project["id"] == project_id:
            project["grade"] = grade_data.grade
            project["updatedAt"] = datetime.now().isoformat()
            save_db(db)
            return Project(**project)

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Projet avec l'ID {project_id} non trouvé",
    )


@app.delete(
    "/projects/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Projects"],
    summary="Supprimer une soumission",
    description="Supprimer un projet de la base de données",
)
def delete_project(project_id: str) -> None:
    db = load_db()

    for i, project in enumerate(db["projects"]):
        if project["id"] == project_id:
            db["projects"].pop(i)
            save_db(db)
            return

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Projet avec l'ID {project_id} non trouvé",
    )


@app.get(
    "/projects/course/{course_name}",
    response_model=List[Project],
    tags=["Projects"],
    summary="Filtrer les projets par cours",
    description="Récupérer tous les projets d'un cours spécifique",
)
def get_projects_by_course(course_name: str) -> List[Project]:
    db = load_db()

    projects = [
        Project(**project)
        for project in db["projects"]
        if project["course"].lower() == course_name.lower()
    ]

    if not projects:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Aucun projet trouvé pour le cours '{course_name}'",
        )

    return projects


@app.get(
    "/health",
    tags=["Health"],
    summary="Vérifier la santé de l'API",
    description="Endpoint de vérification de l'état de l'API",
)
 def health_check() -> dict:  # ❌ ERREUR volontaire : indentation incorrecte
    """Vérifier que l'API fonctionne correctement"""
    return {"status": "ok", "message": "ProjetAPI is running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
