from employee import get_employee_details

def test_get_employee_details():
    name = "Ravi"
    emp_id = 101
    department = "IT"
    salary = 50000

    expected_output = (
        "Employee Name   : Ravi\n"
        "Employee ID     : 101\n"
        "Department      : IT\n"
        "Salary          : 50000"
    )

    result = get_employee_details(name, emp_id, department, salary)

    assert result == expected_output
