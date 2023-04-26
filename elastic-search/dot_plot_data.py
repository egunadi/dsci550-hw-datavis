from elasticsearch import Elasticsearch
import json
import requests

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200/")

# URL for the raw data file on GitHub
url = "https://raw.githubusercontent.com/egunadi/dsci550-hw-dataviz/main/d3_plot/subset_data/data.json"

# Download the JSON file
response = requests.get(url)
json_data = response.json()['data']
# print(json_data)

# index the JSON data into Elasticsearch
index_name = "dot_plot_data"

for item in json_data:
    es.index(index=index_name, body=item) 

# Get the mapping of the index
# mapping = es.indices.get_mapping(index=index_name)
#print(mapping)

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