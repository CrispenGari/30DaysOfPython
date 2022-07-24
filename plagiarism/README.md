### Plagiarism

This is a simple python program that checks the similarity between two texts files. We are going to use a class from `difflib` called `SequenceMatcher`. Here is how we calculate Plagiarism and return the Plagiarism percentage and the indices of word matches.

```py

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
```

Output:

```json
{
  "plagiarism": 86.95652173913044,
  "matching_indices": [
    [0, 0, 11],
    [11, 14, 1],
    [17, 16, 18],
    [35, 34, 0]
  ]
}
```
