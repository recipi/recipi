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



def get_features(text):
    words = []
    # Same steps to start as before
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = words + nltk.word_tokenize(sentence)

    # part of speech tag each of the words
    pos = nltk.pos_tag(words)

    # Then, convert the words to lowercase like before
    words = [i.lower() for i in words if i not in stopwords]

    # Grab the trigrams
    trigrams = nltk.trigrams(words)

    # We need to concatinate the trigrams into a single string to process
    trigrams = ["%s/%s/%s" % (i[0], i[1], i[2]) for i in trigrams]

    # Get our final dict rolling
    features = words + pos + trigrams

    # get our feature dict rolling
    features = dict([(i, True) for i in features])
    return features


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


# Train up our classifier
# TODO: get http://www.umiacs.umd.edu/~hal/megam/version0_91/ working
classifier = MaxentClassifier.train(training_set)

print()
print()

classify(get_features('Please use two eggs'))
classify(get_features('One apple, a dash cider and the cocoa pulver'))
classify(get_features('Please prepare the oven while waiting'))
classify(get_features('Don\'t forget to buy apples'))
classify(get_features('Hey, this is yet another great day to cook.'))
