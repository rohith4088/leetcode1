#concordance , similar and common_context
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
nltk.download('reuters')
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

print(len(set(text))/len(text))
