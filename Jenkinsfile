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

        stage('SCA Scan') {
            steps {
                sh '/opt/dependency-check/bin/dependency-check.sh --project "TP-Jenkins" --scan . --format HTML --data /var/jenkins_home/dependency-check-data'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'dependency-check-report.html', fingerprint: true
        }
        failure {
            echo 'Build failed due to errors or vulnerabilities'
        }
        success {
            echo 'Build completed successfully'
        }
    }
}