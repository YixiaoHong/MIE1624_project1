import pandas as pd
d = 6
url = 'https://raw.githubusercontent.com/YixiaoHong/MIE1624_project1/master/online_shoppers_intention.csv'
d = 7
df = pd.read_csv(url, error_bad_lines=False)
df.dtypes