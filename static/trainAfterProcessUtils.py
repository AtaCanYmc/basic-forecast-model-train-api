from pathlib import Path
import os
import pickle


def save_model(request_id, model):
    directory = Path("prediction-model-saves/")
    if not os.path.exists(str(directory)):
        os.makedirs(str(directory))

    path = str(directory.joinpath(f"model-{request_id}.pickle"))

    with open(path, "wb") as file:
        pickle.dump(model, file)

    return path
