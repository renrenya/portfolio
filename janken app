import streamlit as st
import random

st.title("じゃんけんゲーム")

# 初期化（初回のみ）
if "win" not in st.session_state:
    st.session_state.win = 0
    st.session_state.lose = 0
    st.session_state.draw = 0

hands = ["グー", "チョキ", "パー"]

# プレイヤーの手を選ぶ
player_hand = st.radio("あなたの手を選んでください", hands)

# ボタンを押すとじゃんけん開始
if st.button("じゃんけんポン！"):
    com_hand = random.choice(hands)

    # 勝敗判定
    if player_hand == com_hand:
        result = "ひきわけ"
        st.session_state.draw += 1
    elif (
        (player_hand == "グー" and com_hand == "チョキ") or
        (player_hand == "チョキ" and com_hand == "パー") or
        (player_hand == "パー" and com_hand == "グー")
    ):
        result = "勝ち"
        st.session_state.win += 1
    else:
        result = "負け"
        st.session_state.lose += 1

    # 結果表示
    st.write(f" CPUの手: {com_hand}")
    st.write(f" 結果: あなたは 「{result}」 ました！")

# 勝敗の履歴表示
st.markdown("### 勝敗記録")
st.write(f"〇 勝ち: {st.session_state.win}")
st.write(f"× 負け: {st.session_state.lose}")
st.write(f"△ ひきわけ: {st.session_state.draw}")
