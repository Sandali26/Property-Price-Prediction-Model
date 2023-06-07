# Property-Price-Prediction-Model

A property price prediction model is a computational tool or algorithm that utilizes various data and techniques to estimate the future prices of real estate properties. These models are typically designed to assist buyers, sellers, investors, and real estate professionals in making informed decisions about property transactions.

## **Description**

* Property Price Prediction Model is a Supervised Learning Model. This model is trained using Linear Regression method.
* Dataset used in this model builidng is of Bangalore City . The dataset consists of various features that help in predicting the property price . Past Years data has been incorporated in the dataset for accurate prediction.

## Steps Involved

1. Data collection: Gather relevant data such as historical property sales records, property features (location, size, amenities).
2. Data preprocessing: Clean and prepare the collected data, handle missing values, standardize variables, and transform data into a suitable format for analysis.
3. Feature selection and engineering: Identify significant features that impact property prices using statistical techniques or machine learning algorithms.
4. Model selection: Choose an appropriate machine learning algorithm based on the nature of the data and the complexity of the problem.
5. Training the model: Train the model using historical data, where the relationship between input features and property prices is learned.
6. Model evaluation: Assess the performance of the trained model using validation data.

   ### **Model Selection**

   ---


   - Model used in this project are :- Linear Regression , Lasso Regression , Grid Search CV , Decision Tree Regressor and ShuffleSplit
   - Grid Search CV is a Cross-Validation Technique that wehave used .

#### Server Integration

* Firstly we will be using Pyton Flask Server for Integration .( Connection Between Frontend and Backend )
* Importing the Flask Module and creating a Flask server
* From the model we will export two files one of the prediction and other of locations
* We will create two servers in util.py file and two routes for the respective servers in server.py file .
* For API integration we used Postman
* Run the flask website from html file after performing all the steps.
