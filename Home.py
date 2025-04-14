import streamlit as st
import pandas
import streamlit as st


st.set_page_config(page_title="ITC-Limited",
                   layout="wide",
                   page_icon="images/itc.jpg")

st.title("The Best Company")
content = """dhjjjjjjjjjjjjsfdjksfkjsdfjsdsdfkjsdkjhdfskjfsdnsdfsdfhdsjhdjsdh
dsfjsdlsdhlfsdldslkfsdlknf.lsdhflksdl/ksdfn.,dsn,.dfns,.sfmn,.sfdnsd.,
dslfnsd,sdn,dfsn,.fnsd,.fmnsd,.mnfsd,mnfsd,mnds,nmsd,mnsd,sm.n,sns,mnd,mdns,smdn,fsdmnsd,.nmds.
dslfslsdlsdjhklfsdkhlfdshldslfsdldsflsdfljsdlfjsdfndsdfndlfsknfldnkslfdnldsknflsknldn
sdfnsdlknlkdfn"""
st.info(content)
st.header("Out Team")

col1,empty_col1, col2, empty_col2, col3 = st.columns([2,1,2,1,2])

df = pandas.read_csv("data.csv", sep=",")
with col1:
    for index, row in df[:4].iterrows():
        st.write(f"Name- {row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write("Role- " + row["role"])
        st.image("images/" + row["image"])
        st.markdown("__________________")

with col2:
    for index, row in df[4:8].iterrows():
        st.write(f"Name- {row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write("Role- " + row["role"])
        st.image("images/" + row["image"])
        st.write("_____________________")

with col3:
    for index, row in df[8:12].iterrows():
        st.write(f"Name- {row['first name'].capitalize()} {row['last name'].capitalize()}")
        st.write("Role- " + row["role"])
        st.image("images/" + row["image"])
        st.write("_____________________")





