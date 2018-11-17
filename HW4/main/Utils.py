from difflib import SequenceMatcher


def stringsPartiallyMatch(string1, string2):
    sequenceMatcher = SequenceMatcher(None, string1.lower(), string2.lower())
    return sequenceMatcher.ratio() > 0.6


def sortListById(listToSort):
    for i in range(0, len(listToSort) - 1):
        for j in range(i + 1, len(listToSort)):
            if (listToSort[j]).getId() < listToSort[i].getId():
                aux = listToSort[j]
                listToSort[j] = listToSort[i]
                listToSort[i] = aux
