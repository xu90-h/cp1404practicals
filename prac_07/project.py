from datetime import datetime

class Project:
    """Display project information."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def is_complete(self):
        """Check if the project has been completed."""
        return self.completion_percentage >= 100

    def __lt__(self, other):
        """Define priority comparison."""
        return self.priority < other.priority
