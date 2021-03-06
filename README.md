![](https://github.com/pinocchioVirus/data-analysis-workflow/actions/workflows/etl-proccess.yml/badge.svg)
![](https://github.com/pinocchioVirus/data-analysis-workflow/actions/workflows/sonar-cloud.yml/badge.svg)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=pinocchioVirus_sideProject&metric=code_smells)](https://sonarcloud.io/dashboard?id=pinocchioVirus_sideProject)
![](https://img.shields.io/github/repo-size/pinocchiovirus/data-analysis-workflow?label=project%20size)

<!-- About The Project -->
# Building dashboard using CI/CD, Automation, Docker and SonarCloud
Project focuss on automating and containerizing the proccess of data <b>ETL (extract, transform, load)</b> and import it into our chosen database, to build a dashboard and analyzing it using <b>Superset or GDS</b> with our <b>Automated Data</b>.

<!-- Topics -->
### Topics:
- <a href="#automating-etl-process">Automating ETL Process</a>
- <a href="#cicd-workflow-process">CI/CD Workflow Process</a>
- <a href="#containerization-process">Containerization Workflow Process</a>

<!-- Used Technology's -->
### Used in this project:
- <a href="https://ubuntu.com/">Ubuntu</a> 20.04 LTS (OS) on local and inside containers
- <a href="https://sqlite.org/index.html">SQLlite3</a> (Storage)
- <a href="https://www.postgresql.org/">PostgreSQL</a> on Heroku (Backup)
- <a href="https://superset.apache.org/">Superset</a> & <a href="https://datastudio.google.com/">Google Data Studio</a> (Dashboards and Reports)
- <a href="https://pypi.org/project/jupyterlab/">JupyterLab</a> (Data Analysis & Engineering)
- <a href="https://github.com/features/actions">Github Actions</a> (CI/CD)
- <a href="https://sonarcloud.io/">SonarCloud</a> (Code Quality & Code Security) 
- <a href="https://www.python.org/downloads/">Python 3.8+</a> (Programming language)
- <a href="https://www.sublimetext.com/">Sublime Text</a> (Code Editor)

<!-- Used Container Images -->
### Containers (Docker & Docker Compose) Images
- <a href="https://hub.docker.com/_/ubuntu">Ubunut</a>, <a href="#">JupyterLab</a>
- <a href="https://hub.docker.com/_/postgres">PostgreSQL</a>, <a href="https://hub.docker.com/r/dpage/pgadmin4">pgADmin</a>
- <a href="#">MinIO</a>, <a href="#">Superset</a>, <a href="#">AirFlow</a>

<!-- Automation Workflow -->
# Automating ETL Process
You can run the project by running the following commands inside `code/` folder, after reading the requirements and before you run the code make sure to set your sql instance configurations if you want to connect to other DB service provider or LocalDB (Like `PostgreSQL/MySQL/MSSQL`) in the following file:
```python
code/configurations/SQL_Config.py
``` 

Then after adding your configurations (Or if you want to use SQLite3 as your storge db edit/add on the `transferData.py` file) and downloaded needed packages (can found in `requirements.txt`), excute the code script to import data into our database.

To run the 'ETL' process, make sure to run the following command to install and save the data to the dataset folder, and make sure you are in the right path (`code/`):
```python
python3 etl_data.py
```

We have the dataset and we are ready now to import the data into our database, by running the following command:
```python
python3 transfer_data.py
```

Finally, you can automate above process by running a shell script to automatically run both files and also create `.sql` file in case you have another database to import into it, without needing to take the same proccess to insert data and you just have to import into the database the generated `.sql` file (make sure you make the shell file excutable by running: `chmod +x esc.sh`) by running the following command from the root folder:
```python
./esc.sh
```

<!-- CI/CD Workflow  -->
# CI/CD Workflow Process
We automated the process of <b>'ETL'</b> using shell script and it works right? but, we have still need to run it manualy inside <b>'terminal'</b> and this makes half of the process are not automated, and here where comes the subject of <b>'CI/CD'</b> and we can create custom <b>'continuous integration (CI)'</b> and <b>'continuous deployment (CD)'</b> workflows directly inside our GitHub repository with <a href="https://github.com/features/actions"><b>GitHub Actions</b></a>.

### Steps To Use CI/CD:
- Go to repository > actions > setup python
- Then copy `./github/workflows/etl-proccess.yml` inside your created file
   - Note: make sure you configure as you prefer it to work 
- If you want sonarcloud to be your code quality/security chosen tool:
   - create `sonar-project.properties` file and put your configurations on it
   - copy `./github/workflows/sonar-cloud.yml` inside your created file
   - Note: make sure you configure as you prefer it to work
 
After you configured and enabled github actions, your 'ETL' process now is compatible with 'CI/CD' and the dataset is scheduled to be automaticly downloaded and transfered to the databasefor every 40min <b>'ksa/riyadh'</b> time and after it completed 5min later sonarcloud scan runs and checks the code security and code quality.

<!-- Containerization Workflow -->
# Containerization Process
If you wanna use containers as your labs, environments or even for developing analysis solution (like in example predicting next week rates and cases based on the data you have automated), you can use docker containers to run isolated environments for you to work on.

In this project i have used `Dockerfile` to configure the installation of only `Ubuntu 20.04 LTS`, `jupyterlab` and `python3` with requirements packages to build isolated environment but this will make our life worse if we need to install other tools and make them communicate together, so i used `docker-compose` to install and configure multiple-containers (`5 isolated containers with different purposes`) to handle our `Database (PostgreSQL)`, `Adminstration (pgAdmin)`, `NoteBook (Jupyterlab)`, Dashborad (Superset) and `Storege (MinIO)` and this makes the process of creating multiple containers on isolated environment and they can communicate and share data between them.

In case you need to Containerize your ETL & Analysis Infrastructure with `Docker/Docker-Compose` as an isolated environment for analysis or testing etc., make sure you have first installed <a href="https://docs.docker.com/get-docker/"><b>Docker</b></a> and you have also <a href="https://docs.docker.com/compose/install/"><b>Docker Compose</b></a>, now you are ready to use the project by following next easy steps:

I put two files in the root folder for containerizing the project called `Dockerfile` and `docker-compose.yml`. <b>Dockerfile</b> is handling the process of installing ubuntu image and installs inside the image all jupyterlab prerequisite packages along with all its confirgurations, <b>docker-composer.yml</b> is used to download multi-container applications using <a href="https://hub.docker.com/">DockerHub</a> images and making the process of installing multi-containers with its configuration more easy!.

After we have maked sure that docker and docker-compose are installed on our machine also up and running, for testing purpose on isolated environment with docker container you can simply run the following command (`in the root directory`):
```python
docker build -t testing .
```
And you can see if the container is created or not:
```python
docker ps
```
Then, after we have installed our container successfully run the following command to make it run inside isolated environment on docker:
```python
docker run -d -p 8888 testing
```
We have successfully running isolated jupyterlab environment on docker, and can access it using your browser and pasting the following:
```python
localhost:8888
```

<!-- Implementation of docker-compose -->
After we saw how we can isolate our workflow, for more easy way to work without needing to take care of the environment on each and single container, there is another way for installing `multi-container` which is what we need ex: (`PostgreSQL`, `PgAdmin`, `JupyterLab`, `Superset` and `MinIO` all together) in this case we gonna use <b>docker-compose</b>, just by running following command (`in the root directory`):
```python
docker-compose up -d
```
And we gonna see that a new proccess is running and installing all needed images and configurations as we typed on the docker-compose.yml file, and we can see afer the install process finish all three container are up and running just run the following command now:
```python
docker-compose ps
```

<!-- All Links -->
# Links To Dashboard, Report & Dataset
<table class="tg">
  <tr>
    <th class="tg-yw4l"><b>Name</b></th>
    <th class="tg-yw4l"><b>Description</b></th>
    <th class="tg-yw4l"><b>Link</b></th>
  </tr>
  <!-- Dashboard Links -->
  <tr>
    <td class="tg-yw4l">Job Seekers</td>
    <td class="tg-yw4l">Dashboard of Saudi Arabia Job Seekers for 2021</td>
    <td class="tg-yw4l"><a href="https://datastudio.google.com/reporting/aa7edb66-7d69-402d-a1ff-6a31f464f974"><p>Dashboard</p></a></td>
  </tr>
   <!-- Resources Links -->
   <tr>
    <td class="tg-yw4l">Data Source</td>
    <td class="tg-yw4l">Data of Saudi Arabia Job Seekers for 2021</td>
    <td class="tg-yw4l"><a href="https://data.gov.sa/Data/ar/dataset/job_seeker-2021"><p>Dataset</p></a></td>
  </tr>
</table>
