# Technical Support Knowledge Base

## Production API Outage

Repeated 5xx errors can indicate an outage
or service degradation.

Collect:

- Start time
- Affected endpoints
- Error messages
- Scope of impact
- Environment
- Recent deployments
- Correlation IDs

If multiple customers cannot access a core
production feature, prioritize technical
investigation and consider human escalation.

Never claim an outage is resolved until
recovery is verified.

## Login Failure

Determine whether the problem affects one
customer or many.

Check authentication and application status.

Never request passwords, API keys, or
authentication secrets.

## Troubleshooting

1. Verify the issue.
2. Inspect service status and logs.
3. Determine impact.
4. Check recent changes.
5. Apply approved remediation.
6. Verify recovery.