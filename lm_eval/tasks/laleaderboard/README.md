# La Leaderboard

### About

Homepage: https://huggingface.co/spaces/la-leaderboard/la-leaderboard

A benchmark combining tasks to evaluate generative LLMs in Spanish Varieties and Official Languages (Spanish, Catalan, Basque, Galician).

### Tasks

- aquas
- arc_ca_aina
- bec2016eu
- belebele_glg_Latn
- bertaqa_eu
- bhtc_v2
- cabreu
- catalanqa
- catcola
- clindiagnoses
- clintreates
- copa_ca
- coqcat
- crows_pairs_spanish
- epec_koref_bin
- escola
- eus_exams_eu
- eus_proficiency
- eus_reading
- eus_trivia
- fake_news_es
- galcola
- humorqa
- mgsm_direct_ca
- mgsm_direct_es
- mgsm_direct_eu
- mgsm_direct_gl
- noticia
- offendes
- openbookqa_ca
- openbookqa_gl
- parafraseja
- parafrases_gl
- paws_ca
- paws_es
- paws_gl
- piqa_ca
- qnlieu
- ragquas
- siqa_ca
- spalawex
- summarization_gl
- teca
- teleia
- vaxx_stance
- wiceu
- wnli_ca
- wnli_es
- xcopa_eu
- xnli_ca
- xnli_es
- xnli_eu
- xquad_ca
- xquad_es
- xstorycloze_ca
- xstorycloze_es
- xstorycloze_eu

### Reproducibility

To evaluate a model on this benchmark run:

```bash
lm_eval --model --model=hf \
    --model_args "pretrained=<your_model>,use_accelerate=True,revision=<your_model_revision>" \
    --tasks laleaderboard \
    --num_fewshot 5 \
    --batch_size 1
```

### Citation

```
@misc{laleaderboard2024,
    author = {María Grandury, Javier Aula-Blasco, Clémentine Fourrier, Miguel González, Gonzalo Martínez, Gonzalo Santamaría, Alejandro Vaca},
    title = {Leaderboard de Variedades del Español y Lenguas Oficiales},
    year = {2024},
    publisher = {Hugging Face},
    howpublished = "\url{https://huggingface.co/spaces/la-leaderboard/la-leaderboard}"
}
```
