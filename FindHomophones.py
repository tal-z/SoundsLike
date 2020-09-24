"""
FindHomophones is a module with functions for finding similar-sounding words.
FindHomophones is the first module of the SoundLike library.
Created by Tal Zaken using the English Language CMU Dict.

Credits:
-The CMU Pronouncing Dictionary
-cmudict python wrapper by David L. Day
-g2p-en python module by Kyubyong Park

Dependencies:
-json
-sys
-re
-cmudict
-g2p-en

Notes:
-While this module supports multi-word search terms, it always reduces them to one group of phones.
 This could lead to some unexpected, but still useful, results. 
 Resultantly, multi-word results are not supported at this time.
-Support is not presently offered for multiple pronunciations of a given token.
-English Language CMU Dict can be swapped out for any other pronunciation dict
 by uncommenting and setting the DictionaryFilepath to point at a JSON file.
 This would be useful if one wishes to add terms to a custom dictionary.

Ideas:
-create match pattern for same first and last syllable, and same number of syllables.
-add multi-word results. Check each word in multi-word search terms,
 and concatenate all possible results if all words are found.
 e.g.: "Lee Ann" could return "Leigh Anne," "Lea An," "Lianne," etc.
-For separate module, figure out "smart selection" results for display.

"""

import sys
import re
import cmudict
from GeneratePronunciation import generate_pronunciation

### Set Pronouncing Dictionary Here ###
"""
DictionaryFilepath = "C:/filepath/dictionary.json"
f = open(DictionaryFilepath).read()
CMU_dict = json.loads(f)
"""

CMU_dict = {k: v for k, v in cmudict.entries()}
#######################################



ARPAbet_Phonemes_Dict = {k: v[0] for k, v in cmudict.phones()}



class Word_Functions():

    def preProcess(word):
        """use regex to replace all long white spaces with a single space. Strip out quotes and commas."""
        word = re.sub('  +', ' ', word)
        word = re.sub('\n', ' ', word)
        word = word.strip().strip('"').strip("'").strip(",").lower().strip()
        # If data is missing, indicate that by setting the value to `None`.
        # This avoids errors caused by stripping out all characters in a word, then trying to return it.
        if not word:
            word = None
        return word

    def pronunciation(term, generate=False):
        """Takes a term and returns its pronunciation in CMU dict.
        Default behavior is to throw an error if no pronunciation is found.
        if optional argument generate=True, it will attempt to generate a pronunciation."""
        search_pron = []
        for w in term.lower().split():
            if w in CMU_dict:
                w_pron = CMU_dict[w]
                search_pron.append(w_pron)
            elif generate:
                 return generate_pronunciation(term)
            else:
                sys.exit(
                    "Dictionary Error: Search term or search token not found in dictionary. "
                    "Contact administrator to update dictionary if necessary."
                )

        pron = [p for sublist in search_pron for p in sublist]  # flatten list of lists into one list
        return pron

class Pronunciation_Functions():

    def first_syllable(pron):
        """Given a word's pronunciation, returns the first syllable."""
        s1 = []
        for p in pron:
            if not p[-1].isdigit():
                s1.append(p)
            else:
                s1.append(p)
                return s1

    def count_syllables(pron):
        """Given a word's pronunciation, returns the number of syllables."""
        count = 0
        for p in pron:
            if p[-1].isdigit():
                count += 1
        return count

    def index_first_stressed_vowel(pron):
        """Given a word's pronunciation, returns the index of the first stressed vowel.
        (position of p[-1] where p[-1] is a digit greater than 0)"""
        for p in pron:
            if p[-1].isdigit():
                if int(p[-1]) > 0:
                    return pron.index(p)

    def index_last_stressed_vowel(pron):
        """Given a word's pronunciation, returns the index of the last stressed vowel.
        (position of p[-1] where p[-1] is a digit greater than 0)"""
        for p in reversed(pron):
            if p[-1].isdigit():
                if int(p[-1]) > 0:
                    return pron.index(p)

    def classify_phones(pron):
        """Given a word's pronunciation, returns a simplified pronunciation
        where vowel sounds have been replaced with the name of their ARPAbet classification"""
        classified_pron = []
        for phone in pron:
            if phone[-1].isdigit():
                phone = phone[:-1]
            phone_class = ARPAbet_Phonemes_Dict[phone]
            classified_pron.append(phone_class)

        return classified_pron

    def classify_vowel_phones(pron):
        """Given a word's pronunciation, returns a simplified pronunciation
        where vowel sounds have been replaced with the name of their ARPAbet classification"""
        classified_pron = []
        for phone in pron:
            if phone[-1].isdigit():
                phone = [val for key, val in ARPAbet_Phonemes_Dict.items() if phone[:-1] in key]
            classified_pron.append(phone)

        return classified_pron


