from difflib import SequenceMatcher


def stringsPartiallyMatch(string1, string2):
    sequenceMatcher = SequenceMatcher(None, string1.lower(), string2.lower())
    return sequenceMatcher.ratio() > 0.6
