# Day 01 — Connect to Snowflake

## Goal
Connect a Streamlit app to Snowflake using Snowpark and confirm connectivity by querying 
the Snowflake version.

## Output
- Successfully connected
- `SELECT CURRENT_VERSION()` displayed in the app

## Local Setup
1) Create `.streamlit/secrets.toml` (not committed)
2) Install deps:
```bash
pip install -r requirements.txt

