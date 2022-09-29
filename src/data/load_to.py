import os
import pickle
from datetime import datetime

def data_load_to(data, dataset, dataset_name, result_folder = "./data/result"):
    # Setting folder
    time_string = datetime.now().strftime("%Y%m%d_%H%M%S")
    time_result_folder = os.path.join(result_folder, time_string)

    if not os.path.exists(time_result_folder):
        os.makedirs(time_result_folder)
    
    # Save dataframe to csv file.
    dataframe_file_path = os.path.join(time_result_folder, "{}.csv".format(dataset_name))
    data.to_csv(dataframe_file_path, index=False)
    print("Finish save the dataframe to {}.".format(dataframe_file_path))

    # Save dict dataset to pickle file.
    pickle_file_path = os.path.join(time_result_folder, 'dataset.pickle')
    with open(pickle_file_path, 'wb') as f:
        pickle.dump(dataset, f)
    print("Finish save the dict to {}.".format(pickle_file_path))
