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

def save_projects(projects, filename):
    """Save the project to a file."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {filename}")


def display_projects(projects):
    """Display the project, which is divided into completed and unfinished."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")

    print("\nCompleted projects:")
    for project in sorted(complete):
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter items by date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

        filtered_projects = [p for p in projects if p.start_date > filter_date]
        for project in sorted(filtered_projects, key=lambda x: x.start_date):
            print(project)
    except ValueError:
        print("Invalid date format")


def add_new_project(projects):
    """Add new items."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: ")
    completion = input("Percent complete: ")

    try:
        project = Project(name, start_date, priority, cost_estimate, completion)
        projects.append(project)
    except ValueError as e:
        print(f"Invalid input: {e}")


def update_project(projects):
    """Update project information."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            print(project)

            new_completion = input("New Percentage (leave blank to retain existing): ")
            if new_completion:
                project.completion_percentage = int(new_completion)

            new_priority = input("New Priority (leave blank to retain existing): ")
            if new_priority:
                project.priority = int(new_priority)
        else:
            print("Invalid project number")
    except ValueError:
        print("Invalid input")