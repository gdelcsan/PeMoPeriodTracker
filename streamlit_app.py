import streamlit as st

# Define the pages
main_page = st.Page("main_page.py", title="Main Page", icon="🎈")
page_2 = st.Page("page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("page_3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()

# Main page content
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

#page 2
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

#page 3
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")
