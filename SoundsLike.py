"""
SoundsLike is a module with functions for finding similar-sounding words.
SoundsLike is the first module of the SoundLike package.

Dependencies:
-cmudict (python package available via PyPI)
-g2p-en (python package available via PyPI)

Created by Tal Zaken.
"""

import re
import warnings
import pickle

import cmudict
from g2p_en import G2p

from dictionary import dictionary

### Set Pronouncing Dictionary Here ###
"""
DictionaryFilepath = "C:/filepath/dictionary.json"
f = open(DictionaryFilepath).read()
dictionary = json.loads(f)
"""

# CMU_dict = {k: v for k, v in cmudict.entries()}
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
            if w in dictionary.dset:
                w_pron = dictionary[w]
                search_pron.append(w_pron)
            elif generate:
                 return Pronunciation_Functions.generate_pronunciation(term)
            else:
                raise ValueError(
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

    def generate_pronunciation(text):
        g2p = G2p()
        if text not in dictionary.dset:
            warnings.warn(
                'Search term not found in CMU Dict. Making best guess at pronunciation based on grapheme. Be careful!')
            return [phone for phone in g2p(text) if phone != ' ']
        else:
            return dictionary[text]


class Phone_Functions():

    def unstressed_phone(phone):
        """Takes a phone and removes the stress marker if it exists"""
        if not phone[-1].isdigit():
            return phone
        else:
            return phone[:-1]

    def ARPAbet_class(phone):
        return ARPAbet_Phonemes_Dict[phone]



class Search():

    def perfectHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and returns a list of words with the exact same pronunciation in CMU Dict.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        PerfectHomophones = [word.title() for word in dictionary.dset if dictionary[word] == Search_Pron]

        return PerfectHomophones

    def closeHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and returns a list of words with the near-exact same pronunciation in CMU Dict
        by ignoring stress marks.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        Search_Pron = [Phone_Functions.unstressed_phone(p) for p in Search_Pron]

        CloseHomophones = [word.title() for word in dictionary.dset if [Phone_Functions.unstressed_phone(p) for p in dictionary[word]] == Search_Pron]

        return CloseHomophones

    def vowelClassHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and classifies its vowel phones according to ARPAbet. (See the ARPAbet_phonemes_dict above.)
        Then, it returns a list of words with matching phones
        where vowel phones have been simplified to their ARPAbet classification.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        VowelClassPron = Pronunciation_Functions.classify_vowel_phones(Search_Pron)
        VowelClassHomophones = [word.title() for word in dictionary.dset
                                if Pronunciation_Functions.classify_vowel_phones(dictionary[word]) == VowelClassPron]

        return VowelClassHomophones

    def phoneClassHomophones(Search_Term, generate=False):
        """
        Takes a search term, searches its pronunciation,
        and classifies its phones according to ARPAbet. (See the ARPAbet_phonemes_dict above.)
        Then, it returns a list of words with matching phones
        where phones have been simplified to their ARPAbet classifications.
        """
        Search_Pron = Word_Functions.pronunciation(Search_Term, generate)
        PhoneClassPron = Pronunciation_Functions.classify_phones(Search_Pron)
        PhoneClassHomophones = [word.title() for word in dictionary.dset
                                if Pronunciation_Functions.classify_phones(dictionary[word]) == PhoneClassPron]

        return PhoneClassHomophones

    def endRhymes(Search_Term, match_syllables=False, match_alpha=False, generate=False):
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
                return [key.title() for key, val in dictionary.dictionary.items()
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
            else:
                return [key.title() for key, val in dictionary.dictionary.items()
                        if Search_Term[0].lower() == key[0]
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
        else:
            if not match_alpha:
                return [key.title() for key, val in dictionary.dictionary.items()
                        if Pronunciation_Functions.count_syllables(Search_Pron) == Pronunciation_Functions.count_syllables(val)
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
            else:
                return [key.title() for key, val in dictionary.dictionary.items()
                        if Search_Term[0].lower() == key[0]
                        if Pronunciation_Functions.count_syllables(Search_Pron) == Pronunciation_Functions.count_syllables(val)
                        if Search_Pron[Pronunciation_Functions.index_last_stressed_vowel(Search_Pron):] == val[Pronunciation_Functions.index_last_stressed_vowel(val):]
                        ]
