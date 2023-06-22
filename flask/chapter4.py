def count_word(filename, word):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            count = contents.count(word)
            return count
    except: FileNotFoundError
    print(f"File {filename} not found")
    return None 

files = ['chapter4.txt']
word = 'the'

for file in files:
    count = count_word(file, word)
if count is not None:
    print(f"The word {word} appears {count} times in {file}")