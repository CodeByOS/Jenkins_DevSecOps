pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/CodeByOS/Jenkins_DevSecOps.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py -v'
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
                    dependency-check.sh \
                        --project "TP-Jenkins" \
                        --scan . \
                        --format HTML \
                        --failOnCVSS 7
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline terminé avec succès !'
        }
        failure {
            echo 'Build échoué : erreurs ou vulnérabilités détectées.'
        }
    }
}