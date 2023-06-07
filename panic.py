phrase ="don't Panic"
plist = list(phrase)

for i in range(4):
    print(plist.pop())
plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)
print (plist)
print(new_phrase)




