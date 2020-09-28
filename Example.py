"""
This program is an example implementation of the SoundsLike package. 
This example demonstrates its most basic usage, for generating lists of similar-sounding search terms.
"""
from SoundsLike.SoundsLike import Search
from SoundsLike.FuzzyTerm import fuzzy_term
import cmudict

dictionary = {k: v for k, v in cmudict.entries()} ##  Point this at your preferred dictionary.
                                                  ##  Alternatively, delete it, and remove the dictionary
                                                  ##  keyword from your function calls. In that case,
                                                  ##  you can delete the cmudict import as well.



### Search Setup Area ###

""" Enter Search Term Here """
test_term = 'Leanne' # <--- You may get an error with this term.
                     # Try some other constructions and see what happens.
                     # E.g. Lianne, Lee Ann, Lee N.

"""Specify whether you want to search for similar terms, if your term is not found in CMU Dict."""
enable_fuzzyTerm = False # <--- See what happens when you set this to True.
                         # Perhaps try it with the various constructions from above.

"""Specify whether you want to generate a pronunciation if your term (or fuzzy term) is not found. 
   Note: If using fuzzy_term with pronunciation generation, you will need to suppress fuzzy term errors."""
enable_pronGeneration = False # <--- See what happens when you set this to True
                              # Perhaps try it with the various constructions from above.
                              # Or maybe make up your own.


### Handle fuzzy term settings ###
if enable_fuzzyTerm:
    test_term = fuzzy_term(test_term, cutoff=0, suppress_error=False)


### Call Desired Functions ###
### Uncomment the desired functions to test them one-by-one. Be sure to uncomment the relevant print statements in the next section as well.
a = Search.perfectHomophones(test_term, generate=enable_pronGeneration, dictionary=dictionary)
#b = Search.closeHomophones(test_term, generate=enable_pronGeneration, dictionary=dictionary)
#c = Search.vowelClassHomophones(test_term, generate=enable_pronGeneration, dictionary=dictionary)
#d = Search.phoneClassHomophones(test_term, generate=enable_pronGeneration, dictionary=dictionary)
#e = Search.endRhymes(test_term, match_syllables=False, match_alpha=False, generate=enable_pronGeneration, dictionary=dictionary)
#f = Search.endRhymes(test_term, match_syllables=False, match_alpha=True, generate=enable_pronGeneration, dictionary=dictionary)
#g = Search.endRhymes(test_term, match_syllables=True, match_alpha=False, generate=enable_pronGeneration, dictionary=dictionary)
#h = Search.endRhymes(test_term, match_syllables=True, match_alpha=True, generate=enable_pronGeneration, dictionary=dictionary)




### Print Results ###
print(
    f"Search Term: {test_term.title()}",
    f"Perfect Homophones:   {len(a)} {a}",
    #f"Close Homophones:   {len(b)} {b}",
    #f"Vowel-class Homophones:   {len(c)} {c}",
    #f"Phone-class Homophones:   {len(d)} {d}",
    #f"End-rhymes:   {len(e)} {e}",
    #f"Alpha Matching End-rhymes:   {len(f)} {f}",
    #f"Syllabic Matching End-rhymes:   {len(g)} {g}",
    #f"Alpha-Syllabic Matching End-rhymes:   {len(h)} {h}",
    sep='\n'
)
