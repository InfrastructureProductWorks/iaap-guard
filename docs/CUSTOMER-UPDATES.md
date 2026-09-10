# IaaP Guard customer update lifecycle

IaaP Guard™ follows the Infrastructure Product Works™ documentation-first customer update policy.

A customer-impacting Guard change is documented before it is presented as a supported stable update. Documentation is part of the release contract, not a post-release explanation.

## Update sequence

The customer update lifecycle is:

`Documentation -> Candidate Release -> Compatibility Validation -> Customer Review -> Customer-Authorized Adoption -> Verification`

Publishing a new Guard version does not by itself authorize a customer installation to adopt it.

## What counts as a customer-impacting Guard update

This lifecycle applies when an update changes one or more of the following:

- deterministic evaluation behavior or findings;
- policy or rule semantics;
- supported input, evidence, schema, or contract versions;
- GitHub App permissions, subscribed events, or data-handling behavior;
- customer-visible Check behavior or supported integration behavior;
- installation, upgrade, rollback, or uninstall expectations;
- documented authority or security boundaries; or
- compatibility with an environment previously described as supported.

Provider-operated maintenance that preserves the documented customer contract may be performed without requiring a customer adoption action. It must not be used to silently introduce a customer-impacting semantic, permission, data-handling, or authority change.

## Required documentation before stable distribution

Before a customer-impacting Guard update is offered as a supported stable release, the release record must document:

1. what changed and why;
2. the affected Guard release and component versions;
3. whether deterministic evaluation semantics changed;
4. whether policy or rule semantics changed;
5. supported prior-version compatibility and prerequisites;
6. any required customer action;
7. adoption or upgrade instructions;
8. rollback instructions and retained rollback target;
9. uninstall considerations where applicable;
10. known limitations and unsupported conditions;
11. security, permission, data-handling, and authority-boundary implications;
12. source revision and artifact or package digests where the distribution surface exposes them; and
13. the documentation revision associated with the release.

A release note should say `not applicable` when a lifecycle or authority item genuinely does not apply rather than leave a material question ambiguous.

## Hosted GitHub App customer selection

Installing the IaaP Guard GitHub App establishes the bounded GitHub integration described in [GITHUB-APP-BETA.md](GITHUB-APP-BETA.md). It does not grant IaaP Guard permission to rewrite customer repositories, merge pull requests, deploy infrastructure, hold cloud credentials, or silently authorize customer adoption of a new governance contract.

The concrete customer-selection contract is repository owned. When supported by the deployed Guard runtime, a customer may add `.iaap/guard-update.json` to the repository through its normal change-management process:

```json
{
  "schemaVersion": "iaap-guard-update-selection/v1",
  "policyCatalogVersion": "<published-catalog-version>",
  "policyCatalogDigest": "sha256:<published-catalog-digest>"
}
```

The App reads this file using its existing Contents read permission. It does not create or modify the file.

The selected catalog must be one of the immutable policy catalogs bundled by the deployed Guard runtime, and the configured digest must match that bundled catalog exactly. Unknown versions, duplicate bundled catalog identities, malformed selection documents, unexpected fields, or digest mismatches fail closed rather than falling forward to another policy version.

If `.iaap/guard-update.json` is absent, Guard uses the runtime's explicitly packaged default catalog. This preserves backward compatibility for existing installations. Absence is not treated as permission for Guard to rewrite customer configuration.

A customer adopts a new policy catalog by reviewing the documentation and compatibility evidence and then changing the version and digest in `.iaap/guard-update.json`. Rollback is the inverse customer-controlled change to a previously supported bundled catalog version and digest.

This mechanism separates provider-operated runtime maintenance from customer-selected governance semantics. A runtime release may carry multiple immutable supported catalogs so a newer runtime can continue evaluating a customer against its selected older catalog while a newer candidate remains available for review.

The selection mechanism does not require repository content-write permission and contains no `autoUpdate`, `autoInstall`, merge, deployment, or infrastructure-execution authority.

