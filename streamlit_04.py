import streamlit as st
import pandas as pd
import numpy as np

st.title("レイアウトの練習")

# --- 1. サイドバー (Sidebar) ---
# with st.sidebar: と書くと、その中身は全部サイドバーに入ります
with st.sidebar:
    st.header("設定エリア")
    st.write("ここでグラフを操作します")
    
    # スライダーをサイドバーに配置
    num_points = st.slider("データの数 (N)", 10, 100, 50)
    
    # カラー選択（セレクトボックス）
    color_option = st.selectbox(
        "テーマカラー",
        ["Red", "Blue", "Green"]
    )

# --- 2. カラム分割 (Columns) ---
st.write("以下はメインエリアです。左右に分割します。")

# 画面を2等分する
col1, col2 = st.columns(2)

# 左側のカラム
with col1:
    st.subheader("左側：データ表示")
    st.write(f"選択したデータ数: {num_points}")
    st.write(f"選択した色: {color_option}")
    st.info("ここに文字情報などを置きます")

# 右側のカラム
with col2:
    st.subheader("右側：グラフ表示")
    # ランダムなデータを作ってグラフ化
    df = pd.DataFrame(np.random.randn(num_points, 1), columns=['Data'])
    st.line_chart(df)