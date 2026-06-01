import streamlit as st
import pandas as pd
import numpy as np
import time
import random

# Page Configuration
st.set_page_config(page_title="Bio-Quantum Nexus Enterprise", page_icon="🛰️", layout="wide")

# Custom CSS for Deep Ocean Blue & Futuristic Theme
st.markdown("""
    <style>
    /* Main Background with Deep Cyber Blue Gradient */
    .stApp {
        background: linear-gradient(135deg, #051329 0%, #0a2246 50%, #020c1b 100%);
        color: #e2e8f0;
    }
    
    /* Glowing Blue Metric Cards */
    div[data-testid="stMetricSimpleRegion"] {
        background-color: rgba(10, 37, 74, 0.6);
        padding: 20px;
        border-radius: 12px;
        border: 2px solid #00d2ff;
        box-shadow: 0px 0px 15px rgba(0, 210, 255, 0.3);
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #030f21 !important;
        border-right: 2px solid #0072ff;
    }
    
    /* Headers customized for clarity */
    h1, h2, h3 {
        color: #00d2ff !important;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0px 0px 10px rgba(0, 210, 255, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# Title & Header
st.title("🌌 Bio-Quantum Nexus: Planetary Ocean Monitor")
st.subheader("Synthetic DNA Storage & Quantum-Secured Satellite Telemetry Network")
st.markdown("---")

# Sidebar Configuration (Advanced Control Panel)
st.sidebar.header("📡 Advanced Control Panel")
quantum_key = st.sidebar.text_input("Enter Quantum Encryption Key", value="NEXUS-SECURE-2026", type="password")
system_mode = st.sidebar.selectbox("System Monitoring Mode", ["Live Telemetry Simulation", "Deep Ocean Analysis", "Historical Bio-Data"])

st.sidebar.markdown("---")
st.sidebar.subheader("🚀 Satellite Sub-Systems")
sat_status = st.sidebar.toggle("Activate NEXUS-1 Orbiters", value=True)
bio_shield_status = st.sidebar.toggle("Deploy Eco-Interceptors", value=False)

if sat_status:
    st.sidebar.success("🔗 Quantum Entanglement Link: ACTIVE")
else:
    st.sidebar.warning("🛑 Quantum Link: DISCONNECTED")

# Top Level Metrics (KPIs)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Global Ocean Oxygen Production", value="52.4 %", delta="+0.2% (Optimal)")
with col2:
    st.metric(label="Phytoplankton Bioluminescence", value="89.6 %", delta="-1.4% (Toxicity Alert)", delta_color="inverse")
with col3:
    st.metric(label="Quantum Telemetry Latency", value="0.0001 ms", delta="Zero-Latency Mode")
with col4:
    st.metric(label="Synthetic DNA Storage Density", value="215 PB/g", delta="100% Structural Stability")

st.markdown("---")

# Main Dashboard Layout
left_column, right_column = st.columns([3, 2])

with left_column:
    st.subheader("🗺️ Live Phytoplankton & Bio-Sensor Active Hotspots")
    st.markdown("_Simulating live coordinate telemetry from satellite grids via micro-biosensors._")
    
    # Simulating random coordinates around major ocean zones for the map
    map_data = pd.DataFrame(
        np.random.randn(50, 2) / [10, 20] + [15.0, 75.0], # Centered near Indian Ocean/Equator
        columns=['lat', 'lon']
    )
    st.map(map_data, zoom=3)

    st.markdown("---")
    st.subheader("☣️ Simulated Microplastic Concentration & Chemical Density")
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Atlantic Grid Alpha', 'Pacific Grid Beta', 'Indian Ocean Grid Gamma']
    )
    st.line_chart(chart_data)

with right_column:
    st.subheader("🧬 Synthetic DNA Crypto-Stream Matrix")
    st.write("Live data stream injection directly into synthetic DNA base pairs:")
    
    # Live simulation trigger button
    if st.button("🔄 Inject Fresh Telemetry Data Stream"):
        with st.spinner("Encoding telemetry into ATCG Base Pairs..."):
            progress_bar = st.progress(0)
            for percent_complete in range(100):
                time.sleep(0.005)
                progress_bar.progress(percent_complete + 1)
            st.success("Data Block Stored Successfully!")
    
    # Dynamic DNA sequence generator
    bases = ['A', 'T', 'C', 'G']
    random_sequence = "".join(random.choice(bases) for _ in range(32))
    
    st.code(f"""
    [QUANTUM-NODE-ENCRYPTED]
    Hash ID: Q-NEXUS-{random.randint(1000, 9999)}
    DNA Matrix Sequence: {random_sequence}
    Storage Integrity: SECURE (100%)
    Carbon Emission: 0.00% (Absolute Green Computing)
    """, language="bash")

    st.markdown("---")
    st.subheader("📊 Executive Summary Report")
    st.write("Generate a secure data log for global climate organizations and international youth councils.")
    
    # Download report simulator button
    report_data = "BIO-QUANTUM NEXUS REPORT\nStatus: Active\nOcean Health Index: 8.5/10\nQuantum Latency: Stable"
    st.download_button(
        label="📥 Download Global Ocean Health Log (.txt)",
        data=report_data,
        file_name="nexus_ocean_report.txt",
        mime="text/plain"
    )

# Bio-Shield Protocol Alert System
st.markdown("---")
st.subheader("🚨 Autonomous Bio-Shield Protocol Controls")
st.write("Adjust the slider to simulate changing marine ecosystem conditions.")
toxicity_check = st.slider("Simulate Microplastic Toxicity Threshold (ppm)", 0, 100, 42)

if toxicity_check > 70:
    st.error(f"⚠️ CRITICAL ALERT: Toxicity level reached {toxicity_check} ppm! Autonomous Bio-Shield Protocol triggered. Emergency bioluminescent countermeasures initiated across global coastal lines.")
    if bio_shield_status:
        st.info("⚡ Eco-Interceptors are active. Automated biological neutralization in progress.")
elif 40 <= toxicity_check <= 70:
    st.warning(f"⚡ WARNING: Moderate anomaly detected ({toxicity_check} ppm). Satellite clusters are scanning the affected grids closely.")
else:
    st.success("✅ BIOSPHERE STATUS: SAFE. Phytoplankton activity is standard, and carbon sequestration rates are nominal.")
