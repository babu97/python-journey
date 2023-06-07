def search4vowels(phrase:str) -> set:
   """Return any vowels found in a supplied phrase."""
   vowels = set('aeiou')
   return vowels.intersection(set(phrase))


def search4letter(phrase:str,letters:str= 'aeiou') -> set:
   """Return a set of the 'letter' found in the 'phrase'"""
   return set(letters). intersection(set(phrase))