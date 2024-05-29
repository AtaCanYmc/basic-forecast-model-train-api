import sqlite3
from pathlib import Path
from sklearn.utils import shuffle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle
import os


def shuffle_data(dataframe, random_state=42):
    shuffled_data = shuffle(dataframe, random_state=random_state)
    return shuffled_data


def data_standardization(request_id, dataframe, output_dir='../standardizer'):
    """
    Standardizes the features of the dataframe using StandardScaler and saves the scaler model.

    Parameters:
    request_id (str): Unique identifier for the request, used to name the saved scaler model file.
    dataframe (pd.DataFrame): The dataframe containing features to be standardized.
    output_dir (str): Directory where the scaler model file will be saved.

    Returns:
    pd.DataFrame: A dataframe with standardized features.
    """

    # Initialize the StandardScaler
    scaler = StandardScaler()

    # Scale the features
    scaled_features = scaler.fit_transform(dataframe.values)

    # Create a new dataframe with the scaled features
    dataframe_scaled = pd.DataFrame(scaled_features, columns=dataframe.columns, index=dataframe.index)

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the scaler model to a file
    model_path = os.path.join(output_dir, f'model-{request_id}.pkl')
    with open(model_path, 'wb') as file:
        pickle.dump(scaler, file)

    return dataframe_scaled
