from gensim.models import Word2Vec
from gensim.utils import tokenize
import json

f = open("ata_medica.json")
papers = json.load(f)
tokens = []

for id, paper_info in papers.items():
    tokens_title = list(tokenize(paper_info["title"], lower=True))
    if "abstract" in paper_info:
        tokens_abstract = list(tokenize(paper_info["abstract"], lower=True))
        tokens.append(tokens_abstract)
    tokens.append(tokens_title)


model = Word2Vec(tokens, min_count=1, vector_size=300, epochs=20)

model.save("ata_medica.w2v")