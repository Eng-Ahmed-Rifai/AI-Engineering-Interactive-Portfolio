"""
CLI Demo for LangGraph Autonomous Agents
Author: Ahmed Mohamed Abdullatif Rifai
"""

import sys
from agent_workflow import run_workflow_simulation

def main():
    topic = "Autonomous Multi-Agent Systems in Production"
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])

    print("==================================================================")
    print("   LangGraph Multi-Agent Architecture CLI Demonstration")
    print("   Engineer: Ahmed Mohamed Abdullatif Rifai")
    print("==================================================================\n")
    
    result = run_workflow_simulation(topic)
    print("\n--- Final Draft Output ---")
    print(result["draft"])
    print(f"Total Iteration Cycles: {result['iteration_count']}")
    print(f"Final Quality Score: {result['critique_score']}/100")
    print(f"Human-in-the-Loop Signoff: {result['human_approved']}")

if __name__ == "__main__":
    main()
