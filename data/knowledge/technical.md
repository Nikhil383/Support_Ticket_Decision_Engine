# Technical Support

## Service Errors

Technical tickets may involve: - API errors - Login failures - Service
outages - Timeouts - Application errors - Integration problems

## Production Incidents

Reports affecting production systems or multiple customers should be
treated as potentially high priority.

Examples include: - Widespread login failures - Repeated HTTP 5xx
errors - A production API becoming unavailable - A service outage
affecting multiple customers

These cases may require human review or escalation.

## API Errors

HTTP 5xx responses generally indicate that the server could not
successfully process a request.

When investigating an API issue, collect: - Endpoint - HTTP status
code - Approximate start time - Request or correlation ID, if
available - Whether the issue affects one customer or multiple customers

Do not claim that an outage has been confirmed unless the available
evidence confirms it.

## Troubleshooting

Support responses should use the available technical knowledge and
evidence.

If the retrieved knowledge does not contain enough information to
diagnose or resolve the issue, state that the available information is
insufficient and escalate when appropriate.

Do not invent commands, fixes, incident status, or recovery timelines.
