<html>
    <body>
        <h1>Welcome to SoundsLike. 
            <br>
            <br>
            SoundsLike is a python package. 
            <br>
            SoundsLike helps find words that sound like other words.
        </h1>
        <h3>
            What it does:
        </h3>
            SoundsLike provides various functions that attempt to generate lists of similar-sounding words for a given search term. This general purpose tool is useful for matching similar strings whose content is made up of the English language.
            <br>
            <br>
        <h3>
            Who it's for:
        </h3>
            SoundsLike is for anyone who deals with messy names, misspelled words, or bad transcriptions. It is especially useful for resolving mismatches at the interface of typed text and spoken language. Some example applications include:
            <br>
            -Telephone Customer Service
            <br>
            -Immigration Research
            <br>
            -Entity Resolution
        <br>
        <br>
        <h3>
            How to use it:
        </h3>
            For now, no pip install is available. You'll need to download the .py files and save them where you want them.
        <br>
        <br>
        <h3>
            Simple usage:
        </h3>
            <code>
                <br>
                coming soon!
                <br>
            </code>
        <br>
        <br>
        <h3>
            SoundsLike uses the CMU Pronouncing Dictionary: http://www.speech.cs.cmu.edu/cgi-bin/cmudict
            <br>
            It also offers some tools for working with dictionaries, if you prefer to use your own. 
            <br>
            Phoneme generation, when enabled, is provided by g2p-en: https://github.com/Kyubyong/g2p
            <br>
            Similar string matching is provided by difflib: https://docs.python.org/3/library/difflib.html
            <br>
            <br>
            SoundsLike is developed by Tal Zaken.
        </h3>
        <hr>
        <b>Credits:</b>
        <br>
        -The CMU Pronouncing Dictionary<br>
        -cmudict python wrapper by David L. Day
        <br>
        -g2p-en python module by Kyubyong Park
        <br>
        <br>
        <b>Dependencies:</b>
        <br>
        json, sys, re, cmudict, g2p-en
        <br>
        <br>
        <b>Notes:</b>
        <br>
        -While this module supports multi-token search terms, it always reduces them to one group of phones. This could lead to some unexpected, but still useful, results. Resultantly, multi-token results are not supported at this time.
        <br>
        -Support is not presently offered for multiple pronunciations of a given token.
        <br>
        -English Language CMU Dict can be swapped out for any other pronunciation dict by uncommenting and setting the DictionaryFilepath to point at a JSON file. This would be useful if one wishes to add terms to a custom dictionary.
        <br>
        <br>
        <b>Ideas:</b>
        <br>
        -create match pattern for same first and last syllable, and same number of syllables.
        <br>
        -add multi-token results. Check each token in multi-token search terms,
        and concatenate all possible results if all tokens are found.
        e.g.: "Lee Ann" could return "Leigh Anne," "Lea An," "Lianne," etc.
        <br>
        -Develop module to figure out "smart selection" results for display.
        <br>
        <br>
        <b>License:</b>
        Licensed under the Apache License, Version 2.0
        <br>
        <br>
        Enjoy!
    </body>
</html>



