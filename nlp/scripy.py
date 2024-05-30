#1,2,3,4,6,7,8,9,10,11
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import brown
from collections import Counter
from nltk.corpus import wordnet
from nltk.corpus import movie_reviews
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk import FreqDist
import random
from googletrans import Translator
# nltk.download('movie_reviews')
# nltk.download('stopwords')
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
        def pos_tag_word(word):
            tag = nltk.pos_tag([word])[0][1][0].upper()
            tag_dict = {
                "J" : wordnet.ADJ,
                "N" : wordnet.NOUN,
                "V" : wordnet.VERB,
                "R" : wordnet.ADV
            }
            return tag_dict.get(tag,wordnet.NOUN)
        word = "feet"
        wnl = WordNetLemmatizer()
        wnl.lemmatize(word,pos_tag_word(word))
        sent = "the programmer is programming programs everyday"
        print([wnl.lemmatize(w,pos_tag_word(w) )for w in nltk.word_tokenize(sent)])
    def remove_special_characters(text):
        text = text.strip()
        text = re.sub(r'\s+',' ',text)
        text = text.split(' ')
        text = [word for word in text if word]
        res = ' '.join(text)
        return text , res

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
    def text_classification(sent):
        def feature_extract(word):
            return dict(FreqDist(word))
        document = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
        random.shuffle(document)
        split_ratio = int(len(document)*0.8) 
        train_size , test_size = document[:split_ratio] , document[split_ratio:]
        train_feature = [(feature_extract(words),category) for words,category in train_size]
        test_features = [(feature_extract(words),category) for words , category in test_size]
        clf = NaiveBayesClassifier.train(train_feature)
        acc = classify.accuracy(clf,test_features)
        print(acc)
        for sentence in sent:
            words = nltk.word_tokenize(sentence)
            features = feature_extract(words)
            category = clf.classify(features)
            print(f"predicted class for the sentnce {sentence} : {category}")

    def translate():
        translator = Translator()
        def translate_lang(text,src_lang,dest_lang):
            #translator = Translator()
            translated = translator.translate(text,src = src_lang,dest = dest_lang)
            translated_text = translated.text
            return translated_text
        def FrenchToEnglish(text):
            words = nltk.word_tokenize(text)
            cleaned = ' '.join(words)
            translation = translate_lang(cleaned,'fr','en')
            return translation
        def EnglishToFrench(text):
            words = nltk.word_tokenize(text)
            cleaned = ' '.join(words)
            translation = translate_lang(cleaned,'en','fr')
            return translation
        while True:
            print("enter the choice\n 1--> for french to english\n 2--> for english to french\n q for quitting")
            choice = input()
            if choice == '1':
                text = input("enter the french text")
                print(FrenchToEnglish(text))
            elif choice =='2':
                text = input("enter the english text")
                print(EnglishToFrench(text))
            elif choice == 'q':
                break

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
    new_sentences = [
    "This movie was fantastic!",
    "I didn't like the plot of this film.",
    "The acting was superb in this movie.",
    "The screenplay was terrible."]
    text_classification(new_sentences)
    translate()

if __name__ == "__main__":
    main()