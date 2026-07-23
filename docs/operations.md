# Operations

Operational readiness means reliable service behavior under normal and failure conditions.

Runbook essentials

- Liveness and readiness probes.
- Alerting thresholds for latency/errors.
- Rollback process for model or prompt regressions.
- Incident response checklist and owners.

Suggested SLOs

- API availability: 99.9%
- P95 latency target per critical endpoint
- Error budget policy aligned to release cadence

Change management

- Require CI checks before merge.
- Record architecture-impacting changes as ADRs.
- Test rollout with canary environments where possible.
