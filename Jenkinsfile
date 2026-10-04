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

        stage('Deploy') {
            steps {
                echo 'Deploiement sur le cluster Kubernetes'
                sh 'minikube image load flask:latest'
                sh 'kubectl apply -f manifests/'
                sh 'kubectl rollout status deployment/flask-app --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'Pipeline termine avec succes'
        }
        failure {
            echo 'Le pipeline a echoue'
        }
    }
}
