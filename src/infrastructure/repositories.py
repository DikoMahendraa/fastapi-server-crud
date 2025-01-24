from typing import List
from src.domain.models import Employee

# In-memory "database"
employees_db = [
    Employee(id=1, name="John Doe", ass="johndoe", email="john@example.com", role="Developer"),
    Employee(id=2, name="Jane Smith", username="janesmith", email="jane@example.com", role="Manager"),
]

class EmployeeRepository:
    def get_all(self) -> List[Employee]:
        """Return all employees."""
        return employees_db