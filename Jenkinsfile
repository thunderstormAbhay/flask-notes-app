pipeline{

agent{
    label "dev"
}

stages{
    stage("Install dependencies"){
        steps{
            echo "Installing dependencies"
            sh '''
            python3 -m venv venv
            . venv/bin/activate
            pip install -r requirements.txt
            '''
}
    }
        stage("Run Tests"){
            steps{
                echo "Running tests"
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PWD
                python -m pytest -v
                '''
            }
        }
    stage("Build Docker Image"){
        steps{
            echo "Building Docker image"
            sh ' docker build -t winwithabhay/flask-notes:latest .'
        }
    }
    stage("Docker Login") {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASS'
        )]) {

            sh '''
            echo "$DOCKER_PASS" | docker login \
                -u "$DOCKER_USER" \
                --password-stdin
            '''
        }
    }
}
    stage("Push Image") {
    steps {
        sh '''
        docker push winwithabhay/flask-notes:latest
        '''
    }
}
   stage("Deploy") {
    steps {
        sh '''
        docker rm -f flask-notes || true

        docker image rm winwithabhay/flask-notes:latest || true

        docker pull winwithabhay/flask-notes:latest

        docker run -d \
        --name flask-notes \
        -p 5000:5000 \
        winwithabhay/flask-notes:latest
        '''
    }
}
            
}
}
