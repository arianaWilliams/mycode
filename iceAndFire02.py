#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import pprint
import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## Send https get to the api of ice and fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## decode the response
    got_dj = gotresp.json()

    ## print the response
    ## useing pretty print so we can read it
    pprint.pprint(got_dj)

if __name__ == "__main__":
    main()
