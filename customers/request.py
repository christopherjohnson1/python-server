CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct."
    },
    {
      "id": 2,
      "name": "Mike Cool",
      "address": "4931 Stormy Dr."
    },
    {
      "id": 3,
      "name": "Samantha Blackwell",
      "address": "2945 River Rd."
    },
    {
      "id": 4,
      "name": "David McDavidson",
      "address": "731 Main St."
    },
    {
      "email": "christopherjohnson1@gmail.com",
      "password": "me",
      "name": "Chris Johnson",
      "id": 5
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer