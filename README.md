Setting Up Jenkins on Minikube:

Installed jenkins using yaml files, attached in folder Jenkins (added this folder in repository afterwards to make thing clear) <br />
<br />
  *created the minikube url to expose the jenkins-svc to host's url <br />
  *Loged IN and took the start(admin token) to start jenkins <br />
  *created admin user and installed required basic plugin like git,maven,etc <br />
  *Added ssh-creds from github to clone the repository <br />
  *created new pipeline named: abhay (explained in Screenshot below)<br />
  *configured the pipeline to use git repository as source using ssh creds<br />
  ![Alt text](Sonar/Credentials.png?raw=true "Credentials Jenkins")
<br />
![Alt text](Sonar/JenkinsGitPipeline.png?raw=true "Git Pipeline Config")
*JenkinsPods
![Alt text](Sonar/JenkinsPods.png?raw=true "JenkinsPods")
Created the repository **PyhtonFlaskScoreme** in github<br />
<br />
  *added basic flask code<br />
  *This repo also have Dockerfile to create the Image and upload it to docker registry<br />

Created Docker registry account<br />
  *Added docker secrets into jenkins secret <br />
<br />
<br />
<br />
Installed **sonar** in jenkins<br />
  *Screenshot attached<br />
  <br />
![Alt text](Sonar/SonarJenkinsManageTools.png?raw=true "SonarJenkinsManageTools")
![Alt text](Sonar/SonarPlugin.png?raw=true "SonarPlugin")
  *created the sonar account and took secret to add this as text in jenkins secrets<br />
  *integrated the sonar-project.properties file in repo to handle sonar params<br />

*Already have installed **lizard** to check complexity of code and **coverage** to check code coverage in python<br />
*This is all done in Dockerfile of jenkins itself so that it is available in my jenkins host itself<br />

*Github
![Alt text](Sonar/Github.png?raw=true "Github")

  
  
