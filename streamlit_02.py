import streamlit as st
import pandas as pd
import numpy as np

st.title("グラフ表示の練習")

# 練習用のデータ（ランダムな数値の表）を作る
df = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.write("1. 折れ線グラフ")
st.line_chart(df)

st.write("2. 棒グラフ")
st.bar_chart(df)