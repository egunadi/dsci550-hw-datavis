from elasticsearch import Elasticsearch
import csv
import requests 

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200/")

# URL for the raw data file on GitHub
url = 'https://raw.githubusercontent.com/egunadi/dsci550-hw-dataviz/main/d3_plot/subset_data/avg_toxicity_age_gender.csv'

# Download the TSV file
response = requests.get(url)
data = response.content.decode('utf-8').split('\n')

# Remove the header row
header = data[0].split('\t')
data.pop(0)

# Index each row in Elasticsearch
for line in data:
    row = {}
    fields = line.split('\t')
    for i in range(len(header)):
        row[header[i]] = fields[i]
    es.index(index='avg_toxicity_index', body=row)

# Search query
res = es.search(index="avg_toxicity_index", body={"query": {"match_all": {}}})

for hit in res['hits']['hits']:
    print(hit['_source'])