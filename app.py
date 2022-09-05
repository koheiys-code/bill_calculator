from collections import defaultdict

import streamlit as st
import pandas as pd
# from matplotlib import pyplot as plt


st.title("払う金額を計算します")

lines = st.text_area("'名前、目的、金額'を縦に並べて入力してください")
if lines:
    lines = lines.split('\n')
    bill_dict = defaultdict(list)
    for line in lines:
        name, purpose, bill = line.split('、')
        bill = int(bill)
        bill_dict[name].append([purpose, bill])

    sum_dict = {}
    for name, contents in bill_dict.items():
        df = pd.DataFrame(contents, columns=['目的', '金額'])
        bill_dict[name] = df
        sum_dict[name] = df['金額'].sum()

    sum_df = pd.DataFrame.from_dict(sum_dict, orient='index', columns=['合計'])
    mean_ = df['合計'].mean()
    mean_ = int(mean_)
    df['支払う金額'] = df['合計'] - mean_
    st.write(f'一人当たり{mean_}')
    st.dataframe(df)

    names = list(bill_dict.keys())
    for name, tab in zip(names, st.tabs(names)):
        tab.write(f'合計：{sum_dict[name]}')
        tab.dataframe(df)
