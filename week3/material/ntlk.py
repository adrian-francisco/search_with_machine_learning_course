import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

str = "brand new iphone 13"

nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(str)))