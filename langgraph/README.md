# LangGraph Design Index

| Graph | Workflow | Entry | Terminal |
|-------|----------|-------|----------|
| FeatureGraph | create-feature | `intake` | `done` / `escalated` |
| BugFixGraph | fix-bug | `triage` | `done` / `escalated` |
| ReleaseGraph | release | `preflight` | `released` / `rolled_back` / `aborted` |

## Shared Conventions

- State is typed (see each graph doc) and persisted per run_id.
- Nodes read Markdown artifacts from the repo; they do not invent missing specs.
- Conditional edges implement Approval Gates and Escalation Rules.
- Human Operator interrupts are allowed on CEO escalation nodes.

## Runtime Layout (planned)

```text
langgraph/
  README.md
  state.py                 # shared TypedDict / pydantic state
  feature_graph.py
  bugfix_graph.py
  release_graph.py
  nodes/                   # one module per role node
  feature-graph.md         # design (this folder)
  bugfix-graph.md
  release-graph.md
```

Implementation Python modules are added when the runtime is bootstrapped; Markdown designs are Source of Truth until then.
