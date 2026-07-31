pipeline {
    agent {
        label 'dev'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PWD
                python -m pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-notes .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-notes || true
                docker run -d --name flask-notes -p 5000:5000 flask-notes
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline Finished'
        }
        success {
            echo 'Build Successful'
        }
        failure {
            echo 'Build Failed'
        }
    }
}
