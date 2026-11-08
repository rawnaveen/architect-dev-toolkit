---
name: aws-solution-review
description: >
  This skill should be used when the user shares or discusses an AWS architecture, design doc, Terraform/
  CloudFormation/CDK, Helm or Kubernetes manifests for EKS, or asks to "review this architecture",
  "is this well-architected", "check this AWS design", "harden this EKS setup", "estimate AWS cost",
  or "what could go wrong with this design". Apply proactively when infrastructure code or diagrams
  are being created or changed.
metadata:
  version: "0.1.0"
---

# AWS solution review (Well-Architected lens)

Review against the six Well-Architected pillars and return prioritised findings.

## Pillars and checks
- **Security**: least-privilege IAM (IRSA / EKS Pod Identity, no wildcard actions), KMS encryption at rest,
  TLS in transit, Secrets Manager not env literals, private subnets, security groups minimal, no public
  S3, GuardDuty/Security Hub, audit via CloudTrail, network policies in EKS, image scanning, PSA/OPA.
- **Reliability**: multi-AZ, health checks and PodDisruptionBudgets, HPA/Karpenter limits, retries with
  backoff and timeouts, idempotency, DLQs, backups and tested restore, RTO/RPO stated, quotas checked.
- **Operational excellence**: IaC everywhere, CI/CD with rollback, runbooks, structured logs, metrics,
  traces (OTel), SLOs and alerts on symptoms, change management.
- **Performance efficiency**: right instance families/Graviton, caching, async where possible,
  connection pooling, load tested.
- **Cost optimisation**: Savings Plans/Spot for stateless, rightsizing, S3 lifecycle, NAT gateway and
  cross-AZ data transfer costs, log retention, idle resources, tagging for cost allocation.
- **Sustainability**: utilisation, Graviton, managed services.
- **For Claude/Bedrock workloads**: Bedrock VPC endpoints, model invocation logging policy, request caps
  (20 MB), prompt caching, batch inference for offline jobs, guardrails, quota (TPM/RPM) planning.

## Output
1. Verdict in one line and the top 3 risks.
2. Findings table: pillar | finding | severity (High/Med/Low) | evidence (file:line or diagram element) | fix.
3. Quick wins (under a day) separately from structural changes.
4. Rough monthly cost drivers if enough information is present; state assumptions.
