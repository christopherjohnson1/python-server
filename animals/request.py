ANIMALS = [
    {
      "id": 3,
      "name": "Nilla",
      "breed": "Golden Retriever",
      "locationId": 3,
      "treatment": "Nails trimmed, and ears cleaned.",
      "customerId": 5
    },
    {
      "id": 4,
      "name": "Sully",
      "breed": "Terrier/ Pit Mix",
      "locationId": 2,
      "treatment": "Lots of petting",
      "customerId": 5
    },
    {
      "id": 6,
      "name": "Gracie",
      "breed": "Another Doodle",
      "locationId": 1,
      "treatment": "Fatty lipoma removed",
      "customerId": 5
    },
    {
      "id": 7,
      "name": "Shitty",
      "breed": "Kitty",
      "locationId": 2,
      "treatment": "Behavioral treatment to be less shitty ",
      "customerId": 5
    }
]

def get_all_animals():
    return ANIMALS

    # Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal