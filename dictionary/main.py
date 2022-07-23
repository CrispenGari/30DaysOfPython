
import json
import os

with open(os.path.join(os.getcwd(), 'static/data.json'), 'r') as reader:
    DATA = json.loads(reader.read())
    
    
if __name__ == "__main__":
    from translator import expand_word
    word = input("Enter a word:\n")
    print(expand_word(word, DATA).to_json())
    