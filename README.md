# Bias Detection in Word Embeddings
<img width="1133" alt="Screen Shot 2024-05-31 at 3 21 23 PM" src="https://github.com/nimamot/bias_analysis/assets/64922998/1ddb2564-81e1-4508-9fac-9034c89aca62">

Bias in machine learning models is a critical issue, especially when these models are used in real-world applications affecting people's lives. Word embeddings, which are a common component in natural language processing (NLP), can inadvertently capture and propagate societal biases present in the training data. It is essential to identify and address these biases to create fair and equitable AI systems.

## Project Overview 🪄

In this project, we investigate biases in word embeddings using the `glove_wiki_vectors` model. Word embeddings are vector representations of words, and the relationships between these vectors can reveal underlying biases. For instance, if the word "doctor" (word 2) is strongly associated with "man" (word 1) in the embeddings, we can use this analogy to see which word is similarly associated with "woman" (word 3). This helps in identifying gender biases present in the embeddings.

## How it Works 🛠

The project includes a web application that allows users to input words and explore the biases in the relationships between them. Users can enter three words to form an analogy and the system will predict the word that completes the analogy based on the embeddings. For example, if the user inputs "man" (word 1), "doctor" (word 2), and "woman" (word 3), the application will predict the word that "woman" is associated with in the same way "doctor" is associated with "man".

## Technical Stack 👨🏽‍💻

- **Flask**: A lightweight web framework used for building the web application.
- **joblib**: A library used for loading the pre-trained word embedding model.
- **WTForms**: Used for form handling in Flask.
- **HTML/CSS**: Used for the frontend of the web application.

### Project Structure 💈

- **app.py**: The main Flask application file that handles routing, form handling, and model predictions.
- **bias.joblib**: The pre-trained word embedding model used for bias detection.
- **requirements.txt**: Lists the Python dependencies required for the project.
- **templates/**: Contains the HTML templates for the web pages.
  - **home.html**: The main page where users input words.
  - **prediction.html**: The results page displaying the predicted bias relationships.
- **static/**: Contains static files such as CSS.
  - **style.css**: The stylesheet for the web application.
- **Procfile**: Configuration file for deployment on platforms like Heroku.
- **runtime.txt**: Specifies the Python runtime version.


By exploring the biases present in word embeddings, we can gain insights into the societal biases captured by these models and work towards mitigating them. This project demonstrates the importance of bias detection and provides a tool for investigating biases in word embeddings using analogies.




# Results
<img width="555" alt="Screen Shot 2024-05-31 at 3 33 23 PM" src="https://github.com/nimamot/bias_analysis/assets/64922998/6c7ac3f9-b086-44a8-8ec7-ae66bbb6ab88">
