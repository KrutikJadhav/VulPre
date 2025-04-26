# AutoPenML

An Automated Penetration Testing and Vulnerability Prediction Tool.

## Features
- Automated port scanning (nmap)
- OS fingerprinting
- Machine Learning model to predict vulnerability risks
- Markdown report generation
- Flask API support

## Setup

```bash
pip install -r requirements.txt
```

## Training the Model
```bash
python ml_model/model_trainer.py
```

## Running the Tool (CLI)
```bash
python main.py
```

## Running the Tool (API)
```bash
python api.py
```

Reports are saved inside the `reports/` directory.