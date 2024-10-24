pipeline {
    agent any
    
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/csurqunix/OSDetector.git'
            }
        }
        
        stage('Installation de Python 3.11 et pip') {
            steps {
                script {
                    
                    sh 'sudo apt update'
                    sh 'sudo apt install -y python3.11 python3.11-distutils'
                    sh 'wget https://bootstrap.pypa.io/get-pip.py'
                    sh 'python3.11 get-pip.py'
                    sh 'rm get-pip.py'
                }
            }
        }

        stage('Exécution du script Python') {
            steps {
                script {
                    sh 'python3 os_detector.py'
                }
            }
        }
    }
}
