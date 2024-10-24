pipeline {
    agent any
    
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                // Cloner le dépôt depuis l'URL sans spécifier un fichier, récupère tout le contenu
                git branch: 'main', url: 'https://github.com/Macareux-moine/jenkins2.git'
            }
        }
        
        stage('Installation de Python 3.11 et pip') {
            steps {
                script {
                    // Mise à jour des paquets et installation de Python 3.11 avec sudo
                    sh 'sudo apt update'
                    sh 'sudo apt install -y python3.11 python3.11-distutils'
                    // Installation de pip
                    sh 'wget https://bootstrap.pypa.io/get-pip.py'
                    sh 'sudo python3.11 get-pip.py' // Assurez-vous que l'utilisation de sudo est nécessaire ici
                    sh 'rm get-pip.py'
                }
            }
        }

        stage('Exécution du script Python') {
            steps {
                script {
                    // Exécuter le script Python
                    sh 'python3.11 os_detector.py' // Assurez-vous que le nom du script est correct
                }
            }
        }
    }
}
