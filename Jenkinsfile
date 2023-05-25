pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '10'))
    }
	stages {
		stage('checkout') {
			steps {
				script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
				git 'https://github.com/TomerM25/Project.git'
		    }
		}
		stage('install packages') {
			steps {
				script {
					bat 'pip install flask'
					bat 'pip install pymysql'
					bat 'pip install requests'
					bat 'pip install selenium'
				}
		    }
		}
		stage('run backend') {
			steps {
				script {
					bat 'start /min python rest_app.py'
				}
		    }
		}
		stage('run frontend') {
			steps {
				script {
					bat 'start /min python web_app.py'
				}
		    }
		}
		stage('run backend testing') {
			steps {
				script {
					bat 'python backend_testing.py'
				}
		    }
		}
		stage('run frontend testing') {
			steps {
				script {
					bat 'python frontend_testing.py'
				}
		    }
		}
		stage('run combined testing') {
			steps {
				script {
					bat 'python combined_testing.py'
				}
		    }
		}
		stage('clean') {
			steps {
				script {
					bat 'python clean_environment.py'
				}
		    }
		}
	}
}