import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    df_merg = pd.merge(employees, employee_uni, on='id', how='left')
    df = pd.DataFrame({
        "unique_id": df_merg['unique_id'],
        "name" : df_merg['name']
    })
    return df
#________________________________________
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    # Merge the two tables on the 'id' column using a left join
    merged = employees.merge(employee_uni, on='id', how='left')
    
    # Return the result table with the 'unique_id' column
    result = merged[['unique_id','name']]
    
    return result