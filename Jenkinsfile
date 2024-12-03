pipeline {
    agent any
    stages {
        stage('Example') {
            steps {
                script {
                    def output = sh(returnStdout: true, script: 'pwd')
                    echo "Output: ${output}"
                    def output1 = sh(returnStdout: true, script: 'ls -lart')
                    echo "Output1: ${output1}"
                }
            }
        }
    }
}