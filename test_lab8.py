from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name   : Ravi\n"
        "Employee ID     : 101\n"
        "Department      : IT\n"
        "Salary          : 50000"
    )

    assert employee_details("Alice","E1001","IT",55000) == expected_output
