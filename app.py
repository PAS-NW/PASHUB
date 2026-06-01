
import streamlit as st
from datetime import datetime

FUEL_APP_URL = "https://fuelinvcheck-ykxmchaxngfmx4tcz7afjp.streamlit.app/"
PLANT_APP_URL = "https://pas-plant-matching.streamlit.app/"

st.set_page_config(
    page_title="PAS Operations Hub",
    page_icon="PAS_Logo.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .stApp {
        background: #f6f7f9;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 3rem;
        padding-bottom: 2rem;
    }

    header, footer, #MainMenu {
        visibility: hidden;
    }

    .hero {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 28px;
        margin-bottom: 42px;
    }

    .hero-left {
        display: flex;
        align-items: center;
        gap: 34px;
    }

    .logo {
        width: 170px;
        height: 170px;
        border-radius: 14px;
        box-shadow: 0 10px 28px rgba(0,0,0,0.12);
    }

    .title {
        font-size: 58px;
        font-weight: 900;
        letter-spacing: -2px;
        margin: 0;
        color: #050505;
    }

    .subtitle {
        font-size: 21px;
        color: #4b5563;
        margin-top: 12px;
        margin-bottom: 24px;
    }

    .yellow-line {
        width: 80px;
        height: 4px;
        background: #ffd400;
        border-radius: 100px;
    }

    .status-card {
        background: white;
        border: 1px solid #dfe3ea;
        border-radius: 14px;
        padding: 24px 28px;
        width: 270px;
        box-shadow: 0 10px 28px rgba(15,23,42,0.06);
    }

    .status-title {
        font-size: 17px;
        font-weight: 800;
        color: #111827;
        margin-bottom: 18px;
    }

    .status-ok {
        color: #138a2e;
        font-size: 16px;
        margin-bottom: 18px;
    }

    .status-date {
        color: #5b6472;
        font-size: 14px;
    }

    .cards {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 28px;
        margin-top: 10px;
    }

    .app-card {
        background: white;
        border: 1px solid #dfe3ea;
        border-radius: 15px;
        min-height: 310px;
        padding: 48px;
        box-shadow: 0 12px 28px rgba(15,23,42,0.07);
        display: grid;
        grid-template-columns: 140px 1fr;
        gap: 36px;
        align-items: center;
        position: relative;
        overflow: hidden;
    }

    .app-card.fuel {
        border-left: 6px solid #ffd400;
        background: linear-gradient(135deg, #fffaf0 0%, #ffffff 72%);
    }

    .app-card.plant {
        border-left: 6px solid #0b74de;
        background: linear-gradient(135deg, #f1f7ff 0%, #ffffff 72%);
    }

    .icon-box {
        width: 132px;
        height: 132px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 66px;
    }

    .fuel .icon-box {
        background: #fff1b8;
    }

    .plant .icon-box {
        background: #dbeafe;
    }

    .card-title {
        font-size: 29px;
        font-weight: 900;
        color: #050505;
        margin-bottom: 18px;
    }

    .card-text {
        font-size: 18px;
        line-height: 1.55;
        color: #374151;
        margin-bottom: 34px;
        max-width: 480px;
    }

    .button-row {
        display: flex;
        align-items: center;
        gap: 22px;
    }

    .launch-btn {
        display: inline-block;
        text-decoration: none !important;
        font-size: 18px;
        font-weight: 800;
        border-radius: 9px;
        padding: 15px 32px;
        min-width: 210px;
        text-align: center;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }

    .launch-btn:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 22px rgba(15,23,42,0.14);
    }

    .fuel-btn {
        background: #ffd400;
        color: #000 !important;
    }

    .plant-btn {
        background: #0b74de;
        color: white !important;
    }

    .version {
        border: 1px solid #d4d9e2;
        border-radius: 8px;
        padding: 7px 13px;
        color: #4b5563;
        background: #fff;
        font-size: 14px;
    }

    .footer {
        margin-top: 80px;
        padding-top: 30px;
        border-top: 1px solid #dfe3ea;
        text-align: center;
        color: #4b5563;
        font-size: 15px;
    }

    @media (max-width: 950px) {
        .hero, .hero-left {
            display: block;
        }

        .status-card {
            width: auto;
            margin-top: 30px;
        }

        .cards {
            grid-template-columns: 1fr;
        }

        .app-card {
            grid-template-columns: 1fr;
        }

        .title {
            font-size: 42px;
            margin-top: 25px;
        }
    }
</style>
""", unsafe_allow_html=True)

current_time = datetime.now().strftime("%d %b %Y %H:%M")

st.markdown(f"""
<div class="hero">
    <div class="hero-left">
        <img class="logo" src="app/static/PAS_Logo.png">
        <div>
            <h1 class="title">PAS Operations Hub</h1>
            <div class="subtitle">Central tools and insights for PAS operations.</div>
            <div class="yellow-line"></div>
        </div>
    </div>
    <div class="status-card">
        <div class="status-title">System Status</div>
        <div class="status-ok">●&nbsp;&nbsp;All Systems Operational</div>
        <div class="status-date">Last updated: {current_time}</div>
    </div>
</div>

<div class="cards">
    <div class="app-card fuel">
        <div class="icon-box">⛽</div>
        <div>
            <div class="card-title">Fuel Invoice Checker</div>
            <div class="card-text">Check fuel invoices against vehicle records and assign drivers/jobs.</div>
            <div class="button-row">
                <a class="launch-btn fuel-btn" href="{FUEL_APP_URL}" target="_blank">Launch App&nbsp;&nbsp;→</a>
                <span class="version">v1.0.0</span>
            </div>
        </div>
    </div>

    <div class="app-card plant">
        <div class="icon-box">🚜</div>
        <div>
            <div class="card-title">Plant Invoice Matcher</div>
            <div class="card-text">Match plant hire invoices against PAS hire reports and detect discrepancies.</div>
            <div class="button-row">
                <a class="launch-btn plant-btn" href="{PLANT_APP_URL}" target="_blank">Launch App&nbsp;&nbsp;→</a>
                <span class="version">v1.0.0</span>
            </div>
        </div>
    </div>
</div>

<div class="footer">
    © 2026 PAS Operations Hub &nbsp;&nbsp; | &nbsp;&nbsp; v1.0.0
</div>
""", unsafe_allow_html=True)
