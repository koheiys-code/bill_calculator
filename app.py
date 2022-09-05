import streamlit as st
import pandas as pd
import numpy as np
# from matplotlib import pyplot as plt


st.title('散布図を表示させてください。')
uploaded_file = st.file_uploader("↓↓講義で使用したscore_data.csvをアップロード↓↓")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    a = st.slider("Xの各データの倍数を決定。", 1, 100, 1)
    st.write(f'#### →→Xのデータを{a}倍します。')
    ''
    ''
    b = st.slider("Yの各データの倍数を決定。", 1, 100, 1)
    st.write(f'#### →→Yのデータを{b}倍します。')
    arr_X = []
    arr_Y = []
    for i in range(len(df['score_X'])):
        arr_X.append(df['score_X']*a)
        arr_Y.append(df['score_Y']*b)
    arr_X = np.array(arr_X)
    arr_Y = np.array(arr_Y)
    cov_XY = np.cov(arr_X[0], arr_Y[0], ddof=0)  # 分散共分散行列
    cor_XY = cov_XY[0][1]/(np.sqrt(cov_XY[0][0])*np.sqrt(cov_XY[1][1]))  # 相関係数

    # st.write('## 散布図')
    # fig = plt.figure(figsize=(12, 12))
    # ax = plt.axes()
    # plt.xlabel('X', fontsize=18)
    # plt.ylabel('Y', fontsize=18)
    # plt.tick_params(labelsize=18)
    # plt.tight_layout()
    # plt.scatter(arr_X, arr_Y)
    # st.pyplot(fig)

    st.write("## 分散・共分散・相関係数")

    st.write("Xの分散:", cov_XY[0][0])
    st.write("Yの分散:", cov_XY[1][1])
    st.write("共分散:", cov_XY[0][1])
    st.write("相関係数:", cor_XY)
