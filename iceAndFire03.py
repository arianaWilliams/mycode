#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    ## send https get to the api of ice and fire books resource
    gotresp = requests.get(AOIF_BOOKS)

    ## decode the response
    got_dj = gotresp.json()

    ## loop across resonse
    for singlebook in got_dj:
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tPFI URL -> {singlebook['url']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")
if __name__ == "__main__":
    main()
