import streamlit as st

st.set_page_config(page_title="더치500", page_icon="💸", layout="centered")

st.title("💸 더치500")
st.write("500원 단위로 나누는 더치페이 계산기")

# 입력
total = st.number_input("총 금액 (원)", min_value=0, step=500)
people = st.number_input("인원 수", min_value=1, step=1)

# 계산 함수
def dutch_pay(total_amount, num_people):
    base_amount = (total_amount // num_people) // 500 * 500
    payments = [base_amount] * num_people
    remainder = total_amount - base_amount * num_people
    extra_500_count = remainder // 500
    for i in range(extra_500_count):
        payments[i] += 500
    return payments

# 버튼 누르면 결과 출력
if st.button("계산하기"):
    if total == 0 or people == 0:
        st.warning("총 금액과 인원 수를 올바르게 입력하세요.")
    else:
        result = dutch_pay(total, people)
        st.subheader("💰 결과")
        for i, pay in enumerate(result, 1):
            st.write(f"{i}번 사람: {pay:,}원")
