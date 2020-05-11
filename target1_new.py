import nltk
from nltk.classify.naivebayes import NaiveBayesClassifier
import pickle

def get_words_in_dataset(dataset):
    all_words = []
    for (words, sentiment) in dataset:
      all_words.extend(words)
    return all_words


def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features


def read_datasets(fname, t_type):
    data = []
    f = open(fname, 'r')
    line = f.readline()
    while line != '':
        data.append([line, t_type])
        line = f.readline()
    f.close()
    return data


def extract_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
    return features


def classify_dataset(data):
    return classifier.classify(extract_features(nltk.word_tokenize(data)))


# read in joy , disgust, sadness, shame, anger, guilt, fear training dataset
joy_feel= read_datasets('joy.txt', 'joy')
disgust_feel = read_datasets('disgust.txt', 'disgust')
shame_feel = read_datasets('shame.txt', 'shame')
sadness_feel = read_datasets('sadness.txt', 'sadness')
anger_feel = read_datasets('anger.txt', 'anger')
guilt_feel = read_datasets('guilt.txt', 'guilt')
fear_feel = read_datasets('fear.txt', 'fear')

# filter away words that are less than 3 letters to form the training data
data = []
for (words, sentiment) in joy_feel + disgust_feel + shame_feel + sadness_feel + anger_feel + guilt_feel + fear_feel:
    words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
    data.append((words_filtered, sentiment))


# extract the word features out from the training data
word_features = get_word_features(\
                    get_words_in_dataset(data))


# get the training set and train the Naive Bayes Classifier

'''training_set = nltk.classify.util.apply_features(extract_features, data)
classifier = NaiveBayesClassifier.train(training_set)

with open('train.pickle','wb') as f:
    pickle.dump(classifier,f)'''


pickle_in = open('train.pickle','rb')
classifier = pickle.load(pickle_in)

res = classify_dataset('Go to hell')

print(res)

vul_comment=['disgust','shame','anger','fear']

if res in vul_comment:
    print('Toxic Comment')
else:
    print('Non-Toxic Comment')

'''if res in vul_comment:
    final_res = 'Toxic Comment'
else:
    final_res = 'Non-Toxic Comment'
    '''
