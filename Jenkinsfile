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
                sh 'pip3 install -r requirements.txt --break-system-packages'
            }
        }

        stage('Run Tests') {
            steps {
                sh '/var/jenkins_home/.local/bin/pytest test_app.py -v'
            }
        }

        stage('SAST Scan') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh """
                        ${SONAR_SCANNER_HOME}/bin/sonar-scanner \
                            -Dsonar.projectKey=tp-jenkins \
                            -Dsonar.sources=. \
                            -Dsonar.python.version=3.13 \
                            -Dsonar.exclusions=**/reports/**,**/*.html,**/venv/**
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
                        --data /var/jenkins_home/dependency-check-data \
                        --nvdApiKey CD9D0F86-7820-F111-836A-0EBF96DE670D \
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