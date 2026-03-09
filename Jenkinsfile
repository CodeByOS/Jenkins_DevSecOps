pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '/opt/jenkins-venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '/opt/jenkins-venv/bin/pytest'
            }
        }
    }

    post {
        failure {
            echo 'Build failed due to errors or vulnerabilities'
        }
    }
}