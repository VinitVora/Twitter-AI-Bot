import os
import openai
import tweepy
import requests
from flask import Flask, request
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Authenticate to OpenAI API
client = openai.OpenAI(api_key=os.environ['OPENAI_API_KEY'])

# Authenticate to Twitter API
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET_KEY")

# Set the text model
TEXT_MODEL = "gpt-3.5-turbo"

# Set the persona for the AI assistant
context = [{'role': 'system', 'content': "You are a friendly AI assistant that helps compose professional-sounding tweets for Twitter that often go viral based on a website I provide. You will provide a summary of the website in 10 words or less."}]

# Create Flask app
app = Flask(__name__)

# Helper functions
def get_summary(website, temperature=0):
    prompt = f"Please summarize this website: {website}"
    context.append({'role': 'user', 'content': prompt})
    
    try:
        response = client.chat.completions.create(model=TEXT_MODEL, messages=context, temperature=temperature)
        return response.choices[0].message.content
    except openai.APIError as e:
        print(e.http_status, e.error)
        return e.error

def generate_image(summary):
    try:
        response = client.images.generate(model="dall-e-3", prompt=summary, size="1024x1024", quality="standard", n=1)
        image_url = response.data[0].url
        return image_url
    except openai.APIError as e:
        print(e.http_status, e.error)
        return e.error

def download_image(imageURL):
    img_data = requests.get(imageURL).content
    with open('dalle_image.jpg', 'wb') as handler:
        handler.write(img_data)
    return "dalle_image.jpg"

def upload_image(image):
    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    media = api.media_upload(filename=image)
    return media

def send_tweet(summary, image):
    client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret,
                           access_token=access_token, access_token_secret=access_token_secret)
    
    media = upload_image(image)
    media_ids = [media.media_id]
    response = client.create_tweet(text=summary, media_ids=media_ids)
    print(f"https://twitter.com/user/status/{response.data['id']}")

# Define Flask route
@app.route('/tweets', methods=['GET'])
def index():
    args = request.args
    service = args.get('service')
    
    # Get summary of the website
    summary = get_summary(f"http://www.amazon.com/{service}")
    
    # Generate image using the summary
    image_url = generate_image(summary)
    image_name = download_image(image_url)
    
    # Tweet the image
    send_tweet(summary, image_name)
    
    return 'Tweet sent!'

# Run the app
if __name__ == '__main__':
    app.run(port=5000)
