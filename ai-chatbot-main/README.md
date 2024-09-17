# AI Chat Bot

## Description

This is a simple AI chat bot that can be used to answer questions. The chatbot privides users with a choice of using multiple models for text generation like ```gpt-3.5-turbo-instruct```, ```davinci```, ```text-curie-001``` and ```babbage```.

[product-screenshot]: images/product.png

[![Product Name Screen Shot][product-screenshot]]()

## Getting Started

To get a local copy up and running follow these simple example steps.


### Installation to run this project locally

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Fork this repo- [fork](https://github.com/prayashdash1729/ai-chatbot/fork)
2. Clone the forked repo
    ```sh
   git clone https://github.com/your_username_/forked-reo-name.git
   ```
3. Go the preoject directory
    ```sh
    cd path/to/cloned/repo/
    ```
4. Make a new virtual environment
    ```sh
    conda create -p venv python==3.9 -y
    conda activate venv/
    ```
4. Install requirements
    ```sh
    pip install -r requirements.txt
    ```
    and
    ```sh
    pip install -r requirements2.txt
    ```
5. Setup your OpenAI api keys in ```.env``` file
    ```sh
    OPENAI_API_KEY = "your-api-key"
    ```
6. Run the dashboard
   ```sh
   streamlit run app.py
   ```


