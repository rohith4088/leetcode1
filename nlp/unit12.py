#concordance , similar and common_context
from threading import Condition
import nltk
from nltk.corpus import brown
text = nltk.Text(brown.words())
#concordance helps understand the word usage in diffrenet contexts
#print(text.concordance("women"))

#similar fucntion helps us to understand the occurence of other words in the similar context to the given word
#it helps us to understand of diffrenrt words in similar context possibly identifying synonyms or related words

text = nltk.Text(brown.words())
#print(text.similar("man"))

#common_contexts() shows how two words appear in the same conetxt
#it helps us to guage tye relationship between the words passed

text = nltk.Text(brown.words())
#print(text.common_contexts(["man","woman"]))

#dispresion plots
#dispresion plots are used to know the how and where the words are being used thriugh out the corpus
#nltk.download('reuters')
text1 = nltk.Text(nltk.corpus.reuters.words())
#text1.dispersion_plot(['news','bold','murder'])

#generate()
#generates random texts based on the pattern it has learned from the guiven text.
#it can used  to mimic the style of an author or a text

#.generate()
#print(nltk.__version__)

#generating vocab size of  a text

def vocab(text):
    words = nltk.word_tokenize(text)
    vocabs = set(words)
    return vocabs
text = "This is a sample text with some words. This text is used for demonstration purposes."
print(vocab(text))

#lexical diversity
print(len(set(text))/len(text))

#fine-grained selection words
#Fine-grained selection of words in NLP refers to the process of identifying and categorizing
#words based on subtle distinctions in meaning, usage, or context. This level of analysis allows
#NLP systems to understand language nuances more accurately and make more precise
#decisions in various applications.

def FineGrainSelection(text):
    tokens = nltk.word_tokenize(text)
    unique = [w for w in tokens if len(w) > 3]
    #adding the frequency of the word as the parameter too
    #unique = [w fort w in tokens is len(w) > 3 and nltk.FreqDist(w) > 3]
    return set(sorted(unique))
text = 'this is an example for fine garin selection'
print(FineGrainSelection(text))

#frequencyv distribution of words
#it helps to understand as to which words are more signifinace and has a better contribution to the texts contextual understanding
#The frqDist()
text = brown.words()
#distribution = nltk.FreqDist(text)
#print(distribution.most_common(50))
#distribution.plot(50,cumulative=True)
print("---------------------------")
#to printtyhe unique words that occur only once--> hapaxes
#print(distribution.hapaxes())


#cfd of genders from the names corpus to dtermine the most common male and female nae initials
from nltk.corpus import names
nltk.download('names')
names_corpus = [(name,'male') for name in names.words('male.txt')] + [(name,'female') for name in names.words('female.txt')]
cfd = nltk.ConditionalFreqDist((gender,name[0].lower()) for name,gender in names_corpus)
print(cfd['male'].most_common(5))
print(cfd['female'].most_common(5))

#collocations are nothing but frequent bigram
text3 = nltk.Text(brown.words())
print(list(nltk.bigrams(['most','common'])))
#text3.collocations()

#UNBIT 2 CODES

#ACCESING ELECTRONIC BOOKS

from urllib import request
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
reponse = request.urlopen(url)
raw = reponse.read().decode("utf-8")
print(type(raw))
print(raw[0:75])
tokens = nltk.word_tokenize(raw)
print(type(tokens))
text = nltk.Text(tokens)
print(type(text))
text.collocations()
raw.find("PART I")
raw.rfind("End of Project Gutenberg's Crime")


#using beautiful soup
from bs4 import BeautifulSoup as bs
url ='http://news.bbc.co.uk/2/hi/health/2284783.stm'
html = request.urlopen(url).read().decode('utf-8')
raw = bs(html,'html.parser').get_text()
tokens = nltk.word_tokenize(raw)
print(tokens[:30])

#parsing rss feeds

