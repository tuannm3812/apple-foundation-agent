"""
Foundation Debugger: Enterprise Workspace Edition v2.0.

Features a 5-stage deep-dive assessment, 5 distinct developer archetypes,
base64 background injection, and a premium SaaS UI.
"""

import time
import base64
import os
import streamlit as st


def get_base64_image(image_path: str) -> str:
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    return ""


def inject_custom_css() -> None:
    bg_base64 = get_base64_image("images/workspace_background.png")
    bg_css = f"url('data:image/png;base64,{bg_base64}')" if bg_base64 else "none"

    custom_css = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@400;600;800&family=Inter:wght@300;400;500;600;700&display=swap');

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
        
        h1, h2, h3 {{ 
            font-family: 'Kanit', sans-serif !important;
            font-weight: 800 !important; 
            letter-spacing: -0.02em; 
            color: #ffffff !important;
        }}
        
        p, li {{ font-weight: 400 !important; line-height: 1.6; color: #a1a1aa; }}
        .accent-text {{ color: #ff5033; font-weight: 700; }}

        # .glass-card {{
        #     background-color: rgba(20, 20, 25, 0.6);
        #     border: 1px solid rgba(255, 255, 255, 0.05);
        #     border-radius: 12px;
        #     padding: 40px;
        #     box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
        #     margin-bottom: 24px;
        #     backdrop-filter: blur(20px);
        #     -webkit-backdrop-filter: blur(20px);
        # }}

        /* PRIMARY BUTTONS (Action) */
        button[kind="primary"] {{
            background: linear-gradient(180deg, #ff5436 0%, #e63919 100%) !important;
            border: none !important;
            border-radius: 30px !important;
            padding: 12px 24px !important;
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

        /* SECONDARY BUTTONS (Choices - Full Width Stacked) */
        button[kind="secondary"] {{
            background-color: rgba(255, 255, 255, 0.02) !important;
            color: #e5e5e7 !important;
            border: 1px solid rgba(255, 255, 255, 0.1) !important;
            border-radius: 8px !important;
            padding: 16px 24px !important;
            width: 100% !important;
            text-align: left !important;
            justify-content: flex-start !important;
            font-family: 'Inter', sans-serif !important;
            transition: all 0.2s ease-in-out;
            margin-bottom: 12px !important;
        }}
        button[kind="secondary"] p {{ margin: 0 !important; font-size: 15px !important; color: #e5e5e7 !important;}}
        button[kind="secondary"] strong {{ color: #ffffff !important; font-weight: 600 !important; }}
        button[kind="secondary"]:hover {{
            border-color: #ff5033 !important;
            background-color: rgba(255, 80, 51, 0.05) !important;
            transform: translateX(4px);
        }}

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
        
        .progress-text {{ font-family: 'Kanit', sans-serif; font-size: 14px; color: #ff5033; letter-spacing: 1px; margin-bottom: -10px; display: block; }}
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def init_session() -> None:
    if 'stage' not in st.session_state:
        st.session_state.stage = 0
    if 'scores' not in st.session_state:
        st.session_state.scores = {
            "Tactical": 0, "Architect": 0, "Catalyst": 0, "Visionary": 0, "Researcher": 0
        }


def run_app() -> None:
    st.set_page_config(page_title="Foundation Workspace", layout="centered")
    inject_custom_css()
    init_session()

    st.markdown("<p style='font-weight: 700; font-size: 16px; color: #fff;'><span class='accent-text'>✦</span> Foundation</p>", unsafe_allow_html=True)

    # ================= STAGE 0: THE CONTEXT =================
    if st.session_state.stage == 0:
        st.markdown("""
        <div style='text-align: center; margin-top: 40px; margin-bottom: 50px;'>
            <h1 style='font-size: 64px; line-height: 1.1;'>Code, bugs, and recovery.<br><span class='accent-text'>Finally in one workflow.</span></h1>
            <p style='font-size: 18px; max-width: 600px; margin: 20px auto;'>A 5-step diagnostic tool analyzing workflows, priorities, and resilience — all in one fast workspace you'll actually enjoy using.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown("<div class='badge'>Incident Log v2.0</div>", unsafe_allow_html=True)
        st.write("**ALERT:** Critical system failure detected during your end-to-end NLP project. You accidentally deleted the core preprocessing script without committing to Git. A week of critical logic is missing.")
        st.write("")
        if st.button("EXECUTE DIAGNOSTIC PROTOCOL", type="primary"):
            st.session_state.stage = 1
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ================= STAGES 1-5: THE QUESTIONS =================
    elif 1 <= st.session_state.stage <= 5:
        
        questions = [
            {
                "phase": "Phase 1: The Reaction",
                "q": "The terminal is blank after the deletion. What is your immediate first step?",
                "options": [
                    ("Tactical", "**Speed:** Rewrite immediately from memory to maintain momentum."),
                    ("Architect", "**Logic:** Audit system logs and trace the fault before touching the keyboard."),
                    ("Catalyst", "**Network:** Ping the team comms immediately to distribute the recovery load."),
                    ("Visionary", "**Impact:** Assess how this delay affects the overall release timeline."),
                    ("Researcher", "**Optimization:** Use this as an excuse to research a better library to rebuild it with.")
                ]
            },
            {
                "phase": "Phase 2: The Pivot",
                "q": "You recovered the data, but your NLP model is failing to converge. How do you pivot?",
                "options": [
                    ("Tactical", "**Iterate:** Switch to a simpler, faster baseline model to get immediate results."),
                    ("Architect", "**Pipeline:** Build an automated hyperparameter tuning grid to brute-force the best metrics."),
                    ("Catalyst", "**Consult:** Ask a senior engineer or teammate for a fresh-eyes code review."),
                    ("Visionary", "**Re-evaluate:** Question if this specific accuracy metric actually matters to the end-user."),
                    ("Researcher", "**Deep Dive:** Open the documentation to analyze the mathematical loss function.")
                ]
            },
            {
                "phase": "Phase 3: The Deployment",
                "q": "The model is fixed. It is time to push the application to production. What is your focus?",
                "options": [
                    ("Tactical", "**Ship It:** Deploy manually to get it out immediately and fix bugs live."),
                    ("Architect", "**Containerize:** Package it with Docker and push through an automated staging environment."),
                    ("Catalyst", "**Document:** Write comprehensive API docs so the frontend team can integrate easily."),
                    ("Visionary", "**Analytics:** Set up A/B testing frameworks to track user engagement immediately."),
                    ("Researcher", "**Monitor:** Set up strict drift-detection to monitor statistical degradation over time.")
                ]
            },
            {
                "phase": "Phase 4: The Legacy",
                "q": "You inherit a massive legacy codebase with severe tech debt. How do you handle it?",
                "options": [
                    ("Tactical", "**Bypass:** Ignore the debt and build new features on top as quickly as possible."),
                    ("Architect", "**Refactor:** Propose tearing down the monolith and rebuilding it into microservices."),
                    ("Catalyst", "**Align:** Schedule a workshop to align the team on new coding standards moving forward."),
                    ("Visionary", "**Prioritize:** Check if rewriting the backend will delay the upcoming UI revamp."),
                    ("Researcher", "**Profile:** Benchmark the code and optimize only the most mathematically complex functions.")
                ]
            },
            {
                "phase": "Phase 5: The Pressure",
                "q": "A high-priority feature request comes in at 4 PM on a Friday. What is your move?",
                "options": [
                    ("Tactical", "**Hack It:** Hack together a quick script and deploy it before 5 PM."),
                    ("Architect", "**Queue It:** Add it to the backlog safely for the next sprint's pipeline."),
                    ("Catalyst", "**Compromise:** Sync with the requester to find a collaborative, half-way solution."),
                    ("Visionary", "**Prototype:** Mock up a quick UI wireframe to ensure it's what they actually want first."),
                    ("Researcher", "**Investigate:** Spend the weekend researching the most optimal algorithmic approach.")
                ]
            }
        ]

        current_q = questions[st.session_state.stage - 1]
        
        st.markdown(f"<span class='progress-text'>DIAGNOSTIC: 0{st.session_state.stage} / 05</span>", unsafe_allow_html=True)
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='badge'>{current_q['phase']}</div>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='font-size: 32px; margin-bottom: 20px;'>{current_q['q']}</h2>", unsafe_allow_html=True)
        
        for archetype, text in current_q['options']:
            if st.button(text, key=f"q{st.session_state.stage}_{archetype}", type="secondary"):
                st.session_state.scores[archetype] += 1
                st.session_state.stage += 1
                st.rerun()
                
        st.markdown("</div>", unsafe_allow_html=True)

    # ================= STAGE 6: THE RESULT =================
    elif st.session_state.stage == 6:
        winner = max(st.session_state.scores, key=st.session_state.scores.get)
        
        with st.spinner("Compiling 5-point diagnostic data..."):
            time.sleep(1.5)
            
            st.markdown("""
            <div style='text-align: center; margin-top: 20px; margin-bottom: 30px;'>
                <div class='badge'>Diagnostic complete.</div>
                <h1 style='font-size: 48px;'>Your Developer Profile</h1>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
            col_img, col_text = st.columns([1, 1.5])
            
            with col_img:
                # Dynamically load the correct image based on winner
                img_path = f"images/profile_{winner.lower()}.png"
                if os.path.exists(img_path):
                    st.image(img_path, use_container_width=True)
                else:
                    st.markdown("<div style='height:300px; background:rgba(255,255,255,0.05); border-radius:12px; display:flex; align-items:center; justify-content:center; border:1px solid rgba(255,255,255,0.1);'>[Image Placeholder]</div>", unsafe_allow_html=True)

            with col_text:
                if winner == "Tactical":
                    st.markdown("<h2>The Tactical Solver</h2>", unsafe_allow_html=True)
                    st.write("You are the practical engine of any project. You bypass roadblocks, maintain momentum, and deliver results under pressure.")
                    st.write("**• Core Strength:** High-velocity iteration and adaptability.")
                    st.write("**• Blind Spot:** Sacrificing long-term architecture for short-term speed.")
                    st.write("**• Ideal Role:** Rapid Prototyping, Startup Developer.")
                elif winner == "Architect":
                    st.markdown("<h2>The Systems Architect</h2>", unsafe_allow_html=True)
                    st.write("You don't just fix bugs; you build infrastructure. You prioritize deep logic and treat failures as lessons in MLOps.")
                    st.write("**• Core Strength:** Structural integrity and root-cause analysis.")
                    st.write("**• Blind Spot:** Over-engineering simple solutions (Analysis Paralysis).")
                    st.write("**• Ideal Role:** Data Engineer, Cloud/MLOps Specialist.")
                elif winner == "Catalyst":
                    st.markdown("<h2>The Ecosystem Catalyst</h2>", unsafe_allow_html=True)
                    st.write("You are the central hub. You prioritize team bandwidth and know that the most resilient data products are built collaboratively.")
                    st.write("**• Core Strength:** Empathy, delegation, and breaking down silos.")
                    st.write("**• Blind Spot:** Relying too heavily on consensus, slowing down execution.")
                    st.write("**• Ideal Role:** Technical Product Manager, Scrum Master.")
                elif winner == "Visionary":
                    st.markdown("<h2>The Visionary Engineer</h2>", unsafe_allow_html=True)
                    st.write("You connect the code to the customer. You ensure that the complex backend logic actually serves a meaningful business purpose.")
                    st.write("**• Core Strength:** User empathy and business alignment.")
                    st.write("**• Blind Spot:** Getting distracted by UI/UX over backend stability.")
                    st.write("**• Ideal Role:** Full-Stack Developer, Product Engineer.")
                elif winner == "Researcher":
                    st.markdown("<h2>The Deep Researcher</h2>", unsafe_allow_html=True)
                    st.write("You demand mathematical rigor. You aren't satisfied with a model just 'working'; you need to understand the fundamental algorithms driving it.")
                    st.write("**• Core Strength:** Algorithmic optimization and academic rigor.")
                    st.write("**• Blind Spot:** Academic perfectionism delaying real-world deployment.")
                    st.write("**• Ideal Role:** Core AI/ML Researcher, Algorithm Engineer.")
                
                st.divider()
                st.markdown("<p style='font-size: 14px; color: #a1a1aa; margin-bottom: 5px;'>Recovery Protocol Signature:</p>", unsafe_allow_html=True)
                st.markdown(f"<p class='accent-text'>→ Primary Directive: {winner}</p>", unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

            st.image("images/stage_clear_castle.png", use_container_width=True, caption="[ Confirmed: Destination // Apple Foundation Program ]")
            st.write("")
            if st.button("RESTART DIAGNOSTIC", type="primary"):
                st.session_state.stage = 0
                st.session_state.scores = {"Tactical": 0, "Architect": 0, "Catalyst": 0, "Visionary": 0, "Researcher": 0}
                st.rerun()

if __name__ == "__main__":
    run_app()