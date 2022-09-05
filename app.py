from collections import defaultdict

import streamlit as st
import pandas as pd


st.title("払う金額を計算します")

lines = st.text_area("'名前、内容、金額'を縦に並べて入力してください")
if lines:
    lines = lines.split()
    bill_dict = defaultdict(list)
    for line in lines:
        name, purpose, bill = line.split('、')
        bill = int(bill)
        bill_dict[name].append([purpose, bill])

    sum_dict = {}
    for name, contents in bill_dict.items():
        df = pd.DataFrame(contents, columns=['内容', '金額'])
        bill_dict[name] = df
        sum_dict[name] = df['金額'].sum()

    sum_df = pd.DataFrame.from_dict(sum_dict, orient='index', columns=['合計'])
    total = sum_df['合計'].sum()
    mean_ = int(sum_df['合計'].mean())
    sum_df['支払う金額'] = sum_df['合計'] - mean_
    st.write(f'全員の合計：{total}')
    st.write(f'一人当たり：{mean_}')
    st.dataframe(sum_df)

    names = list(bill_dict.keys())
    for name, tab in zip(names, st.tabs(names)):
        tab.write(f'合計：{sum_dict[name]}')
        tab.dataframe(bill_dict[name])

else:
    st.write('例：')
    st.write('ゴリラ、りんご、300')
    st.write('うさぎ、レタス、200')
    st.write('パンダ、笹、1000')
    st.write('ゴリラ、バナナ、200')
