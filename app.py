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
        bill_dict[name].append([purpose, bill])

    for name, contents in bill_dict.items():
        st.write(name)
        df = pd.DataFrame(contents, columns=['目的', '金額'])
        st.dataframe(df, width=10)
        st.write(df['金額'].sum())
