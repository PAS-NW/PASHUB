from datetime import datetime
from pathlib import Path

import streamlit as st
from PIL import Image

FUEL_APP_URL = "https://fuelinvcheck-ykxmchaxngfmx4tcz7afjp.streamlit.app/"
PLANT_APP_URL = "https://pas-plant-matching.streamlit.app/"
HIRE_REPORT_APP_URL = "https://hirereportbuilder.streamlit.app/"

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
        background: radial-gradient(circle at top left, #ffffff 0%, #f7f8fa 45%, #f1f3f6 100%);
        color: #07111f;
    }

    .block-container {
        max-width: 1550px;
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
        font-size: 25px !important;
        font-weight: 900 !important;
        margin-bottom: 1.2rem !important;
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
        font-size: 17px;
        line-height: 1.55;
        min-height: 110px;
        margin-bottom: 26px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,0.96);
        border: 1px solid #d9dee8;
        border-left: 6px solid #ffd400;
        border-radius: 18px;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.07);
    }

    .status-box div[data-testid="stVerticalBlockBorderWrapper"] {
        border-left: 1px solid #d9dee8;
    }

    /* Button styling */
    .stLinkButton {
        margin-top: 0 !important;
        margin-bottom: 0 !important;
    }

    .stLinkButton a {
        background: #ffd400 !important;
        color: #000000 !important;
        border: 0 !important;
        border-radius: 12px !important;
        min-height: 64px;
        height: 64px;
        font-size: 20px !important;
        font-weight: 900 !important;
        box-shadow: 0 13px 28px rgba(255, 212, 0, 0.25);
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    .stLinkButton a:hover {
        background: #ffdf2e !important;
        color: #000000 !important;
        border: 0 !important;
        transform: translateY(-1px);
    }

    /* Force the version box to sit exactly level with the launch button */
    .version-wrap {
        height: 64px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    .version-pill {
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #d7dde6;
        border-radius: 10px;
        background: white;
        color: #1f2937 !important;
        height: 64px;
        width: 100%;
        font-size: 16px;
        text-align: center;
        box-sizing: border-box;
        margin: 0 !important;
        padding: 0 !important;
    }

    .version-wrap p {
        margin: 0 !important;
        padding: 0 !important;
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
        object-fit: cover;
    }

    @media (max-width: 1050px) {
        .block-container {
            padding-left: 1.5rem;
            padding-right: 1.5rem;
        }

        h1 {
            font-size: 40px !important;
        }

        .muted {
            font-size: 18px;
        }
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
    st.markdown('<div class="status-box">', unsafe_allow_html=True)
    with st.container(border=True):
        st.markdown("### System Status")
        st.markdown('<div class="status-text">●&nbsp;&nbsp;All Systems Operational</div>', unsafe_allow_html=True)
        st.caption(f"Last updated: {datetime.now().strftime('%d %b %Y %H:%M')}")
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")
st.write("")

# App cards
fuel_card, plant_card, hire_card = st.columns(3, gap="large", vertical_alignment="top")

with fuel_card:
    with st.container(border=True):
        st.image(BASE / "fuel_image.jpeg", use_container_width=True)
        st.markdown("## Fuel Invoice Checker")
        st.markdown(
            '<div class="card-text">Check fuel invoices against vehicle records and assign drivers/jobs.</div>',
            unsafe_allow_html=True,
        )
        button_col, version_col = st.columns([2.4, 1], vertical_alignment="top")
        with button_col:
            st.link_button("Launch App  →", FUEL_APP_URL, use_container_width=True)
        with version_col:
            st.markdown('<div class="version-wrap"><div class="version-pill">v1.0.0</div></div>', unsafe_allow_html=True)

with plant_card:
    with st.container(border=True):
        st.image(BASE / "plant_image.png", use_container_width=True)
        st.markdown("## Plant Invoice Matcher")
        st.markdown(
            '<div class="card-text">Match plant hire invoices against PAS hire reports and detect discrepancies.</div>',
            unsafe_allow_html=True,
        )
        button_col, version_col = st.columns([2.4, 1], vertical_alignment="top")
        with button_col:
            st.link_button("Launch App  →", PLANT_APP_URL, use_container_width=True)
        with version_col:
            st.markdown('<div class="version-wrap"><div class="version-pill">v1.0.0</div></div>', unsafe_allow_html=True)


with hire_card:
    with st.container(border=True):
        st.image(BASE / "hire_report_image.png", use_container_width=True)
        st.markdown("## Hire Report Builder")
        st.markdown(
            '<div class="card-text">Build live hire reports quickly from plant and hire data.</div>',
            unsafe_allow_html=True,
        )
        button_col, version_col = st.columns([2.4, 1], vertical_alignment="top")
        with button_col:
            st.link_button("Launch App  →", HIRE_REPORT_APP_URL, use_container_width=True)
        with version_col:
            st.markdown('<div class="version-wrap"><div class="version-pill">v1.0.0</div></div>', unsafe_allow_html=True)

st.markdown('<div class="footer-line">© 2026 PAS Operations Hub &nbsp;&nbsp; | &nbsp;&nbsp; v1.0.0</div>', unsafe_allow_html=True)
