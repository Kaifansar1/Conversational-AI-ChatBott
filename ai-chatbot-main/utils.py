import base64
import streamlit as st

# Getting the image as base64 since direct paths is not working
@st.cache_data
def get_img_as_base64(file):
    with open(file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

class Image:
    def get_bg_img(self, file):
        return get_img_as_base64(file)

class PageStyle:
    def page_style(self, bg_img):
        # Setting the page style and making the bg image responsive
        page_style = f"""
        <style>
            [data-testid="stMarkdownContainer"] {{
                font-weight: bold;
            }}
            [data-testid="stAppViewContainer"] > .main {{
                background-image: url("data:image/png;base64,{bg_img}");
                background-size: cover;
                -webkit-background-size: cover;
                -moz-background-size: cover;
                -o-background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                # background-attachment: local;
            }}
            [data-testid="stHeader"] {{
                background: rgba(0,0,0,0);
            }}
            [data-testid="stToolbar"] {{
                right: 2rem;
            }}
            [data-testid="stVerticalBlock"]{{
                background-color: #fff;
                background-color: rgba(255,255,255,0.5);
                border-radius: 1.0rem;
                padding: 1.0rem;
            }}
            .st-ah {{
                width: 95%;
            }}
            # [data-testid="baseButton-secondary"]{{
            #     background-color: #0CBAFF;
            #     background-color: rgba(12,186,255,0.5);
            #     # border-radius: 1.0rem;
            #     # padding: 1.0rem;
            # }}
        </style>
        """
        return page_style