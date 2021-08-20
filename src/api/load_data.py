import pandas as pd


def read_data(filepath, label=True):
    df = pd.read_csv(filepath, encoding="ISO-8859-1")
    df.drop_duplicates(inplace=True)
    df['text'] = df['text'].astype("U")
    if label:
        labels = df.label.unique()
        categories = {labels[idx]: idx for idx in range(len(labels))}
        def map_to_category(column): return categories[column]
        df.label = df.label.map(map_to_category)
        return df, labels, categories
    return df