class Phone_Functions():

    def unstressed_phone(phone):
        """Takes a phone and removes the stress marker if it exists"""
        if not phone[-1].isdigit():
            return phone
        else:
            return phone[:-1]

    def ARPAbet_class(phone):
        return ARPAbet_Phonemes_Dict[phone]



class Search_Functions():

    def find_perfectHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and returns a list of words with the exact same pronunciation in CMU Dict.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        PerfectHomophones = [word.title() for word in CMU_dict if CMU_dict[word] == Search_Pron]

        return PerfectHomophones

    def find_closeHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and returns a list of words with the near-exact same pronunciation in CMU Dict
        by ignoring stress marks.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        Search_Pron = [Phone_Functions.unstressed_phone(p) for p in Search_Pron]

        CloseHomophones = [word.title() for word in CMU_dict if [Phone_Functions.unstressed_phone(p) for p in CMU_dict[word]] == Search_Pron]

        return CloseHomophones

    def find_vowelClassHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and classifies its vowel phones according to ARPAbet. (See the ARPAbet_phonemes_dict above.)
        Then, it returns a list of words with matching phones
        where vowel phones have been simplified to their ARPAbet classification.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        VowelClassPron = Pronunciation_Functions.classify_vowel_phones(Search_Pron)
        VowelClassHomophones = [word.title() for word in CMU_dict
                                if Pronunciation_Functions.classify_vowel_phones(CMU_dict[word]) == VowelClassPron]

        return VowelClassHomophones

    def find_phoneClassHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and classifies its phones according to ARPAbet. (See the ARPAbet_phonemes_dict above.)
        Then, it returns a list of words with matching phones
        where phones have been simplified to their ARPAbet classifications.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        PhoneClassPron = Pronunciation_Functions.classify_phones(Search_Pron)
        PhoneClassHomophones = [word.title() for word in CMU_dict
                                if Pronunciation_Functions.classify_phones(CMU_dict[word]) == PhoneClassPron]

        return PhoneClassHomophones

    def find_endRhymes(Search_Term, match_syllables=False, match_alpha=False, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and returns a list of end-rhyming words in CMU Dict.
        End-rhyming words are defined as sharing the same phones from the last stressed syllable on.
        Optional arguments include:
            match_syllables (bool):
                If True, returns only words with the same number of syllables as Search_Term.
                If unspecified, defaults to match_syllables=False.
            match_alpha (bool):
                If True, returns only words with the same first letter as Search_Term.
                If unspecified, defaults to match_alpha=False.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        if not match_syllables:
            if not match_alpha:
                return [key.title() for key, val in CMU_dict.items()
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
            else:
                return [key.title() for key, val in CMU_dict.items()
                        if Search_Term[0].lower() == key[0]
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
        else:
            if not match_alpha:
                return [key.title() for key, val in CMU_dict.items()
                        if Pronunciation_Functions.count_syllables(Search_Pron) == Pronunciation_Functions.count_syllables(val)
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
            else:
                return [key.title() for key, val in CMU_dict.items()
                        if Search_Term[0].lower() == key[0]
                        if Pronunciation_Functions.count_syllables(Search_Pron) == Pronunciation_Functions.count_syllables(val)
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
