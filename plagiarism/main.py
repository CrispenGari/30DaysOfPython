
from difflib import SequenceMatcher
import json

def calculate_plagiarism(fileName:str)->dict:
    with open('./files/1.txt', 'r') as f1, open(fileName, 'r') as f2:
        tx1 = f1.read().lower()
        tx2 = f2.read().lower()
        matches = SequenceMatcher(None, tx1, tx2)
    return {
        "plagiarism": matches.ratio() * 100,
        "matching_indices": [
            tuple(i) for i in matches.get_matching_blocks()
        ]
    }

if __name__ == "__main__":
    fileName = "./files/2.txt"
    print(json.dumps(calculate_plagiarism(fileName)))