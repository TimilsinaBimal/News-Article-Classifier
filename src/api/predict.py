import pandas as pd
from clean_string import clean_string
import pickle
import pathlib
import os

ROOT_PATH = pathlib.Path(__file__).parent.parent.parent


def clean_data(data):
    data_df = pd.DataFrame({
        "body": data
    }, index=[0])
    data_df.body = clean_string(data_df.body)
    return data_df


def prepare_data(data):
    transformer = pickle.load(
        open(os.path.join(ROOT_PATH, "pickle_files", "transformer.pkl"), "rb"))
    chi2_selector = pickle.load(
        open(os.path.join(ROOT_PATH, "pickle_files", "chi2_selector.pkl"), "rb"))
    X_test = transformer.transform(data.body)
    X_test = chi2_selector.transform(X_test)
    return X_test


def predict(data):
    model = pickle.load(
        open(os.path.join(ROOT_PATH, "pickle_files", "model.pkl"), "rb"))
    cleaned_data = clean_data(data)
    X_test = prepare_data(cleaned_data)
    prediction = model.predict(X_test)[0]
    return prediction
