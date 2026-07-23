# Deployment

Deployment guidance for AI services should include build, runtime config, and rollback strategy.

Recommended steps

1. Build immutable artifacts (container images).
2. Inject environment-specific configuration securely.
3. Run smoke checks on health and core inference paths.
4. Roll out gradually and observe key metrics.

Checklist

- Runtime secrets configured
- Resource limits defined
- Autoscaling policy configured
- Observability dashboards available
- Rollback command tested

Reference implementation

See the companion repos in this workspace (`local-llm-chat-engine` and `erp-ai-assistant`) for concrete FastAPI deployment examples.
