# EP-08 GHE-01 — Customer-controlled GitHub portability

**Posture:** `CONTINUE_VALIDATION`  
**Evidence class:** synthetic contract evidence  
**Live GHES support:** `NOT OBSERVED`

## Purpose

This tranche separates IaaP Guard's customer-controlled GitHub portability contract from the currently supported hosted GitHub.com App path. It does not rewrite or weaken the accepted GitHub.com distribution evidence.

The currently supported path remains the hosted IaaP Guard GitHub App on GitHub.com. This document defines a synthetic portability boundary for a future customer-controlled GitHub App deployment on GitHub Enterprise Server (GHES), without claiming that a live GHES target has been validated.

## Contract

The machine-readable contract is `schemas/customer-controlled-github.schema.json`. The synthetic GHES fixture is `config/customer-controlled-github-ghes.synthetic.json`.

The contract represents exactly two bounded platform states:

1. `github.com`: the preserved vendor-hosted Guard App baseline, with customer-controlled installation and explicit repository selection; and
2. `ghes`: a synthetic customer-controlled App and installation contract for a future authorized GitHub Enterprise Server target.

GitHub Enterprise Cloud with data residency on `GHE.com` is a hosted cloud platform and is not represented by the `ghes` state in this v0 contract. `ghe.com` and its true subdomains are therefore excluded from GHES coordinates along with `github.com` and its true subdomains.

The contract requires:

- an explicit GitHub platform selection (`github.com` or `ghes`);
- canonical HTTPS web and API coordinates;
- customer ownership of the installation;
- customer ownership of the GitHub App for GHES;
- vendor-hosted App ownership for the preserved GitHub.com baseline;
- explicit repository selection;
- the same bounded repository permissions used by the current Guard App: metadata read, contents read, pull-request read, and checks write;
- no embedded credentials;
- no customer/GHES target network probing in this evidence tranche;
- `supportClaim: false` for this synthetic portability record;
- `authorizedTargetObserved: false`; and
- no added repository-write, infrastructure, authorization, merge, or deployment authority.

`supportClaim: false` is scoped to this synthetic customer-controlled portability record. It does not revoke or contradict the separately accepted hosted GitHub.com Guard App support path.

GHE-01 is a custody, coordinate, permission, and authority portability contract. It is not a replacement GitHub App registration manifest. Existing Guard event subscriptions remain governed by the accepted GitHub App contract; this tranche does not claim that those subscriptions have been registered or exercised on GHES.

## Canonical GHES coordinate profile

GHE-01 v0 intentionally uses a narrow coordinate representation so the published schema and deterministic validator have one meaning rather than several equivalent URI spellings.

For `platform: ghes`:

- `webBaseUrl` is exactly `https://<fqdn>`;
- `apiBaseUrl` is exactly `https://<fqdn>/api/v3`;
- hostnames are lowercase ASCII DNS names with at least two labels;
- each DNS label is 1–63 characters and the hostname is at most 253 characters;
- internationalized/punycode hostnames are outside this v0 evidence contract because IDNA equivalence has not been validated;
- literal IPv4/IPv6 addresses and legacy numeric address spellings, single-label names, explicit ports, trailing root dots, trailing slashes, userinfo, query strings, fragments, semicolon parameters, percent-encoded hostname aliases, Unicode separator aliases, and trailing control characters are outside this v0 evidence contract; and
- hosted GitHub domains (`github.com`, `ghe.com`, and their true subdomains) are excluded from GHES coordinates.

The web and API hostnames are validated independently and are not required to be identical. This contract does not infer or claim a particular reverse-proxy, split-DNS, CNAME/resolved-destination equivalence, or API topology because no authorized GHES target has been observed or probed. The exclusions above are evidence-scope boundaries, not claims that GHES itself can never be configured differently.

## Customer custody model

For a future customer-controlled GHES deployment, the customer owns and controls:

1. the GitHub Enterprise environment;
2. GitHub App registration and installation;
3. App credentials and secret storage;
4. repository selection;
5. network policy and trust configuration;
6. installation lifecycle, including removal; and
7. self-hosted runner configuration and operation. The accepted bounded implementation-validation scope is described in [GHE-04 public validation scope](EP-08-GHE-04-VALIDATION-SCOPE.md); live customer-runner execution remains unobserved.

Infrastructure Product Works supplies the Guard contract and implementation package. The contract does not grant Infrastructure Product Works standing access to the customer's GitHub environment.

## Current GitHub.com path remains unchanged

The hosted `github.com/apps/iaap-guard` application remains the only currently supported Guard adoption path. Existing documentation and historical acceptance evidence are intentionally retained.

The customer-controlled/GHES contract is additive. It must not be interpreted as proof that:

- Guard has been installed on a live GHES instance;
- App registration or installation has succeeded on GHES;
- GHES event-subscription compatibility has been established;
- GHES version compatibility has been established;
- private CA, proxy, or TLS-interception behavior has been validated;
- restricted-egress or disconnected operation has been validated; or
- production, pilot, FedRAMP, ATO, cATO, or FISMA readiness has been established.

## Validation

`.github/workflows/ghe01-portability-contract.yml` performs deterministic static checks against the synthetic contract. It locks the complete published schema and the synthetic GHES fixture to their approved canonical records, validates both platform states, independently checks semantic invariants, executes positive and negative cases that must remain deterministic and fail closed, and cross-checks GHE-01 repository permissions against `config/github-app-v0.json`. Changes to that current App contract also trigger the GHE-01 validation workflow.

The workflow may retrieve its pinned validation dependencies from the normal GitHub Actions execution environment. It does not probe a customer or GHES target, use customer credentials or data, provision infrastructure, execute Crossplane, approve or merge changes, or gain deployment authority.

## Exit from this tranche

GHE-01 may advance from synthetic contract definition only after the protected-main contract and deterministic validation are accepted. That acceptance still does not close GHE-07 or GHE-08. Live support remains gated on an authorized GHES target and digest-bound portability evidence.
