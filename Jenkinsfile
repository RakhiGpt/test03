pipeline {
    agent any

    stages {
        stage('Git Clone') {
            steps {
                git url: 'https://github.com/RakhiGpt/test03.git', branch: 'main'
            }
        }

        stage('Setup Dependencies') {
            steps {
                echo "setting up python virtual environment and installing dependencies"
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install pytest
                '''
            }
        }
        
        stage('Run records' ) {
            steps {
                echo "Executing beneficiary.py"
                bat '''
                call venv\\Scripts\\activate 
                python beneficiary.py
                '''
            }
        }

        stage('Run tests') {
            steps {
                echo "running test_case.py"
                bat '''
                call venv\\Scripts\\activate 
                pytest test_case.py
                '''
            }
        }
    }
}
     