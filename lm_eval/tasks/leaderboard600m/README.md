# Leaderboard 600M

### About

Homepage: TODO

A benchmark combining tasks to evaluate generative LLMs in the languages of LATAM and Spain (i.e. Spanish, Catalan, Galician), spoken in total by 600M people.

### Tasks

[TODO]

### Reproducibility

To evaluate a model on this benchmark run:

```bash
lm_eval --model --model=hf \
    --model_args "pretrained=<your_model>,use_accelerate=True,revision=<your_model_revision>" \
    --tasks leaderboard600m \
    --batch_size 1
```

### Citation

```
TODO
```
