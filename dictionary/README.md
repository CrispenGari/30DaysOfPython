### Dictionary app

This is a simple python console application that give word meanings. Given an english word this application should be able to give meaning for the word.

### Usage

To use this application activate your virtual environment and run the following command:

```shell
python main.py
```

### Example:

Here is an example for the meaning of the word `python`:

```shell
(venv) PS C:\Users\crisp\OneDrive\Documents\My Python\Others\30DaysOfPython\dictionary> python main.py
Enter a word:
python
{
  "word": "python",
  "meaning": [
    "(Pythonidae) The common name for a group of non-venomous constricting snakes."
  ],
  "suggestions": [],
  "ok": true
}
```

The response will be in `json` format as follows:

```json
{
  "word": "python",
  "meaning": [
    "(Pythonidae) The common name for a group of non-venomous constricting snakes."
  ],
  "suggestions": [],
  "ok": true
}
```

### Topics

- dictionaries in python
- file system
- json in python
- OOP in python
- python modules
