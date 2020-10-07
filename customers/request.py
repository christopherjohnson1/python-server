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

def create_customer(customer):
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer