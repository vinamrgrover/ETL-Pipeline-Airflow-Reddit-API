# Creating a Simple ETL Pipeline Using Airflow and Reddit API


## Architecture Diagram

![Airflow_ETL](https://user-images.githubusercontent.com/100070155/231428004-992b0287-439f-49ef-b486-f56df73a552b.png)


## Key Points and Overview

+ The goal of this project is to demonstrate how to create a simple ETL pipeline using Airflow and Reddit API. In this pipeline, we will extract data from Reddit API, transform it, and load it into an AWS S3 bucket using s3fs. 

+ We'll use an AWS EC2 instance to configure Airflow, and create a DAG with a task to schedule the ETL script to run. 

+ An IAM Role is assigned to the AWS EC2 instance with a policy to allow AWS S3 access. Finally the Airflow DAG is set to run on EC2 instance which initiates the ETL Pipeline. 


## Files

reddit_etl.py: This file contains the Python ETL script for extracting, transforming, and loading data from Reddit API to AWS S3 using s3fs.

reddit_dag.py: This file contains the DAG and task definitions for Airflow.
