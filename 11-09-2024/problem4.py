def list_planets():
    return ["Mercury", "Venus", "Earth", "Mars"]

def distance_from_sun(planet):
    distances = {
        "Mercury": "57.9 million km",
        "Venus": "108.2 million km",
        "Earth": "149.6 million km",
        "Mars": "227.9 million km"
    }
    return distances.get(planet, "an unknown distance")

planets = list_planets()
for planet in planets:
    print(f"{planet} is {distance_from_sun(planet)} away from the Sun.")