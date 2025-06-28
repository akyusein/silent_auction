pipeline {
    agent any

      environment {
        PATH = "$HOME/.local/bin:$PATH"
    }

    stages {
        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip
                    pip3 install pytest
                    pip3 install --user coverage
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
           
            sh 'coverage html'
            archiveArtifacts artifacts: 'htmlcov/**', fingerprint: true
        }
        failure {
            echo '❌ Build failed due to low test coverage.'
        }
    }
}
