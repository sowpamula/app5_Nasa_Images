import requests
import streamlit as st


api_key = "fUaqzpC6bmPwmKxKazB68LhxTaqlxjFfx6dgeOxx"
url = "https://api.nasa.gov/planetary/apod?" \
    f"api_key={api_key}"

response1 = requests.get(url)
data = response1.json()

title = data["title"]
image_url = data["url"]
explanation = data["explanation"]

image_filepath = "img.png"
response2 = requests.get(image_url)
with open(image_filepath, 'wb') as file:
    file.write(response2.content)


st.title(title)
st.image(image_filepath)
st.write(explanation)

