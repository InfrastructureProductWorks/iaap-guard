# IaaP Guard — public Marketplace review resources

This page provides GitHub-hosted resources for reviewing the IaaP Guard GitHub App. These links do not pass through the Infrastructure Product Works portfolio's Cloudflare access controls.

| Resource | Public destination |
| --- | --- |
| GitHub App | https://github.com/apps/iaap-guard |
| Product and documentation | https://github.com/InfrastructureProductWorks/iaap-guard |
| Installation prerequisites | https://github.com/InfrastructureProductWorks/iaap-guard/blob/main/docs/ADOPTION-PREREQUISITES.md |
| Support instructions | https://github.com/InfrastructureProductWorks/iaap-guard/blob/main/docs/SUPPORT.md |
| Security and vulnerability reporting | https://github.com/InfrastructureProductWorks/iaap-guard/blob/main/SECURITY.md |
| Known limitations | https://github.com/InfrastructureProductWorks/iaap-guard/blob/main/docs/KNOWN-LIMITS.md |
| Product architecture | https://github.com/InfrastructureProductWorks/iaap-guard/blob/main/docs/ARCHITECTURE.md |

## Functional acceptance for reviewers

Install the GitHub App on a repository you control, granting only the documented repository permissions. Open a pull request changing a supported YAML, JSON, Terraform/HCL, Markdown, Python or shell file. The hosted App should publish the `IaaP Guard / Architecture` Check on the current PR head. The Check provides architecture evidence; it does not authorize deployments or changes.

If the Check is missing, consult [support](docs/SUPPORT.md) and [known limits](docs/KNOWN-LIMITS.md). A successful health endpoint response alone is not proof of pull-request processing.

## Legal and contact information

The Apache-2.0 license in this repository applies to its public contents; it is **not** a substitute for a customer privacy policy or commercial terms for the hosted service. Marketplace privacy-policy and terms-of-service URLs must be supplied from reviewed, approved legal documents. A monitored support email address must be verified separately before being entered into the listing.

Do not use a Cloudflare-restricted portfolio or demo URL as a required public Marketplace review destination.
