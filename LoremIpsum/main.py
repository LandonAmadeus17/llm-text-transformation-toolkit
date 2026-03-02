# Imports
from funx import *
import text as txt
import pprint as pp

# Program
class LoremIpsum:
    text: str;

    def __init__(self, text):
        self.text = text;
        print("<Program Instantiated>");

    def countVowelPairsProgram(self, text):
        lower = text.lower();
        charText = removeWhitespace(removePunctuation(text));
        print(countAdjacentVowels(charText));

    def countPunctuationProgram(self, text):
        punx = countPunctuation(text);
        print(punx);

    def countAlphabeticalVowelTuplets(self, text):
        lower = text.lower();
        lowerVowels = removeNonVowels(lower);
        # Counts Alphabetical Strings of Length 3+
        tuplets: int = countAlphabeticTuplets(lowerVowels);
        print(tuplets);

    def countIndefiniteArticles(self, text):
        print(countIndefiniteArticles(text));

    def countDefiniteArticles(self, text):
        print(countThe(text));

    def countArticles(self, text):
        print(countIndefiniteArticles(text) + countThe(text));

    def countArticleDifference(self, text):
        numDef = countThe(text);
        numIndef = countIndefiniteArticles(text);
        print(f"# Definite - # Indefinite = Difference"
              f"\n{numDef} - {numIndef} = {numDef - numIndef}")

    def countAvgLetterFreq(self, text):
        lower = text.lower();
        letterFreq: dict = countLetterFreq(lower);
        avgLetterFreq = avgDictValues(letterFreq);
        pp.pprint(letterFreq);
        print(avgLetterFreq);

    def multilineSentencesProgram(self, text):
        # Split By Simple Punctuation
        sentences: list = splitBySimplePunctuation(text);
        print(sentences);

        # Remove Character Cues
        for i in range(len(sentences)):
            sentences[i] = removeCharacterCue(sentences[i]);
        print(sentences);

        # Omit Single-Line Sentences
        multilineSentences: list = [];
        for sentence in sentences:
            if hasNewlineCharacter(sentence):
                multilineSentences.append(sentence);
        print(multilineSentences);

        # Count Characters of Multiline Sentences
        totalChars: int = 0;
        for sentence in multilineSentences:
            totalChars += countLetters(re.split(r"""[,;:'"?!.\s\n]+""", sentence));
        print(totalChars);

        # Find Max Unique Words
        maxUniqueWords: list = [];

        # For Each Multiline Sentence
        for sentence in multilineSentences:
            words: list = re.split(r"[,;:\s]+", sentence);

            # Get Distinct Words
            wordFreq: dict = {};
            for word in words:
                if (word not in wordFreq.keys()):
                    wordFreq[word] = 1;
                else:
                    wordFreq[word] += 1;

            # Make Dictionary With Word Keys and Uniqueness Values
            uniquenessDictionary: dict = {};
            for word in wordFreq:
                uniqueLetters = countUniqueLetters(word);

                uniquenessDictionary[word] = uniqueLetters;

            # Keep Only Unique Words
            dictValueMax = max(uniquenessDictionary.values());
            for key, value in uniquenessDictionary.items():
                if (value == dictValueMax):
                    for i in range(wordFreq[key]):
                        maxUniqueWords.append(key);
        print(maxUniqueWords);

        # Find Middle Characters of Max Unique Words
        middleChars: list = [];
        for word in maxUniqueWords:
            middleChars.append(getMiddleChars(word));
        print(middleChars);

        # Concatenate Middle Chars
        middleString: str = "".join(middleChars);
        print(middleString);

        # Final Answer
        print(f"{middleString}{totalChars}");


    def main(self):
        text = self.text;
        self.countAvgLetterFreq(text);

if __name__ == "__main__":
    program = LoremIpsum(txt.text);
    program.main();