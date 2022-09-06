<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Demo NER in a new pipeline (Named Entity Recognition)

A minimal demo NER project for spaCy v3 adapted from the spaCy v2 [`train_ner.py`](https://github.com/explosion/spaCy/blob/v2.3.x/examples/training/train_ner.py) example script for creating an NER component in a new pipeline.

## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `install-requirements` | Download a spaCy model with pretrained vectors |
| `assets-fetch` | Download assets from GitHub |
| `convert` | Convert the data to spaCy's binary format |
| `create-config-cpu` | Create a new config with an NER pipeline component |
| `create-config-gpu` | Create a new config with an NER pipeline component |
| `train-cpu` | Train the NER model |
| `train-gpu` | Train the NER model with vectors |
| `evaluate` | Evaluate the model and export metrics |
| `package` | Package the trained model as a pip package |
| `visualize-model` | Visualize the model's output interactively using Streamlit |
| `install-package` | Install package |
| `documentation-gen` | Generate documentation |
| `serve` | Serve the models via a FastAPI REST API using the given host and port |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `initilize` | `install-requirements` &rarr; `assets-fetch` |
| `training-cpu` | `convert` &rarr; `create-config-cpu` &rarr; `train-cpu` &rarr; `evaluate` |
| `training-gpu` | `convert` &rarr; `create-config-gpu` &rarr; `train-gpu` &rarr; `evaluate` |
| `visualize` | `visualize-model` |
| `deploy` | `package` &rarr; `install-package` &rarr; `serve` |
| `generate-documentation` | `documentation-gen` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets` | Git | Demo training data converted from the v2 `train_ner.py` example with `srsly.write_json("train.json", TRAIN_DATA)` |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
