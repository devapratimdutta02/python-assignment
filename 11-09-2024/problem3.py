def list_animals():
    return ["Dog", "Cat", "Cow", "Lion"]

def animal_sound(animal):
    sounds = {
        "Dog": "barks",
        "Cat": "meows",
        "Cow": "moos",
        "Lion": "roars"
    }
    return sounds.get(animal, "makes an unknown sound")

animals = list_animals()
for animal in animals:
    print(f"A {animal} {animal_sound(animal)}.")
