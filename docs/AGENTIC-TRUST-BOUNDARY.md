# Agentic Trust Boundary

IaaP Guard treats MCP-derived context as **input**, not authority.

## Rules

- Customer MCP connectivity never grants infrastructure, approval, merge, apply, deployment, remediation, IAM, or provisioning authority.
- Any MCP-derived fact that materially influences an infrastructure-product decision must be represented in deterministic input or evidence with source/provenance metadata when required.
- Missing, altered, mismatched, stale, or unauthorized MCP-derived evidence must fail closed where the governed contract requires that evidence.
- Direct paths from MCP to Crossplane administration, Terraform apply, privileged provider APIs, IAM mutation, or direct provisioning are prohibited by the reference architecture.
- Composite AI may consume approved MCP context or bounded tools, but infrastructure-changing intent must still cross the normal contract, entitlement, Guard, evidence, authorization, and fulfillment boundaries.

## Relationship to the portfolio

The canonical architecture is maintained in `InfrastructureProductWorks/ai-powered-infrastructure-as-a-product/docs/GOVERNED-AGENTIC-INTEROPERABILITY.md`.

Guard remains the deterministic validation boundary. MCP is an interoperability protocol, not a substitute for Guard and not an infrastructure control plane.
