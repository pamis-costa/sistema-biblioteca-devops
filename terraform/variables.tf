variable "aws_region" {
  description = "Região da AWS onde o recurso será criado."
  type        = string
  default     = "us-east-1"
}

variable "bucket_name" {
  description = "Nome globalmente único do bucket de artefatos."
  type        = string
}
