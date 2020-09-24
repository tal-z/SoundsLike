# SoundsLike

Welcome to the SoundsLike module. SoundsLike helps find words that sound like other words, using the CMU Pronouncing Dictionary. 
It also offers some tools for working with dictionaries, if you prefer to use your own. 

SoundsLike is developed by Tal Zaken. 

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


Enjoy!
