## Python Tooling for LLM Post-Training

---

### Overview

This project is a Python toolkit for structured text manipulation and evaluation of LLM outputs. It provides modular, reusable components to support post-training benchmarking in problem-solving datasets.

### Design Choices

The code is organized into two modules: `main.py` and `funx.py`.  
- `main.py` defines the `LoremIpsum` class, which implements higher-level text transformation pipelines.  
- `funx.py` contains single-purpose helper functions that are composed by the class methods.  

This structure enforces modularity, separation of concerns, and maintainability, allowing complex workflows to be built from simple, reusable components.

### Impact

The toolkit was used in evaluating flagship generative AI models, enabling controlled dataset generation, automated validation, and reproducible post-training analysis. It improved efficiency in benchmarking workflows and facilitated meta-reviews by standardizing outputs where human evaluators disagreed.

### License

This project is licensed under the MIT License. See the LICENSE file for more details.