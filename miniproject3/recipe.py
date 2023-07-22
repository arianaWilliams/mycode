#!/usr/bin/python3
'''inciate a get request from EDAMAM to get recipes that are rendered for the user to view via html. Practice using GET request from an api and GET & POST request to flask'''

# imported libraries
import database
import requests
import json
from pprint import pprint
from jinja2 import Environment, FileSystemLoader
import os
from flask import Flask, render_template, request, session


app = Flask(__name__)
app.secret_key = "not_very_secret"
# base link to api
EDAMAM = 'https://api.edamam.com/api/recipes/v2?type=public&'

# handles the get request from api and converts the .json() to a dictionary then
# returns a list of useable values
def recipeSearch(myid, mykey, search_string):
    # api url with hidden key and id
    api = f"{EDAMAM}app_id={myid}&app_key={mykey}&imageSize=THUMBNAIL&q={search_string}&from=1&to=10"
    # API call
    resp = requests.get(api)

    # check if request is successful
    if resp.status_code == 200:
        # render the resp as a python dictionary
        data = resp.json()
        # print the data in a more legible way
        pprint(data)
        # create an empty list for the recipe data
        recipes = []
        # create an index
        count = 1

        # Only get relevant info
        hits = data.get("hits", [])
        # iterate over the hits to get each one
        for  hit in hits:
            # get the recipe
            recipe = hit.get("recipe", {})
            # get the thumbnail url
            thumbnail_url = recipe.get("image", "")

            # get the label
            label = recipe.get("label", "")

            # get ingredients as a list
            ingredients = recipe.get("ingredientLines", [])

            # get the source and its URL
            source_name = recipe.get("source", "")
            source_url = recipe.get("url", "")
             # add the data to the list for html view
            recipes.append({"thumbnail_url": thumbnail_url,
                "label": label,
                "ingredients": ingredients,
                "source_url": source_url,
                "recipe_index": count
            })
            count +=1 # increment the count for the index

            # Print the info
            print("Thumbnail Image URL:", thumbnail_url)
            print("label:", label)
            print("Ingredients:")
            for ingredient in ingredients:
              print("-", ingredient)
              print("Source Name:", source_name)
              print("Source URL:", source_url)
              print("---------------------")
    else:
        # if the resp is not successful print the resp code
        print("Error:", resp.status_code)
    # return the recipe list
    return recipes

def harvestid():
    with open("/OneDrive/Documents/Projects/python/apiid.pub") as apiidfile:
        return apiidfile.read().rstrip("\n") # get the api id

def harvestkey():
    with open("/OneDrive/Documents/Projects/python/apikey.priv") as apikeyfile:
        return apikeyfile.read().rstrip("\n") # get the api key

def create_html(recipes):
    # give the path to my template files
    template_env = Environment(loader=FileSystemLoader(os.path.abspath("./templates")))
    template = template_env.get_template("recipephotocard.html")
    return template.render(recipe=recipes)

@app.route("/", methods=["GET", "POST"])
def search_recipes():
    if request.method == "POST":
      # get the search string the user is trying to search for
      search_string = request.form.get("search_string")
      # get api id
      myid = harvestid()
      # get api key
      mykey = harvestkey()
      # create the call to the recipeSearch function with the correct parameters
      recipe_data_list = recipeSearch(myid, mykey, search_string)

      if recipe_data_list:
          # convert the list to a dictionary
          recipe_data_dict = {recipe['recipe_id']: recipe for recipe in recipe_data_list}
          # store the recipe data in the session
          session["set_recipe_data"] = recipe_data_list
          print("recipe dictionary:", recipe_data_dict)
          # set the html content with the call to the create_html function
          html_content = create_html(recipe_data_list)

          # open the html template file and write the html content to it
          with open("recipephotocard.html", "w") as file:
            file.write(html_content)
            # print a helpful statement
            print("HTML file 'recipephotocard.html' created successfully!")
            # return the filled out html template
            return render_template("recipephotocard.html", recipes=recipe_data_list)
      else:
            # return a helpful error message
            return "No recipes found for that search."
    return render_template("home.html")

@app.route("/save_recipe", methods=["POST"])
def save_recipe():
    if request.method == "POST":
        recipe_index = request.form.get("recipe_index")
        print("Recipe Index from Form:", recipe_index)
        if recipe_index is not None:
            try:
                recipe_index = int(recipe_index)
                print("Converted Recipe Index:", recipe_index)
                recipe_data_dict = session.get("set_recipe_data", [])
                print(f"dictionary length = {len(recipe_data_dict)}")
                if 0 <= recipe_index < len(recipe_data_dict):
                    recipe_to_save = recipe_data_dict[recipe_index]
                    database.insert_recipe(recipe_to_save)
                    return "Recipe saved successfully!"
                else:
                    return f"value {recipe_index}. out of bounds the length of list is {len(recipe_data_dict)}"
            except ValueError:
                return f"Invalid: {recipe_index}. Please try again."
        return "no recipe_index provided."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224, debug= True)