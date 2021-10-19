# this is the file is create by the SANDEEP KUMAR PATEL
#! /bin/bash

sudo yum update -y
sudo yum install -y httpd
sudo systemctl enable httpd
sudo service httpd start  
sudo cp index.htnl /var/www/html/index.html