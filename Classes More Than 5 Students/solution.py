import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    counter = courses['class'].value_counts()
    classes = counter[counter >= 5]
    df = classes.reset_index()
    df.drop(columns='count', inplace=True)
    return df