from fastapi import APIRouter
from src.application.use_cases import GetEmployeesUseCase  # Correct import
from src.infrastructure.repositories import EmployeeRepository  # Correct import
from src.domain.models import Employee  # Correct import

router = APIRouter()

# Initialize repository and use case
employee_repository = EmployeeRepository()
get_employees_use_case = GetEmployeesUseCase(employee_repository)

# GET endpoint to retrieve all employees
@router.get("/employees", response_model=list[Employee])
def get_employees():
    """Fetch all employees."""
    return get_employees_use_case.execute()