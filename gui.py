import streamlit as st

if __name__ == '__main__':
    st.title("Zale's Mini Search Engine")
    uploaded_files = st.file_uploader("Choose files:", accept_multiple_files=True)
    # if uploaded_files is not None:
    #     st.write(uploaded_files)
    st.button("Load Engine")
