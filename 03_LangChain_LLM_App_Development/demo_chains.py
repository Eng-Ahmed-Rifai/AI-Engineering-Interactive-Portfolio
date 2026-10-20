"""
CLI Demo for LangChain Chains and Memory
Author: Ahmed Mohamed Abdullatif Rifai
"""

from conversational_memory import run_memory_benchmark

def main():
    print("==================================================================")
    print("   LangChain Orchestration & Memory Benchmark CLI Demonstration")
    print("   Engineer: Ahmed Mohamed Abdullatif Rifai")
    print("==================================================================\n")
    run_memory_benchmark(turns=5)

if __name__ == "__main__":
    main()
