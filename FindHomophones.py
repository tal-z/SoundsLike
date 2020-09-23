"""
FindHomophones is a module with functions for finding similar-sounding words.
FindHomophones is the first module of the SoundLike library.
Created by Tal Zaken using the English Language CMU Dict.
Credits:
-The CMU Pronouncing Dictionary
-cmudict python wrapper by David L. Day
Dependencies:
-json
-sys
-re
-cmudict
Notes:
-English Language CMU Dict can be swapped out for any other pronunciation dict
 by uncommenting and setting the DictionaryFilepath to point at a JSON file.
-Support is not presently offered for multiple pronunciations of a given token.
"""

import json
import sys
import re
import cmudict

### Set Pronouncing Dictionary Here ###
"""
DictionaryFilepath = "C:/filepath/dictionary.json"
f = open(DictionaryFilepath).read()
CMU_dict = json.loads(f)
"""

CMU_dict = {k: v for k, v in cmudict.entries()}
####################



ARPAbet_Phonemes_Dict = {
    'vowels_front': ['IY', 'IH', 'EY', 'EH', 'AE'],
    'vowels_mid': ['ER', 'AX', 'AH'],
    'vowels_back': ['AA', 'AO', 'OW', 'UH', 'UW'],
    'dipthongs': ['AY', 'AW', 'OY', 'IX'],
    'stop_consonants_voiced': ['B', 'D', 'G'],
    'stop_consonants_unvoiced': ['P', 'T', 'K'],
    'fricatives_voiced': ['V', 'DH', 'Z', 'ZH'],
    'fricatives_unvoiced': ['F', 'TH', 'S', 'SH'],
    'semivowels_liquids': ['L', 'EL', 'R'],
    'semivowels_glides': ['W', 'WH', 'Y'],
    'nasal_non-vocalic': ['M', 'N', 'NX'],
    'nasal_vocalic': ['EM', 'EN'],
    'affricates': ['CH', 'JH'],
    'others_whisper': ['HH'],
    'others_vocalic': ['DX'],
    'others_glottal-stop': ['Q']
}

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

    def pronunciation(term):
        """Takes a term and returns its pronunciation in CMU dict. If no pronunciation is found, it throws an error."""
        search_pron = []
        for w in term.lower().split():
            if w in CMU_dict:
                w_pron = CMU_dict[w]
                search_pron.append(w_pron)
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

    def classify_vowel_sounds(pron):
        """Given a word's pronunciation, returns a simplified pronunciation
        where vowel sounds have been replaced with the name of their ARPAbet classification"""
        classified_pron = []
        for phone in pron:
            if phone[-1].isdigit():
                phone = [key for key, val in ARPAbet_Phonemes_Dict.items() if phone[:-1] in val]
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
        pass



class Search_Functions():

    def find_perfectHomophones(Search_Term):
        """
        Takes a search term, searches its pronunciation,
        and returns a list of words with the exact same pronunciation in CMU Dict.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term)
        PerfectHomophones = [word.title() for word in CMU_dict if CMU_dict[word] == Search_Pron]

        return PerfectHomophones

    def find_closeHomophones(Search_Term):
        """
        Takes a search term, searches its pronunciation,
        and returns a list of words with the near-exact same pronunciation in CMU Dict
        by ignoring stress marks.
        """
        Search_Pron = [CMU_dict[w] if w in CMU_dict else sys.exit("Error: Search term or search token not found in dictionary. Contact administrator to update dictionary if necessary.") for w in Search_Term.lower().split()]
        Search_Pron = [Phone_Functions.unstressed_phone(p) for sublist in Search_Pron for p in sublist]  # flatten list of lists of phones into one list of unstressed phones."""

        CloseHomophones = [word.title() for word in CMU_dict if [Phone_Functions.unstressed_phone(p) for p in CMU_dict[word]] == Search_Pron]

        return CloseHomophones

    def find_vowelClassHomophones(Search_Term):
        """
        Takes a search term, searches its pronunciation,
        and classifies its vowel phones according to ARPAbet. (See the ARPAbet_phonemes_dict above.)
        Then, it returns a list of words with matching phones
        where vowel phones have been simplified to their ARPAbet classification.
        This takes longer than other functions because it classifies every vowel sound for every entry in CMU Dict.
        Still runs in an acceptable timeframe, though.
        """
        Search_Pron = [CMU_dict[w] if w in CMU_dict
                       else sys.exit("Error: Search term or search token not found in dictionary. Contact administrator to update dictionary if necessary.")
                       for w in Search_Term.lower().split()]
        Search_Pron = [p for sublist in Search_Pron for p in sublist]  # flatten list of lists into one list
        VowelClassPron = Pronunciation_Functions.classify_vowel_sounds(Search_Pron)
        VowelClassHomophones = [word.title() for word in CMU_dict
                                if Pronunciation_Functions.classify_vowel_sounds(CMU_dict[word]) == VowelClassPron]

        return VowelClassHomophones

    def find_endRhymes(Search_Term, match_syllables=False, match_alpha=False):
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
        Search_Pron = [CMU_dict[w] if w in CMU_dict else sys.exit("Error: Search term or search token not found in dictionary. Contact administrator to update dictionary if necessary.") for w in Search_Term.lower().split()]
        Search_Pron = [p for sublist in Search_Pron for p in sublist]  # flatten list of lists into one list
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




### Test Area ###
"""
test_word = 'Lianne'

a, b, c, d, e, f, g = \
    Search_Functions.find_perfectHomophones(test_word), \
    Search_Functions.find_closeHomophones(test_word), \
    Search_Functions.find_vowelClassHomophones(test_word), \
    Search_Functions.find_endRhymes(test_word, match_syllables=False, match_alpha=False), \
    Search_Functions.find_endRhymes(test_word, match_syllables=False, match_alpha=True), \
    Search_Functions.find_endRhymes(test_word, match_syllables=True, match_alpha=False), \
    Search_Functions.find_endRhymes(test_word, match_syllables=True, match_alpha=True)


print(
    f"Perfect Homophones:   {len(a)} {a}",
    f"Close Homophones:   {len(b)} {b}",
    f"Vowel-class Homophones:   {len(c)} {c}",
    f"End-rhymes:   {len(d)} {d}",
    f"Alpha Matching End-rhymes:   {len(e)} {e}",
    f"Syllabic Matching End-rhymes:   {len(f)} {f}",
    f"Alpha-Syllabic Matching End-rhymes:   {len(g)} {g}",
    sep='\n'
)
"""

"""
Ideas:
-create match pattern that reduces all phones to their ARPAbet classifications. 
--will probably take a while. curious how much quicker if I restructure the dictionary...
-create match pattern for same first and last syllable, and same number of syllables. 
-add multi-word results. Check each word in multi-word search terms, and concatenate all possible results if all words are found.
--e.g.: "Lee Ann" could return "Leigh Anne," "Lea An," "Lianne," etc. 
-For separate module, figure out "smart selection" results for display.
-Ben: edit distance using keyboard key proximity
"""


