import streamlit as st

st.set_page_config(
    page_title="PAS Operations Hub",
    page_icon="PAS_Logo.png",
    layout="wide"
)

st.markdown("""
<style>
.block-container {max-width: 1400px; padding-top: 2rem;}
[data-testid="stHorizontalBlock"] > div {
    border: 1px solid #ddd;
    border-radius: 15px;
    padding: 25px;
    background: #fafafa;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1,4])

with col1:
    st.image("PAS_Logo.png", width=180)

with col2:
    st.title("PAS Operations Hub")
    st.write("Central tools and insights for PAS operations")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("⛽ Fuel Invoice Checker")
    st.write("Check fuel invoices against vehicle records and assign drivers/jobs.")
    st.link_button(
        "Launch Fuel Invoice Checker",
        "https://fuelinvcheck-ykxmchaxngfmx4tcz7afjp.streamlit.app/",
        use_container_width=True
    )

with right:
    st.subheader("🚜 Plant Invoice Matcher")
    st.write("Match plant hire invoices against orders and identify discrepancies.")
    st.link_button(
        "Launch Plant Invoice Matcher",
        "https://pas-plant-matching.streamlit.app/",
        use_container_width=True
    )

st.divider()
st.success("All Systems Operational")
