from pathlib import Path
import os
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split


def save_model(request_id, model):
    directory = Path("prediction-model-saves/")
    if not os.path.exists(str(directory)):
        os.makedirs(str(directory))

    path = str(directory.joinpath(f"model-{request_id}.pickle"))

    with open(path, "wb") as file:
        pickle.dump(model, file)

    return path


def load_model(model_file):
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
    return model


def load_train_data(csv_file_path):
    df = pd.read_csv(csv_file_path)
    return df


def split_data_for_validation(dataframe, validation_percentage):
    train_data, validation_data = train_test_split(dataframe,
                                                   test_size=validation_percentage,
                                                   random_state=42)
    return train_data, validation_data


def validate_model(model, dataframe, kpi_col_name, validation_percentage):
    train_data, validation_data = split_data_for_validation(dataframe, validation_percentage)
    y_column = kpi_col_name.replace(" ", "_")
    result_frame = validation_data.copy()

    X_test = validation_data.copy()
    y_test = X_test.pop(y_column).to_numpy()
    X_test = X_test.to_numpy()
    y_pred = model.predict(X_test)

    # Add columns
    result_frame.pop(y_column)
    result_frame['prediction'] = y_pred
    result_frame['actual'] = y_test
    result_frame['error'] = y_test - y_pred

    return result_frame
