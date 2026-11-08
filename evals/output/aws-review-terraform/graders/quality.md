---
type: llm
weight: 3
---
main.tf has planted issues: a public-read S3 bucket for customer uploads; an IAM policy with Action "*" on
Resource "*" attached to the app role; a single-AZ RDS instance with storage_encrypted = false and
backup_retention_period = 0; and a security group allowing 0.0.0.0/0 on port 5432.
PASS if the review flags at least four of: public bucket, wildcard IAM, unencrypted RDS, no backups or
single-AZ, open database port, and rates the public bucket and wildcard IAM as high severity.
FAIL otherwise.
