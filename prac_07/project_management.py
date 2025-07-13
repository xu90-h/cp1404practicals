from project import Project
from datetime import datetime

FILENAME = "projects.txt"

def load_projects(filename):
    """Load the project from the file."""
    projects = []
    with open(filename, 'r') as in_file:
        next(in_file)  # skip header
        for line in in_file:
            parts = line.strip().split('\t')
            project = Project(*parts)
            projects.append(project)
    return projects

