# 🤗 Open Source Models with Hugging Face

[![Hugging Face](https://img.shields.io/badge/Hugging_Face-Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)
[![DeepLearning.AI](https://img.shields.io/badge/DeepLearning.AI-100%25_Verified-FF6F00?style=for-the-badge)](https://www.deeplearning.ai/)

## 📖 Theoretical Foundations & Curriculum
This module covers working with open-weights foundation models hosted on the Hugging Face Hub, executing local and edge inference, and deploying interactive demos via Gradio and Hugging Face Spaces.

### 🌟 Key Pipeline Patterns
1. **Multimodal Task Specialization:**
   - NLP: Summarization (`facebook/bart-large-cnn`), NLI Zero-Shot (`distilbart-mnli`), Translation.
   - Speech: Automatic Speech Recognition (ASR) via `openai/whisper-small`.
   - Vision: Zero-shot image classification via CLIP (`openai/clip-vit-base-patch32`).
2. **Quantization & Efficiency:**
   - Deploying models using 8-bit and 4-bit NormalFloat (NF4) quantization via `bitsandbytes` to reduce memory footprints by up to 75% without perceptible perplexity loss.
3. **Packaging & Deployment:**
   - Building Gradio UI microservices and deploying to Hugging Face Spaces for public interactive portfolio demonstrations.

---

## 💻 Code Artifacts
- [`multimodal_pipeline.py`](./multimodal_pipeline.py): Production implementation of multi-task pipelines with mock fallback inference.
- [`demo_hf_models.py`](./demo_hf_models.py): Interactive CLI runner.
