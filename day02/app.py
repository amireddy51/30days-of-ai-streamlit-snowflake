import streamlit as st
from snowflake.snowpark import Session

st.title("🤖 Day 2: Hello, Cortex! (Local - SQL)")

session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

model = "claude-3-5-sonnet"
prompt = st.text_area("Enter your prompt:", "Explain Snowflake Cortex in 2 lines")

if st.button("Generate Response"):
    q = f"""
    SELECT SNOWFLAKE.CORTEX.COMPLETE(
      '{model}',
      $$ {prompt} $$
    ) AS response;
    """
    response = session.sql(q).collect()[0][0]
    st.subheader("Response")
    st.write(response)

