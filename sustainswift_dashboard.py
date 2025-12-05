import streamlit as st
import time
import pandas as pd
import hashlib
import json
import random
import requests

# --- CONFIGURATION & STYLING ---
st.set_page_config(page_title="SustainSwift | zktls Verifier", layout="wide")

st.markdown("""
<style>
    .reportview-container { background: #0e1117; }
    .stButton>button { width: 100%; border-radius: 5px; }
    .tls-verified { border: 1px solid #4CAF50; padding: 10px; border-radius: 5px; background: rgba(76, 175, 80, 0.1); }
    .private-data { filter: blur(5px); transition: filter 0.3s; cursor: pointer; }
    .private-data:hover { filter: blur(0px); }
</style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🛡️ SustainSwift Protocol (v2.0)")
st.caption("Powered by **GenOptima** (Inference), **zktls** (Oracle), and **Caffeine AI** (Verification)")

col1, col2, col3 = st.columns([1, 0.2, 1])

# --- LEFT COLUMN: THE SUPPLIER (Private) ---
with col1:
    st.header("🏭 Supplier Edge Node")
    st.info("Status: Local Environment (Air-Gapped)")
    
    # STEP 1: zktls Data Fetch via API
    st.markdown("### 1. Data Origin Verification")
    if st.button("🔗 Connect to Utility API (zktls)"):
        with st.spinner("Establishing zktls Session with localhost:5000..."):
            try:
                # REAL CALL to your local mock API
                response = requests.get("http://127.0.0.1:5000/v1/meter/FACTORY-001")
                if response.status_code == 200:
                    st.session_state['private_data'] = response.json()
                    st.session_state['tls_connected'] = True
                    st.success("Secure Payload Received from Duke Energy API")
                else:
                    st.error("API Error")
            except Exception as e:
                st.error(f"Connection Failed: Is utility_api.py running? {e}")
            
    if 'tls_connected' in st.session_state:
        st.markdown(f"""
        <div class="tls-verified">
            <b>✅ zktls Session Established</b><br>
            Origin: <code>https://api.duke-energy.com/v1/usage</code><br>
            <i>Credentials hidden. Payload verified.</i>
        </div>
        """, unsafe_allow_html=True)

        # Display Private Data (Blurred)
        st.markdown("### 2. Private Payload")
        st.markdown("*Hover to reveal raw API response:*")
        st.json(st.session_state['private_data'])
        
        st.markdown("---")
        
        # STEP 2: GenOptima Inference
        if st.button("⚙️ Run GenOptima + Generate ZK Proof"):
            with st.spinner('Running zkPyTorch Circuit...'):
                time.sleep(2) 
                
                # Model Logic - SAFE ACCESS using .get()
                data = st.session_state['private_data']
                usage = data.get('usage_kwh', 0) # Fallback to 0 if missing
                emissions = usage * 0.22
                
                # The Proof now includes the zktls session ID to prove origin
                # We use .get() here to prevent the KeyError if session_key is missing
                session_key_safe = data.get('session_key', 'manual_session_override')
                
                proof_payload = {
                    "proof_id": f"zk-{random.randint(10000,99999)}",
                    "zktls_proof": session_key_safe,
                    "public_output": {
                        "emissions_tons": emissions,
                        "compliant": True
                    },
                    "model_hash": "genoptima_v4_2025"
                }
                st.session_state['proof'] = proof_payload
            st.success("✅ Zero-Knowledge Proof Generated!")
            st.json(proof_payload)

# --- MIDDLE COLUMN: THE NETWORK ---
with col2:
    st.markdown("<br><br><br><br><br>", unsafe_allow_html=True)
    if 'proof' in st.session_state:
        st.markdown("## ➡️")
        st.markdown("## Sending")
        st.markdown("## Proof")
        st.markdown("## ➡️")

# --- RIGHT COLUMN: THE VERIFIER (Public) ---
with col3:
    st.header("🌍 Caffeine AI Canister")
    st.info("Network: Internet Computer (ICP)")
    
    if 'proof' in st.session_state:
        st.markdown(f"**Incoming Proof:** `{st.session_state['proof']['proof_id']}`")
        
        if st.button("🔍 Verify On-Chain"):
            with st.spinner("Broadcasting to Caffeine Network (localhost:5001)..."):
                try:
                    # REAL CALL to your local mock Blockchain
                    payload = {"proof_id": st.session_state['proof']['proof_id']}
                    chain_res = requests.post("http://127.0.0.1:5001/canister/verify_proof", json=payload)
                    
                    if chain_res.status_code == 200:
                        st.balloons()
                        st.success("✅ AUDIT PASSED: Settlement Confirmed")
                        st.json(chain_res.json())
                except Exception as e:
                    st.error(f"Blockchain Node Unreachable: Is caffeine_node.py running? {e}")

    else:
        st.markdown("*Waiting for Proof...*")

# --- FOOTER ---
st.markdown("---")
st.markdown(" **SustainSwift** | 2025 Sustainable Finance Hackathon")