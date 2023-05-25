pipeline {
    agent any
	stages {
		stage('checkout') {
			steps {
				script {
					properties([pipelineTriggers([pollSCM('* * * * *')])])
				}
				git 'https://github.com/TomerM25/Project.git'
		    }
		}
		stage('run backend') {
			steps {
				script {
					bat 'start /min python rest_app.py'
				}
		    }
		}
	}
}