from datetime import datetime
from pathlib import Path
import base64

import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

FUEL_APP_URL = "https://fuelinvcheck-ykxmchaxngfmx4tcz7afjp.streamlit.app/"
PLANT_APP_URL = "https://pas-plant-matching.streamlit.app/"
HIRE_REPORT_APP_URL = "https://hirereportbuilder.streamlit.app/"
VENDOR_HIRE_APP_URL = "https://vendorhirechecker.streamlit.app/"

BASE = Path(__file__).parent

PAS_LOGO = BASE / "PAS_Logo.png"
FUEL_IMAGE = BASE / "fuel_image.jpeg"
PLANT_IMAGE = BASE / "plant_image.png"
HIRE_IMAGE = BASE / "hire_report_image.png"
VENDOR_IMAGE = BASE / "vendor_hire_image.webp"

logo = Image.open(PAS_LOGO)

st.set_page_config(
    page_title="PAS Operations Hub",
    page_icon=logo,
    layout="wide",
    initial_sidebar_state="collapsed",
)

def img_b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("utf-8")

logo_b64 = img_b64(PAS_LOGO)
fuel_b64 = img_b64(FUEL_IMAGE)
plant_b64 = img_b64(PLANT_IMAGE)
hire_b64 = img_b64(HIRE_IMAGE)
vendor_b64 = img_b64(VENDOR_IMAGE)

updated = datetime.now().strftime("%d %b %Y %H:%M")

