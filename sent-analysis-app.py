import numpy as np
import pandas as pd 
import pickle
import streamlit as st
import base64
from PIL import Image
#df = pd.read_csv('/content/drive/My Drive/amazonreviews.tsv',sep='\t')
model = pickle.load(open('sentiment_analysis_model.p','rb'))

st.set_page_config(page_title="Sentiment Analysis Web App",page_icon="",layout="centered",initial_sidebar_state="expanded",)
st.title('Sentiment Analysis Model')

st.markdown("""
<style>
body {
    color: #ff0000;
    background-color: #001f;
    etc. 
}
</style>
    """, unsafe_allow_html=True)



st.subheader('Enter Text')
message = st.text_area("","Type Here ...")
if st.button('PREDICT'):
  disp=""
  a = model.predict([message])[0]
  if(a == 'pos'):
        disp = "Positive Review!"
  else:
        disp = "Negative Review!"
  st.header(f"**{a}**")
 
  
  #q = model.predict_proba([message])
  
  #for index, item in enumerate(df['review']):
      #st.write(f'{item} : {q[0][index]*100}%')

st.sidebar.subheader("About App")

st.sidebar.info("Click on the 'Predict' button to check whether the entered text is 'Positive' or 'Negative' ")
st.sidebar.info("Don't forget to rate this app")



feedback = st.sidebar.slider('How much would you rate this app?',min_value=0,max_value=10,step=1)

if feedback:
  st.header("Thank you for rating the app!")
