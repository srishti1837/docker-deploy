pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/srishti1837/docker-deploy'
            }
        }

        stage('Stop Old Containers') {
            steps {
                bat 'docker compose down'
            }
        }

        stage('Build and Start Containers') {
            steps {
                bat 'docker compose up -d --build'
            }
        }

        stage('Check Running Containers') {
            steps {
                bat 'docker ps'
            }
        }
    }
    post {
        success {
            echo 'CI/CD Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}