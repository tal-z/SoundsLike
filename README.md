# <p align="right">Welcome to SoundsLike</p>
    
## <p align="right">SoundsLike is a python package  <br>SoundsLike helps find words that sound like other words</p>

### <p align="right">**Developed by Tal Zaken**</p>
***

## What it does:
SoundsLike provides various functions that generate lists of similar-sounding words for a given search term. This general purpose tool is useful for matching similar strings whose content is made up of the English language.

## Who it's for:
SoundsLike is for anyone who deals with messy names, misspelled words, or bad transcriptions. It is especially useful for resolving mismatches at the interface of typed text and spoken language. Some example applications include:
- Telephone Customer Service
- Immigration Research
- Database Entity Resolution

That said, it's mostly just for me and my own learning journey. If it's useful for you too, that's even better!

## How to install it:

`pip install SoundsLike`

## Contents:
- SoundsLike.py
- DictionaryTools.py
- FuzzyTerm.py

## Simple usage:
### Perfect Homophones:
***Example 1***

    from SoundsLike.SoundsLike import Search
    
    Search.perfectHomophones('Jonathan')
    
`['Johnathan', 'Johnathon', 'Jonathan', 'Jonathon', 'Jonothan']`

### Close Homophones:
***Example 1***

    Search.perfectHomophones('Lucy')

`['Lucey', 'Lucie', 'Lucy', 'Luisi']`

    Search.closeHomophones('Lucy')

`['Lucey', 'Lucie', 'Lucy', 'Luisi']`

***Example 2***

     Search.perfectHomophones('Lou C')
    
`[]`

     Search.closeHomophones('Lou C')
    
`['Lucey', 'Lucie', 'Lucy', 'Luisi']`

#### Other homophone and rhyming patterns are available in SoundsLike.py. Explore them using the `help()` function in your interactive interpreter.  <br><br>Examples include:
- **Vowel-class Homophones:**  Vowel phones are reduced to their ARPAbet classification.
- **Phone-class Homophones:**  All phones are reduced to their ARPAbet classification.
- **End-rhymes:**  Traditional rhyming. Takes optional arguments to find end-rhymes with same syllabic length and/or same first initial.



## Full documentation:
Coming eventually! 

For detailed instructions, try running `help(SoundsLike)` in your interactive python interpreter. 
You can also run `help()` on any of the individual modules contained in SoundsLike, though you may need to import them individually to do so. Keep in mind that the package is called SoundsLike, and the primary module is also called SoundsLike, so just make sure you specify the correct one.
            
###### SoundsLike uses the CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict  <br>It also offers some tools for working with dictionaries, if you prefer to use your own. <br>Phoneme generation, when enabled, is provided by g2p-en: https://github.com/Kyubyong/g2p  <br>Similar string matching is provided by difflib: https://docs.python.org/3/library/difflib.html  




***

### Credits:
- The CMU Pronouncing Dictionary
- cmudict python wrapper by David L. Day
- g2p-en python module by Kyubyong Park

### Dependencies:
      
- cmudict
- g2p-en
- json
- re
 
### Notes:
- While this module supports multi-token search terms, it always reduces them to one group of phones. This could lead to some unexpected, but still useful, results. Resultantly, multi-token results are not supported at this time.
- Support is not presently offered for multiple pronunciations of a given token.
- English Language CMU Dict can be swapped out for any other pronunciation dict by uncommenting and setting the DictionaryFilepath to point at a JSON file. This would be useful if one wishes to add terms to a custom dictionary.

### Ideas:
- Provide option to import CMUdict (or any other dict) from a JSON, so that functions can reference it directly (rather than it being imported anew each time a function is called). 
- Create match pattern for same first and last syllable, and same number of syllables.
- Add multi-token results. Check each token in multi-token search terms, and concatenate all possible results if all tokens are found. e.g.: "Lee Ann" could return "Leigh Anne," "Lea An," "Lianne," etc.
- Develop module to figure out "smart selection" results for display.

### License:

Licensed under the Apache License, Version 2.0

Enjoy!



