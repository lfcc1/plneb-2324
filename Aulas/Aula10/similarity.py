from gensim.models import Word2Vec
from gensim.utils import tokenize
import json
import numpy as np
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))


model = Word2Vec.load("ata_medica.w2v")
#print(model.wv.most_similar("cancro"))
f = open("ata_medica.json")
papers = json.load(f)


query = "doenças dos olhos"
def get_mean_vector(text):
    vectors = [model.wv[token] for token in tokenize(text, lower=True) if token not in stop_words]
    mean = np.mean(vectors, axis = 0)
    return mean

def cosine(v1, v2):
    return np.dot(v1,v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

sims = []
query_vector = get_mean_vector(query)
for id, paper_info in papers.items():
    title_vector =  get_mean_vector(paper_info["title"])
    sim = cosine(query_vector,title_vector)
    sims.append((id,sim))

sorted_sims = sorted(sims,key=lambda x : x[1], reverse=True)

for id, sim in sorted_sims[:20]:
    print(sim, papers[id]["title"])
