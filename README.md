# Simple Flask API with Frontend Calculator

This repository contains a simple Flask API that calculates the product of two numbers and a frontend application to interact with the API.

## Features

- Flask API for multiplying two numbers.
- A frontend interface with two input fields and a button to calculate the product.
- CORS support for cross-origin requests.

## How to Run

Follow these steps to run the Flask API and the frontend application:

### 1. Install Dependencies

You'll need Python and pip installed on your system. You can download Python from [Python's official website](https://www.python.org/downloads/).

Run the following command to install Flask and Flask-CORS:

```
git clone https://github.com/ekhar/simple_site/
pip install Flask flask-cors
```

### 2. Run the Frontend 

Open up google chrome and open the frontend html file. Do this either by double clicking the html file, or putting the file's path into the search bar (hint use command ```pwd ``` in the terminal to get the file path) 
(extra hint use command ```chrome filename.extention``` to open any file!)

Notice there is html up top and then javascript in the ```html <script> ... </script>```
The javascript sends a "Post" request containing some information in the form of "JSON" to the backend (which is not running right now)

### 3. Run the Backend
In the backend python directory (I hope you did step 1!) run ```python app.py```
We can pretend that the frontend is talking to a different backend. ```localhost:5000``` or whatever is after the : just means: localhost - your computer, :5000 - the port your computer opened. (Ports are just openings that allow network connections or bluetooth connection or whatever else) 

*The python server has this thing called CORS running. This is extra and only needed because we are running both the frontend and backend on the same computer. This is not needed when the frontend and backend are on different computers

### 4. Run the Frontend (Part 2) 
If the python server is running it is now working locally! Run the frontend again and it should work! You have a client talking to a server

### 5. How does the web work?
Frontend servers (popular one I like and is easy and free - vercel) give your html code to someone's google chrome. That html code talks to a url (in this case http://localhost:5000) which is actually just a computer sitting somewhere that is an api. I like hosting these for free on aws




