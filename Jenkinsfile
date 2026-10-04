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
                echo 'Construction de l image dans le demon Docker du cluster'
                sh '''
                    eval $(minikube docker-env)
                    docker build -t flask:${BUILD_NUMBER} -t flask:latest .
                    docker image ls | grep flask
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploiement sur le cluster Kubernetes'
                sh 'kubectl apply -f manifests/'
                sh 'kubectl rollout restart deployment/flask-app'
                sh 'kubectl rollout status deployment/flask-app --timeout=300s'
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
