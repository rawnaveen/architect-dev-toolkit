#!/usr/bin/env bash
set -euo pipefail
cat > main.tf <<'EOF'
resource "aws_s3_bucket" "uploads" { bucket = "acme-customer-uploads" }
resource "aws_s3_bucket_acl" "uploads" { bucket = aws_s3_bucket.uploads.id  acl = "public-read" }

resource "aws_iam_role_policy" "app" {
  role   = aws_iam_role.app.id
  policy = jsonencode({ Version = "2012-10-17", Statement = [{ Effect = "Allow", Action = "*", Resource = "*" }] })
}

resource "aws_db_instance" "ledger" {
  engine                  = "postgres"
  instance_class          = "db.r6g.large"
  multi_az                = false
  storage_encrypted       = false
  backup_retention_period = 0
  vpc_security_group_ids  = [aws_security_group.db.id]
}

resource "aws_security_group" "db" {
  ingress { from_port = 5432 to_port = 5432 protocol = "tcp" cidr_blocks = ["0.0.0.0/0"] }
}
EOF
