import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipi.settings')

import django
django.setup()

import nltk
from nltk.classify import MaxentClassifier
from nltk.tag import pos_tag, map_tag
from nltk.corpus import stopwords as corpus_stopwords
from nltk.stem.snowball import EnglishStemmer
from textblob import TextBlob
from recipi.food.models import Food


print('setup training data')

# Set up our training material in a nice dictionary.
training = {
    'ingredients': [
        'Pastry for 9-inch tart pan',
        'Apple cider vinegar',
        '3 eggs',
        '1/4 cup sugar',
    ],
    'steps': [
        'Sift the powdered sugar and cocoa powder together.',
        'Coarsely crush the peppercorns using a mortar and pestle.',
        'While the vegetables are cooking, scrub the pig ears clean and cut away any knobby bits of cartilage so they will lie flat.',
        'Heat the oven to 375 degrees.',
    ],
}

stemmer = EnglishStemmer(ignore_stopwords=True)

stopwords = corpus_stopwords.words('english')


def get_features(text):
    words = []
    # Same steps to start as before
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = words + nltk.word_tokenize(sentence)

    # Then, convert the words to lowercase like before
    words = [i.lower() for i in words if i not in stopwords]

    # part of speech tag each of the words
    pos = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in nltk.pos_tag(words)]

    # Grab the trigrams
    trigrams = nltk.trigrams(words)

    # We need to concatinate the trigrams into a single string to process
    trigrams = ["%s/%s/%s" % (i[0], i[1], i[2]) for i in trigrams]

    # Get our final dict rolling
    features = words + pos + trigrams

    # get our feature dict rolling
    features = dict([(i, True) for i in features])
    return features


print('setup training set')

# Set up a list that will contain all of our tagged examples,
# which we will pass into the classifier at the end.
training_set = []
for key, val in training.items():
    for i in val:
        training_set.append((get_features(i), key))


def classify(s):
    p = classifier.prob_classify(s)
    import json
    print("%s\n >>> %s, %s\n" % (s, p.max(), p.prob(p.max())))
    return (p.max(), p.prob(p.max()))


print('setup classifier')

# Train up our classifier
# TODO: get http://www.umiacs.umd.edu/~hal/megam/version0_91/ working
classifier = MaxentClassifier.train(training_set)

print()
print()

tests = [
    'Please use two eggs',
    'One apple, a dash of cider and cocoa pulver',
    'Please prepare the oven while waiting',
    'Dont forget to buy apples',
    'Hey, this is yet another great day to cook.',
]

for line in tests:
    classify(get_features(line))
    blob = TextBlob(line)
    print(line)
    print(blob.translate(to='de'))
    print()
