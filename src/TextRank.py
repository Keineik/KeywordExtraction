import spacy
import pytextrank

with open ('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")
doc = nlp(text)
# examine the top-ranked phrases in the document
for phrase in doc._.phrases[:20]:
    print(phrase.text, end = ", ")