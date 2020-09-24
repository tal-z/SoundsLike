<h1>Welcome to the SoundsLike module.</h1>
<h2>SoundsLike helps find words that sound like other words.</h2>

<h3> <br>
 SoundsLike uses the CMU Pronouncing Dictionary. It also offers some tools for working with dictionaries, if you prefer to use your own. <br>
 Phoneme generation is provided by g2p-en: https://github.com/Kyubyong/g2p
</h3> 

<h3>SoundsLike is developed by Tal Zaken.</h3>

<hr>

<b>Credits:</b>

-The CMU Pronouncing Dictionary<br>
-cmudict python wrapper by David L. Day<br>
-g2p-en python module by Kyubyong Park<br>

<b>Dependencies:</b>

json, sys, re, cmudict, g2p-en

<b>Notes:</b>

-While this module supports multi-token search terms, it always reduces them to one group of phones.
 This could lead to some unexpected, but still useful, results. 
 Resultantly, multi-token results are not supported at this time.
<br>
-Support is not presently offered for multiple pronunciations of a given token.
<br>
-English Language CMU Dict can be swapped out for any other pronunciation dict
 by uncommenting and setting the DictionaryFilepath to point at a JSON file.
 This would be useful if one wishes to add terms to a custom dictionary.

<b>Ideas:</b>
<br>
-create match pattern for same first and last syllable, and same number of syllables.
<br>
-add multi-token results. Check each token in multi-token search terms,
 and concatenate all possible results if all tokens are found.
 e.g.: "Lee Ann" could return "Leigh Anne," "Lea An," "Lianne," etc.
<br>
-For separate module, figure out "smart selection" results for display.


Enjoy!



