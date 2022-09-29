import os
import pandas as pd

def data_extraction(data_resource_url, resource_folder = "./data/resource/"):
    df = pd.read_csv(data_resource_url)
    print("The quantity of row data: {}".format(len(df)))
    print("The number of columns: {}".format(len(df.columns)))

    if not os.path.exists(resource_folder):
        os.makedirs(resource_folder)
        df.to_csv(os.path.join(resource_folder, "{}.csv".format(self.dataset_name)), index=False)
    return df