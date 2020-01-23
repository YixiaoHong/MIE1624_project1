import pandas as pd
ss = 'https://raw.githubusercontent.com/YixiaoHong/MIE1624_project1/master/online_shoppers_intention.csv'
df = pd.read_csv(ss, error_bad_lines=False)
a = 5
df.dtypes
