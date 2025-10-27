
import streamlit as st
import uuid
from datetime import datetime
from windchill_api import fetch_windchill_data

st.title("AI Agent for Sustaining Request Management")

query = st.text_area("Enter your sustaining query")

if st.button("Submit"):
    # Categorize query
    if "engineering change" in query.lower():
        category = "ECR"
    elif "product change" in query.lower():
        category = "PCN"
    elif "defect" in query.lower():
        category = "Quality"
    else:
        category = "General"

    # Generate request ID
    request_id = str(uuid.uuid4())[:8]

    # Simulate stakeholder lookup
    stakeholders = fetch_windchill_data(category)

    # Display result
    st.success("Query submitted successfully!")
    st.json({
        "id": request_id,
        "query": query,
        "category": category,
        "GPL": stakeholders["stakeholders"][0],
        "Contact": f"{stakeholders['stakeholders'][0].lower().replace(' ', '')}@example.com",
        "timestamp": str(datetime.now())
    })
