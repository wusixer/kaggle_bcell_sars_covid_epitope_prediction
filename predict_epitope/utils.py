import torch
from predict_epitope.constant import LETTER_TO_IDX, IDX_TO_LETTER

def convert_aa_to_int(aa_sequence):
    """convert an AA sequence to its integer representation"""
    #[LETTER_TO_IDX[aa] for item in range(batch_size) for LETTER_TO_IDX[aa] bcell_train['peptide_seq'][batch_size]]
    return [LETTER_TO_IDX[aa] for aa in aa_sequence]

def pad_int_to_int_aa_seq(aa_seq_converted_to_int, len_after_pad):
    """pad (with 20) at of the of an int representation of an AA sequence to uniform length ==28"""
    padding_len = len_after_pad - len(aa_seq_converted_to_int)
    # always use a positive integer to represent a character/missing
    #that is next in line with the max number in the dictionary, this
    # is to prevent indexing a matrix that doesn't have the specificed 
    # indices. e.g dictionary goes to {...., 'X':19}, then the next 
    # charater of interest should be assigned 20 instead of any other number.
    return aa_seq_converted_to_int + [20]*padding_len

class Dataset(torch.utils.data.Dataset):
  'Characterizes a dataset for PyTorch'
  def __init__(self, peptide_to_integers, labels):
        'Initialization'
        self.peptide_to_integers = peptide_to_integers
        #self.peptide_to_integers = torch.stack(peptide_to_integers).type(torch.LongTensor)
        self.labels = labels

  def __len__(self):
        'Denotes the total number of samples'
        return len(self.peptide_to_integers)

  def __getitem__(self, index):
        'Generates one sample of data'
        # Load data and get label
        X = self.peptide_to_integers[index]
        y = self.labels[index]

        return X, y

