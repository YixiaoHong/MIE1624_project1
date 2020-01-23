import pandas as pd
url = 'https://raw.githubusercontent.com/YixiaoHong/MIE1624_project1/master/online_shoppers_intention.csv'
df = pd.read_csv(url, error_bad_lines=False)
df.dtypes