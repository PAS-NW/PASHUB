from datetime import datetime
from pathlib import Path

import streamlit as st
from PIL import Image

FUEL_APP_URL = "https://fuelinvcheck-ykxmchaxngfmx4tcz7afjp.streamlit.app/"
PLANT_APP_URL = "https://pas-plant-matching.streamlit.app/"

BASE = Path(__file__).parent
logo = Image.open(BASE / "PAS_Logo.png")

st.set_page_config(
    page_title="PAS Operations Hub",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top left, #ffffff 0%, #f7f8fa 48%, #f1f3f6 100%);
        color: #07111f;
    }

    .block-container {
        max-width: 1480px;
        padding-top: 3rem;
        padding-left: 3rem;
        padding-right: 3rem;
        padding-bottom: 2rem;
    }

    header, footer, #MainMenu {
        visibility: hidden;
    }

    h1, h2, h3, p, div, span {
        color: #07111f;
    }

    h1 {
        font-size: 56px !important;
        font-weight: 900 !important;
        letter-spacing: -2px;
        margin-bottom: 0.6rem !important;
    }

    h2 {
        font-size: 29px !important;
        font-weight: 900 !important;
    }

    .yellow-rule {
        width: 90px;
        height: 5px;
        border-radius: 99px;
        background: #ffd400;
        margin-top: 18px;
    }

    .status-text {
        color: #087a22 !important;
        font-size: 17px;
        font-weight: 500;
    }

    .muted {
        color: #374151 !important;
        font-size: 21px;
    }

    .card-text {
        color: #1f2937 !important;
        font-size: 18px;
        line-height: 1.5;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,0.94);
        border: 1px solid #d9dee8;
        border-radius: 18px;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.07);
    }

    .stLinkButton a {
        background: #ffd400 !important;
        color: #000000 !important;
        border: 0 !important;
        border-radius: 12px !important;
        min-height: 64px;
        font-size: 20px !important;
        font-weight: 900 !important;
        box-shadow: 0 13px 28px rgba(255, 212, 0, 0.25);
    }

    .stLinkButton a:hover {
        background: #ffdf2e !important;
        color: #000000 !important;
        border: 0 !important;
        transform: translateY(-1px);
    }

    .version-pill {
        display: inline-block;
        border: 1px solid #d7dde6;
        border-radius: 10px;
        background: white;
        color: #1f2937 !important;
        padding: 12px 18px;
        font-size: 16px;
        margin-top: 11px;
        text-align: center;
    }

    .footer-line {
        margin-top: 52px;
        border-top: 1px solid #d9dee8;
        padding-top: 30px;
        text-align: center;
        color: #1f2937 !important;
        font-size: 17px;
    }

    [data-testid="stImage"] img {
        border-radius: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
hero_left, hero_right = st.columns([4, 1.45], vertical_alignment="center")

with hero_left:
    logo_col, text_col = st.columns([1, 4], vertical_alignment="center")
    with logo_col:
        st.image(BASE / "PAS_Logo.png", width=190)
    with text_col:
        st.title("PAS Operations Hub")
        st.markdown('<div class="muted">Central tools and insights for PAS operations.</div>', unsafe_allow_html=True)
        st.markdown('<div class="yellow-rule"></div>', unsafe_allow_html=True)

with hero_right:
    with st.container(border=True):
        st.markdown("### System Status")
        st.markdown('<div class="status-text">●&nbsp;&nbsp;All Systems Operational</div>', unsafe_allow_html=True)
        st.caption(f"Last updated: {datetime.now().strftime('%d %b %Y %H:%M')}")

st.write("")
st.write("")

# App cards
fuel_card, plant_card = st.columns(2, gap="large", vertical_alignment="top")

with fuel_card:
    with st.container(border=True):
        inner_icon, inner_text = st.columns([1.25, 2.7], vertical_alignment="center")
        with inner_icon:
            st.image(BASE / "fuel_icon.png", width=180)
        with inner_text:
            st.markdown("## Fuel Invoice Checker")
            st.markdown(
                '<div class="card-text">Check fuel invoices against vehicle records and assign drivers/jobs.</div>',
                unsafe_allow_html=True,
            )
            st.write("")
            button_col, version_col = st.columns([2.2, 1], vertical_alignment="center")
            with button_col:
                st.link_button("Launch App  →", FUEL_APP_URL, use_container_width=True)
            with version_col:
                st.markdown('<div class="version-pill">v1.0.0</div>', unsafe_allow_html=True)

with plant_card:
    with st.container(border=True):
        inner_icon, inner_text = st.columns([1.25, 2.7], vertical_alignment="center")
        with inner_icon:
            st.image(BASE / "excavator_icon.png", width=180)
        with inner_text:
            st.markdown("## Plant Invoice Matcher")
            st.markdown(
                '<div class="card-text">Match plant hire invoices against PAS hire reports and detect discrepancies.</div>',
                unsafe_allow_html=True,
            )
            st.write("")
            button_col, version_col = st.columns([2.2, 1], vertical_alignment="center")
            with button_col:
                st.link_button("Launch App  →", PLANT_APP_URL, use_container_width=True)
            with version_col:
                st.markdown('<div class="version-pill">v1.0.0</div>', unsafe_allow_html=True)

st.markdown('<div class="footer-line">© 2026 PAS Operations Hub &nbsp;&nbsp; | &nbsp;&nbsp; v1.0.0</div>', unsafe_allow_html=True)
