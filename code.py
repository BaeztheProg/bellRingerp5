import codecs
def rot13(text):
    return codecs.encode(text, 'rot13')
message = "Mr. Baez"
encoded_message = rot13(message)
print(encoded_message)
