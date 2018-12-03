import nltk
nltk.download('punkt', quiet=True)
from nltk.tokenize.punkt import PunktSentenceTokenizer

tokenizer = PunktSentenceTokenizer()

def newline_by_sentence(text):
    # Clear the current new lines
    text = text.replace('\n', '')

    # Tokenize the text by sentence
    sentences = tokenizer.tokenize(text)

    return '\n'.join(sentences)

def newline_surround_dialogue(text):
    import re

    # Double quotes
    formatted_text = re.sub('"' + "(\w+)" + '"', r"\n\1\n")


#TODO replace "(w+)" with ``($1)''
