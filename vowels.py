def search4vowels(word):
     vowels = ['a','e', 'i', 'o','u']
     found={}


     for letter in word:
      if letter in vowels: 
          found.setdefault(letter,0)
          found[letter] +=1
     for k,v in sorted(found.items()):
          print(k , 'was found', v, 'time(s).')
          





search4vowels('aeeeess')