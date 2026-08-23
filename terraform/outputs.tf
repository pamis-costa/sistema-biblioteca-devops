output "bucket_name" {
  description = "Nome do bucket criado."
  value       = aws_s3_bucket.biblioteca_artefatos.bucket
}

output "bucket_arn" {
  description = "ARN do bucket criado."
  value       = aws_s3_bucket.biblioteca_artefatos.arn
}
