## Clone the template

## Install requirements
In order to use the GPU the step are:
```
pip install cupy-cuda11x
pip install -U 'spacy[cuda113]'
python -m spacy download en_core_web_trf
```

## NER Documentation
```
curl -X POST http://127.0.0.1:5000/process/entities --data '{"text":"I like London and Berlin."}'
```