import re

def countAdjacentVowels(text) -> int:
    charList = list(text);
    length = len(charList);
    numOfPairs = 0;
    for i in range(length - 1):
        if ((charList[i] in ['a', 'e', 'i', 'o', 'u']) and (charList[i + 1] in ['a', 'e', 'i', 'o', 'u'])):
            numOfPairs += 1;
    return numOfPairs;

def removePunctuation(text) -> str:
    """Does NOT remove whitespace, only the common punctuation shown below!"""
    charList = list(text);
    length = len(charList);
    for i in range(length):
        if (charList[i] in [",", ".", ";", ":", "?", "!", "—", "–", "-", "\'", "\""]):
            charList[i] = "";
    return "".join(charList);

def removeWhitespace(text) -> str:
    charList = list(text);
    length = len(charList);
    for i in range(length):
        if (charList[i] in [" ", "\n"]):
            charList[i] = "";
    return "".join(charList);

def countPunctuation(text) -> int:
    charList = list(text);
    length = len(charList);
    punx = 0;
    for i in range(length):
        # Avoid IndexOutOfRangeException
        if (length - i >= 3):
            # Check For Ellipse
            if (charList[i] + charList[i+1] + charList[i+2] == "..."):
                punx += 1;
                charList[i], charList[i+1], charList[i+2] = "a", "a", "a";
        # Check for Other Punctuation (Excluding Abbreviations)
        if (charList[i] == "." and not charList[i-1].isupper()):
            punx += 1;
        elif (charList[i] in [",", ";", ":", "?", "!", "—", "–", "-", "\'", "\""]):
            punx += 1;
    return punx;

def removeNonVowels(text) -> str:
    """Removes ALL characters excluding 'a', 'e', 'i', 'o', and 'u' (case-insensitive)."""
    charList = list(text);
    length = len(charList);
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'];
    for i in range(length):
        if (charList[i] not in vowels):
            charList[i] = '';
    return "".join(charList);

def countAlphabeticTuplets(text) -> int:
    """Counts Alphabetical Strings of Length 3+"""
    charList = list(text);
    length = len(charList);
    # Compute
    alphaStrings = 0;
    i, j = 0, 0;
    # First *Pointer
    while (i < length):
        stringLength = 1;
        j = i + 1;
        # Second *Pointer
        while (j < length):
            # If Alphabetical
            if (charList[i] < charList[j]):
                stringLength += 1;
                j += 1;
            # If Not Alphabetical
            else:
                # If Long Enough
                if (stringLength >= 3):
                    alphaStrings += 1;
                # Bring i to j and Exit Nested Loop
                i = j;
                break;
        # At the End of the Text
        if (j >= length):
            # If Long Enough
            if (stringLength >= 3):
                alphaStrings += 1;
            break;
    # Return Result
    return alphaStrings;

def countThe(text) -> int:
    """Counts occurrences of THE definite article."""
    whiteString = removePunctuation(text.lower());
    whiteList = whiteString.split();
    length = len(whiteList);
    theCount = 0;
    for i in range(length):
        if (whiteList[i] == "the"): theCount += 1;
    return theCount;

def countIndefiniteArticles(text) -> int:
    """Counts occurrences of the indefinite articles 'a' or 'an'."""
    whiteString = removePunctuation(text.lower());
    whiteList = whiteString.split();
    length = len(whiteList);
    indefiniteArticleCount = 0;
    for i in range(length):
        if (whiteList[i] in ["a", "an"]): indefiniteArticleCount += 1;
    return indefiniteArticleCount;

def countLetterFreq(text) -> dict:
    charString = removePunctuation(removeWhitespace(text));
    letterDict: dict = {};
    for char in charString:
        if char not in letterDict: # If char NOT Exists
            letterDict[char] = 1;
        else: # If char Exists
            letterDict[char] += 1;
    return letterDict;

def avgDictValues(data: dict) -> int:
    total: int = 0;
    for value in data.values():
        total += value;
    return total / len(data);

def splitBySimplePunctuation(text) -> list:
    splitText : list = re.split(r"[.?!]\n?", text);
    return splitText;

def removeCharacterCue(text) -> str:
    colonIndex: int = -1;
    if (text[0:2].isupper()):
        # Find First Colon
        colonIndex = text.find(":");
    # Slice It!
    return text[colonIndex+2:];

def countUniqueLetters(text) -> int:
    letterFreq: dict = {};
    uniqueLetters: int = 0;
    for char in text:
        if char not in letterFreq and char.isalpha():
            letterFreq[char] = 1;
            uniqueLetters += 1;
    return uniqueLetters;

def hasNewlineCharacter(text) -> bool:
    if ("\n" in text):
            return True;
    return False;

def countLetters(text) -> int:
    letterCount: int = 0;
    for char in text:
        if (char.isalpha()):
            letterCount += 1;
    return letterCount;

def getMiddleChars(text) -> str:
    # Remove Hyphens and Apostrophes
    remove_chars = """-'""";
    translation_table = str.maketrans('', '', remove_chars)
    letterString: str = text.translate(translation_table)

    length = len(letterString);
    if (length % 2 == 0): # If Even
        return letterString[length//2 - 1:length//2 + 1];
    else: # If Odd
        return letterString[length//2];