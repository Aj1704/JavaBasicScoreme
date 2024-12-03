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
                    // sh 'docker build -t abhayjain99/abhayscoreme:1.0.0 .'
                    def newapp = docker.build("abhayjain99/abhayscoreme:1.0.0")
                    // withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerhubPassword', usernameVariable: 'dockerhubUser')]) {
                       // sh "docker login -u ${env.dockerhubUser} -p ${env.dockerhubPassword}"
                       // sh 'docker push shanem/spring-petclinic:latest'
                    // }
                }
            }
        }
    }
}