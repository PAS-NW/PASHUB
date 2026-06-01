import streamlit as st

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(
    page_title="PAS App Hub",
    page_icon="🟡",
    layout="wide",
)

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
        .stApp {
            background: #f5f5f5;
        }

        .hub-header {
            background: #111111;
            padding: 34px 38px;
            border-radius: 18px;
            margin-bottom: 28px;
            border: 3px solid #ffd200;
        }

        .hub-title {
            color: #ffd200;
            font-size: 42px;
            font-weight: 800;
            margin-bottom: 6px;
            line-height: 1.1;
        }

        .hub-subtitle {
            color: #ffffff;
            font-size: 18px;
            margin: 0;
        }

        .app-card {
            background: #ffffff;
            border-radius: 18px;
            padding: 28px;
            border: 2px solid #e4e4e4;
            box-shadow: 0 4px 14px rgba(0,0,0,0.08);
            min-height: 260px;
        }

        .app-card h2 {
            color: #111111;
            font-size: 28px;
            margin-bottom: 8px;
        }

        .app-card p {
            color: #333333;
            font-size: 16px;
            min-height: 64px;
        }

        .launch-button a {
            display: inline-block;
            background: #ffd200;
            color: #111111 !important;
            padding: 14px 22px;
            border-radius: 12px;
            font-weight: 800;
            text-decoration: none;
            margin-top: 14px;
            border: 2px solid #111111;
        }

        .launch-button a:hover {
            background: #111111;
            color: #ffd200 !important;
            border-color: #ffd200;
        }

        .footer-note {
            margin-top: 28px;
            color: #666666;
            font-size: 14px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <div class="hub-header">
        <div class="hub-title">PAS App Hub</div>
        <p class="hub-subtitle">Select which invoice checking tool you want to open.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# App cards
# -----------------------------
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown(
        """
        <div class="app-card">
            <h2>Fuel Invoice Checker</h2>
            <p>Upload fuel invoice data and vehicle records to match cards, drivers and sites.</p>
            <div class="launch-button">
                <a href="https://fuelinvcheck-ykxmchaxngfmx4tcz7afjp.streamlit.app/" target="_blank">Open Fuel App</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="app-card">
            <h2>Plant Invoice Matcher</h2>
            <p>Check plant supplier invoices against the hire/order spreadsheet and flag queries.</p>
            <div class="launch-button">
                <a href="https://pas-plant-matching.streamlit.app/" target="_blank">Open Plant App</a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <p class="footer-note">Tip: deploy this as a separate Streamlit app, then save that link as your main PAS tools page.</p>
    """,
    unsafe_allow_html=True,
)
