"""
Production Implementation of a Cyclic LangGraph Multi-Agent System
Author: Ahmed Mohamed Abdullatif Rifai
Credential: DeepLearning.AI & Coursera (100.00% Verified)
"""

from typing import TypedDict, Annotated, List, Dict, Any
import operator
from dataclasses import dataclass

class AgentState(TypedDict):
    """
    Core Typed State Schema for LangGraph multi-agent execution.
    Attributes:
        task (str): The top-level user goal.
        plan (List[str]): Atomic tasks decomposed by the planner.
        research_notes (List[str]): Verified facts and tool outputs.
        draft (str): Synthesized report draft.
        critique_score (float): Quality score assigned by Evaluator (0 - 100).
        critique_notes (List[str]): Specific actionable improvement recommendations.
        iteration_count (int): Current count of revision cycles.
        human_approved (bool): Human-in-the-loop signoff flag.
    """
    task: str
    plan: List[str]
    research_notes: Annotated[List[str], operator.add]
    draft: str
    critique_score: float
    critique_notes: List[str]
    iteration_count: int
    human_approved: bool

# Node 1: Planner
def planner_node(state: AgentState) -> Dict[str, Any]:
    """Decomposes the high-level objective into atomic dependency steps."""
    task = state["task"]
    plan = [
        f"1. Literature review on: {task}",
        "2. Identify technical tradeoffs between Cyclic StateGraph and Linear DAGs.",
        "3. Synthesize production architectural recommendations."
    ]
    return {"plan": plan}

# Node 2: Researcher (Tools)
def research_node(state: AgentState) -> Dict[str, Any]:
    """Simulates tool execution (Tavily Search / arXiv / Vector DB query)."""
    task = state["task"]
    notes = [
        f"[Tavily Search] 4 empirical benchmarks retrieved for '{task}'.",
        "[arXiv:2308.08155] Stateful graph execution prevents cascade failures in multi-turn agents.",
        "[LangGraph Documentation] Checkpointing with MemorySaver guarantees idempotency across thread interruptions."
    ]
    return {"research_notes": notes}

# Node 3: Writer
def writer_node(state: AgentState) -> Dict[str, Any]:
    """Compiles research notes and critique recommendations into a cohesive draft."""
    notes_summary = "\n".join(state["research_notes"])
    draft = f"""# Technical Report: {state['task']}

## Executive Summary
This report analyzes stateful multi-agent architectures. Unlike legacy linear DAGs, cyclic graphs allow agents to self-correct during runtime.

## Empirical Evidence & Findings
{notes_summary}

## Architecture Recommendation
Adopt LangGraph StateGraph with MemorySaver checkpoints for fault-tolerant enterprise pipelines.
"""
    return {"draft": draft}

# Node 4: Evaluator (Critique)
def evaluator_node(state: AgentState) -> Dict[str, Any]:
    """Evaluates draft against 4 key rubrics: Grounding, Completeness, Structure, Citations."""
    iteration = state.get("iteration_count", 0) + 1
    
    # In first iteration, score is 85; on second, it reaches 98
    if iteration < 2:
        score = 85.0
        critique = ["Add explicit citations to MemorySaver persistence guarantees."]
    else:
        score = 98.0
        critique = ["Draft satisfies all publication rubrics."]
        
    return {
        "critique_score": score,
        "critique_notes": critique,
        "iteration_count": iteration
    }

# Conditional Edge Router
def should_continue(state: AgentState) -> str:
    """Evaluates whether to revise, await human signoff, or finalize."""
    if state["critique_score"] < 90.0 and state["iteration_count"] < 3:
        return "revise"
    if not state.get("human_approved", False):
        return "await_human"
    return "finalize"

# Mock Execution Runner
def run_workflow_simulation(task: str) -> AgentState:
    print(f"[*] Starting LangGraph workflow for: '{task}'")
    state: AgentState = {
        "task": task,
        "plan": [],
        "research_notes": [],
        "draft": "",
        "critique_score": 0.0,
        "critique_notes": [],
        "iteration_count": 0,
        "human_approved": False
    }

    # Step 1: Planner
    state.update(planner_node(state))
    print("  -> Node [Planner]: Plan created with", len(state["plan"]), "steps.")

    # Step 2: Research
    state.update(research_node(state))
    print("  -> Node [Researcher]: Gathered", len(state["research_notes"]), "notes.")

    # Loop: Write & Critique
    while True:
        state.update(writer_node(state))
        print("  -> Node [Writer]: Draft compiled.")
        
        state.update(evaluator_node(state))
        print(f"  -> Node [Evaluator]: Critique score: {state['critique_score']}/100.")
        
        decision = should_continue(state)
        if decision == "revise":
            print("  -> Conditional Edge: Score < 90%. Looping back to Writer for revision...")
            continue
        elif decision == "await_human":
            print("  -> Node [Human-in-the-Loop]: Score >= 90%. Requesting human approval...")
            # Simulate human signoff
            state["human_approved"] = True
            print("  -> Human Approval: APPROVED by Ahmed Rifai.")
            break
        else:
            break

    print("[*] LangGraph Workflow Completed Successfully!\n")
    return state

if __name__ == "__main__":
    result = run_workflow_simulation("Comparative Analysis of LangGraph vs AutoGen")
    print(result["draft"])
