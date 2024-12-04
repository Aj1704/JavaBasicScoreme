Setting Up Jenkins on Minikube:

Installed jenkins using yaml files, attached in folder Jenkins (added this folder in repository afterwards to make thing clear) <br />
  created the minikube url to expose the jenkins-svc to host's url <br />
  Loged IN and took the start(admin token) to start jenkins
  created admin user and installed required basic plugin like git,maven,etc
  Added ssh-creds from github to clone the repository
  created new pipeline named: abhay (explained in Screenshot below)
  configured the pipeline to use git repository as source using ssh creds
  ![Alt text](Sonar/Credentials.png?raw=true "Credentials Jenkins")

Created the repository **PyhtonFlaskScoreme** in github
  added basic flask code
  This repo also have Dockerfile to create the Image and upload it to docker registry

Created Docker registry account
Added docker secrets into jenkins secret 


Installed **sonar** in jenkins
  Screenshot attached
  created the sonar account and took secret to add this as text in jenkins secrets
  integrated the sonar-project.properties file in repo to handle sonar params

Already have installed **lizard** to check complexity of code and **coverage** to check code coverage in python
This is all done in Dockerfile of jenkins itself so that it is available in my jenkins host itself


  
  
