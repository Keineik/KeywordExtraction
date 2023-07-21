import yake

with open ('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
	
max_ngram_size = 5
deduplication_threshold = 0.4
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 20
custom_kw_extractor = yake.KeywordExtractor(n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

for kw in keywords:
	print(kw[0], end = ", ")