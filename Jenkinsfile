pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests..."
                    pytest .
                '''
            }
        }
    }
}
