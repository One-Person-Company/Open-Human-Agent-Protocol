# OHAP Schema Examples

This directory contains example JSON files demonstrating how to use the OHAP schemas in real-world scenarios.

## Example Workflow: Logo Design

A complete human-AI collaborative logo design workflow:

1. **[task-example.json](task-example.json)** - An AI agent creates a logo design task with clear requirements
2. **[proposal-example.json](proposal-example.json)** - A human designer submits a proposal with approach and timeline
3. **[contract-example.json](contract-example.json)** - The accepted proposal becomes a binding contract (coming soon)
4. **[deliverable-example.json](deliverable-example.json)** - The designer submits final work with evidence and provenance
5. **[review-example.json](review-example.json)** - The initiator reviews and accepts the deliverable (coming soon)

## Key Patterns Demonstrated

### Human-AI Fusion
- Shared intent documented in task objective and collaboration context
- AI coordinates asynchronously while human works at their own pace
- Both parties contribute: AI provides requirements, human provides creative execution

### Verifiability
- Checksums for all artifacts
- Work logs documenting the process
- Source attribution and provenance tracking
- Evidence of AI tool usage with proper disclosure

### Agency & Co-ownership
- Human can negotiate scope, timeline, and cost
- Clear acceptance criteria established collaboratively
- Feedback loops and iteration supported
- Credit given to all contributors (human + AI coordinator)

## Validating Examples

```bash
# Validate task example
ajv validate -s ../task.schema.json -d task-example.json

# Validate proposal example
ajv validate -s ../proposal.schema.json -d proposal-example.json

# Validate deliverable example
ajv validate -s ../deliverable.schema.json -d deliverable-example.json
```

## More Examples Coming Soon

- Research collaboration (human literature review + AI data analysis)
- Code review (human judgment + AI static analysis)
- Content creation (human writing + AI fact-checking)
- Legal analysis (human expert interpretation + AI document processing)

## Contributing Examples

Have a great use case? Submit a PR with:
1. Complete workflow JSON files
2. Brief narrative explaining the collaboration pattern
3. Any domain-specific schema extensions used

See [CONTRIBUTING.md](../../CONTRIBUTING.md) for guidelines.
