classinfo = {
    "all": [
        {
            "name": "Ariana",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Lily",
            "skill level": "admirable",
            "spirit animal": "Shark",
            "super power": "Super Strength",
        },
        {
            "name": "Eric",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Exxon",
            "skill level": "astonishing",
            "spirit animal": "Banana",
            "super power": "Flight",
        },
        {
            "name": "Jason",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "James",
            "skill level": "brilliant",
            "spirit animal": "Eagle",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Kevin",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Michael",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Immobility",
        },
        {
            "name": "Raylan",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Immutability",
        },
        {
            "name": "Richard",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Joseph",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Jet Propulsion",
        },
        {
            "name": "Josia",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "Kendra",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "Tito",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Ryan",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Nail Manipulation",
        },
        {
            "name": "Sabin",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Sheraz",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Sonic Voice",
        },
        {
            "name": "Sunny",
            "skill level": "remarkable",
            "spirit animal": "Alpaca",
            "super power": "Hydrokinesis",
        },
    ]
}
me = classinfo['all'][0]
name = me['name']
print(name)

skill_level = me['skill level']
spirit_animal = me['spirit animal']
super_power = me['super power']
print(f'My name is {name} and my sprit animal is {spirit_animal}.')
print(f'My name is {name} and my skills are {skill_level}.')
print(f'My name is {name} and my super power is {super_power}.')

myclass = classinfo['all']
for i in myclass:
    name = i["name"]
    skill= i["skill level"]
    power = i["super power"]
    animal = i["spirit animal"]
    print(f"{name}, a {skill} {animal} of a programmer, posseses a {power} factor for moonlightin as a superhero!")
