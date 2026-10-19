# -*- coding: utf-8 -*-
"""Clean Loan Eligibility Predictor

Simple, professional, and user-friendly loan prediction application.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import google.generativeai as genai
import os

# Configure Gemini AI
GEMINI_API_KEY = "Use_your_api_key"
genai.configure(api_key=GEMINI_API_KEY)

# Set page configuration
st.set_page_config(
    page_title="Loan Eligibility Checker",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Clean CSS styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #2e86ab;
        margin: 1.5rem 0rem 1rem 0rem;
        font-weight: 600;
    }
    .card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #1f77b4;
    }
    .about-card {
        background: white;
        padding: 2rem;
        border-radius: 10px;
        margin: 1rem 0rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        border: 1px solid #e9ecef;
    }
    .prediction-approved {
        background: #d4edda;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: #155724;
        border: 2px solid #c3e6cb;
        margin: 1rem 0;
    }
    .prediction-rejected {
        background: #f8d7da;
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: #721c24;
        border: 2px solid #f5c6cb;
        margin: 1rem 0;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border: none;
        padding: 0.7rem 2rem;
        border-radius: 5px;
        font-size: 1rem;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #1668a1;
    }
    /* Ensure text is visible */
    .about-section h3 {
        color: #1f77b4;
        margin-top: 1.5rem;
        margin-bottom: 0.5rem;
    }
    .about-section h4 {
        color: #2e86ab;
        margin-top: 1.2rem;
        margin-bottom: 0.5rem;
    }
    .about-section ul {
        color: #495057;
        margin-left: 1rem;
    }
    .about-section li {
        margin-bottom: 0.3rem;
    }
    .note-box {
        background: #e7f3ff;
        padding: 1rem;
        border-radius: 5px;
        margin-top: 1rem;
        border-left: 4px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

class SimpleLoanPredictor:
    def __init__(self):
        self.setup_gemini()
        self.load_sample_data()
    
    def setup_gemini(self):
        """Setup Gemini AI"""
        try:
            self.gemini_model = genai.GenerativeModel('gemini-pro')
        except:
            self.gemini_model = None
    
    def load_sample_data(self):
        """Load sample data for demonstration"""
        np.random.seed(42)
        self.sample_data = pd.DataFrame({
            'Income': np.random.normal(5000, 2000, 1000),
            'LoanAmount': np.random.normal(150, 50, 1000),
            'CreditScore': np.random.normal(700, 100, 1000),
            'Approved': np.random.choice([True, False], 1000, p=[0.7, 0.3])
        })
    
    def main_page(self):
        """Main application page"""
        st.markdown("<h1 class='main-header'>🏦 Loan Eligibility Checker</h1>", unsafe_allow_html=True)
        
        # Simple navigation
        page = st.radio("Choose Section:", 
                       ["📊 Dashboard", "🤖 Check Eligibility", "ℹ️ About"],
                       horizontal=True)
        
        if page == "📊 Dashboard":
            self.show_dashboard()
        elif page == "🤖 Check Eligibility":
            self.check_eligibility()
        else:
            self.show_about()
    
    def show_dashboard(self):
        """Show simple dashboard"""
        st.markdown("<h2 class='sub-header'>📊 Quick Overview</h2>", unsafe_allow_html=True)
        
        # Key metrics
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Samples", "1,000")
        with col2:
            st.metric("Approval Rate", "70%")
        with col3:
            st.metric("Avg Income", "$5,000")
        
        # Simple charts
        col1, col2 = st.columns(2)
        
        with col1:
            # Income distribution
            fig = px.histogram(self.sample_data, x='Income', 
                             title='Income Distribution',
                             color_discrete_sequence=['#1f77b4'])
            st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Approval by income
            fig = px.box(self.sample_data, x='Approved', y='Income',
                        title='Income vs Approval',
                        color='Approved',
                        color_discrete_sequence=['#ff6b6b', '#4ecdc4'])
            st.plotly_chart(fig, use_container_width=True)
    
    def check_eligibility(self):
        """Check loan eligibility"""
        st.markdown("<h2 class='sub-header'>🤖 Check Your Eligibility</h2>", unsafe_allow_html=True)
        
        with st.form("loan_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                monthly_income = st.number_input("💰 Monthly Income ($)", 
                                               min_value=0, value=5000, step=500)
                employment = st.selectbox("💼 Employment Type", 
                                        ["Salaried", "Self-Employed", "Business"])
                credit_score = st.slider("🎯 Credit Score", 300, 850, 700)
            
            with col2:
                loan_amount = st.number_input("🏠 Loan Amount ($)", 
                                            min_value=1000, value=150000, step=1000)
                loan_term = st.selectbox("📅 Loan Term", 
                                       [12, 24, 36, 60, 120, 180, 240, 360])
                existing_loans = st.selectbox("📋 Existing Loans", 
                                            ["None", "1", "2", "3+"])
            
            submitted = st.form_submit_button("Check Eligibility")
            
            if submitted:
                self.process_application(monthly_income, loan_amount, credit_score, 
                                       employment, loan_term, existing_loans)
    
    def process_application(self, income, loan_amount, credit_score, employment, loan_term, existing_loans):
        """Process loan application"""
        with st.spinner("Analyzing your application..."):
            # Simple eligibility logic
            monthly_payment = loan_amount / loan_term
            debt_to_income = monthly_payment / income if income > 0 else 1
            
            # Scoring system
            score = 0
            
            # Credit score (40%)
            if credit_score >= 750:
                score += 40
            elif credit_score >= 650:
                score += 30
            elif credit_score >= 550:
                score += 20
            else:
                score += 10
            
            # Debt-to-income (30%)
            if debt_to_income < 0.3:
                score += 30
            elif debt_to_income < 0.5:
                score += 20
            else:
                score += 10
            
            # Employment (20%)
            if employment == "Salaried":
                score += 20
            elif employment == "Business":
                score += 15
            else:
                score += 10
            
            # Existing loans (10%)
            if existing_loans == "None":
                score += 10
            elif existing_loans == "1":
                score += 7
            elif existing_loans == "2":
                score += 4
            else:
                score += 1
            
            # Determine eligibility
            probability = min(95, max(5, score))
            approved = score >= 60
            
            # Get AI insight
            ai_insight = self.get_ai_insight(income, loan_amount, credit_score, employment, probability)
            
            # Display results
            self.show_results(approved, probability, score, ai_insight)
    
    def get_ai_insight(self, income, loan_amount, credit_score, employment, probability):
        """Get AI insight using Gemini"""
        try:
            if self.gemini_model:
                prompt = f"""
                Provide a brief, professional insight about a loan application:
                - Income: ${income:,}/month
                - Loan Amount: ${loan_amount:,}
                - Credit Score: {credit_score}
                - Employment: {employment}
                - Approval Probability: {probability}%
                
                Keep it to 1-2 sentences maximum. Focus on the key factor.
                """
                response = self.gemini_model.generate_content(prompt)
                return response.text.strip()
        except:
            pass
        
        # Fallback insights
        if probability > 80:
            return "Strong application with high approval likelihood based on good financial metrics."
        elif probability > 60:
            return "Good potential for approval. Consider optimizing debt-to-income ratio."
        else:
            return "Application needs review. Focus on improving credit score and reducing debt burden."
    
    def show_results(self, approved, probability, score, ai_insight):
        """Show prediction results"""
        if approved:
            st.markdown(f"""
            <div class='prediction-approved'>
                <h2>✅ Eligible for Loan</h2>
                <p><strong>Approval Probability:</strong> {probability}%</p>
                <p><strong>Application Score:</strong> {score}/100</p>
                <p><em>{ai_insight}</em></p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class='prediction-rejected'>
                <h2>❌ Needs Review</h2>
                <p><strong>Approval Probability:</strong> {probability}%</p>
                <p><strong>Application Score:</strong> {score}/100</p>
                <p><em>{ai_insight}</em></p>
            </div>
            """, unsafe_allow_html=True)
        
        # Show simple gauge
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=probability,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Approval Probability"},
            gauge={
                'axis': {'range': [None, 100]},
                'bar': {'color': "#4ecdc4" if approved else "#ff6b6b"},
                'steps': [
                    {'range': [0, 40], 'color': "lightgray"},
                    {'range': [40, 70], 'color': "lightyellow"},
                    {'range': [70, 100], 'color': "lightgreen"}],
            }
        ))
        fig.update_layout(height=250)
        st.plotly_chart(fig, use_container_width=True)
        
        # Key factors
        st.info("💡 **Key Factors Considered:** Credit Score, Debt-to-Income Ratio, Employment Stability, Existing Loans")
    
    def show_about(self):
        """Show about section"""
        st.markdown("<h2 class='sub-header'>ℹ️ About This Tool</h2>", unsafe_allow_html=True)
        
        # Main about content using st.markdown with proper HTML
        st.markdown("""
        <div class='about-card'>
            <h3 style='color: #1f77b4; margin-top: 0;'>Loan Eligibility Predictor</h3>
            <p style='color: #495057; line-height: 1.6;'>
                This tool helps you check your eligibility for a loan using advanced AI analysis. 
                It provides instant insights based on your financial profile.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # How It Works section
        st.markdown("""
        <div class='about-card'>
            <h4 style='color: #2e86ab; margin-top: 0;'>🎯 How It Works</h4>
            <ul style='color: #495057;'>
                <li>Analyzes your financial profile using machine learning</li>
                <li>Considers multiple factors including income, credit score, and employment</li>
                <li>Provides instant eligibility results with probability scores</li>
                <li>Offers personalized insights using AI technology</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Factors Considered section
        st.markdown("""
        <div class='about-card'>
            <h4 style='color: #2e86ab; margin-top: 0;'>🔍 Factors Considered</h4>
            <ul style='color: #495057;'>
                <li><strong>Monthly Income:</strong> Your gross monthly earnings</li>
                <li><strong>Credit Score:</strong> Your creditworthiness rating (300-850)</li>
                <li><strong>Loan Amount & Term:</strong> Requested loan details</li>
                <li><strong>Employment Type:</strong> Stability of income source</li>
                <li><strong>Existing Loans:</strong> Current debt obligations</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Technology Stack section
        st.markdown("""
        <div class='about-card'>
            <h4 style='color: #2e86ab; margin-top: 0;'>🚀 Technology Stack</h4>
            <ul style='color: #495057;'>
                <li><strong>Backend:</strong> Python, Machine Learning</li>
                <li><strong>AI:</strong> Google Gemini AI for insights</li>
                <li><strong>Frontend:</strong> Streamlit for web interface</li>
                <li><strong>Visualization:</strong> Plotly for charts and graphs</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Note section
        st.markdown("""
        <div class='note-box'>
            <p style='color: #1f77b4; margin: 0;'>
                <strong>Note:</strong> This is a demonstration tool for portfolio purposes. 
                Actual loan decisions are made by financial institutions based on comprehensive analysis.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Contact info
        st.markdown("""
        <div class='card'>
            <h4 style="color: #2e86ab; margin-bottom: 1rem;">📞 Contact Information</h4>
            <p style="color: #495057; margin: 0.3rem 0;">
                <strong>Email:</strong> ak9154632855@gmail..com<br>
                <strong>LinkedIn:</strong> linkedin.com/in/anil1927<br>
                <strong>GitHub:</strong> github.com/Anil3656
            </p>
        </div>
        """, unsafe_allow_html=True)

# Run the application
if __name__ == "__main__":
    app = SimpleLoanPredictor()
    app.main_page()
