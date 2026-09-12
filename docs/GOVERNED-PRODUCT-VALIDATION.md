# Governed Product Validation

IaaP Guard validates whether proposed infrastructure change remains inside the approved product envelope. It does not define Security policy intent and it does not provision or approve infrastructure.

## Where Guard fits

```text
Governance / Security
  → define baselines, standards, evidence, exception criteria
Platform Engineering
  → encode those requirements into service-product contracts and implementations
Guard
  → validate architecture, policy, security, entitlement, and evidence conditions
Human reviewers
  → decide exceptions and material changes where required
```

## Governed service-product expectation

Raw provider services should not be exposed directly to developers as the product boundary. Each cloud capability should first be productized into a governed service product with:

- a stable consumer contract;
- minimum security baseline;
- approved configuration envelope;
- entitlement and quota constraints;
- required evidence;
- lifecycle/versioning rules;
- exception criteria.

Composite products inherit those constraints from the governed service products they compose.

## Guard validation responsibilities

Guard can deterministically verify that a proposed change preserves requirements such as:

- mandatory security controls;
- approved architecture patterns;
- network and identity boundaries;
- required encryption and logging conditions;
- entitlement or quota constraints represented in the evaluated contract/evidence;
- evidence continuity and source binding;
- exception metadata where a governed deviation is requested.

## What Guard does not own

Guard does not:

- decide the organization's security policy;
- define commercial pricing or customer licensing;
- grant product entitlement;
- approve exceptions;
- merge or deploy changes;
- reconcile cloud state.

Security and governance define **what must remain true**. Guard answers **whether the proposed change still satisfies those declared requirements**.

> **Review the product once. Automate compliant consumption. Escalate exceptions.**
