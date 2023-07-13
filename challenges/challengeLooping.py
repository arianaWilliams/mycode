#!/usr/bin/env python

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

NE_animals = farms[0]["agriculture"]
W_animals = farms[1]["agriculture"]
SE_animals = farms[2]["agriculture"]

for animals in NE_animals:
    print(animals)

farm_names = [farm["name"] for farm in farms]
veg = ["carrots", "celery"]

user_choice = input("Please choose a farm NE farm, W Farm, or SE Farm")

if user_choice in farm_names: 
    if user_choice == "NE Farm":
        for animals in NE_animals:
            print(animals)
    elif user_choice == "W Farm":
        for animals in W_animals:
            print(animals)
    elif user_choice == "SE Farm":
        for animals in SE_animals:
            if animals not in veg:
                print(animals)
else: 
    print("Please choose a valid farm name")


