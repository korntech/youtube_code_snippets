pipeline{
    agent any
    environment {
        RELEASE='20.04'
    }
    stages {
        stage('Build'){
            agent any
            environment {
                LOG_LEVEL='INFO'
            }
        steps{
            echo "Building release ${RELEASE} with log level ${LOG_LEVEL}..."

        }


        }
        stage('Deploy'){
           input{
               message 'Deploy?'
               ok 'Do it'
               parameters{
                   string(name: 'TARGET_ENVIRONMENT', defaultValue: 'PROD', description: 'Target deployment env')
               }


           }
            steps{
                echo "Deploying release ${RELEASE} to env ${TARGET_ENVIRONMENT}"

            }




        }

    }
    post {
        always {
            echo "Prints whether deploy happened or not."
        }

    }

}