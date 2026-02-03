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

# --- タブの作成 ---
tab_analysis, tab_data, tab_report = st.tabs(["分析", "データ", "レポート"])

# --- タブ1: 分析 ---
with tab_analysis:
    st.header("売上分析ダッシュボード")
    
    # 重要な指標 (KPI) の計算
    total_sales = filtered_df['sales'].sum()
    total_expense = filtered_df['ad_expense'].sum()
    
    # 指標の表示 (st.metricを使用)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("総売上", f"{total_sales:,.0f} 万円")
    with col2:
        st.metric("総広告費", f"{total_expense:,.0f} 万円")
        
    st.divider()

    st.subheader("可視化グラフ")
    
    # グラフ1: 広告費と売上の散布図
    # 散布図で相関を見ます
    fig_scatter = px.scatter(
        filtered_df,
        x='ad_expense',
        y='sales',
        color='prod_category',
        title="1. 広告費と売上の関係"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    # グラフ2: 季節ごとの平均売上
    # 棒グラフで比較します
    st.subheader("季節ごとの傾向")
    # 平均値を計算
    avg_sales = filtered_df.groupby('season', as_index=False)['sales'].mean()
    
    fig_bar = px.bar(
        avg_sales,
        x='season',
        y='sales',
        title="2. 季節ごとの平均売上"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- タブ2: データ ---
with tab_data:
    st.subheader("使用しているデータ")
    st.write(f"データ件数: {len(filtered_df)} 件")
    st.dataframe(filtered_df, use_container_width=True)
    
    # st.expanderを使って詳細情報を折りたたむ
    # 課題要件：未使用のUI部品（Expander）を使用
    with st.expander("各カラム（列）の意味を確認"):
        st.markdown("""
        - **prod_category**: 製品のカテゴリ
        - **sales**: 売上実績（万円）
        - **ad_expense**: 広告宣伝費（万円）
        - **season**: 販売された季節
        """)

# --- タブ3: レポート ---
with tab_report:
    st.subheader("分析レポート")
    st.markdown("""
    **【考察】**
    
    1. **広告費と売上の関係**
       - 散布図を見ると、広告費が高いほど売上も高くなる傾向が見られます。
       - 特に「パソコン」カテゴリでその傾向が顕著です。
       
    2. **季節ごとの傾向**
       - 季節ごとの平均売上を比較すると、特定の季節（例えば夏や冬）に売上が伸びている、あるいは変わらない等が読み取れます。
       - このデータでは季節による大きな差は少ないようですが、製品ごとに見ると違いがあるかもしれません。
       
    （ここに自分の考察を追記してください）
    """)