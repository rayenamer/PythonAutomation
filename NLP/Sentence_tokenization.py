import nltk

from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')


lemmatizer = WordNetLemmatizer()

def lemma_me(sent):
    sentence_tokens = nltk.word_tokenize(sent.lower())
    pos_tags = nltk.pos_tag(sentence_tokens)

    sentence_lemmas = []
    for token, pos_tag in zip(sentence_tokens, pos_tags):
        if pos_tag[1][0].lower() in ['n', 'v', 'a', 'r']:
            lemma = lemmatizer.lemmatize(token, pos_tag[1][0].lower())
            sentence_lemmas.append(lemma)

    return sentence_lemmas

tv = TfidfVectorizer(tokenizer=lemma_me)

text = 'Originally, vegetables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked.'
question = 'What are vegetables?'

sentence_tokens = nltk.sent_tokenize(text)
sentence_tokens.append(question)
sentence_tokens

tf = tv.fit_transform(sentence_tokens)
tf.toarray()
df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())


values = cosine_similarity(tf[-1], tf)
index = values.argsort()[0][-2]
values_flat = values.flatten()
values_flat.sort()
coeff = values_flat[-2]
if coeff > 0.3:
    print(sentence_tokens[index])
