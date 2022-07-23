
from difflib import get_close_matches
import json

class TranslationType:
    def __init__(self, word: str, meaning: str, ok:bool = False, suggestions: list =[]) -> None:
        self.word = word
        self.meaning = meaning
        self.suggestions = suggestions
        self.ok = ok
        
    def __str__(self) -> str:
        return "Word <{self.word}>"
    
    def __repr__(self) -> str:
       return "Word <{self.word}>"
   
    def  to_json(self):
        return json.dumps(dict({
            "word": self.word,
            "meaning": self.meaning,
            "suggestions": self.suggestions,
            "ok": self.ok
        }), indent=2)
        
def expand_word(word: str, dictionary: dict)->TranslationType:
    word = word.strip()
    if word.lower() in dictionary:
        return TranslationType(word, dictionary.get(word), ok=True)
    elif word.title() in dictionary:
        return TranslationType(word,dictionary.get(word.title()))
    elif word.upper() in dictionary:
        return TranslationType(word,dictionary.get(word.upper()))
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        suggestions =get_close_matches(word, dictionary.keys())[:5]
        return   TranslationType(word,"Look for suggested words", False, suggestions)
    else:
        return TranslationType(word,"Look for suggested words", False, suggestions)