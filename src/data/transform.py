import pandas as pd
from sklearn.preprocessing import minmax_scale
from sklearn.model_selection import train_test_split

def data_transform(df, 
                   data_column_list = ['sepal.length','sepal.width','petal.length','petal.width'], 
                   label_column = 'variety'):
    # Get the dataset and y label.
    ## Dataset
    x_data = df[data_column_list]
    x_data = minmax_scale(x_data, feature_range=(0, 1), axis=0, copy=True)
    ## Label
    y_data = list(pd.factorize(df[label_column])[0])

    # Split to training and testing dataset
    dataset = {}
    dataset['x_train'], dataset['x_test'], dataset['y_train'], dataset['y_test'] = \
        train_test_split(x_data, y_data, test_size=0.25, random_state=42)
    
    # Concat to the pandas dataframe.
    x_data = pd.DataFrame(x_data, columns=['sepal.length','sepal.width','petal.length','petal.width'])
    y_data = pd.DataFrame(y_data, columns=['target'])
    data = pd.concat([x_data, y_data], axis=1)
    
    return data, dataset