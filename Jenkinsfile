pipeline {
    agent any
    stages {
        stage('Dummy') {
            steps {
                script {
                    def output = sh(returnStdout: true, script: 'pwd')
                    echo "Output: ${output}"
                    def output1 = sh(returnStdout: true, script: 'ls -lart')
                    echo "Output1: ${output1}"
                }
            }
        }
        stage('Create DockerImage') {
            steps {
                script {
                    sh 'docker build --file ./app/Dockerfile -t abhayjain99/abhayscoreme:1.0.0 .'
                    //def newapp = docker.build("abhayjain99/abhayscoreme:1.0.0")
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhubPassword', usernameVariable: 'dockerhubUser')]) {
                       sh "docker login -u ${env.dockerhubUser} -p ${env.dockerhubPassword}"
                       sh 'docker push abhayjain99/abhayscoreme:1.0.0'
                    }
                }
            }
        }
        stage('SonarQube analysis') {
          steps {
            script {
                scannerHome = tool 'sonar'
            }
            withSonarQubeEnv('sonar') {
              sh "${scannerHome}/bin/sonar-scanner -Dsonar.sources=app -Dsonar.projectKey=Aj1704_PythonFlaskScoreme -Dsonar.organization=aj1704"
            }
          }
        }
        stage("Quality Gate") {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    // Parameter indicates whether to set pipeline to UNSTABLE if Quality Gate fails
                    // true = set pipeline to UNSTABLE, false = don't
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        stage('Coverage') {
            steps {
                script {
                    sh """
                    /bin/bash -c "python3 -m venv ~/venv; . ~/venv/bin/activate; lizard"
                    """
                }
            }
        }
    }
}