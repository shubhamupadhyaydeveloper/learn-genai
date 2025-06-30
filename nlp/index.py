import nltk
import matplotlib.pyplot as plt
nltk.download('stopwords')

from nltk.corpus import stopwords

all_stop_words = stopwords.words('english')
all_stop_words.remove('from')

sentence = 'hi my name is shubham upadhyay and i am living in delhi i am came from uttar pradesh'

new_sentence = [x for x in sentence.split() if x not in all_stop_words]
# print('new setence',new_sentence)

# regular expression
import re

find_all = re.findall(r"\D+",'The numbers are 12 134 24')
# print(find_all)

dog_string = 'i love cats ,all cats are very good'
change_to_dogs = re.sub('cats','dogs',dog_string)
# print(change_to_dogs)

people_reviews = ['hi shubham review','hi suraj review','hi golu review','hi bholu review']

shubham_reviews = [x for x in people_reviews if re.search(r"shubham", x)]
h_reviews = [x for x in people_reviews if re.search(r"w$",x)]
print(shubham_reviews)
print(h_reviews)

# tokenisation
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize,sent_tokenize

token_sentence = 'Hi my name is shubham upadhyay. my friend name is react'
print(word_tokenize(token_sentence))

# stemming
from nltk.stem import PorterStemmer
ps = PorterStemmer()

connect_tokens = ['connecting','connects','connected']
stem_tokens = [ps.stem(x) for x in connect_tokens]
print(stem_tokens)

# lemmatization
nltk.download('wordnet')
from  nltk.stem import WordNetLemmatizer

lm = WordNetLemmatizer()
connect_tokens = ['connecting','connects','connected']
lemm_tokens = [lm.lemmatize(x) for x in connect_tokens]
print(lemm_tokens)

# n grams
import pandas as pd
import matplotlib.pyplot as plt

tokens = ['the','rise','of','artificial','intellegence','has','led','to','significiant','advancements','in','the','ai']

unigrams = pd.Series(nltk.ngrams(tokens,1)).value_counts()
unigrams[:10].sort_values().plot.barh(color='orange',width=9,figsize=(12,8))
plt.title('import unigrmas')
plt.show()