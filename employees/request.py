EMPLOYEES = [
    {
      "name": "Kurt Russel",
      "locationId": 3,
      "animalId": 3,
      "id": 6
    },
    {
      "name": "Chris Johnson",
      "locationId": 3,
      "animalId": 3,
      "id": 7
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee