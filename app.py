import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------
# PAGE SETUP
# ---------------------------------------------------------

st.set_page_config(
    page_title="EcoMorph",
    page_icon="🌿",
    layout="wide"
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🌿 EcoMorph")

st.write("### Change the city. Watch nature respond.")

st.write("**Your choices shape the city — and nature answers back.**")

st.write(
    "EcoMorph is an interactive city environment simulator where every decision "
    "creates a visible ripple in the world around you."
)

st.write(
    "Add trees. Increase pollution. Choose cleaner transport. Invest in solar energy."
)

st.write("**Then watch your city react — live.** 🌱🏙️")

st.write("### *Small decisions. Visible consequences. A living city.*")

st.write(
    "*EcoMorph turns environmental choices into a live animated visual showcase, "
    "helping you see how the way we build and manage a city can change the health "
    "of its environment.*"
)

# ---------------------------------------------------------
# CITY CONTROLS
# ---------------------------------------------------------

st.subheader("🏗️ Build Your City")

col1, col2, col3 = st.columns(3)

with col1:

    trees = st.slider(
        "🌳 Trees",
        0,
        100,
        60
    )

    cars = st.slider(
        "🚗 Cars",
        0,
        100,
        40
    )

with col2:

    factories = st.slider(
        "🏭 Factories",
        0,
        100,
        30
    )

    recycling = st.slider(
        "♻️ Recycling",
        0,
        100,
        70
    )

with col3:

    solar = st.slider(
        "☀️ Solar Energy",
        0,
        100,
        60
    )

    transport = st.slider(
        "🚌 Public Transport",
        0,
        100,
        70
    )

# ---------------------------------------------------------
# POLLUTION CALCULATION
# ---------------------------------------------------------

pollution = (
    cars * 0.30
    + factories * 0.25
    + (100 - recycling) * 0.15
    + (100 - transport) * 0.10
    - trees * 0.12
    - solar * 0.08
)

if pollution < 0:
    pollution = 0

if pollution > 100:
    pollution = 100

pollution = round(pollution)

eco_score = 100 - pollution

# ---------------------------------------------------------
# CITY CONDITION
# ---------------------------------------------------------

if pollution < 30:

    city_class = "good"

    city_title = "🌿 ECO UTOPIA"

    city_message = (
        "Your city is thriving! Nature and development "
        "are living in harmony."
    )

    popup_message = "🌿 YAY! Your city is pollution-free!"

elif pollution < 60:

    city_class = "medium"

    city_title = "🌱 BALANCED ECOSYSTEM"

    city_message = (
        "Your city is doing okay, but there is still "
        "room to make it greener!"
    )

    popup_message = (
        "🌱 Your city is doing okay — "
        "but it can become greener!"
    )

else:

    city_class = "bad"

    city_title = "⚠️ CRITICAL POLLUTION"

    city_message = (
        "Pollution levels are high. The environment "
        "needs urgent attention!"
    )

    popup_message = (
        "🌧️ OH NO! Pollution is damaging your city!"
    )

# ---------------------------------------------------------
# CITY INFORMATION
# ---------------------------------------------------------

st.subheader(city_title)

st.write(city_message)

# ---------------------------------------------------------
# STATISTICS
# ---------------------------------------------------------

stat1, stat2, stat3 = st.columns(3)

with stat1:
    st.metric(
        "🌫️ Pollution Level",
        str(pollution) + "%"
    )

with stat2:
    st.metric(
        "🌳 Trees",
        trees
    )

with stat3:
    st.metric(
        "🌍 Eco Score",
        str(eco_score) + "/100"
    )

# ---------------------------------------------------------
# CITY HTML
# ---------------------------------------------------------

city_html = f"""
<!DOCTYPE html>

<html>

<head>

<style>

* {{
    box-sizing: border-box;
}}

html, body {{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
}}

body {{
    font-family: Arial, sans-serif;
}}

.city {{
    position: relative;
    width: 100%;
    height: 500px;
    overflow: hidden;
    border-radius: 25px;
    background: linear-gradient(
        to bottom,
        #81D4FA 0%,
        #B3E5FC 55%,
        #E1F5FE 100%
    );
}}

.city.good {{
    background: linear-gradient(
        to bottom,
        #4FC3F7,
        #B3E5FC 55%,
        #E8F5E9
    );
}}

.city.medium {{
    background: linear-gradient(
        to bottom,
        #90CAF9,
        #CFD8DC 55%,
        #E8F5E9
    );
}}

.city.bad {{
    background: linear-gradient(
        to bottom,
        #78909C,
        #B0BEC5 55%,
        #CFD8DC
    );
}}

/* SUN */

.sun {{
    position: absolute;
    width: 85px;
    height: 85px;
    border-radius: 50%;
    background: #FFD54F;
    top: 40px;
    right: 90px;
    box-shadow:
        0 0 25px #FFD54F,
        0 0 55px #FFEE58;
    animation: sunGlow 3s infinite alternate;
}}

@keyframes sunGlow {{
    from {{
        transform: scale(1);
    }}

    to {{
        transform: scale(1.08);
    }}
}}

.bad .sun {{
    opacity: 0.35;
    filter: grayscale(60%);
}}

/* CLOUDS */

.cloud {{
    position: absolute;
    width: 110px;
    height: 35px;
    background: white;
    border-radius: 40px;
    opacity: 0.8;
    animation: cloudMove 25s linear infinite;
}}

.cloud:before {{
    content: "";
    position: absolute;
    width: 45px;
    height: 45px;
    background: white;
    border-radius: 50%;
    left: 20px;
    top: -22px;
}}

.cloud:after {{
    content: "";
    position: absolute;
    width: 55px;
    height: 55px;
    background: white;
    border-radius: 50%;
    right: 15px;
    top: -28px;
}}

.cloud1 {{
    top: 70px;
    left: 40px;
}}

.cloud2 {{
    top: 135px;
    left: 420px;
    animation-delay: -10s;
}}

@keyframes cloudMove {{
    from {{
        transform: translateX(-40px);
    }}

    to {{
        transform: translateX(100px);
    }}
}}

.bad .cloud {{
    background: #607D8B;
    opacity: 0.7;
}}

.bad .cloud:before,
.bad .cloud:after {{
    background: #607D8B;
}}

/* MOUNTAINS */

.mountain {{
    position: absolute;
    bottom: 180px;
    width: 0;
    height: 0;
    border-left: 150px solid transparent;
    border-right: 150px solid transparent;
    border-bottom: 180px solid #66BB6A;
}}

.m1 {{
    left: 20px;
}}

.m2 {{
    left: 220px;
    border-bottom-color: #43A047;
}}

.m3 {{
    right: 20px;
    border-bottom-color: #388E3C;
}}

.medium .mountain {{
    filter: saturate(70%);
}}

.bad .mountain {{
    border-bottom-color: #78909C;
    filter: grayscale(70%);
}}

/* GROUND */

.ground {{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 185px;
    background: #43A047;
    z-index: 4;
}}

.medium .ground {{
    background: #7CB342;
}}

.bad .ground {{
    background: #827717;
}}

/* RIVER */

.river {{
    position: absolute;
    left: 0;
    bottom: 65px;
    width: 60%;
    height: 120px;
    background: #29B6F6;
    clip-path: polygon(
        0 20%,
        20% 10%,
        40% 35%,
        60% 15%,
        80% 30%,
        100% 5%,
        100% 100%,
        0 100%
    );
    z-index: 5;
    overflow: hidden;
}}

.medium .river {{
    background: #4DB6AC;
}}

.bad .river {{
    background: #795548;
}}

/* WATER FLOW */

.wave {{
    position: absolute;
    width: 160%;
    height: 20px;
    border-top: 4px solid rgba(255,255,255,0.6);
    border-radius: 50%;
    left: -60%;
    animation: waterFlow 4s linear infinite;
}}

.wave1 {{
    top: 25px;
}}

.wave2 {{
    top: 55px;
    animation-delay: -1.3s;
}}

.wave3 {{
    top: 85px;
    animation-delay: -2.6s;
}}

@keyframes waterFlow {{
    from {{
        transform: translateX(0);
    }}

    to {{
        transform: translateX(35%);
    }}
}}

.bad .wave {{
    border-color: rgba(210,190,170,0.45);
}}

/* BUILDINGS */

.building {{
    position: absolute;
    bottom: 150px;
    width: 75px;
    background: #607D8B;
    z-index: 7;
    border-radius: 5px 5px 0 0;
}}

.b1 {{
    left: 56%;
    height: 145px;
}}

.b2 {{
    left: 67%;
    height: 190px;
}}

.b3 {{
    left: 79%;
    height: 125px;
}}

.window {{
    position: absolute;
    width: 12px;
    height: 17px;
    background: #FFF176;
    box-shadow:
        25px 0 #FFF176,
        0 30px #FFF176,
        25px 30px #FFF176,
        0 60px #FFF176,
        25px 60px #FFF176;
    left: 15px;
    top: 20px;
}}

.bad .building {{
    background: #546E7A;
}}

.bad .window {{
    background: #B0BEC5;
    box-shadow:
        25px 0 #B0BEC5,
        0 30px #B0BEC5,
        25px 30px #B0BEC5,
        0 60px #B0BEC5,
        25px 60px #B0BEC5;
}}

/* TREES */

.tree {{
    position: absolute;
    font-size: 65px;
    z-index: 11;
    animation: treeSway 3s ease-in-out infinite alternate;
}}

.t1 {{
    bottom: 120px;
    left: 5%;
}}

.t2 {{
    bottom: 130px;
    left: 18%;
    animation-delay: -1s;
}}

.t3 {{
    bottom: 115px;
    left: 38%;
    animation-delay: -2s;
}}

.t4 {{
    bottom: 125px;
    left: 72%;
    animation-delay: -1.5s;
}}

.t5 {{
    bottom: 115px;
    right: 3%;
    animation-delay: -0.5s;
}}

@keyframes treeSway {{
    from {{
        transform: rotate(-2deg);
    }}

    to {{
        transform: rotate(2deg);
    }}
}}

.bad .tree {{
    filter: grayscale(80%);
    opacity: 0.65;
}}

/* FLOWERS */

.flower {{
    position: absolute;
    font-size: 25px;
    z-index: 12;
    animation: flowerFloat 2s ease-in-out infinite alternate;
}}

.f1 {{
    left: 12%;
    bottom: 85px;
}}

.f2 {{
    left: 32%;
    bottom: 70px;
    animation-delay: -1s;
}}

.f3 {{
    right: 25%;
    bottom: 80px;
    animation-delay: -0.5s;
}}

@keyframes flowerFloat {{
    from {{
        transform: translateY(0);
    }}

    to {{
        transform: translateY(-6px);
    }}
}}

.bad .flower {{
    filter: grayscale(100%);
    opacity: 0.35;
}}

/* BUTTERFLIES */

.butterfly {{
    position: absolute;
    font-size: 28px;
    z-index: 14;
    animation: butterflyMove 7s linear infinite;
}}

.bf1 {{
    left: 25%;
    top: 230px;
}}

.bf2 {{
    left: 45%;
    top: 280px;
    animation-delay: -3s;
}}

@keyframes butterflyMove {{
    0% {{
        transform: translate(0,0);
    }}

    25% {{
        transform: translate(40px,-30px);
    }}

    50% {{
        transform: translate(80px,10px);
    }}

    75% {{
        transform: translate(30px,35px);
    }}

    100% {{
        transform: translate(0,0);
    }}
}}

.medium .butterfly,
.bad .butterfly {{
    display: none;
}}

/* ROAD */

.road {{
    position: absolute;
    bottom: 0;
    width: 100%;
    height: 65px;
    background: #37474F;
    z-index: 22;
}}

.roadLine {{
    position: absolute;
    top: 30px;
    left: 0;
    width: 100%;
    height: 5px;
    background: repeating-linear-gradient(
        to right,
        #FFD54F 0px,
        #FFD54F 55px,
        transparent 55px,
        transparent 100px
    );
}}

/* WIND */

.wind {{
    position: absolute;
    width: 100%;
    height: 100%;
    pointer-events: none;
    z-index: 18;
    opacity: 0;
}}

.bad .wind {{
    opacity: 1;
}}

.windLine {{
    position: absolute;
    width: 120px;
    height: 3px;
    background: rgba(255,255,255,0.7);
    border-radius: 10px;
    animation: windMove 2s linear infinite;
}}

.w1 {{
    top: 210px;
    left: -150px;
}}

.w2 {{
    top: 260px;
    left: -250px;
    animation-delay: -0.7s;
}}

.w3 {{
    top: 310px;
    left: -180px;
    animation-delay: -1.2s;
}}

.w4 {{
    top: 170px;
    left: -300px;
    animation-delay: -1.7s;
}}

@keyframes windMove {{
    from {{
        transform: translateX(0);
    }}

    to {{
        transform: translateX(900px);
    }}
}}

/* RAIN */

.rain {{
    position: absolute;
    width: 100%;
    height: 100%;
    z-index: 20;
    pointer-events: none;
    opacity: 0;
}}

.bad .rain {{
    opacity: 1;
}}

.rainDrop {{
    position: absolute;
    top: -30px;
    width: 2px;
    height: 25px;
    background: rgba(220,235,245,0.75);
    animation: rainFall 0.8s linear infinite;
}}

.r1 {{ left: 5%; animation-delay: -0.1s; }}
.r2 {{ left: 12%; animation-delay: -0.5s; }}
.r3 {{ left: 20%; animation-delay: -0.2s; }}
.r4 {{ left: 28%; animation-delay: -0.7s; }}
.r5 {{ left: 36%; animation-delay: -0.3s; }}
.r6 {{ left: 44%; animation-delay: -0.6s; }}
.r7 {{ left: 52%; animation-delay: -0.1s; }}
.r8 {{ left: 60%; animation-delay: -0.4s; }}
.r9 {{ left: 68%; animation-delay: -0.8s; }}
.r10 {{ left: 76%; animation-delay: -0.2s; }}
.r11 {{ left: 84%; animation-delay: -0.5s; }}
.r12 {{ left: 92%; animation-delay: -0.3s; }}

@keyframes rainFall {{
    from {{
        transform: translateY(0);
    }}

    to {{
        transform: translateY(560px);
    }}
}}

/* POLLUTION HAZE */

.haze {{
    position: absolute;
    inset: 0;
    background: rgba(80,80,80,0.15);
    z-index: 16;
    opacity: 0;
    pointer-events: none;
}}

.bad .haze {{
    opacity: 1;
}}

/* POPUP */

.popup {{
    position: absolute;
    top: 25px;
    left: 50%;
    transform: translateX(-50%) translateY(-120px);
    padding: 14px 25px;
    background: rgba(255,255,255,0.96);
    border-radius: 30px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    font-size: 18px;
    font-weight: bold;
    color: #2E7D32;
    z-index: 50;
    white-space: nowrap;
    animation: popupAnimation 4s ease forwards;
}}

.bad .popup {{
    color: #C62828;
}}

.medium .popup {{
    color: #F57F17;
}}

@keyframes popupAnimation {{
    0% {{
        transform: translateX(-50%) translateY(-120px);
        opacity: 0;
    }}

    15% {{
        transform: translateX(-50%) translateY(0);
        opacity: 1;
    }}

    75% {{
        transform: translateX(-50%) translateY(0);
        opacity: 1;
    }}

    100% {{
        transform: translateX(-50%) translateY(-120px);
        opacity: 0;
    }}
}}

</style>

</head>

<body>

<div class="city {city_class}">

    <div class="sun"></div>

    <div class="cloud cloud1"></div>
    <div class="cloud cloud2"></div>

    <div class="mountain m1"></div>
    <div class="mountain m2"></div>
    <div class="mountain m3"></div>

    <div class="ground"></div>

    <div class="river">
        <div class="wave wave1"></div>
        <div class="wave wave2"></div>
        <div class="wave wave3"></div>
    </div>

    <div class="building b1">
        <div class="window"></div>
    </div>

    <div class="building b2">
        <div class="window"></div>
    </div>

    <div class="building b3">
        <div class="window"></div>
    </div>

    <div class="tree t1">🌳</div>
    <div class="tree t2">🌳</div>
    <div class="tree t3">🌳</div>
    <div class="tree t4">🌳</div>
    <div class="tree t5">🌳</div>

    <div class="flower f1">🌸</div>
    <div class="flower f2">🌼</div>
    <div class="flower f3">🌷</div>

    <div class="butterfly bf1">🦋</div>
    <div class="butterfly bf2">🦋</div>

    <div class="wind">
        <div class="windLine w1"></div>
        <div class="windLine w2"></div>
        <div class="windLine w3"></div>
        <div class="windLine w4"></div>
    </div>

    <div class="rain">
        <div class="rainDrop r1"></div>
        <div class="rainDrop r2"></div>
        <div class="rainDrop r3"></div>
        <div class="rainDrop r4"></div>
        <div class="rainDrop r5"></div>
        <div class="rainDrop r6"></div>
        <div class="rainDrop r7"></div>
        <div class="rainDrop r8"></div>
        <div class="rainDrop r9"></div>
        <div class="rainDrop r10"></div>
        <div class="rainDrop r11"></div>
        <div class="rainDrop r12"></div>
    </div>

    <div class="haze"></div>

    <div class="road">
        <div class="roadLine"></div>
    </div>

    <div class="popup">
        {popup_message}
    </div>

</div>

</body>

</html>
"""

# ---------------------------------------------------------
# DISPLAY CITY
# ---------------------------------------------------------

components.html(
    city_html,
    height=525,
    scrolling=False
)

# ---------------------------------------------------------
# ENVIRONMENT MESSAGE
# ---------------------------------------------------------

if pollution < 30:

    st.success(
        "🌿 Excellent! Your environmental choices "
        "are creating a healthy city."
    )

elif pollution < 60:

    st.warning(
        "🌱 Your city is balanced, but increasing "
        "trees, recycling and public transport can improve it."
    )

else:

    st.error(
        "⚠️ Pollution is too high! Try increasing "
        "trees, recycling, solar energy and public transport."
    )

# ---------------------------------------------------------
# POLLUTION FORMULA
# ---------------------------------------------------------

with st.expander("📊 How is the pollution calculated?"):

    st.write(
        "The simulator uses a simple weighted formula."
    )

    st.write(
        "Pollution increases with cars and factories."
    )

    st.write(
        "Pollution decreases with trees, recycling, "
        "solar energy and public transport."
    )

    st.code(
        """
pollution =
    cars × 0.30
    + factories × 0.25
    + (100 - recycling) × 0.15
    + (100 - transport) × 0.10
    - trees × 0.12
    - solar × 0.08
        """
    )

    st.write(
        "The final value is kept between 0 and 100."
    )
    
# ---------------------------------------------------------
# ECOPULSE - DATAFRAME AND DATA VISUALISATION
# ---------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

st.divider()

st.header("🌿 EcoPulse")
st.subheader("Every choice leaves a footprint.")

st.write(
    "Discover the story behind your city's environmental health."
)

# Creating a DataFrame

data = {
    "Environmental Factor": [
        "Cars",
        "Factories",
        "Recycling",
        "Public Transport",
        "Trees",
        "Solar Energy"
    ],
    "Current Value": [
        cars, factories, recycling,
        transport, trees, solar
    ],
    "Pollution Impact": [
        cars * 0.30,
        factories * 0.25,
        (100 - recycling) * 0.15,
        (100 - transport) * 0.10,
        -trees * 0.12,
        -solar * 0.08
    ]
}

df = pd.DataFrame(data)
df["Pollution Impact"] = df["Pollution Impact"].round(2)

st.subheader("📋 Environmental Report")
st.dataframe(df, hide_index=True)

st.caption(
    "Positive values increase pollution. "
    "Negative values reduce pollution. "
    "Recycling and transport impacts represent their shortfalls."
)

# Data Visualisation

st.subheader("📊 Nature in Numbers")

graph1, graph2 = st.columns(2)

# Horizontal Bar Graph

with graph1:

    st.markdown("#### What Shapes Your City?")

    colors = [
        "#E07A5F" if x > 0 else "#40916C"
        for x in df["Pollution Impact"]
    ]

    fig, ax = plt.subplots(figsize=(7, 5))

    ax.barh(
        df["Environmental Factor"],
        df["Pollution Impact"],
        color=colors
    )

    ax.axvline(0, color="gray")
    ax.set_xlabel("Pollution Impact")
    ax.invert_yaxis()

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

# Doughnut Chart

with graph2:

    st.markdown("#### The City's Green Balance")

    fig2, ax2 = plt.subplots(figsize=(6, 5))

    ax2.pie(
        [eco_score, pollution],
        labels=["Eco Score", "Pollution"],
        colors=["#40916C", "#E07A5F"],
        autopct="%1.0f%%",
        startangle=90,
        wedgeprops={
            "width": 0.35,
            "edgecolor": "white"
        }
    )

    ax2.text(
        0, 0,
        str(eco_score) + "%",
        ha="center",
        va="center",
        fontsize=25,
        fontweight="bold",
        color="#40916C"
    )

    st.pyplot(fig2)
    plt.close(fig2)

# Environmental Analysis

st.subheader("🔍 What Is Your City Telling You?")

if pollution < 30:
    st.success("Your choices are helping nature thrive!")

elif pollution < 60:
    st.warning("Small changes can make a big difference.")

else:
    st.error("Your city needs greener choices!")

st.caption("Values are based on the EcoMorph simulation.")

st.divider()

st.markdown("## 🌍 The Future Is in Your Hands.")

st.write(
    "Every number tells a story. "
    "Every choice changes its ending."
)

st.markdown("**What kind of world will you create?**")
