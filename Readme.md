# Install two-bucket-lambda-infer


### Preparing Deployment environment

To deploy lambda function we use docker container. Check out the docker 
project from github: https://github.com/agilebeat-inc/docker-serverless-aws-client

Follow instructions in the Readme.md file for the docker project

### Prepering serverless environment on the docker container

Before we deploy lambda function to the aws we need to execute few preparation 
steps. First will be creating virtual environment for python 3.6 where we will
install all packages necessary for the lambda function. Then we will install 
serverless plugins necessary for deployment (plugins are extensions allowing more granular
control over aws). Finally we will deploy lambda function.

At this point we are assuming that you have executed the steps listed in the
Readme.md for the docker-serverless-aws-client project. You should have running 
docker container and have shell terminal: `root@<IMAGE-ID>:/notebooks#`

#### Step 1. Set pu virtual python environment

1. Run: `python3 -m venv python.venv`
   This comman will create python virtual environment which is a folder `python.venv`
   insde the project. Please don't check in that folder to the github.
   
2. Activate python virtual environment. Run command:

   `source python.venv/bin/activate`
   
   You should see:
   
   `(python.venv) root@<IMAGE-ID>:~/classify-lambda#`
   
3. Install packages necessary for lambda in the virtual environment:

   `pip install tensorflow==1.10.0`