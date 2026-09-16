# EP-08 GHE-05: public Guard validation scope

**Disposition:** bounded synthetic GitHub-client validation accepted on 2026-09-16.  
**Evidence basis:** maintainer attestation following review, protected merge and successful validation of the accepted implementation revision. Evidence remains privately retained; this public statement is not independently reproducible implementation proof.  
**Portfolio GHE-05 closure, customer-runner execution and live GHES support:** unclaimed.

The accepted client profile uses an explicit private-CA bundle, mandatory certificate and hostname verification, TLS 1.2 or newer, and optional unauthenticated HTTP CONNECT routing for HTTPS requests. Synthetic loopback checks cover successful verified connections and fail-closed handling of untrusted, expired and wrong-host certificates, obsolete TLS, proxy failures, credential forwarding, unsafe redirects and invalid configuration. The client does not fall back to direct egress after a configured proxy failure or enable insecure verification defaults.

This profile is **HTTPS-over-HTTP-CONNECT**. It does not validate a TLS-encrypted connection to the proxy itself, authenticated proxies, PAC, mTLS, revocation services or real customer interception appliances. Other portfolio transports and checkout, package installation, cloud SDK, deployment and telemetry networking are outside this proof. Operator-controlled trust provisioning, egress policy, execution limits and the trusted-runner prerequisites remain required.

This acceptance does not deploy the hosted App or change its supported GitHub.com adoption path. It does not establish customer installation, customer-runner execution, live GHES version support, restricted-network readiness, pilot or production readiness. GHE-05 remains open for additional product-specific trust/proxy profiles; GHE-06 dependency profiles follow, and GHE-07/GHE-08 live acceptance remains gated.

This public repository contains contracts, documentation and sanitized assurance statements. It publishes no executable product implementation, private producer revision, workflow/job identifier, cloud coordinate, credential, customer data or raw operational log. No deployment, provisioning, approval, merge, pilot, production or policy authority is added.
