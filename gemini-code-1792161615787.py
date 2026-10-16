import streamlit as st
import streamlit.components.v1 as components
import html
import random

# -------------------------------------------------
# PAGE CONFIGURATION
# -------------------------------------------------
st.set_page_config(
    page_title="Hello World Motion Lab",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Hello World Motion Lab")
st.caption("An interactive app demonstrating dynamic fonts, backgrounds, and continuous motion particle effects.")

# -------------------------------------------------
# USER CONTROLS (SIDEBAR)
# -------------------------------------------------
st.sidebar.header("⚙️ App Controls")

name = st.sidebar.text_input("Enter your name", "Hello World")

font_family = st.sidebar.selectbox(
    "Font type",
    [
        "Arial", 
        "Courier New", 
        "Georgia", 
        "Times New Roman", 
        "Verdana", 
        "Trebuchet MS", 
        "Impact", 
        "Comic Sans MS"
    ]
)

font_size = st.sidebar.slider("Font size (px)", 20, 120, 48)

background = st.sidebar.selectbox(
    "Background",
    ["Light", "Dark", "Ocean Gradient", "Cyberpunk", "Sunset"]
)

name_mode = st.sidebar.selectbox(
    "Name display mode",
    ["Centered", "Ticker Tape", "Repeated"]
)

effect = st.sidebar.selectbox(
    "Dynamic action",
    ["None", "Rain", "Snow", "Hail", "Wind", "Confetti", "Tornado"]
)

speed = st.sidebar.slider("Animation speed", 0.5, 3.0, 1.0, step=0.1)

# -------------------------------------------------
# THEME & BACKGROUND MAPPING
# -------------------------------------------------
bg_presets = {
    "Light": {
        "bg": "#ffffff",
        "text": "#1e293b",
        "border": "#e2e8f0"
    },
    "Dark": {
        "bg": "#0f172a",
        "text": "#f8fafc",
        "border": "#334155"
    },
    "Ocean Gradient": {
        "bg": "linear-gradient(135deg, #0f172a, #1e3a8a, #0284c7)",
        "text": "#ffffff",
        "border": "#38bdf8"
    },
    "Cyberpunk": {
        "bg": "linear-gradient(135deg, #18012e, #4c0519)",
        "text": "#00ffcc",
        "border": "#ff007f"
    },
    "Sunset": {
        "bg": "linear-gradient(135deg, #4c1d95, #c026d3, #ea580c)",
        "text": "#ffffff",
        "border": "#fbbf24"
    }
}

current_theme = bg_presets.get(background, bg_presets["Dark"])
bg_style = current_theme["bg"]
text_color = current_theme["text"]
border_color = current_theme["border"]

# Escape special characters in name string safely
safe_name = html.escape(name if name.strip() != "" else "Hello World")

# -------------------------------------------------
# DYNAMIC ACTION PARTICLES (CSS CONTINUOUS LOOPS)
# -------------------------------------------------
effect_symbols = {
    "Rain": ["💧", "🌧️", "💧"],
    "Snow": ["❄️", "🌨️", "✨"],
    "Hail": ["🧊", "⚪", "🧊"],
    "Wind": ["💨", "🍃", "🌬️"],
    "Confetti": ["🎉", "🎊", "✨", "🎈", "⭐"],
    "Tornado": ["🌪️", "🌀", "🌪️"],
    "None": []
}

symbols = effect_symbols.get(effect, [])
particles_html = []
base_duration = max(0.4, 4.0 / speed)

if effect != "None" and symbols:
    random.seed(42)  # Consistent particle layout
    for _ in range(40):
        sym = random.choice(symbols)
        left = random.uniform(2, 98)
        delay = random.uniform(0, base_duration)
        dur = base_duration * random.uniform(0.7, 1.3)
        size = random.randint(18, 36)
        
        if effect in ["Rain", "Snow", "Hail", "Confetti"]:
            p_style = f"left: {left:.1f}%; font-size: {size}px; animation: fall-{effect.lower()} {dur:.2f}s linear infinite; animation-delay: -{delay:.2f}s;"
        elif effect == "Wind":
            top = random.uniform(5, 95)
            p_style = f"top: {top:.1f}%; font-size: {size}px; animation: blow-wind {dur:.2f}s linear infinite; animation-delay: -{delay:.2f}s;"
        elif effect == "Tornado":
            top = random.uniform(20, 80)
            p_style = f"left: {left:.1f}%; top: {top:.1f}%; font-size: {size * 1.2:.0f}px; animation: swirl-tornado {dur * 0.8:.2f}s ease-in-out infinite; animation-delay: -{delay:.2f}s;"
        else:
            p_style = ""
            
        particles_html.append(f'<div class="particle" style="{p_style}">{sym}</div>')

particles_str = "\n".join(particles_html)

# -------------------------------------------------
# NAME DISPLAY MODE FORMATTING
# -------------------------------------------------
duration_sec = max(2.0, 15.0 / speed)

if name_mode == "Ticker Tape":
    ticker_text = f"{safe_name} &nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp; " * 6
    name_html = f"""
    <div class="ticker-wrapper">
        <div class="ticker-content" style="font-family: '{font_family}', sans-serif; font-size: {font_size}px; color: {text_color}; animation-duration: {duration_sec:.1f}s;">
            {ticker_text}
        </div>
    </div>
    """
elif name_mode == "Repeated":
    row_text = " &nbsp;&nbsp;•&nbsp;&nbsp; ".join([safe_name] * 6)
    repeated_rows = "<br>".join([f"<div>{row_text}</div>"] * 6)
    name_html = f"""
    <div class="repeated-wrapper" style="font-family: '{font_family}', sans-serif; font-size: {font_size * 0.6:.0f}px; color: {text_color};">
        {repeated_rows}
    </div>
    """
else:  # Centered
    name_html = f"""
    <div class="centered-wrapper" style="font-family: '{font_family}', sans-serif; font-size: {font_size}px; color: {text_color};">
        {safe_name}
    </div>
    """

# -------------------------------------------------
# COMPLETE HTML & CSS EMBED
# -------------------------------------------------
full_html = f"""
<!DOCTYPE html>
<html>
<head>
<style>
    * {{
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }}
    body {{
        background: {bg_style};
        color: {text_color};
        height: 520px;
        width: 100%;
        overflow: hidden;
        border-radius: 12px;
        border: 2px solid {border_color};
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: '{font_family}', sans-serif;
    }}
    .particles-layer {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: 1;
        pointer-events: none;
    }}
    .particle {{
        position: absolute;
        user-select: none;
    }}
    .content-layer {{
        position: relative;
        z-index: 10;
        width: 100%;
        text-align: center;
        padding: 20px;
        word-break: break-word;
    }}
    .centered-wrapper {{
        font-weight: bold;
        text-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }}
    .repeated-wrapper {{
        line-height: 1.6;
        opacity: 0.9;
        font-weight: 600;
    }}
    .ticker-wrapper {{
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
    }}
    .ticker-content {{
        display: inline-block;
        white-space: nowrap;
        font-weight: bold;
        animation: ticker-slide linear infinite;
    }}
    @keyframes ticker-slide {{
        0% {{ transform: translateX(0%); }}
        100% {{ transform: translateX(-50%); }}
    }}
    @keyframes fall-rain {{
        0% {{ transform: translateY(-50px); opacity: 1; }}
        100% {{ transform: translateY(550px); opacity: 0.2; }}
    }}
    @keyframes fall-snow {{
        0% {{ transform: translateY(-50px) translateX(0px) rotate(0deg); opacity: 0.9; }}
        50% {{ transform: translateY(260px) translateX(30px) rotate(180deg); }}
        100% {{ transform: translateY(550px) translateX(-30px) rotate(360deg); opacity: 0.2; }}
    }}
    @keyframes fall-hail {{
        0% {{ transform: translateY(-50px) scale(0.8); opacity: 1; }}
        85% {{ transform: translateY(510px) scale(1.1); opacity: 1; }}
        100% {{ transform: translateY(550px) scale(0.4); opacity: 0; }}
    }}
    @keyframes blow-wind {{
        0% {{ transform: translateX(-80px); opacity: 0; }}
        15% {{ opacity: 0.9; }}
        85% {{ opacity: 0.9; }}
        100% {{ transform: translateX(1100px); opacity: 0; }}
    }}
    @keyframes fall-confetti {{
        0% {{ transform: translateY(-50px) rotate(0deg) scale(0.8); opacity: 1; }}
        50% {{ transform: translateY(260px) rotate(180deg) scale(1.2); }}
        100% {{ transform: translateY(550px) rotate(360deg) scale(0.8); opacity: 0.3; }}
    }}
    @keyframes swirl-tornado {{
        0% {{ transform: rotate(0deg) translateX(0px) translateY(0px) scale(0.8); }}
        25% {{ transform: rotate(90deg) translateX(70px) translateY(-35px) scale(1.2); }}
        50% {{ transform: rotate(180deg) translateX(0px) translateY(45px) scale(1.4); }}
        75% {{ transform: rotate(270deg) translateX(-70px) translateY(-25px) scale(1.0); }}
        100% {{ transform: rotate(360deg) translateX(0px) translateY(0px) scale(0.8); }}
    }}
</style>
</head>
<body>
    <div class="particles-layer">
        {particles_str}
    </div>
    <div class="content-layer">
        {name_html}
    </div>
</body>
</html>
"""

components.html(full_html, height=540)