import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    id = []
    for i in range(len(views)):
        if views['author_id'][i] == views['viewer_id'][i]:
            if views['author_id'][i] not in id:
                id.append(views['author_id'][i])
            else:
                pass
        else:
            pass
    ids = sorted(id)
    df = pd.DataFrame({"id": ids})
    return df