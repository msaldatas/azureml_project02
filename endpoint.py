import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://fd59d40d-1b79-463f-803e-83b3b2468e76.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "KOQtdVqT3qsBdifroR0hg4apkd8DQnTs"

# Two sets of data to score, so we get two results back
data = {
    "data": [
        {
      "age": 0,
      "job": "admin",
      "marital": "divorced",
      "education": "university.degree",
      "default": "no",
      "housing": "yes",
      "loan": "yes",
      "contact": "cellular",
      "month": "may",
      "day_of_week": "thu",
      "duration": 120,
      "campaign": 2,
      "pdays": 999,
      "previous": 1,
      "poutcome": "failure",
      "emp.var.rate": 1.4,
      "cons.price.idx": 93.99,
      "cons.conf.idx": -36.40,
      "euribor3m": 4.96,
      "nr.employed": 5228.1
    },
    ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
