from elasticsearch import Elasticsearch
import json
import requests

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200/")

# URL for the raw data file on GitHub
url = "https://raw.githubusercontent.com/egunadi/dsci550-hw-dataviz/main/d3_plot/subset_data/Butterfly%20Plot_Narrative%20Length%20vs%20AgeGender.json"

# Download the JSON file
response = requests.get(url)
json_data = response.json()
print(json_data)

# index the JSON data into Elasticsearch
index_name = "butterfly_index"

for item in json_data:
    es.index(index=index_name, body=item)


# Search query
search_query = {
    "query": {
        "match_all": {}
    }
}

# Execute search query
search_results = es.search(index=index_name, body=search_query)

# Print search results
print(search_results)