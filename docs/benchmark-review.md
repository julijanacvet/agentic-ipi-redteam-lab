# Public Benchmark and Tooling Review

This is a selective orientation to public resources relevant to indirect prompt injection and tool-using agents. It is not an exhaustive systematic review.

## AgentDojo

**Project:** [ethz-spylab/agentdojo](https://github.com/ethz-spylab/agentdojo)  
**Paper:** [AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents](https://arxiv.org/abs/2406.13352)

AgentDojo provides a dynamic benchmark environment for evaluating prompt-injection attacks and defenses in tool-using agents. Its task-oriented setup is relevant because it evaluates agents interacting with tools and environments, rather than only classifying isolated text.

**Relevance here:** a useful design reference for realistic tasks, controlled environments, and evaluating both task utility and security.

**Limitations:** benchmark tasks and environments do not automatically predict the behavior of a different agent, model, tool configuration, or platform. Reproduction requires attention to the benchmark's version and setup.

## InjecAgent

**Project:** [uiuc-kang-lab/InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent)  
**Paper:** [InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents](https://arxiv.org/abs/2403.02691)

InjecAgent studies indirect prompt injection in tool-integrated agents. Its cases distinguish attacks that seek harmful actions from attacks that seek disclosure of private information. Its repository includes user tasks and attacker cases, making it useful for studying how an ordinary task can encounter adversarial tool-returned content.

**Relevance here:** useful taxonomy and examples for separating the user's legitimate objective from the attacker's objective, and for considering multi-step tool interactions.

**Limitations:** results from the paper reflect the models, agent setup, and evaluation conditions used at that time. They should not be presented as current success-rate predictions for newer models. A static benchmark response is also not equivalent to verifying a live coding agent's final repository state.

## BIPIA

**Project:** [microsoft/BIPIA](https://github.com/microsoft/BIPIA)  
**Paper:** [Benchmarking and Defending Against Indirect Prompt Injection Attacks on Large Language Models](https://arxiv.org/abs/2312.14197)

BIPIA examines indirect prompt injection across several content-processing settings, including question answering and summarization tasks.

**Relevance here:** helps reason about how malicious instructions can be embedded in otherwise relevant external content, and how presentation or stealth can affect detection.

**Limitations:** content-processing evaluations are not the same as end-to-end coding-agent evaluations with repository writes, shell commands, and stateful tools.

## Promptfoo coding-agent red-team documentation

**Documentation:** [Coding Agent Plugins](https://www.promptfoo.dev/docs/red-team/plugins/coding-agent/)  
**Documentation:** [Red Team Configuration](https://www.promptfoo.dev/docs/red-team/configuration/)

Promptfoo documents security tests specifically for coding-agent environments, including repository prompt injection, terminal-output injection, secret-access boundaries, sandbox boundaries, network egress, and verifier-related risks. Its coding-agent evaluation approach can use an actual agent harness and inspect traces or workspace changes.

**Relevance here:** useful for organizing test categories and designing checks around tool traces and repository state.

**Limitations:** availability of particular plugins, attack-generation strategies, providers, and cloud features depends on configuration and may require remote services or paid access. A documented feature is not proof that it is available in every environment or free tier.

## How these sources inform this project

The initial project design adopts four broad lessons:

1. Evaluate agents in a task environment, not only with isolated prompt-response questions.
2. Make the user's intended task and the attacker's objective distinct.
3. Treat repository files and tool outputs as untrusted data unless explicitly granted authority.
4. Verify actual side effects with deterministic checks.

This review summarizes the resources for project planning. It does not claim that this repository has reproduced their experiments or independently validated their reported results.
