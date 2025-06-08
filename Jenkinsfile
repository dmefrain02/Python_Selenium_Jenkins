pipeline {
    agent any

    environment {
        VIRTUAL_ENV = "${WORKSPACE}/venv"
        PATH = "${env.VIRTUAL_ENV}/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/dmefrain02/Python_Selenium_Jenkins'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv venv'
                sh 'source venv/bin/activate && pip install --upgrade pip'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && python -m unittest discover -s tests'
            }
        }
    }

    post {
        always {
            junit 'test-reports/*.xml'  // si generas XML con unittest-xml-reporting
        }
    }
}