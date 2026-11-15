# IaaP Guard GitHub App — Privacy Notice

**Last updated:** November 14, 2026  
**Service operator:** Infrastructure Product Works (IPW)  
**Applies to:** The hosted [IaaP Guard GitHub App](https://github.com/apps/iaap-guard), not the separate IPW website or its demonstrations.

## What the App does

When installed on selected GitHub repositories, IaaP Guard receives GitHub webhook events and uses GitHub APIs to inspect pull-request changes and relevant repository revisions. It evaluates architecture, policy and evidence rules and publishes an `IaaP Guard / Architecture` Check to GitHub. Findings may include repository names, file paths, rule identifiers, scores, evaluation results, and revision identifiers. These results are visible to people who can access the relevant GitHub repository and its Checks.

## Information the App processes

The App receives webhook metadata and event payloads from GitHub, including installation identifiers, repository identifiers, pull-request identifiers, commit hashes, changed-file metadata, and GitHub account identifiers included in events. To evaluate supported changes, it reads repository content at relevant revisions, including full repository archives where required by its evaluation workflow. **Repository contents can include personal or confidential information if a repository owner places it there.** Do not commit secrets or unrelated personal data for Guard to evaluate.

The App's documented GitHub permissions are metadata read, repository contents read, pull requests read, and checks read/write. The App does not request repository contents write, workflow administration, merge authority, or customer-cloud credentials. Repository administrators control which repositories are included in an installation and can revoke access through GitHub.

## Why this information is used

The service processes the above information to authenticate and handle GitHub events, determine the scope of requested checks, evaluate product and architecture rules, publish findings and evidence through GitHub Checks, and diagnose service failures and security events. Marketplace purchase notifications are acknowledged without granting repository evaluation or billing authority; the current handler does not persist marketplace account data.

## Where processing occurs and service providers

The currently deployed webhook adapter runs on **Amazon Web Services (AWS) Lambda in the US East (Ohio), us-east-2 region**. It uses AWS Secrets Manager to retrieve application credentials and AWS CloudWatch for operational logs. It uses GitHub's API and GitHub App infrastructure for event delivery, installation authorization, repository access, and Check publication. GitHub and AWS may process information under their own service terms and practices. The AWS Lambda region is **not** a guarantee that all GitHub or AWS data, support, or backups remain in that region or the United States.

## Security

The hosted adapter checks GitHub's cryptographic webhook signature before processing event content. It uses GitHub App authentication and installation-scoped tokens for authorized repository access. The current implementation scans repository archives in temporary Lambda storage and publishes Check outputs to GitHub. Security issues should be reported through [GitHub Private Vulnerability Reporting](../SECURITY.md), not through public issues containing secrets or sensitive content.

## Storage and retention

The current Lambda deployment template configures **14 days of retention for its designated CloudWatch log group**. This setting does **not** describe or guarantee retention of GitHub webhook delivery records, GitHub Checks, AWS service-level logs, backups, repository content held by GitHub, or other provider records. The evaluation implementation uses temporary storage for repository archive processing. The current Marketplace event handler does not persist purchase account data. The service does not promise a single universal deletion period across GitHub, AWS, or provider backups.

Published Check results remain in GitHub subject to repository permissions and GitHub's retention and deletion controls. Repository owners can revoke the App's access through GitHub, but uninstalling the App should not be assumed to delete previously published GitHub Check records or provider-held logs.

## Requests and support

For product questions and privacy-related requests, use the [public support instructions](SUPPORT.md) to initiate a non-sensitive inquiry. **Do not include credentials, private repository contents, sensitive personal information, or identity documents in public GitHub issues.** For security reports, use private vulnerability reporting. A monitored direct privacy contact channel and any identity verification needed for a request should be established before sensitive details are exchanged. Requests will be assessed in light of the records, access controls, and provider mechanisms actually available; this notice does not promise immediate erasure of provider backups or GitHub records.

## Other uses and updates

This notice describes the hosted GitHub App behavior identified in the current product implementation. It does not authorize using customer repository content for marketing, advertising, or model training. It does not establish a data-processing agreement, contractual service-level guarantee, or deployment authorization. Any material change in processing, additional subprocessors, optional telemetry, or data-handling commitments requires a corresponding notice and product review. Changes to this notice will be reflected by updating the date above.

For the separate IPW marketing website and Cloudflare-protected demos, see the [website privacy notice](https://infrastructureproductworks.com/privacy/), which is a different processing context.
