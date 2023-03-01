import requests


# get the API KEY here: https://developers.google.com/custom-search/v1/overview
API_KEY = "AIzaSyCrVM9MLoGDkRd-fkYQzVyZgU7PMdARIIw"
# get your Search Engine ID on your CSE control panel
SEARCH_ENGINE_ID = "77944f04abb4f40a1"
# the search query you want, from the command line (e.g python search_engine.py 'python')
query='alexis.l.wilson@bofa.com site:linkedin.com'

url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}"

# make the API request
data = requests.get(url).json()
# get the result items
search_items = data.get("items")
# iterate over 10 results found
for i, search_item in enumerate(search_items, start=1):
    
    # get the page title
    title = search_item.get("title")
    # page snippet
    
    # alternatively, you can get the HTML snippet (bolded keywords)
   
    # extract the page url
    link = search_item.get("link")
    # print the results
    print("Title:", title)
    
    print("URL:", link, "\n")
    break