import pandas as pd
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.corpus import stopwords

data = pd.Series(["hello", "world", "nlp", "rocks"])
english_stopwords = stopwords.words('english')

# df = pd.DataFrame({
#     'text': ["Hello world", "NLP is awesome", "Text processing","Text processing"],
#     'label': [1, 0, 1,1]
# })


df = pd.read_csv("resources/tripadvisor_hotel_reviews.csv")
df["Review"] = df["Review"].str.lower()
df["Review"] = df["Review"].str.replace("[^\w\s]", "", regex=True)

df['Token'] = df['Review'].apply(nltk.word_tokenize)
df['Filtered_Token'] = df['Review'].apply(lambda Token : [t for t in Token if t.lower() not in english_stopwords ])

print(df)
