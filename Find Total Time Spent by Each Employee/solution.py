import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees_group = employees.groupby(["emp_id", "event_day"])[['in_time', 'out_time']].sum().reset_index()
    employees_group['total_time'] = employees_group['out_time'] - employees_group['in_time']
    employees_group = employees_group[['event_day', 'emp_id', 'total_time']]
    employees_group.rename(columns={'event_day' : 'day'}, inplace=True)
    return employees_group
