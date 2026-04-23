import streamlit as st

def apply_custom_styles():
    st.markdown("""
        <style>
        /* Import Premium Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

        :root {
            --primary-gradient: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%);
            --secondary-gradient: linear-gradient(135deg, #667EEA 0%, #764BA2 100%);
            --ai-bubble-gradient: linear-gradient(135deg, rgba(79, 172, 254, 0.2) 0%, rgba(0, 242, 254, 0.1) 100%);
            --glass-bg: rgba(15, 23, 42, 0.7);
            --glass-border: rgba(255, 255, 255, 0.08);
            --text-main: #F1F5F9;
            --text-dim: #94A3B8;
            --neon-blue: #38BDF8;
        }

        /* Base Styles */
        .stApp {
            background: radial-gradient(circle at 0% 0%, rgba(56, 189, 248, 0.05) 0%, transparent 25%),
                        radial-gradient(circle at 100% 100%, rgba(118, 75, 162, 0.05) 0%, transparent 25%),
                        #020617;
            font-family: 'Plus Jakarta Sans', sans-serif;
            color: var(--text-main);
        }

        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: rgba(2, 6, 23, 0.8) !important;
            backdrop-filter: blur(20px);
            border-right: 1px solid var(--glass-border);
        }

        /* Main Title */
        .main-title {
            font-size: 3.5rem;
            font-weight: 800;
            letter-spacing: -0.02em;
            background: linear-gradient(to right, #F8FAFC, #94A3B8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            animation: fadeInDown 0.8s ease-out;
        }

        .sub-title {
            color: var(--text-dim);
            font-size: 1.1rem;
            margin-bottom: 3rem;
            animation: fadeIn 1.2s ease-out;
        }

        /* Stat Cards */
        .stat-card-container {
            background: var(--glass-bg);
            border: 1px solid var(--glass-border);
            border-radius: 24px;
            padding: 24px;
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }

        .stat-card-container:hover {
            transform: translateY(-8px);
            border-color: var(--neon-blue);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), 
                        0 0 20px rgba(56, 189, 248, 0.1);
        }

        .stat-card-container::after {
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, transparent 0%, rgba(255, 255, 255, 0.03) 100%);
            pointer-events: none;
        }

        .stat-value {
            font-size: 2.2rem;
            font-weight: 700;
            color: #FFFFFF;
            margin: 0;
            line-height: 1.2;
        }

        .stat-label {
            font-size: 0.85rem;
            font-weight: 600;
            color: var(--text-dim);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 4px;
        }

        /* Chat Interface */
        .chat-container {
            margin-top: 2rem;
        }

        .user-bubble {
            background: rgba(30, 41, 59, 0.5);
            border: 1px solid var(--glass-border);
            padding: 1.2rem;
            border-radius: 20px 20px 4px 20px;
            margin: 1.5rem 0 1.5rem 2rem;
            color: var(--text-main);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            position: relative;
        }

        .ai-bubble {
            background: var(--ai-bubble-gradient);
            border: 1px solid rgba(56, 189, 248, 0.2);
            padding: 1.5rem;
            border-radius: 20px 20px 20px 4px;
            margin: 1.5rem 2rem 1.5rem 0;
            color: var(--text-main);
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            backdrop-filter: blur(10px);
        }

        /* Animations */
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-20px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        /* Buttons & Inputs */
        .stButton>button {
            border-radius: 12px !important;
            background: var(--primary-gradient) !important;
            color: white !important;
            border: none !important;
            font-weight: 600 !important;
            padding: 0.6rem 1.5rem !important;
            transition: all 0.3s ease !important;
        }

        .stButton>button:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 20px rgba(79, 172, 254, 0.4) !important;
        }

        /* Quick Action Chips */
        .quick-action-btn {
            display: inline-flex;
            align-items: center;
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid var(--glass-border);
            color: var(--text-dim);
            padding: 8px 16px;
            border-radius: 100px;
            font-size: 0.9rem;
            cursor: pointer;
            transition: all 0.2s;
            margin-right: 8px;
            margin-bottom: 8px;
        }

        .quick-action-btn:hover {
            background: rgba(255, 255, 255, 0.08);
            color: var(--text-main);
            border-color: var(--neon-blue);
        }

        /* Hide Streamlit Header/Footer */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}

        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: transparent;
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(255, 255, 255, 0.1);
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

def stat_card(label, value, icon=""):
    st.markdown(f"""
        <div class="stat-card-container">
            <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                <div>
                    <p class="stat-label">{label}</p>
                    <p class="stat-value">{value}</p>
                </div>
                <div style="font-size: 1.5rem; opacity: 0.5;">{icon}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
