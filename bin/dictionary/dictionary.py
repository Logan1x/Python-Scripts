from nltk.corpus import wordnet as wn


def extractInfo(synset):
    """
    get string containing definition from a synset
    """
    out = synset.pos() + ' : '
    out += synset.definition()

    return out


def definition(word):
    ssets = wn.synsets(word)
    defns = list()

    for i in ssets:
        # ensure words in synsets are same
        if i.name().split('.')[0] == word:
            info = extractInfo(i)
            defns.append(info)

    # return defns
    return '\n'.join(defns)
