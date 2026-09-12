# Governed Product Validation

IaaP Guard validates whether proposed infrastructure change satisfies the deterministic rules actually present in its accepted rule catalog. It does not define Security policy intent, provision infrastructure, or approve infrastructure.

## Where Guard fits

```text
Governance / Security
  → define baselines, standards, evidence, exception criteria
Platform Engineering
  → encode those requirements into service-product contracts and implementations
Guard
  → validate the implemented deterministic architecture/evidence rules in its rule catalog
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

Composite products should inherit those constraints from the governed service products they compose. This is a portfolio operating-model requirement; it is not a claim that every listed control is already represented by a built-in Guard V1 rule.

## Current Guard validation scope

Guard's supported V1 behavior is bounded by the frozen accepted rule catalog. The current catalog focuses on Infrastructure-as-a-Product architecture and evidence concerns such as product boundaries, authority boundaries, lifecycle/evidence expectations, traceability, and related deterministic architecture checks.

A Guard PASS means that the evaluated change passed the rules that were actually executed. It must **not** be interpreted as proof that every possible security, compliance, networking, identity, encryption, logging, cost, quota, or entitlement requirement has been checked.

## Security and service-product controls

The broader governed service-product model expects minimum security, architecture, entitlement, and evidence requirements to become executable policy over time. Those requirements may be enforced by one or more layers, including:

- closed product schemas and contracts;
- provider-specific compositions and implementation tests;
- cloud-native organization/policy controls;
- admission or policy engines;
- future accepted Guard rules or customer-supplied deterministic policy where explicitly supported;
- human exception review for deviations that cross the approved product envelope.

Guard should only claim validation for a control when an implemented, accepted rule actually evaluates that control and produces the corresponding evidence.

## What Guard does not own

Guard does not:

- decide the organization's security policy;
- imply that absent rules were evaluated;
- define commercial pricing or customer licensing;
- grant product entitlement;
- approve exceptions;
- merge or deploy changes;
- reconcile cloud state.

Security and governance define **what must remain true**. Platform Engineering makes those requirements executable. Guard answers only the questions represented by its implemented deterministic rules.

> **Review the product once. Automate compliant consumption. Escalate exceptions.**
