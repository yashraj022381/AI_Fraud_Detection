import os
import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.tools import tool
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

load_dotenv()

# Initialize Groq LLM (Llama 3.1 70B for efficiency, low hallucinations)
llm = ChatMistralAI(model="Mistral-large-latest", temperature=0.3)

# Tools for Financial and Legal Tasks (MSME & Consumer)
@tool
def generate_invoice(amount: float, description: str, gst_rate: float = 0.18) -> str:
    """Generate invoice with GST for MSMEs or consumers."""
    subtotal = amount
    gst = subtotal * gst_rate
    total = subtotal + gst
    return f"Invoice:\nDescription: {description}\nSubtotal: ₹{subtotal}\nGST ({gst_rate*100}%): ₹{gst}\nTotal: ₹{total}"

@tool
def budget_advice(revenue_or_income: float, expenses: float) -> str:
    """Budget advice for MSMEs or personal finances."""
    savings = revenue_or_income - expenses
    if savings > 0:
        return f"Surplus: ₹{savings}. Save 20% for emergencies, invest 30%."
    else:
        return f"Deficit: ₹{-savings}. Reduce non-essentials by 15%."

@tool
def review_contract(contract_text: str) -> str:
    """Review contract for risks (e.g., loans, rentals)."""
    risks = []
    if "penalty" in contract_text.lower():
        risks.append("High penalties—negotiate limits per RBI.")
    if "interest" in contract_text.lower():
        risks.append("Verify interest vs. market rates (e.g., 8-15% for personal loans).")
    suggestions = "Include arbitration for disputes; consult lawyer for complex cases."
    return f"Risks: {', '.join(risks) or 'Low'}\nSuggestions: {suggestions}"

@tool
def personal_loan_advice(principal: float, interest_rate: float, tenure_months: int) -> str:
    """Advice on personal loans for consumers."""
    monthly_rate = interest_rate / 12 / 100
    emi = principal * monthly_rate * (1 + monthly_rate)**tenure_months / ((1 + monthly_rate)**tenure_months - 1)
    return f"EMI: ₹{emi:.2f}. Total interest: ₹{(emi * tenure_months) - principal:.2f}. Ensure rate <15% per RBI guidelines."

# System Prompt (Handles MSME/Consumer, Multilingual, Accurate)
system_prompt = """
You are FinLegal AI, assisting MSMEs and consumers in India with finance and legal aid.
Respond in user's preferred language (Hindi/English).
Use tools for facts; verify to avoid errors.
Financial: Budgets, invoices, loans.
Legal: Contract reviews, simple advice (not legal substitute).
If complex, recommend professionals.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# Agent Setup
tools = [generate_invoice, budget_advice, review_contract, personal_loan_advice]
agent = create_tool_calling_agent(llm, tools, prompt)
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
agent_executor = AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=True)

# Streamlit UI
st.title("FinLegal AI: Finance & Legal Aid for MSMEs/Consumers")
st.write("Query examples: 'Generate invoice for ₹10000 services' or 'Review this rental contract: [text]' or 'Advice on ₹50000 loan at 12% for 24 months'")

language = st.selectbox("Language", ["English", "Hindi"])
user_input = st.text_area("Your Query:")
if st.button("Submit"):
    if user_input:
        with st.spinner("Analyzing..."):
            response = agent_executor.invoke({"input": f"{user_input} in {language}"})
        st.success(response['output'])
    else:
        st.warning("Enter a query.")
