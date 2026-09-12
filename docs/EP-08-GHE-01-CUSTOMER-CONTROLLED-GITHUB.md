# EP-08 GHE-01 — Customer-controlled GitHub portability

**Posture:** `CONTINUE_VALIDATION`  
**Evidence class:** synthetic contract evidence  
**Live GHES support:** `NOT OBSERVED`

## Purpose

This tranche separates IaaP Guard's customer-controlled GitHub portability contract from the currently supported hosted GitHub.com App path. It does not rewrite or weaken the accepted GitHub.com distribution evidence.

The currently supported path remains the hosted IaaP Guard GitHub App on GitHub.com. This document defines a synthetic portability boundary for a future customer-controlled GitHub App deployment, including GitHub Enterprise Server, without claiming that a live GHES target has been validated.

## Contract

The machine-readable contract is `schemas/customer-controlled-github.schema.json`. The synthetic GHES fixture is `config/customer-controlled-github-ghes.synthetic.json`.

The contract requires:

- an explicit GitHub platform selection (`github.com` or `ghes`);
- HTTPS web and API base URLs rather than hard-coded GitHub.com runtime coordinates;
- customer ownership of the installation;
- customer ownership of the GitHub App for GHES;
- explicit repository selection;
- the same bounded repository permissions used by the current Guard App: metadata read, contents read, pull-request read, and checks write;
- no embedded credentials;
- no network probing in this evidence tranche;
- `supportClaim: false`;
- `authorizedTargetObserved: false`; and
- no added repository-write, infrastructure, authorization, merge, or deployment authority.

## Customer custody model

For a future customer-controlled GHES deployment, the customer owns and controls:

1. the GitHub Enterprise environment;
2. GitHub App registration and installation;
3. App credentials and secret storage;
4. repository selection;
5. network policy and trust configuration;
6. installation lifecycle, including removal; and
7. any later self-hosted runner configuration introduced under GHE-04.

Infrastructure Product Works supplies the Guard contract and implementation package. The contract does not grant Infrastructure Product Works standing access to the customer's GitHub environment.

## Current GitHub.com path remains unchanged

The hosted `github.com/apps/iaap-guard` application remains the only currently supported Guard adoption path. Existing documentation and historical acceptance evidence are intentionally retained.

The customer-controlled/GHES contract is additive. It must not be interpreted as proof that:

- Guard has been installed on a live GHES instance;
- App registration or installation has succeeded on GHES;
- GHES version compatibility has been established;
- private CA, proxy, or TLS-interception behavior has been validated;
- restricted-egress or disconnected operation has been validated; or
- production, pilot, FedRAMP, ATO, cATO, or FISMA readiness has been established.

## Validation

`.github/workflows/ghe01-portability-contract.yml` performs deterministic static checks against the synthetic contract. It verifies the customer-custody and no-authority invariants and executes negative mutations that must fail closed.

No credentials, live network calls, customer data, infrastructure provisioning, Crossplane execution, approval authority, or deployment authority are introduced by this tranche.

## Exit from this tranche

GHE-01 may advance from synthetic contract definition only after the protected-main contract and deterministic validation are accepted. That acceptance still does not close GHE-07 or GHE-08. Live support remains gated on an authorized GHES target and digest-bound portability evidence.
