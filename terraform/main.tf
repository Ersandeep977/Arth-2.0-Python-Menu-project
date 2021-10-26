# this teraafrom scrit file wich are used
provider "aws" {
  profile    = "default"
  region     = "us-east-1"
  access_key = var.my-access-key
  secret_key = var.my-secret-key
}

variable "my-access-key" {
    type = string
  default =""
}
variable "my-secret-key" {
    type = string
  default = ""
}

resource "aws_instance" "example" {
  ami           = "ami-02e136e904f3da870"
  instance_type = "t2.micro"
  tags = {
    "name" = "sandeep-vm"
  }
}