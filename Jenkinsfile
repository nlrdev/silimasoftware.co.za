pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'docker-compose -f production.yml build'
            }
        }
        stage('Push') {
            steps {
                sh 'docker-compose push silimasoftware'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose -f production.yml up -d'
            }
        }
    }
}
