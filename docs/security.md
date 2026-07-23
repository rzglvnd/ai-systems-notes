# Security

Security for AI systems spans data handling, model behavior, and infrastructure.

Control areas

- Data protection: classify inputs/outputs and enforce access boundaries.
- Secret management: keep API keys and tokens in secure secret stores.
- Prompt safety: define policies for unsafe or disallowed requests.
- Network security: restrict east-west service traffic where possible.
- Dependency hygiene: pin and regularly scan dependencies.

Operational practices

- Log request IDs and security-relevant events.
- Implement rate limits and abuse detection.
- Review model outputs for policy and compliance risks.
