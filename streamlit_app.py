import streamlit as st

st.write('Kalpana App')
#Find the greatest  of 3 numbers
a= st.number_input(label='First Number', step=1)
b= st.number_input(label='Second Number',step=1)
c= st.number_input(label='Third Number',step=1)
array = [a,b,c]
array.sort(reverse=True)
greatest_num = array[0]
st.write('The Greatest Number is ',greatest_num)

