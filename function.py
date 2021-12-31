import  pandas as pd
def dataset():
    data=pd.read_csv('G:/my_project/barcode-reader/upc_corpus.csv')
    barcode_data=data.iloc[:,0]
    barcode_target=data.iloc[:,1]
    barcode_target=list(barcode_target)
    barcode_data=list(barcode_data)
    return  barcode_data,barcode_target
