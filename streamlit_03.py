import streamlit as st

st.title("UI部品の練習")

# 1. スライダー（資料20ページの「値はすべて変数に入る」を体験）
st.subheader("スライダー")
number = st.slider("好きな数値を選んでください", 0, 100, 50)
st.write(f"現在の値は: {number}")

# 2. チェックボックス（資料20ページの「値を使って条件分岐」を体験）
st.subheader("条件分岐")
is_checked = st.checkbox("メッセージを表示する")

if is_checked:
    st.write("✅ チェックボックスがONになりました！")
else:
    st.write("⬜️ チェックが外れています")

# 3. ボタン
if st.button("ここをクリック"):
    st.balloons()  # お楽しみ機能（風船が飛びます）