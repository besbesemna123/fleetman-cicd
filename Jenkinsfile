pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Recuperation du code source'
                sh 'ls -la'
            }
        }

        stage('Build') {
            steps {
                echo 'Construction de l image Docker'
                sh 'docker build -t flask:${BUILD_NUMBER} -t flask:latest .'
                sh 'docker image ls | grep flask'
            }
        }

        stage('Analyse SonarQube') {
            steps {
                echo 'Analyse de la qualite du code'
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh 'echo "URL du serveur : $SONAR_HOST_URL"'
                        sh 'echo "Jeton transmis : ${SONAR_AUTH_TOKEN:+oui}${SONAR_AUTH_TOKEN:-non}"'
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.token=\$SONAR_AUTH_TOKEN"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploiement sur le cluster Kubernetes'
                sh 'minikube image load flask:latest'
                sh 'kubectl apply -f manifests/'
                sh 'kubectl rollout restart deployment/flask-app'
                sh 'kubectl rollout status deployment/flask-app --timeout=300s'
            }
        }
    }

    post {
        always {
            sh 'docker image prune -f'
        }
        success {
            echo 'Pipeline termine avec succes'
        }
        failure {
            echo 'Le pipeline a echoue'
        }
    }
}
