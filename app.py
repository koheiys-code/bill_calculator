from collections import defaultdict

import streamlit as st
import pandas as pd
import numpy as np
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

    sum_table = {}
    for name, contents in bill_dict.items():
        st.write(name)
        df = pd.DataFrame(contents, columns=['目的', '金額'])
        st.dataframe(df)
        sum_ = df['金額'].sum()
        st.write(f'合計：{sum_}')
        sum_table[name] = sum_

    df = pd.DataFrame.from_dict(sum_table, orient='index', columns=['合計'])
