pipeline {
    agent any

    environment {
        SONAR_SCANNER_HOME = tool 'SonarScanner'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/CodeByOS/Jenkins_DevSecOps.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest test_app.py -v'
            }
        }

        stage('SAST Scan') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh """
                        ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                            -Dsonar.projectKey=tp-jenkins \
                            -Dsonar.sources=. \
                            -Dsonar.language=py
                    """
                }
            }
        }

        stage('SCA Scan') {
            steps {
                sh '''
                    dependency-check.sh \
                        --project "TP-Jenkins" \
                        --scan . \
                        --format HTML \
                        --out ./reports \
                        --failOnCVSS 7
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/*.html',
                             allowEmptyArchive: true
        }
        success {
            echo 'Pipeline terminé avec succès !'
        }
        failure {
            echo 'Build échoué : erreurs ou vulnérabilités détectées.'
        }
    }
}