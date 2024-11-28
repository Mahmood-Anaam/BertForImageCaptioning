
# BERTForImageCaptioning

This repository contains the implementation of a **BERT-based image captioning model**, leveraging a modular and configurable architecture for generating captions from images.

## Project Architecture

The repository is organized into the following directories:

```
BERTForImageCaptioning/
│
├── configs/
│   ├── default_config.yaml         # General configurations for the model.
│   ├── vinvl_config.yaml           # Configuration specific to the VinVL feature extractor.
│
├── notebooks/
│   ├── dataset.ipynb               # Dataset visualization and preparation.
│   ├── training.ipynb              # Training pipeline for the model.
│   ├── inference.ipynb             # Inference pipeline for generating captions.
│   ├── evaluation.ipynb            # Evaluation pipeline with metrics like BLEU, METEOR.
│
├── src/
│   ├── datasets/                   # Data loading and preprocessing scripts.
│   ├── modeling/                   # Model architecture and BERT integration.
│   ├── utils/                      # Utility functions for processing and visualization.
│
├── tests/
│   ├── test_dataloader.py          # Tests for the dataset loader.
│   ├── test_model.py               # Tests for the model architecture.
│   ├── test_utils.py               # Tests for utility scripts.
│
├── .gitignore                      # Files to exclude from version control.
├── LICENSE                         # License for the project.
├── README.md                       # Project documentation.
├── requirements.txt                # Dependencies required to run the project.
└── setup.py                        # Installation setup script.
```

## Installation Instructions

### Prerequisites

- Python >= 3.9
- PyTorch >= 1.9
- CUDA (if GPU is used)

### Steps to Install

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Mahmood-Anaam/BertForImageCaptioning.git
   cd BertForImageCaptioning
   ```

2. **Install dependencies:**

   Use the provided `requirements.txt` file to install the necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install the project:**

   Run the `setup.py` script to install the repository as a Python package:

   ```bash
   python setup.py install
   ```

4. **Verify installation:**

   Ensure everything is set up correctly by running the tests:

   ```bash
   pytest tests/
   ```

