

import numpy as np
import openpyxl
import json
import pandas as pd
import streamlit as st

st.title("5G Quality Check") 
st.sidebar.subheader("품질데이터 업로드")
data_file = st.sidebar.file_uploader("Upload CSV",type=["csv","xlsx"])
if data_file is not None:
    file_details = {"filename":data_file.name, "filetype":data_file.type,"filesize":data_file.size}
    #st.write(file_details)
df = pd.read_csv(data_file)
     
option = st.sidebar.selectbox("시도",("","광주광역시","전라남도"))
if option == "":
    option2 = st.sidebar.selectbox("시군구",("",""))
elif option == "광주광역시":
    option2 = st.sidebar.selectbox("시군구",("","광산구","남구","동구","북구","서구"))
elif option == "전라남도":
    option2 = st.sidebar.selectbox("시군구",("","광양시","나주시","목포시","순천시","여수시")) 
if option2 == "":
    option3 = st.sidebar.selectbox("읍면동",("",""))
elif option2 == "광산구":
    option3 = st.sidebar.selectbox("읍면동",("","수완동","신가동","신창동","어룡동","우산동","운남동","첨단2동","하남동"))    
elif option2 == "남구":
    option3 = st.sidebar.selectbox("읍면동",("","방림1동","방림동","송암동","양림동","주월1동","효덕동"))     
elif option2 == "동구":
    option3 = st.sidebar.selectbox("읍면동",("","동명동","산수2동","서남동","지산2동","지원2동","충장동","학동","학운동"))     
elif option2 == "북구":
    option3 = st.sidebar.selectbox("읍면동",("","건국동","동림동","매곡동","신안동","양산동","오룡동","용봉동","운암1동","일곡동"))
elif option2 == "서구":
    option3 = st.sidebar.selectbox("읍면동",("","광천동","금호2동","상무1동","상무2동","치평동","풍암동","화정1동"))
elif option2 == "광양시":
    option3 = st.sidebar.selectbox("읍면동",("","광영동","금호동","중마동"))
elif option2 == "나주시":
    option3 = st.sidebar.selectbox("읍면동",("","빛가람동","성북동","송월동"))
elif option2 == "순천시":
    option3 = st.sidebar.selectbox("읍면동",("","덕연동","도사동","삼산동","왕조1동","조곡동"))
elif option2 == "여수시":
    option3 = st.sidebar.selectbox("읍면동",("","국동","대교동","문수동","삼일동","시전동","쌍봉동","여서동","여천동"))
elif option2 == "목포시":
    option3 = st.sidebar.selectbox("읍면동",("","목원동","부주동","상동","신흥동","옥암동","용해동","하당동"))

st.write(option,"  ",option2, "  ",option3)

df2 = df[df['시도']==option]
df3 = df2[ df2['시군구']==option2]
df4 = df3[ df3['읍면동']==option3]
if option =="":
    st.dataframe(df)    
elif option2 =="":
    st.dataframe(df2)
elif option3 =="":
    st.dataframe(df3) 
else :     
    date=df4['일자']
    date2=date.values.tolist()
    date2=set(date2)
    date3=st.sidebar.selectbox("측정일자",date2)
    df4t1=df4[df4['일자']==date3]
    if date3 =="":
        st.dataframe(df4)
    else:
        st.dataframe(df4t1)
