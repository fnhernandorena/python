#Requieres stramlit, pyshorteners and qrcode

import streamlit as st
import pyshorteners as pyst
import qrcode

filename = 'qr_codes/qr_code.png'

#shorter url function
def shorter_url(url): 
    s = pyst.Shortener()
    shorter_url = s.tinyurl.short(url)
    return shorter_url

#Create QR codes Function
def generate_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color='black', black_color='white')
    img.save(filename)

#web page create
st.set_page_config(page_title='Python Tools', layout='centered')
st.title('Python Tools')

#urlshorter
st.subheader('URL Shorter')
url = st.text_input('Enter the URL for short this')
if st.button('Generate the new URL'):
    st.write('URL shorted: ', shorter_url(url))

#qrcode generator
st.subheader('QR Code Generator')
url = st.text_input('Enter the URL for QR code')
if st.button('Generate the QR Code'):
    generate_qr_code(url, filename)
    st.image(filename, use_column_width='true')
    with open(filename, 'rb') as f:
         image_data = f.read()
    download = st.download_button(label='Download QR', data=image_data, file_name='qr_generated.png')

