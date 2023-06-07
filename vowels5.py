def search5vowels(word:str) -> set:
 """Returning any vowels found in a supplied word."""
 vowels = set('aeiou')
 return vowels.intersection(set(word))


 search5vowels('babubabu')