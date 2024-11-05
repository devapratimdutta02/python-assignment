def list_countries():
    return ["India", "USA", "Germany", "Australia"]

def capital_of(country):
    capitals = {
        "India": "New Delhi",
        "USA": "Washington, D.C.",
        "Germany": "Berlin",
        "Australia": "Canberra"
    }
    return capitals.get(country, "Unknown Capital")

countries = list_countries()
for country in countries:
    print(f"The capital of {country} is {capital_of(country)}.")