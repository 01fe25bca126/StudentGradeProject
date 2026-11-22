pipeline {
    agent any
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Test') { steps { bat 'pytest test_main.py' } }
        stage('Build Docker Image') { steps { bat 'docker build -t studentgrade:latest .' } }
        stage('Run Docker Container') { steps { bat 'docker run --rm studentgrade:latest' } }
    }
}