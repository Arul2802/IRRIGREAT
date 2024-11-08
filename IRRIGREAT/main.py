import streamlit as st

st.set_page_config(page_title="IRRIGREAT", page_icon=":seedling:", layout="wide")

from streamlit_option_menu import option_menu
import os
from dotenv import load_dotenv
load_dotenv()

import home, crop_pred, price_pred, trending, account, your, about, agribot, weather_pred


# Google Analytics script
st.markdown(
    f"""
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){{dataLayer.push(arguments);}}
        gtag('js', new Date());
        gtag('config', '{os.getenv('analytics_tag')}');
    </script>
    """,
    unsafe_allow_html=True
)
print(os.getenv('analytics_tag'))


class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Sidebar navigation
        with st.sidebar:
            app = option_menu(
                menu_title='IRRIGREAT',
                options=['Home', 'Account', 'Crop Recommendation', 'Price Prediction','Trending', 'Your Posts', 'About','Agri Bot','Weather Forecast'],
                icons=['house-fill', 'person-circle', 'trophy-fill', 'trophy-fill','chat-fill','person-circle','info-circle-fill','chat-text-fill','cloud'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Page navigation logic
        if app == "Home":
            home.app()
        elif app == "Account":
            account.app()
        elif app == 'Crop Recommendation':
            crop_pred.app()  # Calls crop_pred.py app
        elif app == 'Price Prediction':
            price_pred.app() 
        elif app == "Trending":
            trending.app()
        elif app == 'Your Posts':
            your.app()
        elif app == 'Agri Bot':
            agribot.app()
        elif app == 'Weather Forecast':
            weather_pred.app()
        elif app == 'About':
            about.app()

# Run the multi-app framework
if __name__ == '__main__':
    app = MultiApp()
    app.run()
