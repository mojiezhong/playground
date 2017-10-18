provider "aws" {
  access_key = "AKIAIOLLMDB2LPH2TBIQ"
  secret_key = "Jpt/hLG6yQGMTNIXIPYwD/jDbszXZTbkjV+XiccE"
  region     = "us-east-1"
}

resource "aws_instance" "example" {
  ami           = "dev-jiezhong-try-terraformami-2757f631"
  instance_type = "t2.micro"
}
