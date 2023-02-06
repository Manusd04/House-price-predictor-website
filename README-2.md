
# House Price Prediction Web Application



This is a Flask-based web application that utilizes machine learning algorithms to predict the prices of houses based on user-inputted features. The application is deployed on Apache server and hosted on Amazon Web Services (AWS) Cloud, offering a fast and reliable user experience.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

* Python 3.x

* Flask

* Apache server

* AWS account (for hosting)


## Installation

Clone the repository to your local machine

```bash
$ git clone https://github.com/Manusd04/House-price-predictor-website.git

```
Navigate to the project directory

```bash
$ cd house-price-prediction
```

Install the required packages

```bash
$ pip install -r requirements.txt
```

Start the Flask development server

```bash
$ export FLASK_APP=app.py
$ flask run

```
The web application should now be running on your local machine at http://localhost:5000/.



## Deployment

The application can be deployed on Apache server and hosted on AWS Cloud using the following steps:

* Install Apache server on your local machine

* Copy the entire project directory to the Apache server's htdocs folder

* Set up the necessary configurations on Apache to serve the Flask application

* Create an AWS account and set up an AWS ec2 instance to host your application

* Deploy the application to the AWS ec2 instance

Please refer to the official Flask and AWS documentation for detailed instructions on deploying Flask applications.


## Tech Stack

**[Flask:](https://flask.palletsprojects.com/en/2.0.x/)** A Python web framework

**[Apache server:](https://httpd.apache.org)** A popular open-source web server

**[AWS Cloud:](https://aws.amazon.com)** Amazon Web Services for hosting

## Authors

- [@Manusd04](https://github.com/Manusd04?tab=repositories)


## License

This project is open source and does not have a license. Contributions, bug reports, and suggestions for improvements are welcome and encouraged. Feel free to open an issue or submit a pull request with any changes or advice to improve the project

