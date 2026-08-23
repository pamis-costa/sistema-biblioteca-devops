terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }

  required_version = ">= 1.6.0"
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "biblioteca_artefatos" {
  bucket = var.bucket_name

  tags = {
    Projeto = "SistemaBiblioteca"
    Ambiente = "dev"
    Finalidade = "Armazenamento de artefatos"
  }
}

resource "aws_s3_bucket_versioning" "biblioteca_artefatos" {
  bucket = aws_s3_bucket.biblioteca_artefatos.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "biblioteca_artefatos" {
  bucket = aws_s3_bucket.biblioteca_artefatos.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
