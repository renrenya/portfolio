# calculator.py
import streamlit as st

st.title("簡易電卓アプリ")

# 入力欄
expr = st.text_input("計算式を入力（例: 1 + 2）,( 2 * 3)")

# 計算履歴
if "history" not in st.session_state:
    st.session_state.history = []

# 計算ボタンを押したとき
if st.button("計算"):
    try:
        result = eval(expr)
        st.session_state.history.append(f"{expr} = {result}")
        st.success(f"結果: {result}")
    except Exception as e:
        st.error(f"エラー: {e}")

# 履歴表示
st.markdown("### 計算履歴")
for h in reversed(st.session_state.history):
    st.write(h)
