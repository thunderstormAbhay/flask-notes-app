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
            }
        }
    stage("Build Docker Image"){
        steps{
            echo "Building Docker image"
        }
    }
    stage("Run Container"){
        steps{
            echo "Running container"
        }
    }
            
}
}
