"""
This module is provided along with the SoundsLike library.
This module provides helper functions for configuring and re-configuring dictionaries.
"""

import json



def flattenDict(dict):
    """
    Takes a dictionary with aggregated values and turns each value into a key
    with the aggregated key (from dict) as the corresponding value.
    """
    flat_dict =  {p: g for g, sublist in dict.items() for p in sublist}
    return flat_dict

def mergeDicts(dict1, dict2):
    """
    Merges values from dict2 into dict1.
    If a key exists in both dictionaries, dict2 will overwrite dict1.
    """
    res = {**dict1, **dict2}
    return res

def textToJSON(text, filepath, entry_delimiter="\n", key_value_delimiter="  "):
    """
    The intent of this function is to take CMU Sphinx .dic files (plain text)
    and prepare them for use with this library.
    This library prefers to read external dictionaries from JSON.

    Implementation:
        Takes a text file, breaks it down into entries (type=str),
        then breaks each entry into key: value pairs and packs them into a dictionary.
        By default, entries are split at line breaks.
            To change the entry delimiter, pass your desired delimiter to 'entry_delimiter'
        By default, key: value pairs are split at the first double-space in an entry string.
            To change the key_value delimiter, pass your desired delimiter to 'key_value_delimiter'
    """
    split_text = sorted(text.split(entry_delimiter))
    dictionary = {k: v for row in split_text for k, v in row.split(key_value_delimiter, 1)}
    dict_to_json = json.dumps(dictionary)
    f = open(filepath, "w")
    f.write(dict_to_json)
    f.close()
    return


