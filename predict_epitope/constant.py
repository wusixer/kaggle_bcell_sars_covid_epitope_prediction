import numpy as np
import pandas as pd
# read in data, filter out sequences
bcell_sars = pd.read_csv("../data/bcell_sars_processed.csv")
bcell_sars = bcell_sars[bcell_sars['peptide_length']<30]

# get unique AA from all sequences presented
all_seq = bcell_sars.protein_seq.to_list()+ bcell_sars.peptide_seq.to_list()
unique_aa = set([letter for item in range(len(all_seq)) for letter in all_seq[item] ])


def create_dictionary(unique_aa):
    """given the unique amino acids, output two dictionary, one maps each AA 
    to a numeric value, the other map the numeric value back to AA"""
    char_to_idx = dict()
    idx_to_char = dict()
    idx = 0
    for char in unique_aa:
        if char not in char_to_idx.keys():
        # Build dictionaries
            char_to_idx[char] = idx
            idx_to_char[idx] = char
            idx += 1

    return char_to_idx, idx_to_char

#make word_to_int dict and int_to_word dict
LETTER_TO_IDX, IDX_TO_LETTER = create_dictionary(unique_aa)
print(LETTER_TO_IDX, IDX_TO_LETTER)
