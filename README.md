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
- [License](#license)

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
   git clone https://github.com/yourusername/twitter-ai-assistant.git
   cd twitter-ai-assistant
