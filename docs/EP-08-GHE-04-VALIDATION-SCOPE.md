# EP-08 GHE-04: public Guard validation scope

**Disposition:** bounded implementation validation accepted on 2026-09-16.  
**Evidence basis:** maintainer attestation following review, merge, and successful validation of the accepted implementation revision. The implementation evidence is retained privately; this public statement does not make that evidence independently reproducible from this repository.  
**Live customer-runner execution and GHES support:** not observed or claimed.

The accepted implementation has an opt-in self-hosted deterministic validation path. Its entry point is bound to an immutable default-branch event revision, fixed runner routing, read-only repository access, and nonpersisted checkout credentials. The reviewed validation path isolates inherited execution settings, checks its complete workflow contract, and reserves time for cleanup after validation timeout.

This public repository remains a contract, documentation, and distribution surface. Its publication boundary prohibits executable product implementation and the retired Composite Action. Therefore it deliberately contains no product runner implementation. Existing hosted publication and contract checks remain their baseline; this scope statement does not claim that every public Actions workflow has been ported.

The Guard product milestone can proceed to GHE-05 private-CA/proxy/TLS validation and then GHE-06 restricted-network work. Portfolio-wide reconciliation is maintained separately. The currently supported hosted GitHub.com App adoption path remains unchanged. Customer installation, self-hosted execution, live GHES version acceptance, private-CA/proxy behavior, restricted egress, and support readiness are not established by this attestation.

No private implementation content, producer revision, workflow/job identifier, cloud coordinate, credential, raw operational log, customer data, or additional execution authority is published here. No deployment, provisioning, approval, pilot, production, or policy authority is added.
