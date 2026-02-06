# OHAP JSON Schemas

This directory contains the core JSON Schema definitions for the Open Human Agent Protocol (OHAP).

## Schema Files

### Core Entities

- **[task.schema.json](task.schema.json)** - Shared unit of work with metadata, inputs, constraints, and outputs
- **[proposal.schema.json](proposal.schema.json)** - Human or broker offer to execute a task
- **[contract.schema.json](contract.schema.json)** - Accepted proposal with binding terms and shared commitments
- **[deliverable.schema.json](deliverable.schema.json)** - Output artifacts, evidence, and completion metadata
- **[review.schema.json](review.schema.json)** - Verification report, approvals, or rejection with reasons

## Usage

### Validation

Use any JSON Schema validator (draft-07 compatible) to validate OHAP messages:

```bash
# Using ajv-cli
npm install -g ajv-cli
ajv validate -s task.schema.json -d your-task.json
```

### Code Generation

Generate type definitions for your programming language:

```bash
# TypeScript
npx quicktype task.schema.json -o task.ts

# Python
pip install datamodel-code-generator
datamodel-codegen --input task.schema.json --output task.py
```

## Schema Design Principles

1. **Human-AI Fusion**: Schemas emphasize shared intent, co-ownership, and mutual responsibility
2. **Verifiability**: Evidence and provenance fields ensure accountability
3. **Asynchrony**: Support for partial updates and milestone-based progress
4. **Extensibility**: Additional properties allowed for domain-specific extensions
5. **Privacy**: Built-in data classification and consent tracking

## Examples

See the `/examples` directory (coming soon) for complete workflow examples using these schemas.

## Versioning

Schemas follow semantic versioning. Current version: **0.1**

Breaking changes will increment the major version and be reflected in the `version` field of task objects.

## Contributing

To propose schema changes:
1. Open an issue describing the use case
2. Submit a PR with schema updates and examples
3. Ensure backward compatibility or document breaking changes

## License

Same as parent project - see [LICENSE](../LICENSE)
