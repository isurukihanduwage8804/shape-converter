import streamlit as st
import numpy as np

# පිටුවේ මූලික සැකසුම්
st.set_page_config(page_title="ත්‍රිමාණ වස්තු පරිවර්තකය", layout="wide")

# CSS මගින් පෙනුම හැඩගැන්වීම
st.markdown("""
    <style>
    .main-title { color: #2c3e50; text-align: center; font-size: 35px; font-weight: bold; }
    .res-box { background-color: #f4f6f7; padding: 20px; border-radius: 10px; border-left: 10px solid #27ae60; font-size: 20px; color: #1e8449;}
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="main-title">📐 ත්‍රිමාණ වස්තු පරිමාව සහ මිනුම් Calculator (cm)</p>', unsafe_allow_html=True)

# වස්තූන් ලැයිස්තුව
shapes = ["ගෝලය (Sphere)", "ඝනකය (Cube)", "පිරමිඩය (Pyramid)", "චතුස්තලය (Tetrahedron)", "සිලින්ඩරය (Cylinder)", "ඝනකාභය (Cuboid)"]

# Sidebar - මුල් වස්තුව ලබා ගැනීම
st.sidebar.header("📥 මුල් වස්තුවේ මිනුම් (cm)")
source_shape = st.sidebar.selectbox("වස්තුව තෝරන්න:", shapes)

volume = 0.0

if source_shape == "ගෝලය (Sphere)":
    r = st.sidebar.number_input("අරය (r) cm වලින්:", value=5.0, min_value=0.1)
    volume = (4/3) * np.pi * (r**3)
elif source_shape == "ඝනකය (Cube)":
    a = st.sidebar.number_input("පැත්තක දිග (a) cm වලින්:", value=5.0, min_value=0.1)
    volume = a**3
elif source_shape == "පිරමිඩය (Pyramid)":
    a = st.sidebar.number_input("පාදමේ පැත්තක දිග (a) cm වලින්:", value=5.0, min_value=0.1)
    h = st.sidebar.number_input("සිරස් උස (h) cm වලින්:", value=10.0, min_value=0.1)
    volume = (1/3) * (a**2) * h
elif source_shape == "චතුස්තලය (Tetrahedron)":
    a = st.sidebar.number_input("දාරයක දිග (a) cm වලින්:", value=5.0, min_value=0.1)
    volume = (a**3) / (6 * np.sqrt(2))
elif source_shape == "සිලින්ඩරය (Cylinder)":
    r = st.sidebar.number_input("අරය (r) cm වලින්:", value=3.0, min_value=0.1)
    h = st.sidebar.number_input("උස (h) cm වලින්:", value=10.0, min_value=0.1)
    volume = np.pi * (r**2) * h
elif source_shape == "ඝනකාභය (Cuboid)":
    l = st.sidebar.number_input("දිග (l) cm වලින්:", value=5.0, min_value=0.1)
    w = st.sidebar.number_input("පළල (w) cm වලින්:", value=4.0, min_value=0.1)
    h = st.sidebar.number_input("උස (h) cm වලින්:", value=3.0, min_value=0.1)
    volume = l * w * h

# Sidebar - ඉලක්ක වස්තුව තෝරා ගැනීම
st.sidebar.markdown("---")
st.sidebar.header("📤 පරිවර්තනය වන වස්තුව")
target_shape = st.sidebar.selectbox("අලුත් හැඩය තෝරන්න:", shapes)

# ප්‍රධාන ප්‍රදර්ශන කොටස
st.subheader(f"📊 {source_shape} -> {target_shape} පරිවර්තනය")
col1, col2 = st.columns([1, 1])

with col1:
    st.info(f"මුල් වස්තුවේ පරිමාව: **{volume:.2f} cm³**")
    result_text = ""
    
    if target_shape == "ගෝලය (Sphere)":
        r_new = ((3 * volume) / (4 * np.pi))**(1/3)
        result_text = f"අලුත් ගෝලයේ අරය (r): **{r_new:.2f} cm**"
    elif target_shape == "ඝනකය (Cube)":
        a_new = volume**(1/3)
        result_text = f"අලුත් ඝනකයේ පැත්තක දිග (a): **{a_new:.2f} cm**"
    elif target_shape == "සිලින්ඩරය (Cylinder)":
        r_fix = 5.0 
        h_new = volume / (np.pi * (r_fix**2))
        result_text = f"අරය {r_fix} cm ලෙස ස්ථාවරව තැබුවහොත්, අවශ්ය උස (h): **{h_new:.2f} cm**"
    elif target_shape == "පිරමිඩය (Pyramid)":
        a_fix = 5.0
        h_new = (3 * volume) / (a_fix**2)
        result_text = f"පාදම පැත්ත {a_fix} cm ලෙස ගතහොත්, අවශ්ය උස (h): **{h_new:.2f} cm**"
    elif target_shape == "චතුස්තලය (Tetrahedron)":
        a_new = (volume * 6 * np.sqrt(2))**(1/3)
        result_text = f"අලුත් චතුස්තලයේ දාරයක දිග (a): **{a_new:.2f} cm**"
    elif target_shape == "ඝනකාභය (Cuboid)":
        l_fix, w_fix = 5.0, 4.0
        h_new = volume / (l_fix * w_fix)
        result_text = f"දිග {l_fix}cm සහ පළල {w_fix}cm ලෙස ගතහොත්, අවශ්ය උස (h): **{h_new:.2f} cm**"

    st.markdown(f'<div class="res-box">{result_text}</div>', unsafe_allow_html=True)

with col2:
    st.write("**පරිමාව ගණනයට අදාළ රූප සටහන්:**")
    # මෙහිදී පරිශීලකයාට වැටහෙන සේ වස්තූන්ගේ හැඩතල පෙන්වයි
    if "ගෝලය" in target_shape:
        st.latex(r"V = \frac{4}{3}\pi r^3 \implies r = \sqrt[3]{\frac{3V}{4\pi}}")
    elif "ඝනකය" in target_shape:
        st.latex(r"V = a^3 \implies a = \sqrt[3]{V}")
    else:
        st.write("වෙනත් වස්තූන් සඳහා පරිමාව $V = \text{පාදම වර්ගඵලය} \times \text{උස}$ සූත්‍රය භාවිතා වේ.")

st.markdown("<br><hr><center>ගණිත අධ්‍යාපන සහායක පද්ධතිය</center>", unsafe_allow_html=True)