st.markdown(
    """
    <style>
    .stApp {
        background: #f4f6f8;
    }

    .block-container {
        max-width: 1500px;
        padding: 0 !important;
    }

    header, footer, #MainMenu {
        visibility: hidden;
    }

    iframe {
        width: 100%;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
* {{
    box-sizing: border-box;
}}

body {{
    margin: 0;
    padding: 42px 48px 24px 48px;
    font-family: Arial, Helvetica, sans-serif;
    background: radial-gradient(circle at top left, #ffffff 0%, #f7f8fa 45%, #f1f3f6 100%);
    color: #07111f;
}}

.pas-header {{
    display: grid;
    grid-template-columns: 1fr 310px;
    gap: 48px;
    align-items: center;
    margin-bottom: 48px;
}}

.pas-title-area {{
    display: flex;
    align-items: center;
    gap: 28px;
}}

.pas-logo {{
    width: 150px;
    height: 150px;
    border-radius: 14px;
    box-shadow: 0 16px 36px rgba(15, 23, 42, 0.13);
    flex-shrink: 0;
}}

.pas-title {{
    margin: 0;
    color: #07111f;
    font-size: 48px;
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -1.8px;
}}

.pas-subtitle {{
    margin-top: 18px;
    color: #374151;
    font-size: 19px;
    line-height: 1.4;
}}

.yellow-line {{
    width: 82px;
    height: 5px;
    background: #ffd400;
    border-radius: 99px;
    margin-top: 18px;
}}

.status-card {{
    background: rgba(255,255,255,0.96);
    border: 1px solid #d9dee8;
    border-radius: 16px;
    padding: 26px 30px;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.07);
}}

.status-title {{
    color: #07111f;
    font-size: 20px;
    font-weight: 900;
    margin-bottom: 18px;
}}

.status-ok {{
    color: #087a22;
    font-size: 16px;
    margin-bottom: 14px;
}}

.status-date {{
    color: #6b7280;
    font-size: 13px;
}}

.app-grid {{
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 24px;
    align-items: stretch;
}}

.app-card {{
    background: rgba(255,255,255,0.96);
    border: 1px solid #d9dee8;
    border-left: 6px solid #ffd400;
    border-radius: 18px;
    box-shadow: 0 18px 40px rgba(15, 23, 42, 0.07);
    padding: 26px;
    min-height: 540px;
    display: flex;
    flex-direction: column;
}}

.card-img {{
    width: 100%;
    height: 220px;
    border-radius: 16px;
    overflow: hidden;
    background: #e5e7eb;
    margin-bottom: 26px;
}}

.card-img img {{
    width: 100%;
    height: 220px;
    object-fit: cover;
    display: block;
}}

.card-title {{
    color: #07111f;
    font-size: 22px;
    line-height: 1.15;
    font-weight: 900;
    margin: 0 0 24px 0;
}}

.card-text {{
    color: #1f2937;
    font-size: 16px;
    line-height: 1.55;
    min-height: 76px;
    margin-bottom: 34px;
}}

.card-actions {{
    display: grid;
    grid-template-columns: 1fr 78px;
    gap: 14px;
    align-items: center;
    margin-top: auto;
}}

.launch-btn {{
    height: 58px;
    border-radius: 11px;
    background: #ffd400;
    color: #000000 !important;
    display: flex;
    align-items: center;
    justify-content: center;
    text-decoration: none !important;
    font-size: 16px;
    font-weight: 900;
    box-shadow: 0 13px 28px rgba(255, 212, 0, 0.25);
}}

.launch-btn:hover {{
    background: #ffdf2e;
    transform: translateY(-1px);
}}

.version-pill {{
    height: 58px;
    border: 1px solid #d7dde6;
    border-radius: 10px;
    background: #ffffff;
    color: #1f2937;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
}}

.pas-footer {{
    margin-top: 54px;
    border-top: 1px solid #d9dee8;
    padding-top: 28px;
    text-align: center;
    color: #1f2937;
    font-size: 16px;
}}

@media (max-width: 1100px) {{
    body {{
        padding: 28px 24px;
    }}

    .pas-header {{
        grid-template-columns: 1fr;
        margin-bottom: 36px;
    }}

    .app-grid {{
        grid-template-columns: 1fr;
    }}

    .pas-title {{
        font-size: 38px;
    }}

    .pas-logo {{
        width: 120px;
        height: 120px;
    }}
}}
</style>
</head>

<body>
    <div class="pas-header">
        <div class="pas-title-area">
            <img class="pas-logo" src="data:image/png;base64,{logo_b64}">
            <div>
                <h1 class="pas-title">PAS Operations Hub</h1>
                <div class="pas-subtitle">Central tools and insights for PAS operations.</div>
                <div class="yellow-line"></div>
            </div>
        </div>

        <div class="status-card">
            <div class="status-title">System Status</div>
            <div class="status-ok">●&nbsp;&nbsp;All Systems Operational</div>
            <div class="status-date">Last updated: {updated}</div>
        </div>
    </div>

    <div class="app-grid">
        <div class="app-card">
            <div class="card-img"><img src="data:image/jpeg;base64,{fuel_b64}"></div>
            <div class="card-title">Fuel Invoice Checker</div>
            <div class="card-text">Check fuel invoices against vehicle records and assign drivers/jobs.</div>
            <div class="card-actions">
                <a class="launch-btn" href="{FUEL_APP_URL}" target="_blank" rel="noopener noreferrer">Launch App&nbsp;&nbsp;→</a>
                <div class="version-pill">v1.0.0</div>
            </div>
        </div>

        <div class="app-card">
            <div class="card-img"><img src="data:image/png;base64,{plant_b64}"></div>
            <div class="card-title">Plant Invoice Matcher</div>
            <div class="card-text">Match plant hire invoices against PAS hire reports and detect discrepancies.</div>
            <div class="card-actions">
                <a class="launch-btn" href="{PLANT_APP_URL}" target="_blank" rel="noopener noreferrer">Launch App&nbsp;&nbsp;→</a>
                <div class="version-pill">v1.0.0</div>
            </div>
        </div>

        <div class="app-card">
            <div class="card-img"><img src="data:image/png;base64,{hire_b64}"></div>
            <div class="card-title">Hire Report Builder</div>
            <div class="card-text">Build live hire reports quickly from plant and hire data.</div>
            <div class="card-actions">
                <a class="launch-btn" href="{HIRE_REPORT_APP_URL}" target="_blank" rel="noopener noreferrer">Launch App&nbsp;&nbsp;→</a>
                <div class="version-pill">v1.0.0</div>
            </div>
        </div>

        <div class="app-card">
            <div class="card-img"><img src="data:image/webp;base64,{vendor_b64}"></div>
            <div class="card-title">Vendor Hire Checker</div>
            <div class="card-text">Check vendor hire reports agree with PAS records and highlight differences.</div>
            <div class="card-actions">
                <a class="launch-btn" href="{VENDOR_HIRE_APP_URL}" target="_blank" rel="noopener noreferrer">Launch App&nbsp;&nbsp;→</a>
                <div class="version-pill">v1.0.0</div>
            </div>
        </div>
    </div>

    <div class="pas-footer">© 2026 PAS Operations Hub &nbsp;&nbsp; | &nbsp;&nbsp; v1.0.0</div>
</body>
</html>
"""

components.html(html, height=820, scrolling=False)
