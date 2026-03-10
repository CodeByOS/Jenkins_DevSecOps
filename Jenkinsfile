pipeline {
    agent any

    environment {
        DC_DATA = "/var/jenkins_home/dependency-check-data"
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

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

        stage('SAST Scan') {
            steps {
                sh 'sonar-scanner'
            }
        }

        stage('SCA Scan') {
            steps {
                sh '''
                /opt/dependency-check/bin/dependency-check.sh \
                --project "TP-Jenkins" \
                --scan . \
                --format HTML \
                --out . \
                --data $DC_DATA \
                --enableExperimental
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'dependency-check-report.html', fingerprint: true
        }
    }
}