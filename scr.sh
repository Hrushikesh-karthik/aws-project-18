#!/bin/bash
sudo apt update -y
sudo apt install -y python3 git
git clone https://github.com/Hrushikesh-karthik/aws-project-18.git
cd aws-project-18
sudo apt install -y python3-venv
python3 -m venv myenv
source myenv/bin/activate

pip3 install -r requirements.txt
