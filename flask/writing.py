def count_word(filename):
    """Count the approximate number of words in a file"""
    try:
        with open (filename, encoding='utf-8') as f:
           
          contents  =  f.read()

    except FileNotFoundError:
       print(f"Sorry, the file {filename} does not exist.")
    else:
       words = contents.split()
       num_words = len(words)

       print(f"The file {filename} has about {num_words} words.")

filenames = ['ben.txt', 'babu.txt', 'alice.txt', 'babuu.txt']
for  filename in filenames:
  count_word(filename)
       
       



   

    





