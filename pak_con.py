import pandas as pd
import streamlit as st
import os

CSV_FILE = "data.csv"
st.title("Ideas to Rebuild Pakistan 🇵🇰")
st.markdown("""
**Students!**  
Share your thoughts, your dreams, and your ideas 💡 on how we can make Pakistan a better place.  
Education, economy, unity, environment.**No idea is too small!**
""")


# Ensure the CSV file exists
if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["User_Name", "Institute_Name", "Topic"])
    df.to_csv(CSV_FILE, index=False)



# Input fields
username = st.text_input("Write down name here:")
institute_name = st.text_input("Write down Institute name here:")
topic = st.text_input("Write down Something you want to change in Pakistan:")

# Button to submit input
if st.button("Submit Entry"):
    if username and institute_name and topic:
        new_data = pd.DataFrame([{
            "User_Name": username,
            "Institute_Name": institute_name,
            "Topic": topic
        }])
        new_data.to_csv(CSV_FILE, mode='a', header=False, index=False)
        st.success("Entry added and saved to CSV!")
    else:
        st.warning("Please fill out all fields.")
st.markdown("##### Muhammad Hamza")

# Developer section
with st.expander("Developer Work"):
    password_dev = st.text_input("Write down password here to check database:", type="password")
    if password_dev == 'hamza123qwe':
        data_df = pd.read_csv(CSV_FILE)
        st.dataframe(data_df)
    else:
        if password_dev:  # Only show warning if something is typed
            st.warning("Incorrect password!")
 