import feedparser
log = feedparser.parse('http://languagelog.ldc.upenn.edu/nll/?feed=atom')
log['feed']['title']
len(log.entries)
post = log.entries[2]
post.title
content = post.content[0].value
raw = bs(content,'html.parser').get_text()
print(raw[:50])

#finding files using nltk.data.find()
path = nltk.data.find('/Users/rohithr/Desktop/leetcode/stock_prices.csv')
#raw = open(path,'rU')
print("---------------------------------------------------------")

#nlp pipeline code implementation
import requests
from bs4 import BeautifulSoup as bs
url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
html = request.urlopen(url).read().decode('utf-8')
raw = bs(html,'html.parser').get_text()
tokens = nltk.word_tokenize(raw)
print(len(tokens))
print(tokens[:30])
text = nltk.Text(tokens)
print(text.concordance('similar'))
print(text.collocations())




#assesing wordnet's cincept hierrachy
from nltk.corpus import wordnet as wn

# Retrieve the synset for 'motorcar'
motorcar_synset = wn.synset('car.n.01')

# Get hyponyms of 'motorcar'
types_of_motorcar = motorcar_synset.hyponyms()

# Accessing the first hyponym directly might not always be meaningful without checking if there are any hyponyms
if types_of_motorcar:
    print(types_of_motorcar[0])  # Example output: Synset('ambulance.n.01')

# Generate a sorted list of lemma names for all hyponyms
sorted_lemmas = sorted(lemma.name() for synset in types_of_motorcar for lemma in synset.lemmas())

# Print the sorted list of lemma names
for lemma_name in sorted_lemmas:
    print(lemma_name)

print("----------------------------")
#similar frequency distribution table
cfd = nltk.ConditionalFreqDist((genre,word) for genre in brown.categories() for word in brown.words(categories = genre))
genre = genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
#cfd.tabulate(Condition = genre,sampels = modals)

#extracting encoded text from files
nltk.download('unicode_samples')
path = nltk.data.find('corpora/unicode_samples/polish-lat2.txt')
file = open(path,encoding = 'latin2')
for char in file:
    tokens = char.split()
    print(tokens)
    #print(tokens.encode('unicode_escape'))
print("--------------------------")
#the re module
import re
sample_text = "this is a sample to asses the importanceof re moudle"
res = [w for w in nltk.word_tokenize(sample_text) if re.search('^.a.m.l$',w)]
print(res)
#res1 = [w for w in nltk.corpus.brown.words(categories = 'news') if re.search('^[a-z]+[r-n]$',w)]
#print(res1)


#segmentation usinf python
def segment(text,segs):
    word = []
    last = 0
    for i in range(len(segs)):
        word.append(text[last:i+1])
        last =i+1
    word.append(text[last:])
    return word
text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 = "0100100100100001001001000010100100010010000100010010000"
segment(text, seg1)
segment(text,seg2)
def evaluate(text,segs):
    words = segment(text,segs)
    size = len(words)
    lexicon_size = sum(len(word) + 1 for word in set(words))
    return size + lexicon_size


#including multiple languages from the udhr corpus
nltk.download('udhr')
from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist((lang,len(word)) for lang in languages for word in udhr.words(lang+'-Latin1'))
#cfd.plot(cumulative=True)


#getting insights inot the gutenberg corpus
nltk.download('gutenberg')
from nltk.corpus import gutenberg
for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sent = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    print(num_chars/num_words)
    print(num_words/num_sent)
    print(num_words/num_vocab)

#re module

import re
pattern = r'D*'
text = "this is Data science"
if re.search(pattern,text):
    print("yes")
else:
    print("no")

#removing white spaces
def RemoveWhiteSpace(text):
    text = text.strip()
    text = re.sub(r'\s+',' ',text)
    return text
text = '  this sentence     contains whitespaces'
print(RemoveWhiteSpace(text))

#truncate the suffix
def truncatesuffix(text):
    for char in  ['ing','ed','ly','ious']:
        if text.endswith(char):
            return text[:-len(char)]
    return text
print(truncatesuffix("playing"))
