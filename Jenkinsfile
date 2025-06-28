pipeline {
    agent any

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install -r requirements.txt
                    pip3 install pytest
                    pip3 install coverage
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    echo "Running tests..."
                    pytest .
                    coverage run -m unittest discover
                    coverage report --fail-under=90
                '''
            }
        }
    }

    post {
        always {
            // Optional: save report file
            sh 'coverage html'
            archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
        }
        failure {
            echo '❌ Build failed due to low test coverage.'
        }
    }
}
