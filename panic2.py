phrase = "don't panic"
phrase1 = list(phrase)
new_phrase = ''.join(phrase1[1:3])
new_phrase1 = new_phrase + ''.join([phrase1[5], phrase1[4], phrase1[7], phrase1[6]])
print(phrase1)
print(new_phrase1)