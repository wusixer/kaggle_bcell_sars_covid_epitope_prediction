##COVID-19/SARS B-cell Epitope Prediction
project data [link](https://www.kaggle.com/futurecorporation/epitope-prediction
)

See `epitope_predict_notebook` folder for more results and details

Basically, peptides were converted to numerical representations (0 to 20, with 20 being a padded character). It is then feed through:

1. an embedding layer
2. a bi-lstm layer
3. a FC layer 
4. a FC layer with 1 node (output)

The results were not super promising (at least in training), it seems to always predicting the same class. Several modifications have been attempted:

1. Pad all peptides length to 28
2. Use the most frequent peptide (len 15) without padding
3. Use parental protein to pad

None of them solved the mono-class prediction problem. 

I found that there are several entrie errors (e.g wrong starting position, mislabel of labels). The conclusion is that this dataset is of poor quality, and splitting it further for deep learning task would not give better performance.
  