Until a Guard runtime containing this selection contract is accepted and deployed, the current hosted App continues to use its packaged default policy catalog. Documentation of this mechanism does not claim that a not-yet-deployed runtime feature is already active.

## Engine, policy, and contract identity

Guard updates distinguish these identities where the distribution mode supports separate versioning:

- **evaluation engine** - the deterministic implementation version;
- **policy or rule bundle** - the version of deterministic governance semantics;
- **contract/schema set** - the accepted input and evidence contract versions; and
- **distribution surface** - the GitHub App, local/offline package, or another explicitly supported Guard distribution mode.

A runtime implementation fix that does not change evaluation semantics is materially different from a policy update that can change an evaluation outcome. Release documentation must make that distinction clear.

## Compatibility validation

When a candidate update can affect evaluation outcomes or accepted contracts, the preferred update path is to compare the candidate against the currently selected behavior before adoption.

A compatibility result should answer at least:

- whether the candidate can evaluate the customer's supported inputs;
- whether contract/schema compatibility is preserved;
- whether findings or conclusions differ from the current supported version; and
- whether a difference requires customer review before adoption.

A compatibility result is evidence for a decision. It is not adoption authority.

Where candidate comparison is not yet implemented for a distribution mode, the release documentation must say so and provide the bounded validation steps that are available.

## Customer notification

A Guard update-notification surface may report information such as:

- current or selected supported version;
- available candidate or stable version;
- release-documentation reference;
- compatibility status when available; and
- whether customer action is required.

Such a notification remains advisory unless the customer separately performs the documented adoption action. Notification alone must not rewrite repository content, change a selected evaluation contract, merge a change, or activate infrastructure authority.

## Customer-authorized adoption

For the hosted selection contract, adoption is an explicit customer-controlled change to `.iaap/guard-update.json`. Other future customer-pinned Guard distribution modes may use an equivalent immutable version or digest selection in customer-owned configuration or source control.

The adoption record should preserve enough information to identify:

- prior selected version;
- newly selected version;
- applicable artifact or revision digest;
- documentation revision;
- compatibility evidence when produced; and
- the customer-controlled change that authorized the selection.

The GitHub App does not need repository content-write permission to satisfy this model. Customers make and review the adoption change using their existing change-management process.

## Verification after adoption

After a customer-authorized update, verify the selected release against its documented contract. Verification should confirm the expected version or revision, integrity reference where applicable, supported contract state, and expected bounded Guard behavior.

A successful verification does not create cloud execution, merge, provisioning, remediation, or production authority.

## Rollback

Every supported update path must provide a rollback procedure or explicitly state why rollback is not applicable.

For the hosted repository-owned selection contract, rollback means restoring `.iaap/guard-update.json` to the previously supported bundled catalog version and digest and then re-running Guard verification.

Rollback documentation must identify any evidence or configuration that must be retained to reproduce the prior state. Historical release documentation should remain available so the prior behavior can be understood rather than reconstructed from current documentation.

## Security and urgent maintenance

Security urgency does not eliminate the documentation-first rule for a customer-impacting change. The documentation may be concise or staged when disclosure itself has security implications, but customers still need an authoritative release record describing the affected versions, required action, compatibility or behavioral impact, and rollback or recovery path before the changed release is represented as the supported customer update.

Contract-neutral hosted infrastructure maintenance may proceed under the existing service boundary without pretending it is a customer-selected Guard semantic upgrade.

## Evidence retention

Where the distribution surface supports it, retain or make reproducible the relationship among:

- Guard release version;
- source revision;
- artifact/package digest;
- policy or rule-bundle identity when separately versioned;
- contract/schema identity when separately versioned;
- release documentation revision;
- compatibility evidence; and
- customer adoption evidence when generated in the customer environment.

This makes the release history useful for audit, rollback, support, and later provenance checks.

## Authority boundary

The update lifecycle does not add repository content-write, workflow administration, merge, deployment, secrets, member-management, provisioning, remediation, cloud-credential, approval, spending, pilot, production, or compliance authority.

IaaP Guard remains a deterministic architecture and evidence guard. Customer update controls must not turn it into an infrastructure execution or customer change-approval system.
