# IaaP Guard hosted service privacy notice — DRAFT FOR REVIEW

> **Not yet approved or effective.** This document is a proposed product-specific privacy notice for review by the service owner and legal/privacy reviewer. Do not use this draft as the Marketplace privacy-policy URL until its factual and legal review is complete.

## Scope

This notice is intended to cover the hosted IaaP Guard GitHub App operated by Infrastructure Product Works, not the separate marketing website, Cloudflare-protected demonstrations, or other IPW products. GitHub's own privacy practices apply separately to GitHub accounts and its platform.

## Information processed for Guard evaluations

The hosted App receives GitHub webhook events associated with its installation and pull requests. The public product contract requests metadata (read), repository contents (read), pull requests (read), and checks (read/write). It uses installation-scoped credentials to read repository revisions and publish the `IaaP Guard / Architecture` Check with rule findings and evidence. A Check may identify repository paths, rules, scores, findings, and evidence continuity. Repository files and pull-request material can contain personal or sensitive information if an organization puts it there; avoid committing secrets or unnecessary personal data.

## Service providers and processing location

The deployed webhook adapter runs on AWS Lambda in `us-east-2`, using AWS Secrets Manager for App credentials and AWS CloudWatch for operational logging. The App uses GitHub APIs for installation-scoped repository access and Check publication. **Confirm** whether additional providers, cross-region backups, data transfers, telemetry, or other deployments are used before approving this notice. The AWS region alone is not a guarantee that all data stays in one country.

## Security and operational boundaries

The webhook adapter verifies GitHub's webhook signature before processing events. GitHub App tokens are short-lived and installation-scoped. The public App contract does not grant repository content write, workflow administration, merge, cloud provisioning, or deployment authority. Security reports should use GitHub Private Vulnerability Reporting rather than public issues.

## Logging and retention — review required

The current AWS deployment template configures a 14-day CloudWatch log retention period for the Lambda function's designated log group. **This is not a verified universal retention or deletion commitment.** The service owner must verify what webhook metadata, payload fields, repository contents, Check outputs, GitHub records, AWS service logs, backups, and any other operational data are stored; how long each is retained; and how access, correction, deletion, and security requests are handled. Do not assume all records are deleted after 14 days.

## Purposes, sharing, and user requests — review required

The observed service purpose is processing installation events and evaluating pull-request changes to publish architecture Checks. Before approval, verify all purposes, categories of recipients and processors, international transfer practices, applicable legal bases and rights, contact details, and whether any optional analytics or model training occurs. No assertion is made here about unverified practices.

## Support and contact

Product support instructions: [IaaP Guard support](SUPPORT.md). The operator must confirm a monitored privacy/support contact address before this notice becomes effective.

## Approval checklist

- [ ] Confirm legal operator name and privacy contact address
- [ ] Verify all data categories and sources from the running production implementation
- [ ] Verify GitHub and AWS processing and any additional subprocessors
- [ ] Verify actual retention, backups, deletion, and access-request handling
- [ ] Verify geographic processing and any transfer disclosures
- [ ] Verify security and incident contact procedures
- [ ] Obtain legal/privacy owner approval and effective date
- [ ] Publish approved notice on a publicly accessible, stable URL, then update the Marketplace required privacy-policy field
