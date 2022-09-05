"""
[name] app.py
[purpose] calculate how much you will pay per person.
[reference]
    https://docs.streamlit.io/library/api-reference/widgets/st.text_area
    https://docs.streamlit.io/library/api-reference/layout/st.tabs

written by Kohei YOSHIDA, 2022/9/6
"""
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

    subtotal_dict = {}
    for name, contents in bill_dict.items():
        df = pd.DataFrame(contents, columns=['内容', '金額'])
        bill_dict[name] = df
        subtotal_dict[name] = df['金額'].sum()

    subtotal_df =\
        pd.DataFrame.from_dict(subtotal_dict, orient='index', columns=['小計'])
    total = subtotal_df['小計'].sum()
    mean_ = int(subtotal_df['小計'].mean())
    subtotal_df['支払う金額'] = mean_ - subtotal_df['小計']
    st.write(f'全員の合計：{total}')
    st.write(f'一人当たり：{mean_}')
    st.dataframe(subtotal_df)

    names = list(bill_dict.keys())
    for name, tab in zip(names, st.tabs(names)):
        tab.write(f'小計：{subtotal_dict[name]}')
        tab.dataframe(bill_dict[name])

else:
    st.write('例：')
    st.write('ゴリラ、りんご、300')
    st.write('うさぎ、レタス、200')
    st.write('パンダ、笹、1000')
    st.write('ゴリラ、バナナ、200')
