# this teraafrom scrip file wich are used
################################################################
# Provider Section
################################################################

provider "aws" {
  profile    = "default"
  region     = "us-east-1"
  access_key = var.my-access-key
  secret_key = var.my-secret-key
}
################################################################
# Variable Section
################################################################

variable "my-access-key" {
    type = string
  default =""
}
variable "my-secret-key" {
    type = string
  default = ""
}

################################################################
# Resource Section
################################################################
resource "aws_instance" "example" {
  ami           = "ami-02e136e904f3da870"
  instance_type = "t2.micro"
  tags = {
    "name" = "sandeep-vm"
  }
}

################################################################
# Output Section
################################################################

output "instances-key_name" {
  value = aws_instance.example.key_name  
}

output "intances-ip_addresh"{
value = aws_instance.example.public_ip
}

output "intances-ip_addresh"{
value = aws_instance.example.private_ip
}
