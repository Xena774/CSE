states = {
    "CA": "California",
    "NJ": "New Jersey",
    "WI": "Wisconsin",
    "NY": "New York"
}

print(states["CA"])
print(states["WI"])

nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000
    },
    "NY": {
        "NAME": "New York",
        "POPULATION": 19500000
    }
}

print(nested_dictionary["CA"])
print(nested_dictionary["CA"]["POPULATION"])
print(nested_dictionary["NY"]["NAME"])

complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39500000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "NJ": {
        "NAME": "New Jersey",
        "POPULATION": 9000000,
        "CITIES": [
            "Newark",
            "Trenton",
            "Princeton"
        ]
    },
    "WI": {
        "NAME": "Wisconsin",
        "POPULATION": 5800000,
        "CITIES": [
            "Madison",
            "Milwaukee",
            "Green Bay",
        ]
    },
    "NY": {
        "NAME": "New York",
        "POPULATION": 19500000,
        "CITIES": [
            "New York City",
            "Rochester",
            "Buffalo"
        ]
    }
}

print(complex_dictionary["NY"]["CITIES"][0])
print(complex_dictionary["NJ"]["CITIES"][2])

print(complex_dictionary.keys())
print(complex_dictionary.items())
print(nested_dictionary.items())

for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

for state, info in complex_dictionary.items():
    for title, desc in info.items():
        print(title)
        print(desc)
        print("-" * 20)
    print("=" * 20)
