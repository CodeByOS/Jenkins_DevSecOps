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
                sh '''
                rm -f dependency-check-report.html

                /opt/dependency-check/bin/dependency-check.sh \
                  --project "TP-Jenkins" \
                  --scan requirements.txt \
                  --format HTML \
                  --out . \
                  --data /var/jenkins_home/dependency-check-data \
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