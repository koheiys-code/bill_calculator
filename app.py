"""
[name] app.py
[purpose] calculate how much you will pay per person.
[reference]
    https://docs.streamlit.io/library/api-reference/layout/st.columns
    https://docs.streamlit.io/library/api-reference/widgets/st.slider
    https://docs.streamlit.io/library/api-reference/widgets/st.text_input
    https://docs.streamlit.io/library/api-reference/widgets/st.text_area
    https://docs.streamlit.io/library/api-reference/layout/st.tabs

written by Kohei YOSHIDA, 2022/9/10
"""
from collections import defaultdict

import streamlit as st
import pandas as pd


st.title("払い戻す金額を計算します")

left, right = st.columns(2)
number = left.slider('人数を入れてください', 1, 30, value=17)
per_pool = right.text_input('一人当たりのプール金額を入れてください', value=20000)

lines = st.text_area("立て替えた人の'名前、内容、金額'を縦に並べて入力してください")

if number and per_pool and lines:
    pool = int(number) * int(per_pool)
    lines = lines.split()
    bill_dict = defaultdict(list)
    bill_dict['プール'] = []
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
    rest_pool = pool - subtotal_df['小計'].sum()
    return_pool = rest_pool // number
    subtotal_df['払い戻し金額'] = subtotal_df['小計'] + return_pool
    st.write(f'プールされた金額：{pool}')
    st.write(f'プールに残る金額：{rest_pool}')
    st.write(f'立て替えていない人：{return_pool}')
    st.dataframe(subtotal_df.iloc[1:])

    names = list(bill_dict.keys())
    for name, tab in zip(names, st.tabs(names)):
        tab.write(f'小計：{subtotal_dict[name]}')
        tab.dataframe(bill_dict[name])

else:
    st.write('例：')
    st.write('ゴリラ、りんご、4000')
    st.write('うさぎ、レタス、2000')
    st.write('パンダ、笹、1000')
    st.write('ゴリラ、バナナ、2000')
    st.write('プール、車代、30000')
