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
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploiement sur le cluster Kubernetes'
                sh 'minikube image load flask:latest'
                sh 'minikube ssh -- sudo crictl images | grep flask'
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
