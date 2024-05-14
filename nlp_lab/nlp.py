import nltk
from nltk.corpus import brown
from nltk.tag import UnigramTagger
fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = list(fd.keys())[:100]
likely_tags = dict((words,cfd[words].max()) for words in most_freq_words)
tagger = UnigramTagger(model = likely_tags,backoff = nltk.DefaultTagger('NN'))
brown_news_tagged = brown.tagged_words(categories='news')
tagged_sents = brown.tagged_sents(categories='news')
# print(tagger.evaluate(brown_news_tagged)
nltk.download('indian')
nltk.download('omw-1.4')

# from nltk.corpus import brown
# from nltk.probability import FreqDist

# tagged_sent = brown.tagged_sents(categories = 'news')
# tags = [tag for sent in tagged_sent for (words,tag) in sent]
# fd = FreqDist(tags)
# print(fd.most_common(10))

# unigram tagger
# from nltk.tag import UnigramTagger
# tagged_sents = brown.tagged_sents(categories = 'news')
# sents = brown.sents(categories = 'news')
# tagger = UnigramTagger(tagged_sents)
# print(tagger.tag(sents[2007]))

# from nltk.tbl import demo as brill_demo
# brill_demo.demo()


# tagged_words = nltk.tag.str2tuple('fly/NN')
# print(tagged_words)
# print(tagged_words[0])
# print(tagged_words[1])
# print(nltk.corpus.brown.tagged_words())
# print(nltk.corpus.brown.tagged_words(tagset = 'universal'))
# print(nltk.corpus.indian.tagged_words())
# #most common news category in brown corpus
# tagged = nltk.corpus.brown.tagged_words(categories = 'news',tagset = 'universal')
# fd_tagged = nltk.FreqDist(tag for(word,tag) in tagged)
# print(fd_tagged.most_common)