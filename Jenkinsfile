pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        PATH = "${env.VIRTUAL_ENV}/Scripts:${env.PATH}" // en Windows
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dmefrain02/Python_Selenium_Jenkins'
            }
        }

        stage('Setup Python Env') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirement.txt'
            }
        }

        stage('Run Tests and Generate Report') {
            steps {
                bat 'venv\\Scripts\\python -m xmlrunner discover -s tests -o results'
            }
        }
        stage('Publish Results') {
            steps {
                junit 'results/TEST-*.xml'
            }
        }
    }
}