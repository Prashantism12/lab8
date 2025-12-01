from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name   : Ravi\n"
        "Employee ID     : E1001\n"
        "Department      : IT\n"
        "Salary          : 550000"
    )

    assert employee_details("Alice","E1001","IT",55000) == expected_output
