from Bio import Entrez
import pandas as pd
import ssl
import urllib.request

#Disabled SSL certification, as there was difficulty accessing the URL via MacOS.
context = ssl._create_unverified_context()

url = "https://www.ncbi.nlm.nih.gov/nucleotide"
response = urllib.request.urlopen(url, context=context)

def search_genbank(species_code):
    Entrez.email = 'EMAIL' #Update with user's email
    handle = Entrez.efetch(db = 'nucleotide', id = species_code, retmode = 'xml') #db specifies the database of interest. Any database should work with this script.
    record = Entrez.read(handle)
    handle.close()
    definition = record[0]['GBSeq_definition'] #"Definition" was the variable of interest from the database. However, this can be changed to any variable found within a specific database
    return definition

species_codes = [] #Insert species code(s) of interest or upload file containing codes here
for code in species_codes:
    definition = search_genbank(code)
    print(definition)
