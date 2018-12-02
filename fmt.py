import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize.punkt import PunktSentenceTokenizer

def newline_by_sentence(text):
    tokenizer = PunktSentenceTokenizer()

    # Clear the current new lines
    text.replace('\n', '')

    # Tokenize the text by sentence
    sentences = tokenizer.tokenize(text)

    return '\n'.join(sentences)
