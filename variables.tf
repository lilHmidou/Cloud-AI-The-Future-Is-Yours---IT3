variable "project_id" {
  type = string
}

variable "region" {
    type = string 
    default = "europe-west1"
}

variable "zone" {
    type = string 
    default = "europe-west1-b"
}

variable "ssh_user" {
    type = string 
    default = "ansible"
}

variable "web_port" {
    type    = number
    default = 8080
}

variable "api_port" {
    type    = number
    default = 5000
}

locals {
  name_prefix = "demo-hmidou"
  roles = {
    web = var.web_port
    api = var.api_port
  }
}