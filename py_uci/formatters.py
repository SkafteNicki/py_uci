# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 08:36:20 2019

@author: nsde
"""

#%%
import pandas as pd
import zipfile

#%%
def Abalone(dataset):
    for f in dataset.files:
        if 'abalone.data' in f:
            df = pd.read_csv(f, sep=',', header=None)
    df.columns = ['Sex', 'Length', 'Diameter', 'Hight', 'Whole weight',
                  'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']
    return df

#%%
def Adult(dataset):
    for f in dataset.files:
        if 'adult.data' in f:
            df1 = pd.read_csv(f, sep=',', header=None)
        if 'adult.test' in f:
            df2 = pd.read_csv(f, sep=',', header=None, skiprows=1)
    df = pd.concat([df1, df2], axis=0, ignore_index=True)
    df.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num',
                  'marital-status', 'occupation', 'relationship', 'race',
                  'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country',
                  'income']
    df['income'] = df['income'].replace(' <=50K.', '<=50K')
    df['income'] = df['income'].replace(' >50K.', '>50K')
    return df

#%%
def Bike_Sharing_Dataset(dataset):
    # Extract .zip file
    for f in dataset.files:
        if 'Bike-Sharing-Dataset.zip' in f:
            zipref = zipfile.ZipFile(f, 'r')
            zipref.extractall('/'.join(f.split('/')[:-1]))
            zipref.close()
    
    dataset._update_file_list()
    
    # Get dataframe
    for f in dataset.files:
        if 'day.csv' in f:
            df = pd.read_csv(f)
    df = df.drop('instant', 1)
    df = df.drop('dteday', 1)
    return df

#%%
def Boston(dataset):
    for f in dataset.files:
        if 'housing.data' in f:
            df = pd.read_csv(f, delim_whitespace=True)
    df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS',
                  'NOX', 'RM', 'AGE', 'DIS', 'RAD',
                  'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
    
#%%
def Carbon_Nanotubes(dataset):
    for f in dataset.files:
        if 'carbon_nanotubes.csv' in f:
            df = pd.read_csv(f, sep=';')
    return df
        
#%%
def Concreate(dataset):
    for f in dataset.files:
        if 'Concrete_Data.xls' in f:
            df = pd.read_excel(f)
    return df

#%%
def Forest_Fire(dataset):
    for f in self.files:
        if 'forestfires.csv' in f:
            df = pd.read_csv(f)
    return df
        
#%%
def Iris(dataset):
    for f in dataset.files:
        if 'iris.data' in f:
            df = pd.read_csv(f, header=None)
    df.columns = ['sepal length', 'sepal width', 
                  'petal length', 'petal width', 'flower type']
    return df

#%%
def Navel(dataset):
    # Extract .zip file
    for f in dataset.files:
        if 'UCI%20CBM%20Dataset.zip' in f:
            zipref = zipfile.ZipFile(f, 'r')
            zipref.extractall('/'.join(f.split('/')[:-1]))
            zipref.close()
        
    dataset._update_files_list()
             
    # Move files from folder to data folder
    for f in dataset.files:
        if os.path.isdir(f) and '_MACOSX' not in f:
            for ff in os.listdir(f):
                old = f + '/' + ff
                new = '/'.join(f.split('/')[:-1]) + '/' + ff.split('/')[-1]
                os.rename(old, new)

    dataset._update_files_list()
        
    # Get dataframe
    for f in self.files:
        if 'data.txt' in f:
            df = pd.read_fwf(f, header=None)
    df.columns = ['Lever position', 'Speed', 'GTT',
                  'GTn', 'GGn', 'Ts', 'Tp', 'T48', 'T1', 'T2', 'P48', 'P1', 
                  'P2', 'Pexh', 'TIC', 'mf', 'Comp. decay', 'Turb. decay ']
    return df

#%%
def Power_Plant(dataset):
    # Extract .zip file
    for f in dataset.files:
        if 'CCPP.zip' in f:
            zipref = zipfile.ZipFile(f, 'r')
            zipref.extractall('/'.join(f.split('/')[:-1]))
            zipref.close()
        
    dataset._update_files_list()
        
    # Move files from folder to data folder
    for f in dataset.files:
        if os.path.isdir(f):
            for ff in os.listdir(f):
                old = f + '/' + ff
                new = '/'.join(f.split('/')[:-1]) + '/' + ff.split('/')[-1]
                os.rename(old, new)

    dataset._update_files_list()
        
    # Get dataframe
    for f in dataset.files:
        if 'Folds5x2_pp.xlsx' in f:
            df = pd.read_excel(f)
    return df
        
#%%
def Protein_Structure(dataset):
    for f in dataset.files:
        if 'CASP.csv' in f:
            df = pd.read_csv(f)
    dataframe = df
    dataframe.columns = ['RMSD-Size of the residue.',
                         'F1 - Total surface area.',
                         'F2 - Non polar exposed area.',
                         'F3 - Fractional area of exposed non polar residue.',
                         'F4 - Fractional area of exposed non polar part of residue.',
                         'F5 - Molecular mass weighted exposed area.',
                         'F6 - Average deviation from standard exposed area of residue.',
                         'F7 - Euclidian distance.',
                         'F8 - Secondary structure penalty.',
                         'F9 - Spacial Distribution constraints (N,K Value).']
    return df

#%%
def Superconduct(dataset):
    # Extract .zip file
    for f in dataset.files:
        if 'superconduct.zip' in f:
            zipref = zipfile.ZipFile(f, 'r')
            zipref.extractall('/'.join(f.split('/')[:-1]))
            zipref.close()
        
    dataset._update_files_list()
               
    # Get dataframe
    for f in dataset.files:
        if 'train.csv' in f:
                df = pd.read_csv(f)
    return df

#%%
def wine_quality(dataset):
    for f in dataset.files:
        if 'winequality-red.csv' in f:
            df_red = pd.read_csv(f, sep=';')
        if 'winequality-white.csv' in f:
            df_white = pd.read_csv(f, sep=';')
    df = pd.concat([df_red, df_white], axis=0)
    df['type'] = [*(len(df_red)*['red']), *(len(df_white)*['white'])]
    return df
        
#%%        
def wine_red(dataset):
    for f in dataset.files:
        if 'winequality-red.csv' in f:
            df = pd.read_csv(f, sep=';')
    return df
    
#%%        
def wine_white:   
    for f in dataset.files:
        if 'winequality-white.csv' in f:
            df = pd.read_csv(f, sep=';')
    return df
        
#%%
def yacht_hydrodynamics:
    for f in dataset.files:
        if 'yacht_hydrodynamics.data' in f:
            df = pd.read_csv(f, header=None, delim_whitespace=True)
    df.dataframe.columns = ['Longitudinal position of the center of buoyancy, adimensional.',
                            'Prismatic coefficient, adimensional.',
                            'Length-displacement ratio, adimensional.',
                            'Beam-draught ratio, adimensional.',
                            'Length-beam ratio, adimensional.',
                            'Froude number, adimensional. ']
    return df
