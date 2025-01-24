from typing import List
from src.domain.models import Employee
from src.infrastructure.repositories import EmployeeRepository

class GetEmployeesUseCase:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def execute(self) -> List[Employee]:
        """Fetch all employees."""
        return self.employee_repository.get_all()