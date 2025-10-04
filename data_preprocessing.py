import pandas as pd
import numpy as np

def data_cleaning(train):
    train.drop_duplicates(keep='first', inplace=True)
    # split 'MONTH' column into 'YEAR' and 'MONTH' columns
    train[['YEAR', 'MONTH']] = train['MONTH'].str.split('-', expand=True).astype(int)
    # ensure consistent formatting in 'FLAT_TYPE' column
    train['FLAT_TYPE'] = train['FLAT_TYPE'].str.replace('-', ' ', regex=False)
    # drop 'ECO_CATEGORY' column as it has the same value for all rows
    train.drop(columns=['ECO_CATEGORY'], inplace=True)
    # create 'FLAT_AGE' column and drop 'LEASE_COMMENCE_DATA' column
    train['FLAT_AGE'] = train['YEAR'] - train['LEASE_COMMENCE_DATA']
    train.drop(columns=['LEASE_COMMENCE_DATA'], inplace=True)
    return train

def merge_hdb_info(train, hdb_info):
    train[['BLOCK', 'STREET']] = train[['BLOCK', 'STREET']].apply(lambda x: x.str.lower())
    hdb_info[['BLOCK', 'ADDRESS']] = hdb_info[['BLOCK', 'ADDRESS']].apply(lambda x: x.str.lower())
    train_merge = train.merge(hdb_info, 
                          how='left', 
                          left_on=['BLOCK', 'STREET'], 
                          right_on=['BLOCK', 'ADDRESS'],
                          indicator=True,
                          suffixes=('', '_HDB'))
    train_merge.drop(columns=['BLOCK', 'STREET', 'TOWN_HDB', 'ADDRESS', 'POSTAL_CODE', '_merge'], inplace=True)
    return train_merge

if __name__ == "__main__":
    train = pd.read_csv('dataset/train.csv', index_col= None)
    test = pd.read_csv('dataset/test.csv', index_col= None)
    hdb_info = pd.read_csv('dataset/auxiliary-data/sg-hdb-block-details.csv', index_col=None)
    cleaned_train = data_cleaning(train)
    cleaned_test = data_cleaning(test)
    merged_train = merge_hdb_info(cleaned_train, hdb_info)
    merged_train.to_csv('merged_train.csv', index=False)
    merged_test = merge_hdb_info(cleaned_test, hdb_info)
    merged_test.to_csv('merged_test.csv', index=False)