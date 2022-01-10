import docassemble_pattern.en as pattern

import nltk
from nltk.corpus import wordnet as wn
try:
    wn.all_synsets
except LookupError:
    print("Downloading wordnet...")
    nltk.download("wordnet")

from nltk.corpus import verbnet
try:  
    verbnet.lemmas  
except LookupError:
    print("Downloading verbnet...")
    nltk.download("verbnet")
    
from qanom import utils

# Lists of verbs - take union as verb-seed

# from pattern - 8.5K
all_pattern_verbs = []
"""
Original pattern package have bugs in this verbs.infinitives class.
For this reason, in the annotation pipeline, we didn't use their verb seed. 
Here we are installing pattern from git, so bug is fixed. 
If you wish for consistency with original QANom dataset, leave the next line commented out.
If you care only for better coverage, uncomment the following line:
"""
# all_pattern_verbs = list(pattern.verbs.infinitives)

# from wordnet - 8.7K verbs
all_wn_verbs = sorted(set(l.name()
                for v_syn in wn.all_synsets(pos="v")
                for l in v_syn.lemmas()
                if "_" not in l.name()))
# from verbnet - 3.6K verbs
all_verbnet_verbs = list(verbnet.lemmas())
# together - 10.6K verbs
infinitives = sorted(set(all_wn_verbs + all_pattern_verbs + all_verbnet_verbs))

def as_gerund(verb):
    try:    # pattern's lazy-loaders have a bug (first-time failure)
        v_prog = pattern.conjugate(verb, aspect=pattern.PROGRESSIVE)
    except:
        v_prog = pattern.conjugate(verb, aspect=pattern.PROGRESSIVE)

    return v_prog

class SuffixBasedNominalizationCandidates:

    def __init__(self, verb_seed=infinitives):
        """
        :param verb_seed: a list of verbs (infinitive form). The seed for the artificial deverbal-nouns list.
        Generates a list of (possible-nom, source-verb) based on affix heuristics for each verb in verb_seed.
        The list is available via self.get_deverbal_pairs() method and in other formats through other methods.
        """
        self.verb_seed = verb_seed

        # initialize the deverbal-pairs list
        self._nom_verb_pair_list = self._generate_deverbal_pairs()

        # initialize the dict
        self._affixes_based_nom_dict = self._generate_deverbal_dict(multipleEntriesPerNom=True)

    @classmethod
    def with_suffix(cls, verb, suffix, replace=[]):
        for suf_to_replace in sorted(replace, key=lambda s:len(s), reverse=True):
            if verb.endswith(suf_to_replace):
                return verb.rstrip(suf_to_replace) + suffix
        return verb + suffix

    @classmethod
    def replace_suffix(cls, verb, replacements):
        # replacements is dict {"current-suffix" : "new-suffix"}
        for suf, new_suf in sorted(replacements.items(), key=lambda pair: len(pair[0]), reverse=True):
            if verb.endswith(suf):
                return verb.rstrip(suf) + new_suf
        return verb

    @classmethod
    def verb_to_all_possible_nominalizations(cls, verb):
        # returns ~17 possible nominal forms of the verb, using morphology only (some are probably not words)
        noms = [verb,
                str(as_gerund(verb)),
                # -tion suffix: ("construction")
                cls.with_suffix(verb, suffix="tion", replace=["t", "te"]),
                cls.replace_suffix(verb, {"ire": "iration",
                                      "ume": "umption",
                                      "quire": "quisition",
                                      "lve": "lution"}),
                # -sion suffix: ("conclusion", "transmission")
                cls.replace_suffix(verb, {"it": "ission",
                                      "t": "sion",
                                      "de": "sion",
                                      "d": "sion",
                                      "se": "sion",
                                      "ss": "ssion"
                                      }),
                # -ment suffix: ("development")
                cls.with_suffix(verb, suffix="ment"),
                # -ance suffix: ("acceptance")
                cls.replace_suffix(verb, {"ance": "ance",
                                      "e": "ance",
                                      "": "ance",
                                      "y": "iance"}),
                # -ence suffix: ("reference")
                cls.replace_suffix(verb, {"ent": "ence",
                                      "e": "ence",
                                      "": "ence"}),
                # -ure suffix: ("failure")
                cls.with_suffix(verb, suffix="ure", replace=["e", "ure"]),
                # -al suffix: (e.g. proposal, withdrawal)
                cls.with_suffix(verb, suffix="al", replace=["e", "al"]),
               ]
        plural_nominalizations = list(map(pattern.pluralize, set(noms)))
        all_verb_derived_noms = list(set(noms + plural_nominalizations))
        return all_verb_derived_noms

    def _generate_deverbal_dict(self, multipleEntriesPerNom):
        """
        Returns:
            multipleEntriesPerNom==False:   a dict { nom : source-verb }
            multipleEntriesPerNom==True:    a dict { nom : [source-verbs] }
        Note: when multipleEntriesPerNom == False, function is not handling cases where
        the same affix-based potential nominalization is derived from multiple verbs.
        The dict will conflate these arbitrarily.
        """
        pairs = self.get_deverbal_pairs()
        if multipleEntriesPerNom:
            return utils.dictOfLists(pairs)
        else:
            return dict(pairs)


    def get_deverbal_dict(self):
        """
        Returns the field generated by self._generate_deverbal_dict()
        """
        return self._affixes_based_nom_dict

    # this method is called upon import. it creates the long list of pairs and returns it
    def _generate_deverbal_pairs(self):
        """
        Return a list of (possible-nom, source-verb) based on affix heuristics for each verb in self.verb_seed.
        """
        return [(nom, verb)
                for verb in self.verb_seed
                for nom in self.verb_to_all_possible_nominalizations(verb)]


    def get_deverbal_pairs(self):
        """
        Return a list of (possible-nom, source-verb) based on affix heuristics for each verb in verb_seed.
        """
        return self._nom_verb_pair_list


    def get_all_possible_nominalizations(self):
        return self.get_deverbal_dict().keys()

    # End usage - create verb_to_nom list and query noun for source verbs
    def get_source_verbs(self, nn):
        """ Return a list of source verbs per noun if noun is in artificially generated verb_to_nom list.
            If noun is not in list, returns empty list.
        """
        if nn in self._affixes_based_nom_dict:
            return self._affixes_based_nom_dict[nn]
        else:
            return []



# A shortcut name for the class - VTN (verb-to-nominal)
VTN = SuffixBasedNominalizationCandidates


"""
Unit testing:
"""
if __name__ == '__main__':
    print("Testing SuffixBasedNominalizationCandidates class:")
    vtn = SuffixBasedNominalizationCandidates()
    test_verb = "show"
    all_noms = VTN.verb_to_all_possible_nominalizations(test_verb)
    print(f"all noms of {test_verb} are: {all_noms}")
    pairs = vtn.get_deverbal_pairs()
    print(f"number of all possible_noms pairs is {len(pairs)}")
    dct = vtn.get_deverbal_dict()

    print(f'source verb for "development": {vtn.get_source_verbs("development")}')