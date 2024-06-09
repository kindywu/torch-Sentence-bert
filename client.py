import requests
import json
from scipy import spatial

sentences = ["这是一首简单的小情歌", "这是一首周杰伦唱的情歌", "Hello World"]
sbert_api = "http://localhost:3000"
# response = requests.post(sbert_api+"/predictions/sentence_Transformer_BERT",
#                          data={'data': json.dumps({"queries": sentences})})

response = requests.post(sbert_api+"/predictions/SBERT",
                         data={'data': json.dumps({"queries": sentences})})

if response.status_code == 200:
    vectors = response.json()
    similarity = 1 - spatial.distance.cosine(vectors[0], vectors[1])
    print(round(similarity, 3))
    similarity = 1 - spatial.distance.cosine(vectors[1], vectors[2])
    print(round(similarity, 3))
    similarity = 1 - spatial.distance.cosine(vectors[0], vectors[2])
    print(round(similarity, 3))
else:
    print(response.content)
