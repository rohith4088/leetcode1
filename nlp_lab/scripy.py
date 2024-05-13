#1,2,3,4,6,7,8,9,10,11
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import brown
from collections import Counter
nltk.download('stopwords')
def main():
    ps = PorterStemmer()
    wnl = WordNetLemmatizer()
    def remove_stopwords(text):
        words = word_tokenize(text)
        stop_words = set(stopwords.words("english"))
        filtered = [word for word in words if word not in stop_words]
        return " ".join(filtered)
    def stemming(text):
        words = word_tokenize(text)
        print("{0:20}{1:20}".format("Word", "Stemmed Word"))
        for word in words:
            print("{0:20}{1:20}".format(word, ps.stem(word)))
    def lemmatization(text):
        words = word_tokenize(text)
        print("{0:20}{1:20}".format("Word", "Lemmatized Word"))
        for word in words:
            print("{0:20}{1:20}".format(word, wnl.lemmatize(word, pos="v")))
    def remove_special_characters(text):
        text = text.strip()
        text = re.sub(r'\s+',' ',text)
        return text

    def wh_words(text):
        words = word_tokenize(text)
        stop_words = set(stopwords.words("english"))
        wh = [word for word in words if word.lower().startswith("wh") and word not in stop_words]
        return wh.sort()
    def word_freq():
        words = brown.words(categories = "news")
        freq = nltk.FreqDist(words)
        for word, frequency in freq.items():
            print("{0:20}{1:20}".format(word, frequency))
    def frequent_bigram(tetx,n):
        words = word_tokenize(text)
        stop_words = set(stopwords.words("english"))
        filtered_bigram = [bigram for bigram in nltk.bigrams(words) if bigram[0] not in stop_words and bigram[1] not in stop_words]
        return nltk.FreqDist(filtered_bigram).most_common(n)
    def most_common(text):
        words = word_tokenize(text)
        stop_words = set(stopwords.words("english"))
        filtered = [word for word in words if word not in stop_words]
        return nltk.FreqDist(filtered).most_common(5)
    def common_words():
        words = brown.words(categories = 'news')
        word_count = Counter(words)
        common_words = [word for word,count in word_count.items() if count > 3]
        return common_words
    text = " I am learning Natural Language Processing "
    print("Original Text:", text)
    print("Text after removing stopwords:", remove_stopwords(text))
    print("Stemming:")
    stemming(text)
    print("Lemmatization:")
    lemmatization(text)
    print("Text after removing special characters:", remove_special_characters(text))
    print("Wh words:", wh_words(text))
    print("Word Frequency:")
    word_freq()
    print("Frequent Bigrams:", frequent_bigram(text, 5))
    print("Most Common Words:", most_common(text))
    print("Common Words:", common_words())

if __name__ == "__main__":
    main()

