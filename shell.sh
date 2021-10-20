# this is the file is create by the SANDEEP KUMAR PATEL
#! /bin/bash

sudo yum update -y
sudo yum install -y httpd
sudo systemctl enable httpd
sudo systemctl start httpd   
sudo cp index.html ./var/www/html/index.html
