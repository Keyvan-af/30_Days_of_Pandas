import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee['managerId'].value_counts()
    result = employee.loc[employee['id'].isin(df[df>=5].index), ['name']]
    return result