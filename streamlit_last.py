import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="売上分析アプリ", layout="wide")
st.title("広告費と売上の相関分析アプリ")

# データの読み込み
df = pd.read_csv('ad_expense_sales.csv')

# --- サイドバーの作成 ---
st.sidebar.header("検索オプション")

# 1. カテゴリでフィルタ
categories = df['prod_category'].unique()
selected_cat = st.sidebar.multiselect('製品カテゴリ選択', categories, default=categories)

# 2. 季節でフィルタ
seasons = df['season'].unique()
# 'All'の選択肢を追加
selected_season = st.sidebar.selectbox('季節選択', ['All'] + list(seasons))

# --- データの抽出 ---
filtered_df = df[df['prod_category'].isin(selected_cat)]

if selected_season != 'All':
    filtered_df = filtered_df[filtered_df['season'] == selected_season]

# データ件数の表示
st.write(f"データ件数: {len(filtered_df)} 件")
st.dataframe(filtered_df)