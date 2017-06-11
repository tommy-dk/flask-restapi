node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("flask-restapi:{env.BUILD_NUMBER}")
    }

    stage('Push image') {
        //app.push("${env.BUILD_NUMBER}")
    }
    stage('Test image') {
        docker.image('flask-restapi').withRun('-p 8111:8000') {c ->
            sh "curl -i http://localhost:8111/"
        }
    }

    stage('Deploy image') {
        sh 'docker stop flask-restapi'
        docker.image('flask-restapi').run('-p 8000:8000 --name flask-restapi')
    }
}
