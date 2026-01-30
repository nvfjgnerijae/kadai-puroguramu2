import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="売上分析アプリ", layout="wide")
st.title("広告費と売上の相関分析アプリ")

# データの読み込み
df = pd.read_csv('ad_expense_sales.csv')

# データが正しく読めているか確認
st.write("データプレビュー:", df.head())