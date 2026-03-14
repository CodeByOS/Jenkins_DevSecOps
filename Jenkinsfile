pipeline {
    agent any

    stages {

        stage('Setup Python Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                pytest
                '''
            }
        }

        stage('SCA Scan') {
            steps {
                sh '''
                /opt/dependency-check/bin/dependency-check.sh \
                --updateonly

                /opt/dependency-check/bin/dependency-check.sh \
                --project "TP-Jenkins" \
                --scan . \
                --format HTML \
                --failOnCVSS 7
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'dependency-check-report.html'
        }

        failure {
            echo 'Build failed due to vulnerabilities (CVSS >= 7)'
        }
    }
}