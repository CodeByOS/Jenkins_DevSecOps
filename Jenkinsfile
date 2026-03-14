pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('SCA Scan') {
            steps {
                sh '''
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