import streamlit as st

st.title("ỨNG DỤNG ĐÁNH GIÁ KHẢ NĂNG CHO VAY")

# Nhập dữ liệu
STV = st.number_input(
    "Nhập số tiền muốn vay (triệu đồng)",
    min_value=0.0
)

TGV = st.number_input(
    "Nhập thời gian vay (năm)",
    min_value=0.1
)

LSV = st.number_input(
    "Nhập lãi suất vay (dạng thập phân, ví dụ 0.12)",
    min_value=0.0,
    format="%.4f"
)

TN = st.number_input(
    "Nhập thu nhập hàng tháng (triệu đồng/tháng)",
    min_value=0.0
)

SNTGD = st.number_input(
    "Nhập số người trong gia đình",
    min_value=1.0,
    step=1.0
)

PTMC = st.number_input(
    "Nhập số tiền phải trả cho khoản vay cũ (triệu đồng/tháng)",
    min_value=0.0
)

GTTSDB = st.number_input(
    "Nhập giá trị tài sản đảm bảo (triệu đồng)",
    min_value=0.1
)

STKH = st.number_input(
    "Nhập tuổi khách hàng",
    min_value=0.0
)

# Nút tính toán
if st.button("ĐÁNH GIÁ KHOẢN VAY"):

    CPSH = 5

    try:
        PTMM = (STV / (TGV * 12)) + (STV * (LSV / 12))

        DTI = (PTMC + PTMM) / (TN - SNTGD * CPSH)

        LTV = STV / GTTSDB

        st.write(f"### Chỉ số DTI: {DTI*100:.2f}%")
        st.write(f"### Chỉ số LTV: {LTV*100:.2f}%")

        if DTI <= 0.7 and LTV <= 0.7 and 18 <= STKH <= 70:
            st.success("ĐƯỢC CHO VAY")
        else:
            st.error("KHÔNG ĐƯỢC CHO VAY")

    except ZeroDivisionError:
        st.error("Dữ liệu không hợp lệ. Vui lòng kiểm tra lại.")
