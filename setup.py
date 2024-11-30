from setuptools import setup, find_packages

setup(
    name="bertforimagecaptioning",
    version="0.1.0",
    description="BERT-based Image Captioning Model with Visual Features Integration",
    author="Mahmood Anaam",
    author_email="eng.mahmood.anaam@gmail.com",
    url="https://github.com/Mahmood-Anaam/BertForImageCaptioning",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "torch>=1.9.0",
        "torchvision>=0.10.0",
        "transformers>=4.12.0",
        "pytorch-transformers>=1.2.0",
        "datasets>=2.0.0",
        "numpy>=1.19.5",
        "pandas>=1.1.5",
        "opencv-python>=4.5.3",
        "matplotlib>=3.4.3",
        "PyYAML>=5.4.1",
        "tqdm>=4.62.3",
        "scipy>=1.5.4",
        "scikit-learn>=0.24.2",
        "Pillow>=8.3.2",
        "anytree>=2.12.1",
        
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
