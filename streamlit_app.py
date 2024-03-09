import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color="black", back_color="white")
    return qr_img

def main():
    st.title("Webpage QR Code Generator")
    st.write("Enter the webpage link below to generate a QR code.")

    url = st.text_input("Enter webpage link:")
    if st.button("Generate QR Code"):
        if url:
            qr_img = generate_qr_code(url)

            # Convert PIL image to bytes
            img_byte_array = io.BytesIO()
            qr_img.save(img_byte_array, format='PNG')
            img_byte_array = img_byte_array.getvalue()

            # Display the QR code image
            st.image(img_byte_array, caption='Generated QR Code', use_column_width=True)
        else:
            st.warning("Please enter a webpage link.")

if __name__ == "__main__":
    main()
