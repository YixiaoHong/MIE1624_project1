import pandas as pd
dd = 'https://raw.githubusercontent.com/YixiaoHong/MIE1624_project1/master/online_shoppers_intention.csv'
df = pd.read_csv(dd, error_bad_lines=False)
df.dtypes