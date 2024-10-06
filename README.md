# Twitter-AI-Bot

# Twitter AI Assistant

A Python-based Twitter bot that generates professional-sounding tweets by summarizing content from a provided website. The bot leverages the OpenAI API for text generation and image creation, and tweets the results on Twitter.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Contributing](#contributing)

## Features
- Summarizes content from a given website in 10 words or less.
- Generates an image based on the summary using OpenAI's DALL-E model.
- Tweets the summary and image on Twitter automatically.
- Error handling and debugging capabilities built-in.

## Technologies Used
- **Python**: Programming language used for the application.
- **Flask**: Framework for building the web API.
- **OpenAI API**: For generating text and images.
- **Tweepy**: Library for interacting with the Twitter API.
- **Requests**: For making HTTP requests to download images.
- **Dotenv**: For managing environment variables.

## Setup

### Prerequisites
- Python 3.x installed on your machine.
- An OpenAI API key.
- Twitter Developer Account and API keys.

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vinitvora28/twitter-ai-assistant.git
   cd twitter-ai-assistant

2. **Set up environment variables**:
   ```
   Create a .env file in the root of the project and add your API keys:
   OPENAI_API_KEY=your_openai_api_key
   API_KEY=your_twitter_api_key
   API_SECRET_KEY=your_twitter_api_secret_key
   ACCESS_TOKEN=your_twitter_access_token
   ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

### Usage

1. **Run the Flask application**:
```
   python app.py
```
2. **Trigger the Tweet Generation**:
 ```
   Open your web browser and navigate to the following URL, replacing your_service with the service you want to summarize: http://127.0.0.1:5000/tweets?service=your_service
```
3. **The bot will summarize the website content, generate an image, and post the tweet automatically.**

### EndPoints**:
```
   GET /tweets
```
1. **Parameters**:
```
   service: A string representing the service you want to summarize (e.g., amazon, example).
```
2. **Response**:
```
   Sends a tweet with the summary and the generated image.
```

### Contributing**:

1. **Contributions are welcome! Please follow these steps**:
```
   Fork the repository.
   Create a new branch (git checkout -b feature-YourFeature).
   Make your changes and commit them (git commit -m 'Add some feature').
   Push to the branch (git push origin feature-YourFeature).
   Create a new Pull Request.
```
### Notes for Customization:
- Update the API key placeholders with actual values or instructions for obtaining them.
- Adjust any section according to your project’s specific details.
