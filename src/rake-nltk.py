from rake_nltk import Rake
import nltk

nltk.download('stopwords')
nltk.download('punkt')
r = Rake()
with open('text.txt', encoding="utf-8") as f:
  my_text = f.read()
r.extract_keywords_from_text(my_text)
keywordList           = []
rankedList            = r.get_ranked_phrases_with_scores()
for keyword in rankedList:
  keyword_updated       = keyword[1].split()
  keyword_updated_string    = " ".join(keyword_updated[:5])
  keywordList.append(keyword_updated_string)
count = 0
for i in keywordList:
  if (count == 20): break
  print(i, end=", ")
  count += 1