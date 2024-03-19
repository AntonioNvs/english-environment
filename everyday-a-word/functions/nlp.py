import spacy

from tqdm import tqdm

nlp = spacy.load("en_core_web_sm")

def select_verbs(words):
    verbs = []

    progress_bar = tqdm(total=len(words), unit='B', unit_scale=True)

    for word in words:
        doc = nlp(word)

        for token in doc:
            if token.pos_ == 'VERB':
                verbs.append(token.text)
        
        progress_bar.update(1)

    progress_bar.close()

    return verbs

def eliminate_unnecessary_words(words, stopwords=True, nouns=True):
    real_words = []

    progress_bar = tqdm(total=len(words), unit='B', unit_scale=True)

    for word in words:
        if not isinstance(word, str):
            continue
        
        doc = nlp(word)

        for token in doc:
            if stopwords and token.is_stop:
                continue
            if nouns and token.pos_ == 'NOUN':
                continue
            real_words.append(token.text)
        
        progress_bar.update(1)

    progress_bar.close()

    return real_words