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
            sh ' docker build -t flask-notes .'
        }
    }
    stage("Run Container"){
        steps{
            echo "Running container"
        }
    }
            
}
}
