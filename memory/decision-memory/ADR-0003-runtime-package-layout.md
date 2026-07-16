# ADR-0003: Runtime Package Layout

| Field | Value |
|-------|-------|
| Status | Accepted |
| Date | 2026-07-15 |
| Deciders | Architect |

## Context

Labs need an executable Python package beside Markdown Company OS docs.

## Decision

Place runtime under `runtime/` with `company_os/` library and `labs/` entrypoints, managed by `uv`.

## Consequences

### Positive
- Clear separation of docs vs executable labs
- Reusable FeatureGraph/BugFixGraph modules

### Negative
- Dual mental model (Markdown SoT + Python runtime)

## Rejected Alternatives

| Option | Why Rejected |
|--------|--------------|
| Scripts scattered at repo root | Hard to package/test |
| Notebooks only | Weak CI / weak graph reuse |
