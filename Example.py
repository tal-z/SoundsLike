from SoundsLike.SoundsLike import Search
from SoundsLike.FuzzyTerm import fuzzy_term


### Search Setup Area ###

"""Enter Search Term Here:"""
test_term = 'Leanne Rhymes'

"""Specify whether you want to search for similar terms, if your term is not found."""
enable_fuzzyTerm = False # <--- See what happens when you set this to True

"""Specify whether you want to generate a pronunciation if your term (or fuzzy term) is not found. 
   Note: If using fuzzy_term with pronunciation generation, you will need to suppress fuzzy term errors."""
enable_pronGeneration = False # <--- See what happens when you set this to True




### Handle fuzzy term settings ###
if enable_fuzzyTerm:
    test_term = fuzzy_term(test_term, 0, suppress_error=False)




### Call Desired Functions ###
a = Search.perfectHomophones(test_term, generate=enable_pronGeneration)
b = Search.closeHomophones(test_term, generate=enable_pronGeneration)
c = Search.vowelClassHomophones(test_term, generate=enable_pronGeneration)
d = Search.phoneClassHomophones(test_term, generate=enable_pronGeneration)
e = Search.endRhymes(test_term, match_syllables=False, match_alpha=False, generate=enable_pronGeneration)
f = Search.endRhymes(test_term, match_syllables=False, match_alpha=True, generate=enable_pronGeneration)
g = Search.endRhymes(test_term, match_syllables=True, match_alpha=False, generate=enable_pronGeneration)
h = Search.endRhymes(test_term, match_syllables=True, match_alpha=True, generate=enable_pronGeneration)




### Print Results ###
print(
    f"Search Term: {test_term.title()}",
    f"Perfect Homophones:   {len(a)} {a}",
    f"Close Homophones:   {len(b)} {b}",
    f"Vowel-class Homophones:   {len(c)} {c}",
    f"Phone-class Homophones:   {len(d)} {d}",
    f"End-rhymes:   {len(e)} {e}",
    f"Alpha Matching End-rhymes:   {len(f)} {f}",
    f"Syllabic Matching End-rhymes:   {len(g)} {g}",
    f"Alpha-Syllabic Matching End-rhymes:   {len(h)} {h}",
    sep='\n'
)
