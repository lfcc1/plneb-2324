filename = "../../data/CIH Bilingual Medical Glossary English-Spanish.txt"

file = open(filename)
text = file.read()

# Remover pontuação
text = text.replace("."," ")
text = text.replace(","," ")
text = text.replace("-"," ")
# ...

text = text.lower()

# Dividir o texto por tokens
anagramas = {}
tokens = text.split()

# remover repetidos
tokens = list(set(tokens))




