from googlesearch import search

def gSearch(query : str) -> str: 
  
  for item in search(query, tld = "co.in", num=10, stop = 10, pause = 2):
    print(item) 


# This is the text that you want to search for.
query = input("Enter your query : ")
  
# Search Function called
gSearch(query)