#!/bin/bash
sudo yum update -y
sudo yum install -y python3 git
git clone https://github.com/Hrushikesh-karthik/aws-project-18.git
cd aws-project-18
pip3 install -r requirements.txt
