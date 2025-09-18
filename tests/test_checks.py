import pandas as pd
from src.checks import check_missing

def test_check_missing():
    df = pd.DataFrame({"a": [1, None, 3]})
    result = check_missing(df)
    assert result["a"] == 1
