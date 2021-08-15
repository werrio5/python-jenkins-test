pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                //sh 'python main.py'
                echo 'build not required'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'python3 test_main.py'
                sh 'coverage run -m unittest discover'
            }
        }
        stage('Deploy') {
            steps {
                echo '(not) Deploying....'
            }
        }
    }
}