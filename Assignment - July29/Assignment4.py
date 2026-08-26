def clean_sentence(text):
    words = text.split()
    
    sentence = " ".join(words)
    
    return sentence.capitalize()


text = "   python    is    a    very    powerful   language   "

print(clean_sentence(text))