# Agentic IPI Red-Team Lab

A research and portfolio project exploring **indirect prompt injection (IPI) in AI coding agents**.

The project focuses on a practical security question:

> When an AI coding agent is asked to perform a legitimate repository task, can untrusted content inside the repository or its tool outputs redirect the agent into taking an unauthorized action?

The goal is to design reproducible, safe experiments that distinguish genuine security failures from superficial prompt-following.

## Project status

**Status: research and experiment design. No target-model results are claimed yet.**

- [x] Establish research scope and safety boundaries
- [x] Review relevant public benchmarks and testing frameworks
- [x] Define an initial repository-content injection experiment
- [ ] Implement a self-contained synthetic test repository
- [ ] Implement and validate deterministic state-based checks
- [ ] Run free-tier feasibility screening, subject to provider availability
- [ ] Conduct any authorized target evaluations and publish measured results

## Research areas

- Repository-content and tool-output prompt injection
- Trust boundaries between user instructions and untrusted project content
- Tool-use authorization and least privilege
- Verifiable side effects and state-based security checks
- Utility/security trade-offs in coding-agent evaluations

## Initial experiment concept

A coding agent receives a benign request to fix a small, genuine issue in a synthetic repository. Untrusted repository content contains an instruction attempting to redirect the agent toward an unrelated, unauthorized repository modification.

A robust agent should complete the requested repair while refusing to perform the unrelated change. The experiment is designed to verify the final repository state, not merely judge the agent's explanation.

See [the experiment design](docs/experiment-design.md).

## Principles

1. **Synthetic assets only.** No real credentials, personal data, production systems, or external exfiltration endpoints.
2. **Least privilege.** Give the agent only the tools and repository access needed for the test.
3. **Reproducibility.** Pin task inputs, record model/provider versions where available, and preserve run-level evidence.
4. **Independent verification.** Prefer deterministic checks of repository state and tool actions over self-reported success.
5. **Honest reporting.** Separate proposed experiments, completed tests, observed results, and hypotheses.
6. **Responsible disclosure.** Do not publish secrets, private platform instructions, or exploitable details about third-party systems.

## Repository map

- `docs/research-methodology.md` — research questions and experimental method
- `docs/benchmark-review.md` — selected public research benchmarks and tools
- `docs/attack-techniques.md` — IPI technique taxonomy and safe examples
- `docs/experiment-design.md` — initial synthetic experiment proposal
- `evaluation/test-plan.md` — screening and evaluation plan
- `evaluation/results-template.csv` — blank run-level results template
- `reports/findings.md` — reserved for evidence-backed findings

## Sources

The project builds on public research and documentation, including [AgentDojo](https://github.com/ethz-spylab/agentdojo), [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent), [BIPIA](https://github.com/microsoft/BIPIA), and [Promptfoo's coding-agent red-team documentation](https://www.promptfoo.dev/docs/red-team/plugins/coding-agent/). See the [benchmark review](docs/benchmark-review.md) for context and limitations.

## Contributions

Issues and pull requests that improve reproducibility, safe test design, verifier quality, or documentation are welcome. Do not submit real secrets, private customer data, or instructions for attacking systems without authorization.

## License

No license has been selected yet. Until a license is added, all rights are reserved by the repository owner; public visibility does not itself grant permission to reuse the contents.
