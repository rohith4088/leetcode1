import nltk
#some codes related to dictionary
#incrementally updating the dictonary
from collections import defaultdict
counts = defaultdict(int)
for(word,tag) in nltk.corpus.brown.tagged_words(categories = 'news',tagset = 'universal'):
    counts[tag] += 1
print(counts['NOUN'])
print(sorted(counts))

#transformation based tagging
#brill-tagginf demo
from nltk.tbl import demo
#nltk.download('treebank')
#demo.demo()

#default tagging
from nltk.tag import DefaultTagger
tags = [tag for (word,tag) in nltk.corpus.brown.tagged_words(categories = 'news')]
nltk.FreqDist(tags).max()

text = "this is an exmpale for default tagger"
tokens = nltk.word_tokenize(text)
tagging = nltk.tag.DefaultTagger('NN')
tag = tagging.tag(tokens)
print(tag)
