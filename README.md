Setting Up Jenkins on Minikube: <br />
***1. Jenkins Setup***
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

***2. SCM***
Created the repository **PyhtonFlaskScoreme** in github<br />
<br />
  *added basic flask code<br />
  *This repo also have Dockerfile to create the Image and upload it to docker registry<br />
*Github
![Alt text](Sonar/Github.png?raw=true "Github")

**Created Docker registry account<br />**
  *Added docker secrets into jenkins secret <br />
  
<br />
<br />
<br />
***3. Pipeline Creation***
![Alt text](Sonar/Pipeline.png?raw=true "Pipeline")
*GithubPolling*
![Alt text](Sonar/GithubPoll.png?raw=true "GithubPolling")
***4. Code Quality Check***
Installed **sonar** in jenkins<br />
  *Screenshot attached<br />
  <br />
![Alt text](Sonar/SonarJenkinsManageTools.png?raw=true "SonarJenkinsManageTools")
![Alt text](Sonar/SonarPlugin.png?raw=true "SonarPlugin")
  *created the sonar account and took secret to add this as text in jenkins secrets<br />
  *integrated the sonar-project.properties file in repo to handle sonar params<br />

 
***5. Code Coverage and 6. Cyclomatic Complexity***
*Already have installed **lizard** to check complexity of code [Can be found in logs] and **coverage** to check code coverage [can be seen in attahced artifacts] in python using pytest, also this lead to coverage issues on sonar so have bypassed the test files there<br />
*This is all done in Dockerfile of jenkins itself so that it is available in my jenkins host itself<br />
![Alt text](Sonar/Artifacts.png?raw=true "Artifacts")


***7. Security Vulnerability Scan: Tried to use depscan and safety-cli***

Safety CLI: issue with subscritptions
depscan: having some issue with dependency, will try to figure this.

 ***8. Notifications:*** 
 Tried to send mails through gmail smtp but having isse with connections [Screenshot attached]
  Email 
  ![Alt text](Sonar/EmailSetup.png?raw=true "Email Setup")

Summary:

1. Jenkins Setup --> done
2. SCM --> done along with SCM polling
3. Pipeline Creation --> done
4. Code Quality Check --> done 
5. Code Coverage --> done
6. Cyclomatic Complexity --> done
7. Security Vulnerability Scan --> failed
8. Notifications --> failed
