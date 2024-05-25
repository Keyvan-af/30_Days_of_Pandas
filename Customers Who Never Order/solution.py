import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    names = []
    for i in range(len(customers)):
        if customers['id'][i] not in orders['customerId'].tolist():
            names.append(customers['name'][i])
    df = pd.DataFrame({
        "Customers": names
    })
    return df