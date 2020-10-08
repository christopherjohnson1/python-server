CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct.",
      "status": "Loyal Customer"
    },
    {
      "id": 2,
      "name": "Mike Cool",
      "address": "4931 Stormy Dr.",
      "status": "Loyal Customer"
    },
    {
      "id": 3,
      "name": "Samantha Blackwell",
      "address": "2945 River Rd.",
      "status": "Loyal Customer"
    },
    {
      "id": 4,
      "name": "David McDavidson",
      "address": "731 Main St.",
      "status": "Loyal Customer"
    },
    {
      "email": "christopherjohnson1@gmail.com",
      "password": "me",
      "name": "Chris Johnson",
      "id": 5,
      "status": "Loyal Customer"
    }
]

def update_customer(id, new_customer):
    # Iterate the CUSTOMERS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break

def delete_customer(id):
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the CUSTOMERS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

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