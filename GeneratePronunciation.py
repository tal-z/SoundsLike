from g2p_en import G2p
import cmudict
import warnings


g2p = G2p()

def generate_pronunciation(text):
    if text not in cmudict.dict():

        warnings.warn('Search term not found in CMU Dict. Making best guess at pronunciation based on grapheme. Be careful!')
        return [phone for phone in g2p(text) if phone != ' ']
    else:
        return cmudict.dict()[text]
