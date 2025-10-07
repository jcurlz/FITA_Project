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
                python -m pip install --upgrade pip
                python -m pip install -r requirements.txt
                set REPORT_PATH=behave_report.html
                python -m behave features/ -t '%TAGS%' --format behave_html_formatter:HTMLFormatter --out behave_report.html --no-skipped --no-capture -f plain
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
