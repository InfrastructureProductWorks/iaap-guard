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

## Hosted GitHub App versus selected Guard behavior

Installing the IaaP Guard GitHub App establishes the bounded GitHub integration described in [GITHUB-APP-BETA.md](GITHUB-APP-BETA.md). It does not grant IaaP Guard permission to rewrite customer repositories, merge pull requests, deploy infrastructure, hold cloud credentials, or silently authorize customer adoption of a new governance contract.

The hosted service may receive contract-neutral operational maintenance. A change that alters supported Guard evaluation behavior, contracts, permissions, data handling, or authority boundaries is instead handled as a documented customer-impacting release.

Where a Guard distribution mode supports an explicitly selected or pinned evaluation version, that selection should remain customer controlled and integrity bound. The customer should be able to identify the selected release, its integrity reference, and the documentation that described the release.

The current hosted GitHub App permission boundary must not be widened merely to automate customer upgrades.

## Engine, policy, and contract identity

Guard updates should distinguish these identities when the distribution mode supports separate versioning:

- **evaluation engine** - the deterministic implementation version;
- **policy or rule bundle** - the version of deterministic governance semantics;
- **contract/schema set** - the accepted input and evidence contract versions; and
- **distribution surface** - the GitHub App, local/offline package, or another explicitly supported Guard distribution mode.

A runtime implementation fix that does not change evaluation semantics is materially different from a policy update that can change an evaluation outcome. Release documentation must make that distinction clear.

This document does not claim that every Guard distribution mode currently exposes all four identifiers independently. Separate identity is the update-contract direction where it can be implemented without weakening integrity or authority boundaries.

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

A future Guard update-notification surface may report information such as:

- current or selected supported version;
- available candidate or stable version;
- release-documentation reference;
- compatibility status when available; and
- whether customer action is required.

Such a notification must remain advisory unless the customer separately performs the documented adoption action. Notification alone must not rewrite repository content, change a selected evaluation contract, merge a change, or activate infrastructure authority.

This section defines the intended update experience; it does not claim that automated update notification or candidate comparison is implemented today.

## Customer-authorized adoption

For customer-pinned Guard distribution modes, adoption should be an explicit customer-controlled change such as a version, immutable revision, or digest update in customer-owned configuration or source control.

The adoption record should be reviewable and should preserve enough information to identify:

- prior selected version;
- newly selected version;
- applicable artifact or revision digest;
- documentation revision;
- compatibility evidence when produced; and
- the customer-controlled change that authorized the selection.

The GitHub App does not need repository content-write permission to satisfy this model. Customers can make and review the adoption change using their existing change-management process.

## Verification after adoption

After a customer-authorized update, verify the selected release against its documented contract. Verification should confirm the expected version or revision, integrity reference where applicable, supported contract state, and expected bounded Guard behavior.

A successful verification does not create cloud execution, merge, provisioning, remediation, or production authority.

## Rollback

Every supported update path must provide a rollback procedure or explicitly state why rollback is not applicable.

For a version-pinned distribution mode, rollback should normally mean returning the customer-controlled selection to a previously supported immutable version or digest and then re-running verification.

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
