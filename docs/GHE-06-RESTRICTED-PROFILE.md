# GHE-06 restricted-network boundary

Public IaaP Guard is the product/adoption/contracts surface. It is **not** the
restricted-network execution engine.

For GHE-06, the bounded public-repository profile is contracts and sanitized
assurance only. The hosted GitHub App, every workflow in this repository,
devcontainer/package acquisition, hosted status publication, GitHub API access,
and the retired historical composite Action are outside that bounded runtime.

The maintained deterministic engine is private. Its separately governed GHE-06 evidence covers the executable restricted path.

`config/ghe06-restricted-profile.json` is machine-checked by the normal validation
workflow. The check fails if a workflow is added without being explicitly excluded,
if the public repository starts claiming restricted execution/support, if the
retired Action returns, or if package/telemetry/GitHub orchestration is silently
promoted into the GHE-06 runtime.

This boundary does not disable the normal hosted product. It only prevents hosted
delivery mechanics from being mistaken for restricted-network runtime support.
Customer-runner and live GHES execution remain GHE-07 work. Authorized customer
target/support acceptance remains GHE-08.
