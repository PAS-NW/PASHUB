import base64
from datetime import datetime
from pathlib import Path

import streamlit as st
from PIL import Image

FUEL_APP_URL = "https://fuelinvcheck-ykxmchaxngfmx4tcz7afjp.streamlit.app/"
PLANT_APP_URL = "https://pas-plant-matching.streamlit.app/"

logo_path = Path(__file__).parent / "PAS_Logo.png"
logo_img = Image.open(logo_path)
logo_b64 = base64.b64encode(logo_path.read_bytes()).decode()

st.set_page_config(
    page_title="PAS Operations Hub",
    page_icon=logo_img,
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .stApp {
        background: radial-gradient(circle at top left, #ffffff 0%, #f6f7f9 45%, #f2f4f7 100%);
        color: #07111f;
    }

    .block-container {
        max-width: 1480px;
        padding-top: 3.2rem;
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;
    }

    header, footer, #MainMenu {
        visibility: hidden;
    }

    .pas-hero {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 40px;
        margin-bottom: 66px;
    }

    .pas-hero-left {
        display: flex;
        align-items: center;
        gap: 50px;
    }

    .pas-logo {
        width: 190px;
        height: 190px;
        border-radius: 18px;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.13);
    }

    .pas-title {
        color: #07111f !important;
        font-size: 64px;
        line-height: 1.02;
        font-weight: 900;
        letter-spacing: -2.5px;
        margin: 0;
    }

    .pas-subtitle {
        color: #1f2937 !important;
        font-size: 25px;
        line-height: 1.4;
        margin-top: 24px;
        margin-bottom: 28px;
    }

    .pas-line {
        width: 90px;
        height: 5px;
        border-radius: 999px;
        background: #ffd400;
    }

    .status-card {
        width: 315px;
        background: rgba(255, 255, 255, 0.94);
        border: 1px solid #d9dee8;
        border-radius: 18px;
        padding: 34px 38px;
        box-shadow: 0 18px 40px rgba(15, 23, 42, 0.07);
    }

    .status-title {
        color: #07111f;
        font-size: 20px;
        font-weight: 900;
        margin-bottom: 25px;
    }

    .status-ok {
        color: #087a22;
        font-size: 18px;
        margin-bottom: 24px;
    }

    .status-date {
        color: #1f2937;
        font-size: 16px;
    }

    .app-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 36px;
    }

    .app-card {
        min-height: 360px;
        display: grid;
        grid-template-columns: 190px 1fr;
        gap: 46px;
        align-items: center;
        padding: 55px 48px;
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid #d9dee8;
        border-left: 7px solid #ffd400;
        border-radius: 19px;
        box-shadow: 0 20px 46px rgba(15, 23, 42, 0.08);
    }

    .fuel-card {
        background: linear-gradient(135deg, #fffaf0 0%, #ffffff 78%);
    }

    .plant-card {
        background: linear-gradient(135deg, #f8fbff 0%, #ffffff 78%);
    }

    .icon-box {
        width: 180px;
        height: 180px;
        border-radius: 19px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #fff0ad;
        font-size: 98px;
        box-shadow: inset 0 0 0 1px rgba(255, 212, 0, 0.18);
    }

    .card-title {
        color: #07111f;
        font-size: 34px;
        line-height: 1.15;
        font-weight: 900;
        margin-bottom: 28px;
        letter-spacing: -0.8px;
    }

    .card-text {
        color: #1f2937;
        font-size: 23px;
        line-height: 1.48;
        max-width: 540px;
        margin-bottom: 55px;
    }

    .button-row {
        display: flex;
        align-items: center;
        gap: 40px;
    }

    .launch-btn {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        min-width: 255px;
        height: 82px;
        border-radius: 14px;
        background: #ffd400;
        color: #000000 !important;
        font-size: 25px;
        font-weight: 900;
        text-decoration: none !important;
        box-shadow: 0 13px 28px rgba(255, 212, 0, 0.28);
        transition: 0.15s ease;
    }

    .launch-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 17px 34px rgba(255, 212, 0, 0.38);
    }

    .version {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        height: 56px;
        min-width: 86px;
        padding: 0 18px;
        border: 1px solid #d7dde6;
        border-radius: 12px;
        background: white;
        color: #1f2937;
        font-size: 20px;
    }

    .pas-footer {
        margin-top: 58px;
        border-top: 1px solid #d9dee8;
        padding-top: 34px;
        text-align: center;
        color: #1f2937;
        font-size: 19px;
    }

    @media (max-width: 1050px) {
        .pas-hero, .pas-hero-left {
            display: block;
        }

        .pas-title {
            font-size: 42px;
            margin-top: 28px;
        }

        .pas-subtitle {
            font-size: 20px;
        }

        .status-card {
            width: auto;
            margin-top: 30px;
        }

        .app-grid {
            grid-template-columns: 1fr;
        }

        .app-card {
            grid-template-columns: 1fr;
            padding: 36px;
        }

        .button-row {
            flex-wrap: wrap;
        }
    }
</style>
""", unsafe_allow_html=True)

current_time = datetime.now().strftime("%d %b %Y %H:%M")

st.markdown(f"""
<div class="pas-hero">
    <div class="pas-hero-left">
        <img class="pas-logo" src="data:image/png;base64,{logo_b64}">
        <div>
            <h1 class="pas-title">PAS Operations Hub</h1>
            <div class="pas-subtitle">Central tools and insights for PAS operations.</div>
            <div class="pas-line"></div>
        </div>
    </div>

    <div class="status-card">
        <div class="status-title">System Status</div>
        <div class="status-ok">●&nbsp;&nbsp;All Systems Operational</div>
        <div class="status-date">Last updated: {current_time}</div>
    </div>
</div>

<div class="app-grid">
    <div class="app-card fuel-card">
        <div class="icon-box">⛽</div>
        <div>
            <div class="card-title">Fuel Invoice Checker</div>
            <div class="card-text">Check fuel invoices against vehicle records and assign drivers/jobs.</div>
            <div class="button-row">
                <a class="launch-btn" href="{FUEL_APP_URL}" target="_blank" rel="noopener noreferrer">Launch App&nbsp;&nbsp;→</a>
                <span class="version">v1.0.0</span>
            </div>
        </div>
    </div>

    <div class="app-card plant-card">
        <div class="icon-box">🚧</div>
        <div>
            <div class="card-title">Plant Invoice Matcher</div>
            <div class="card-text">Match plant hire invoices against PAS hire reports and detect discrepancies.</div>
            <div class="button-row">
                <a class="launch-btn" href="{PLANT_APP_URL}" target="_blank" rel="noopener noreferrer">Launch App&nbsp;&nbsp;→</a>
                <span class="version">v1.0.0</span>
            </div>
        </div>
    </div>
</div>

<div class="pas-footer">
    © 2026 PAS Operations Hub &nbsp;&nbsp; | &nbsp;&nbsp; v1.0.0
</div>
""", unsafe_allow_html=True)
