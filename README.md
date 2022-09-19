# Spacy Projects

This repository helps you to use the Spacy Projects.

## Install requirements
Install first the requirements for Spacy Projects CLI:
```
pip install cupy-cuda11x
pip install -U 'spacy[cuda113]'
```

## Clone the template

Clone the template:
```
spacy project clone templates/ner_demo --repo https://github.com/opertifelipe/spacy-templates.git
```

# NER DEMO

## Initialize

To initialize
```
spacy project run initialize
```

## Train
To train
```
spacy project run train-{cpu;gpu}
```

## Deploy
To train
```
spacy project run deploy
```

## API test
```
curl -X GET -H 'Content-Type: application/json' http://127.0.0.1:5000/
curl -X POST http://127.0.0.1:5000/process/entities  -H 'Content-Type: application/json' --data '{"text":"I like London and Berlin."}'
```