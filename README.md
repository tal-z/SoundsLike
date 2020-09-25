# Welcome to SoundsLike.  <br>SoundsLike is a python package.  <br>SoundsLike helps find words that sound like other words.

## What it does:
SoundsLike provides various functions that attempt to generate lists of similar-sounding words for a given search term. This general purpose tool is useful for matching similar strings whose content is made up of the English language.

## Who it's for:
SoundsLike is for anyone who deals with messy names, misspelled words, or bad transcriptions. It is especially useful for resolving mismatches at the interface of typed text and spoken language. Some example applications include:
- Telephone Customer Service
- Immigration Research
- Database Entity Resolution

## How to install it:
For now, no pip install is available. To use SoundsLike, you'll need to download the SoundsLike directory and save it where you want it. Pip install is planned for the future.

## Contents:
- Homophones.py
- DictionaryTools.py
- FuzzyTerm.py

### Simple usage:
#### Perfect Homophones:

    from SoundsLike.Homophones import Search
    
    Search.perfectHomophones('Jonathan')
    
`['Johnathan', 'Johnathon', 'Jonathan', 'Jonathon', 'Jonothan']`

#### Close Homophones:
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

### Other homophone patterns available in Homophones.py using the `help()` function in your interactive interpreter. Examples include:
*- Vowel-class Homophones:  Vowel sounds are reduced to their ARPAbet classification.*
*- Phone-class Homophones:  All phones are reduced to their ARPAbet classification.*
*- End-rhymes:  Traditional rhyming. Takes optional arguments to find end-rhymes with same syllabic length and/or same first initial.*



### Full documentation:

Coming soon! 
For detailed instructions, try running `help(SoundsLike)` in your interactive python interpreter. You can also run `help()` on any of the individual modules contained in SoundsLike.
            
###### SoundsLike uses the CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict  <br>It also offers some tools for working with dictionaries, if you prefer to use your own. <br>Phoneme generation, when enabled, is provided by g2p-en: https://github.com/Kyubyong/g2p  <br>Similar string matching is provided by difflib: https://docs.python.org/3/library/difflib.html  


### **SoundsLike is developed by Tal Zaken.**

***

### Credits:
- The CMU Pronouncing Dictionary
- cmudict python wrapper by David L. Day
- g2p-en python module by Kyubyong Park

### Dependencies:
      
json, sys, re, cmudict, g2p-en
 
### Notes:
- While this module supports multi-token search terms, it always reduces them to one group of phones. This could lead to some unexpected, but still useful, results. Resultantly, multi-token results are not supported at this time.
- Support is not presently offered for multiple pronunciations of a given token.
- English Language CMU Dict can be swapped out for any other pronunciation dict by uncommenting and setting the DictionaryFilepath to point at a JSON file. This would be useful if one wishes to add terms to a custom dictionary.

### Ideas:

- Create match pattern for same first and last syllable, and same number of syllables.
- Add multi-token results. Check each token in multi-token search terms, and concatenate all possible results if all tokens are found. e.g.: "Lee Ann" could return "Leigh Anne," "Lea An," "Lianne," etc.
- Develop module to figure out "smart selection" results for display.

### License:

Licensed under the Apache License, Version 2.0

Enjoy!



