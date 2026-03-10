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

        stage('SCA Scan - OWASP Dependency Check') {
            steps {
                sh '''
                rm -f dependency-check-report.html

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
        success {
            echo 'Build completed successfully'
        }
        failure {
            echo 'Build failed due to errors or vulnerabilities'
        }
    }
}