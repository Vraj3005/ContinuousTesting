pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from Git repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing required testing dependencies (pytest)...'
                bat 'python -m pip install pytest'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo 'Executing automated pytest test suite...'
                bat 'python -m pytest -v'
            }
        }
    }

    post {
        success {
            echo '========================================='
            echo 'All tests passed successfully!'
            echo 'Build: SUCCESS'
            echo '========================================='
        }
        failure {
            echo '========================================='
            echo 'Pipeline failed. Check the test results.'
            echo 'Build: FAILURE'
            echo '========================================='
        }
    }
}
