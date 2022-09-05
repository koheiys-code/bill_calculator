from collections import defaultdict

import streamlit as st
import pandas as pd
import numpy as np
# from matplotlib import pyplot as plt


st.title("払う金額を計算します")

lines = st.text_area("'名前、目的、金額'を縦に並べて入力してください")
if lines:
    st.write(lines)
    for line in lines.split(' '):
        st.write('###')
        st.write(line)
        st.write('###')
    # bill_dict = defaultdict(list)
    # for line in lines:
    #     st.write('#####')
    #     st.write(line)
    #     st.write('#####')
    #     name, purpose, bill = line.split('、')
    #     bill_dict[name].append([purpose, bill])

    # for name, contents in bill_dict.items():
    #     st.write(name)
    #     for content in contents:
    #         content = ' '.join(content)
    #         st.write('\t'+content)
