import nltk
from nltk.classify import MaxentClassifier

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

from nltk.corpus import stopwords as corpus_stopwords
from nltk.stem.snowball import EnglishStemmer

stemmer = EnglishStemmer(ignore_stopwords=True)

stopwords = corpus_stopwords.words('english')

# Set up a list that will contain all of our tagged examples,
# which we will pass into the classifier at the end.
training_set = []
for key, val in training.items():
    for i in val:
        # Set up a list we can use for all of our features,
        # which are just individual words in this case.
        features = []
        
        # Before we can tokenize words, we need to break the
        # text out into sentences.
        sentences = nltk.sent_tokenize(i)
        for sentence in sentences:
            features = features + nltk.word_tokenize(sentence)

        # For this example, it's a good idea to normalize for case.
        # You may or may not need to do this.
        features = [stemmer.stem(i.lower()) for i in features if i not in stopwords]
        
        # Each feature needs a value. A typical use for a case like this
        # is to use True or 1, though you can use almost any value for
        # a more complicated application or analysis.
        features = dict([(i, True) for i in features])
        
        # NLTK expects you to feed a classifier a list of tuples
        # where each tuple is (features, tag).
        training_set.append((features, key))


def classify(s):
    p = classifier.prob_classify(s)
    import json
    print("%s\n >>> %s, %s\n" % (json.dumps(s), p.max(), p.prob(p.max())))
    return (p.max(), p.prob(p.max()))

# Train up our classifier
# TODO: get http://www.umiacs.umd.edu/~hal/megam/version0_91/ working
classifier = MaxentClassifier.train(training_set)

print()
print()

# Test it out!
# You need to feed the classifier your data in the same format you used
# to train it, in this case individual lowercase words.
classify({'apple': True, 'cider': True, 'vinegar': True, 'cocoa': True})
classify({'heat': True, 'oven': True})
classify({'prepare': True, 'oven': True})
classify({'nothing': True})
