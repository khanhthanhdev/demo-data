import streamlit as st

st.title("World Population")

st.header("Top 10 most populous countries")
st.subheader("Dựa vào dữ liệu dân số các nước trên thế giới này chúng ta xác định được: Nước đông dân nhất thế giới: Trung Quốc. ")
st.image("population.png")
st.header("Top 10 largest area")
st.subheader("Dựa vào dữ liệu diện tích các nước trên thế giới này chúng ta xác định được: Nước có diện tích đất liền lớn nhất thế giới: Liên Bang Nga.")
st.image("largest_country.png")
st.header("World Share")
st.subheader("Dựa vào dữ liệu dân số các nước trên thế giới này chúng ta xác định được: Nước chiếm tỉ lệ dân số lớn nhất nhất thế giới: Trung Quốc.")
st.image("share.png")

st.header("You can dowload data and code blow")
st.download_button(
    label="Download data as CSV",
    data= "population.csv",
    file_name='population.csv',
    mime='text/csv',
)
st.download_button(
    label="Download code as ipynb",
    data= "population.ipynb",
    file_name='population.ipynb',
    mime='text/ipynb',
)
st.write("Using Google Colab [link](https://colab.research.google.com/drive/1eB3W94YgkvvjwWLb2J3SEZnEjnzof-iT?usp=sharing)")