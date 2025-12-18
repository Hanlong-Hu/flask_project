import re
def count_words(text):
    # filter non-alphanumeric characters
    text = re.sub(r'[^a-zA-Z0-9]', ' ', text)
    return len(text.split())
