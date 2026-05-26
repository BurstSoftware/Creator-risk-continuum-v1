import streamlit as st

st.set_page_config(
    page_title="Creator Risk Continuum",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title("🧠 Creator Risk Continuum")
st.markdown("### How vulnerable is your content to **AI disruption**? — Updated with Proof & Demonstration Strategies")

# Sidebar
with st.sidebar:
    st.header("The Framework")
    st.markdown("""
    Creators exist on a **continuum** based on consumer risk/stakes:

    **Low Risk** → Pure Entertainment (self-contained)  
    **Medium Risk** → Low-stakes Education/Tutorials  
    **High Risk** → Financial, Business, High-Stakes Advice
    """)
    
    st.divider()
    st.markdown("""
    ### New Key Insight: **Proof Wins**
    - AI can easily replicate claims.
    - **Real-world proof + live demonstration** is extremely hard for AI to fake (for now).
    - Credibility compounds: subscribers, revenue, exits, documented results.
    - People follow and act on advice from those who have **done it**.
    """)

# Continuum Visualization
st.markdown("### Risk Continuum")
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.success("**LOW RISK**\n\nEntertainers\nMemes, Comedy, Clips")
with col2:
    st.warning("**MEDIUM RISK**\n\nEducators\nTutorials, Fitness, Beauty, Relationships")
with col3:
    st.error("**HIGH RISK**\n\nBusiness / Financial Advisors\nHigh-Stakes Decisions")

st.markdown("""
<div style="height: 30px; background: linear-gradient(to right, #22c55e, #eab308, #ef4444); 
border-radius: 15px; margin: 10px 0; position: relative;">
    <div style="position: absolute; left: 10%; top: -35px; font-weight: bold; color: #4ade80;">Entertainers</div>
    <div style="position: absolute; left: 50%; top: -35px; font-weight: bold; color: #facc15;">Educators</div>
    <div style="position: absolute; left: 85%; top: -35px; font-weight: bold; color: #f87171;">High-Stakes</div>
</div>
""", unsafe_allow_html=True)

# Input Section
st.divider()
st.subheader("Analyze Your Content")

col_a, col_b = st.columns(2)

with col_a:
    content_type = st.selectbox(
        "What kind of content do you primarily create?",
        options=[
            "Entertainment (memes, comedy, viral clips)",
            "Educational / Tutorials (hair, makeup, fitness, cooking, relationships)",
            "Business / Financial / Investing advice",
            "High-stakes B2B / Professional advice",
            "Mixed (entertainment + education + advice)",
            "Other"
        ]
    )

with col_b:
    outcome = st.selectbox(
        "What is the main thing you want the viewer to do?",
        options=[
            "Just laugh / be entertained",
            "Try a low-stakes action (recipe, workout, tutorial)",
            "Apply business or financial advice",
            "Make high-stakes decisions (invest, hire, strategy)",
            "Follow professional/high-risk recommendations"
        ]
    )

description = st.text_area(
    "Describe your typical content (1-2 sentences):",
    placeholder="I give business advice on scaling sales teams and building companies...",
    height=100
)

credibility = st.slider(
    "How strong is your current real-world proof? (0 = none, 10 = proven exits, large audience, documented results)",
    0, 10, 5
)

if st.button("🔍 Analyze AI Disruption Risk + Proof Strategy", type="primary", use_container_width=True):
    # Risk scoring
    risk_score = 0
    if "Entertainment" in content_type or "laugh" in outcome.lower():
        risk_score += 1
    elif "Educational" in content_type or "low-stakes" in outcome.lower():
        risk_score += 4
    elif "Business" in content_type or "Financial" in content_type or "high-stakes" in outcome.lower():
        risk_score += 8
    else:
        risk_score += 5
    
    if "laugh" in outcome.lower():
        risk_score = 2
    elif "high-stakes" in outcome.lower() or "financial" in outcome.lower() or "business" in outcome.lower():
        risk_score += 3  # higher if high stakes
    
    # Adjust with credibility
    effective_risk = max(1, risk_score - (credibility // 2))
    
    if effective_risk <= 4:
        risk_level = "LOW"
        color = "🟢"
        ai_disruption = "Very High"
        explanation = "Self-contained entertainment or low-stakes content. AI can replicate this easily."
    elif effective_risk <= 7:
        risk_level = "MEDIUM"
        color = "🟡"
        ai_disruption = "High"
        explanation = "Low-to-medium stakes education. AI avatars work well unless you show strong personal proof."
    else:
        risk_level = "HIGH"
        color = "🔴"
        ai_disruption = "Lower (with strong proof)"
        explanation = "High-stakes / business advice. **Proof and demonstration are your biggest moat** against AI."

    st.divider()
    st.subheader(f"{color} Your AI Disruption Risk: **{risk_level}**")
    st.metric("AI Replacement Potential", ai_disruption, delta=f"Credibility Score: {credibility}/10")
    
    st.info(explanation)
    
    if description:
        st.markdown(f"**Your content:** {description}")

    # Proof-Focused Recommendations
    st.success("### Proof & Demonstration Strategies (Your AI Moat)")
    
    if risk_level in ["HIGH", "MEDIUM"]:
        st.markdown("""
        **High-Impact Tactics to Build Proof at Scale:**
        - Document real business activities (meetings, calls, decisions) instead of scripting content.
        - Transcribe meetings → extract key moments → turn into content.
        - Engineer proof into your operations (customer audits, case studies, live results).
        - Run sweepstakes / customer spotlights → film real outcomes.
        - Offer free/paid audits or implementations and document everything publicly.
        - Capture live Q&A, events, and customer interactions.
        - Share third-party validation (revenue, exits, testimonials) + real-time demonstration.
        """)
    else:
        st.markdown("Focus on personality and speed. Still document your process to build long-term trust.")

    # General Tips
    st.divider()
    st.markdown("### Actionable Tips to Stay Ahead of AI")
    tips = [
        "Capture content from what you're already doing (don't create extra)",
        "Prioritize live demonstration over polished scripts",
        "Build a 'proof machine' into your business operations",
        "Document customer results in real time",
        "Combine third-party proof (numbers) with live expertise",
        "For high-risk content: credibility compounds — real results win"
    ]
    for tip in tips:
        st.markdown(f"• {tip}")

st.caption("Updated with strategies from Alex Hormozi-style creator framework • Built with Streamlit")
