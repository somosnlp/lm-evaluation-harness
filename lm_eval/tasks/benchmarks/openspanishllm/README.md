# Open Spanish LLM Leaderboard

### About

Homepage: https://huggingface.co/spaces/somosnlp/open-spanish-llm-leaderboard

A benchmark combining tasks to evaluate Spanish generative LLMs.

### Tasks

[TODO]

### Reproducibility

To evaluate a model on this benchmark run:

```bash
lm_eval --model --model=hf \
    --model_args "pretrained=<your_model>,use_accelerate=True,revision=<your_model_revision>" \
    --tasks openspanishllm \
    --batch_size 1
```

### Citation

```
TODO
```
