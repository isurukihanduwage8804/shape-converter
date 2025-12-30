import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="3D වස්තු මිනුම් Calculator", layout="wide")

st.title("📐 ත්‍රිමාණ වස්තු පරිමාව සහ හැඩතල")

# Sidebar - මුල් වස්තුව
st.sidebar.header("📥 මුල් වස්තුව (cm)")
source_shape = st.sidebar.selectbox("වස්තුව තෝරන්න:", 
    ["ගෝලය (Sphere)", "ඝනකය (Cube)", "පිරමිඩය (Pyramid)", "සිලින්ඩරය (Cylinder)", "ඝනකාභය (Cuboid)"])

volume = 0.0
if source_shape == "ගෝලය (Sphere)":
    r = st.sidebar.number_input("අරය (r):", value=5.0)
    volume = (4/3) * np.pi * (r**3)
elif source_shape == "ඝනකය (Cube)":
    a = st.sidebar.number_input("පැත්ත (a):", value=5.0)
    volume = a**3
elif source_shape == "සිලින්ඩරය (Cylinder)":
    r = st.sidebar.number_input("අරය (r):", value=3.0)
    h = st.sidebar.number_input("උස (h):", value=10.0)
    volume = np.pi * (r**2) * h
# (අනෙක් වස්තූන්ද මේ ආකාරයටම එක් කළ හැක)

# Sidebar - අලුත් වස්තුව
st.sidebar.markdown("---")
target_shape = st.sidebar.selectbox("පරිවර්තනය වන හැඩය:", ["ගෝලය (Sphere)", "ඝනකය (Cube)", "සිලින්ඩරය (Cylinder)"])

# 3D රූපය ඇඳීම සඳහා Function එකක්
def draw_shape(shape_name):
    fig = go.Figure()
    if shape_name == "ගෝලය (Sphere)":
        u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
        x = np.cos(u)*np.sin(v)
        y = np.sin(u)*np.sin(v)
        z = np.cos(v)
        fig.add_trace(go.Surface(x=x, y=y, z=z, colorscale='Blues', showscale=False))
    elif shape_name == "ඝනකය (Cube)":
        fig.add_trace(go.Mesh3d(x=[0,1,1,0,0,1,1,0], y=[0,0,1,1,0,0,1,1], z=[0,0,0,0,1,1,1,1], 
                     i=[7,0,0,0,4,4,6,6,4,0,3,2], j=[3,4,1,2,5,6,5,2,0,1,6,3], k=[0,7,2,3,6,7,1,1,5,5,7,6], color='orange'))
    elif shape_name == "සිලින්ඩරය (Cylinder)":
        z = np.linspace(0, 1, 20)
        theta = np.linspace(0, 2*np.pi, 20)
        theta_grid, z_grid = np.meshgrid(theta, z)
        x = np.cos(theta_grid)
        y = np.sin(theta_grid)
        fig.add_trace(go.Surface(x=x, y=y, z=z_grid, colorscale='Greens', showscale=False))
    
    fig.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False), height=400)
    return fig

# ප්‍රතිඵල පෙන්වීම
col1, col2 = st.columns(2)

with col1:
    st.info(f"පරිමාව: {volume:.2f} cm³")
    if target_shape == "ගෝලය (Sphere)":
        res = ((3 * volume) / (4 * np.pi))**(1/3)
        st.success(f"අලුත් අරය: {res:.2f} cm")
    elif target_shape == "ඝනකය (Cube)":
        res = volume**(1/3)
        st.success(f"අලුත් පැත්ත: {res:.2f} cm")

with col2:
    st.write(f"**{target_shape} හි දර්ශනය:**")
    st.plotly_chart(draw_shape(target_shape))
