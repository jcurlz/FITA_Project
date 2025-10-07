pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo 'Upgrading pip'
                bat 'python -m pip install --upgrade pip'
            }
        }

        stage('Build') {
            steps {
                echo 'Build step here'
                bat 'echo Building project...'
            }
        }

        stage('Test') {
            steps {
                echo 'Run tests here'
                bat 'echo Testing project...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy step here'
                bat 'echo Deploying project...'
            }
        }
    }
}
