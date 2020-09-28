"""
This module provides spellchecker functionality that plays nicely with SoundsLike search functions. See test program for sample usage.
"""

import cmudict
from difflib import get_close_matches
import warnings


CMU_dict = cmudict.dict()
CMU_keys = CMU_dict.keys()



def DEPREC_fuzzy_CMU_keys(word, tolerance=91):
    """
    Returns a list of tuples with fuzzy matching string in tuple[0] and similarity score in tuple[1].
    ex: [(fuzzy_string1, similarity_score1), (fuzzy_string2, similarity_score2), ...]
    Takes fuzzy tolerance as an optional argument (0-100), and defaults to 91.
    """
    if word.lower() in CMU_keys:
        return [(word,)]
    else:
        print(f"Search term not found. Looking for fuzzy matches. (Tolerance={tolerance})")
        fuzz_list = get_close_matches(word.lower(), CMU_keys, cutoff=tolerance*.01)
        if not len(fuzz_list) == 0:
            return fuzz_list
        else:
            raise ValueError("I tried, but I couldn't find any good results. "
                     "Consider lowering the similarity tolerance to increase the number of matches."
                     )

def DEPREC_fuzzy_CMU_key(word, tolerance=91):
    """
    Returns a tuple with fuzzy matching string in tuple[0] and similarity score in tuple[1].
    ex: (fuzzy_string, similarity_score)
    Takes fuzzy tolerance as an optional argument (0-100), and defaults to 91.
    """
    if word.lower() in CMU_keys:
        return (word,)
    else:
        warnings.warn(f"Search term not found. Looking for closest fuzzy match. (Tolerance={tolerance*.01})")
        fuzz_list = get_close_matches(word.lower(),  CMU_keys, n=1, cutoff=tolerance*.01)
        if not len(fuzz_list) == 0:
            closest_fuzz = fuzz_list
            return closest_fuzz
        else:
            raise ValueError("Could not find any good search terms. "
                     "Consider lowering the similarity tolerance to find a match."
                     )


def fuzzy_term(term, cutoff=.9, suppress_error=False):
    """
    Takes a multi-word search term.
    For each word in the term:
        check if the word is in CMU dict.
        if the word is in CMU dict:
            append it to a result list.
        if the word is not in CMU dict:
            find the closest fuzzy match within CMU_dict above the given (or default) cutoff, and append that to fuzzy term.
            if no fuzzy match is found:
                skip the word but proceed with the search anyway.
    If search term exists:
        return search term.
    Otherwise:
        throw an error.
    """

    fuzzy_term = []
    for word in term.lower().split():
        if word in CMU_dict:
            fuzzy_term.append(word.title())
        else:
            warnings.warn(f"Search term not found. Looking for similar terms.")
            fuzzy_word = get_close_matches(word, CMU_keys, n=1, cutoff=cutoff)
            if not fuzzy_word == []:
                fuzzy_term.append(fuzzy_word[0].title())

    fuzzy_term = ' '.join(fuzzy_term)
    if fuzzy_term:
        return fuzzy_term
    elif suppress_error:
        return term
    else:
        raise ValueError('Error: Could not identify a similar term. Perhaps try adjusting the delta cutoff. '
                 '(Cutoff must be between 0 and 1)'
                         )
