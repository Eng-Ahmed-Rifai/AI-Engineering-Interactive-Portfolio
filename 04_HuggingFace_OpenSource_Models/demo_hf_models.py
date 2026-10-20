"""
CLI Demo for Hugging Face Open-Source Models
Author: Ahmed Mohamed Abdullatif Rifai
"""

from multimodal_pipeline import OpenSourceModelHub

def main():
    hub = OpenSourceModelHub()
    print("==================================================================")
    print("   Hugging Face Open Source Models Inference CLI Demonstration")
    print("   Engineer: Ahmed Mohamed Abdullatif Rifai")
    print("==================================================================\n")

    sample_doc = (
        "Open-source models offer unparalleled control, transparency, and data privacy for enterprise "
        "deployments. By utilizing Hugging Face Transformers, engineering teams can run local models "
        "without leaking proprietary proprietary queries to third-party proprietary APIs."
    )

    print("Task 1: Document Summarization (BART-Large)")
    summary_res = hub.summarize(sample_doc)
    print("  -> Summary:", summary_res["summary"])

    print("\nTask 2: Zero-Shot Domain Classification")
    classify_res = hub.zero_shot_classify(sample_doc, ["Cloud Security", "Enterprise AI", "E-Commerce"])
    for label, score in zip(classify_res["labels"], classify_res["scores"]):
        print(f"  -> Label: {label:<18} | Probability: {score * 100:.1f}%")

if __name__ == "__main__":
    main()
