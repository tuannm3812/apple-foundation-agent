"""
Foundation Debugger: Enterprise Workspace Edition.

Fixed alignment issues by enforcing a minimum height on text blocks,
ensuring images and buttons always align perfectly horizontally.
"""

import time
import base64
import os
import streamlit as st


def get_base64_image(image_path: str) -> str:
    """Loads a local image and converts it to base64 for CSS injection."""
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""


def inject_custom_css() -> None:
    # Load the background image
    bg_base64 = get_base64_image("images/workspace_background.png")
    bg_css = f"url('data:image/png;base64,{bg_base64}')" if bg_base64 else "none"

    custom_css = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@400;600;800&family=Inter:wght@300;400;600;700&display=swap');

        /* 1. App Background with Base64 Image Injection */
        .stApp {{
            background-color: #0b0b0f;
            background-image: 
                radial-gradient(circle at 50% 0%, rgba(255, 80, 51, 0.12) 0%, rgba(11, 11, 15, 0.95) 70%),
                {bg_css}; 
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: 'Inter', sans-serif;
            color: #ffffff;
        }}
        
        /* Typography */
        h1, h2, h3 {{ 
            font-family: 'Kanit', sans-serif !important;
            font-weight: 800 !important; 
            letter-spacing: -0.02em; 
            color: #ffffff !important;
        }}
        
        /* ALIGNMENT FIX: min-height ensures short text doesn't pull elements up */
        .column-header {{ 
            font-size: 22px; 
            font-weight: 800; 
            font-family: 'Kanit', sans-serif; 
            margin-bottom: 5px; 
            color: #ffffff; 
            min-height: 33px; 
        }}
        .column-text {{ 
            font-size: 14px; 
            color: #a1a1aa; 
            font-family: 'Inter', sans-serif; 
            margin-bottom: 15px; 
            line-height: 1.5; 
            min-height: 48px; /* Forces space for 2 lines of text */
        }}
        
        p, li {{ font-weight: 400 !important; line-height: 1.6; color: #a1a1aa; }}
        .accent-text {{ color: #ff5033; font-weight: 700; }}

        .glass-card {{
            background-color: rgba(20, 20, 25, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            margin-bottom: 24px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
        }}

        /* 2. PRIMARY BUTTONS */
        button[kind="primary"] {{
            background: linear-gradient(180deg, #ff5436 0%, #e63919 100%) !important;
            border: none !important;
            border-radius: 30px !important;
            padding: 10px 24px !important;
            width: 100% !important;
            transition: all 0.2s ease-in-out;
            box-shadow: 0 4px 14px rgba(255, 80, 51, 0.2) !important;
        }}
        button[kind="primary"] p {{
            color: #ffffff !important; 
            font-size: 16px !important;
            font-weight: 700 !important;
            font-family: 'Inter', sans-serif !important;
            margin: 0 !important;
        }}
        button[kind="primary"]:hover {{
            transform: scale(1.02) !important;
            box-shadow: 0 6px 20px rgba(255, 80, 51, 0.4) !important;
            filter: brightness(1.1);
        }}

        /* Badges */
        .badge {{
            background-color: rgba(255, 80, 51, 0.15);
            color: #ff5033;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 12px;
            font-weight: 700;
            display: inline-block;
            margin-bottom: 16px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* Clean up column padding */
        [data-testid="column"] {{ padding: 0 10px; }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def init_session() -> None:
    if 'stage' not in st.session_state:
        st.session_state.stage = 1
    if 'scores' not in st.session_state:
        st.session_state.scores = {"iPhone": 0, "MacStudio": 0, "iPadPro": 0}


def run_app() -> None:
    st.set_page_config(page_title="Foundation Workspace", layout="wide")
    inject_custom_css()
    init_session()

    st.markdown("<p style='font-weight: 700; font-size: 16px; color: #fff;'><span class='accent-text'>✦</span> Foundation</p>", unsafe_allow_html=True)

    # ================= STAGE 1: THE CONTEXT =================
    if st.session_state.stage == 1:
        st.markdown("""
        <div style='text-align: center; margin-top: 60px; margin-bottom: 60px;'>
            <h1 style='font-size: 64px; line-height: 1.1;'>Code, bugs, and recovery.<br><span class='accent-text'>Finally in one workflow.</span></h1>
            <p style='font-size: 18px; max-width: 600px; margin: 20px auto;'>The diagnostic tool for workflows, priorities, and resilience — all in one fast workspace you'll actually enjoy using.</p>
        </div>
        """, unsafe_allow_html=True)
        
        _, col_center, _ = st.columns([1, 2, 1])
        with col_center:
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            st.markdown("<div class='badge'>Incident Log v1.0</div>", unsafe_allow_html=True)
            st.write("**ALERT:** Critical system failure detected during end-to-end NLP project. Accidentally deleted the core preprocessing script without committing to Git. A week of critical logic is missing.")
            st.write("")
            if st.button("EXECUTE DIAGNOSTIC PROTOCOL", type="primary"):
                st.session_state.stage = 2
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    # ================= STAGE 2: INITIAL REACTION =================
    elif st.session_state.stage == 2:
        st.markdown("<div class='badge'>Phase 1 of 2: Immediate Protocol</div>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 42px;'>Action Items & Priorities</h2>", unsafe_allow_html=True)
        st.write("The terminal is blank. What is your immediate first step?")
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='column-header'>Priority Speed</div>", unsafe_allow_html=True)
            st.markdown("<div class='column-text'>Rewrite immediately from memory. Rely on momentum and fresh context to recreate the logic fast.</div>", unsafe_allow_html=True)
            st.image("images/card_speed.png", use_container_width=True)
            if st.button("Select Speed", key="s2_speed", type="primary"):
                st.session_state.scores["iPhone"] += 1
                st.session_state.stage = 3
                st.rerun()
                
        with col2:
            st.markdown("<div class='column-header'>Priority Logic</div>", unsafe_allow_html=True)
            st.markdown("<div class='column-text'>Audit local cache & trace the fault. Analyze system logs before touching the keyboard.</div>", unsafe_allow_html=True)
            st.image("images/card_logic.png", use_container_width=True)
            if st.button("Select Logic", key="s2_logic", type="primary"):
                st.session_state.scores["MacStudio"] += 1
                st.session_state.stage = 3
                st.rerun()

        with col3:
            st.markdown("<div class='column-header'>Priority Network</div>", unsafe_allow_html=True)
            st.markdown("<div class='column-text'>Ping team comms to distribute the load. Transparency and collaboration are the first line of defense.</div>", unsafe_allow_html=True)
            st.image("images/card_network.png", use_container_width=True)
            if st.button("Select Network", key="s2_network", type="primary"):
                st.session_state.scores["iPadPro"] += 1
                st.session_state.stage = 3
                st.rerun()

    # ================= STAGE 3: THE RESOLUTION =================
    elif st.session_state.stage == 3:
        st.markdown("<div class='badge'>Phase 2 of 2: Deployment Strategy</div>", unsafe_allow_html=True)
        st.markdown("<h2 style='font-size: 42px;'>System Stabilization</h2>", unsafe_allow_html=True)
        st.write("The initial shock has passed. How do you ensure this project ships on time?")
        st.write("")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("<div class='column-header'>Velocity Tactic</div>", unsafe_allow_html=True)
            st.markdown("<div class='column-text'>Find a clever workaround to bypass the missing step. Hit the deadline at all costs.</div>", unsafe_allow_html=True)
            st.image("images/card_velocity.png", use_container_width=True)
            if st.button("Deploy Workaround", key="s3_speed", type="primary"):
                st.session_state.scores["iPhone"] += 1
                st.session_state.stage = 4
                st.rerun()
                
        with col2:
            st.markdown("<div class='column-header'>Infrastructure</div>", unsafe_allow_html=True)
            st.markdown("<div class='column-text'>Architect strict CI/CD pipelines and automated Git backups to prevent recurrence.</div>", unsafe_allow_html=True)
            st.image("images/card_infra.png", use_container_width=True)
            if st.button("Build Infrastructure", key="s3_logic", type="primary"):
                st.session_state.scores["MacStudio"] += 1
                st.session_state.stage = 4
                st.rerun()

        with col3:
            st.markdown("<div class='column-header'>Collaboration</div>", unsafe_allow_html=True)
            st.markdown("<div class='column-text'>Organize a pair-programming swarm session to rebuild the logic together.</div>", unsafe_allow_html=True)
            st.image("images/card_collab.png", use_container_width=True)
            if st.button("Initiate Swarm", key="s3_network", type="primary"):
                st.session_state.scores["iPadPro"] += 1
                st.session_state.stage = 4
                st.rerun()

    # ================= STAGE 4: THE RESULT =================
    elif st.session_state.stage == 4:
        winner = max(st.session_state.scores, key=st.session_state.scores.get)
        
        with st.spinner("Compiling diagnostic data..."):
            time.sleep(1.5)
            
            _, col_center, _ = st.columns([1, 4, 1])
            with col_center:
                st.markdown("""
                <div style='text-align: center; margin-top: 20px; margin-bottom: 30px;'>
                    <div class='badge'>Diagnostic complete.</div>
                    <h1 style='font-size: 48px;'>Your Developer Profile</h1>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                col_img, col_text = st.columns([1, 1.2])
                
                with col_img:
                    if winner == "iPhone":
                        st.image("images/iphone_speed.png", use_container_width=True)
                    elif winner == "MacStudio":
                        st.image("images/macstudio_logic.png", use_container_width=True)
                    else:
                        st.image("images/ipad_team.png", use_container_width=True)

                with col_text:
                    if winner == "iPhone":
                        st.markdown("<h2>The Tactical Solver</h2>", unsafe_allow_html=True)
                        st.write("You are the practical engine of any project. You bypass roadblocks, maintain momentum, and deliver results under pressure.")
                    elif winner == "MacStudio":
                        st.markdown("<h2>The Systems Architect</h2>", unsafe_allow_html=True)
                        st.write("You don't just fix bugs; you build infrastructure. You prioritize deep logic and treat failures as lessons in MLOps.")
                    else:
                        st.markdown("<h2>The Ecosystem Catalyst</h2>", unsafe_allow_html=True)
                        st.write("You are the central hub. You prioritize team bandwidth and know that the most resilient data products are built collaboratively.")
                    
                    st.divider()
                    st.markdown("<p style='font-size: 14px; color: #a1a1aa;'>Recovery Protocol Signature:</p>", unsafe_allow_html=True)
                    if winner == "iPhone":
                        st.markdown("<p class='accent-text'>→ Adapt, Execute, and Keep Moving.</p>", unsafe_allow_html=True)
                    elif winner == "MacStudio":
                        st.markdown("<p class='accent-text'>→ Analyze Fault, Engineer the Fix.</p>", unsafe_allow_html=True)
                    else:
                        st.markdown("<p class='accent-text'>→ Synchronize Team, Distribute Load.</p>", unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)

                st.image("images/stage_clear_castle.png", use_container_width=True, caption="[ Confirmed: Destination // Apple Foundation Program ]")
                st.write("")
                if st.button("INSERT NEW PROJECT PROTOCOL", type="primary"):
                    st.session_state.stage = 1
                    st.session_state.scores = {"iPhone": 0, "MacStudio": 0, "iPadPro": 0}
                    st.rerun()

if __name__ == "__main__":
    run_app()