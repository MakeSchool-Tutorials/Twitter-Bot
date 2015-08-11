text = "We _really_ love parsing &#38; tokenization."
text = text.replace('_', '')
text = text.replace('&#38;', '&')
print(text)
