pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Test') {
            steps { bat 'pytest test_main.py' }
        }
        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\Hp\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t studentgrade:latest .'
            }
        }
        stage('Run Docker Container') {
            steps {
                bat '"C:\\Users\\Hp\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" run --rm studentgrade:latest'
            }
        }
    }
}