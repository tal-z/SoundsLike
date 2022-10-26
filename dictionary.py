import pickle

class Dictionary:
    def __init__(self, custom_dict: str='pn_phoneme_dict.pickle'):
        self.dictionary = self.load_dictionary(custom_dict)
        self.dset = set(list(self.dictionary.keys()))
        
    def load_dictionary(self, custom_dict):
        with open(custom_dict, 'rb') as f:
            dictionary = pickle.load(f)
        return dictionary
    
    def __getitem__(self, key):
        return self.dictionary[key]
    

dictionary = Dictionary()