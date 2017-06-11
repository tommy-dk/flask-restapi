node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */

        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        app = docker.build("flask-restapi")
    }

    stage('Push image') {
        /* Finally, we'll push the image with two tags:
         * First, the incremental build number from Jenkins
         * Second, the 'latest' tag.
         * Pushing multiple tags is cheap, as all the layers are reused. */
    /*
        docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
            app.push("${env.BUILD_NUMBER}")
            app.push("latest")
        }
    */
    }
    stage('Test image') {
        docker.image('flask-restapi').withRun('-p 8000:8000') {c ->
            sh "curl -i http://localhost:8000/"
        }
    }

    stage('Deploy image') {
        docker.image('flask-restapi').run('-p 8000:8000')
    }
}
