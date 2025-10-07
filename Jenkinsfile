pipeline {
    agent any

    triggers {
        GenericTrigger(
            genericVariables: [
                [key: 'ref', value: '$.ref']
            ],
            token: 'Kazakh',
            printContributedVariables: true,
            printPostContent: true
        )
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Building project triggered by GitHub push..."
                // Add your build commands here
            }
        }

        stage('Test') {
            steps {
                echo "Running tests..."
                // Add your test commands here
            }
        }
    }
}
