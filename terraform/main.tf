# this teraafrom scrit file wich are used

provider "aws" {
  region     = "us-east-1"
  access_key = var.access_key
  secret_key = var.secret_key
}
variable "access_key" {
   
}

variable "secret_key" {
    
}

resource "aws_instance" "my-vm" {
  ami = "ami-02e136e904f3da870"
  instance_type = "t2.micro"
  tags = {
    name = "sandeep-vm"
  } 
}
