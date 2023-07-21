from keybert import KeyBERT

with open ('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
kw_model = KeyBERT(model='all-MiniLM-L6-v2')
keywords = kw_model.extract_keywords(
    text, 
    keyphrase_ngram_range=(2, 5), 
    stop_words=None, 
    use_mmr=True,
    diversity=0.4,
    nr_candidates=20,
    top_n=20
    )

for words in keywords:
    print(words[0], end=", ")