# La Leaderboard

### About

Homepage: https://huggingface.co/spaces/la-leaderboard/la-leaderboard

A benchmark combining tasks to evaluate generative LLMs in Spanish Varieties and Official Languages (Spanish, Catalan, Basque, Galician).

### Tasks

## Spanish

- aquas
- belebele_spa_Latn
- clindiagnoses
- clintreates
- copa_es
- crows_pairs_spanish
- escola
- fake_news_es
- humorqa
- mgsm_direct_es_spanish_bench
- noticia
- offendes
- openbookqa_es
- paws_es_spanish_bench
- ragquas
- spalawex
- teleia
- wnli_es
- xnli_es_spanish_bench
- xlsum_es
- xquad_es
- xstorycloze_es

## Catalan

- arc_ca_catalan_bench
- belebele_cat_Latn
- cabreu
- catalanqa
- catcola
- copa_ca
- coqcat
- mgsm_direct_ca
- openbookqa_ca
- parafraseja
- paws_ca
- piqa_ca
- siqa_ca
- teca
- wnli_ca
- xnli_ca
- xquad_ca
- xstorycloze_ca

## Basque

- bec2016eu
- belebele_eus_Latn
- bertaqa_eu
- bhtc_v2
- epec_koref_bin
- eus_exams_eu
- eus_proficiency
- eus_reading
- eus_trivia
- mgsm_native_cot_eu
- qnlieu
- vaxx_stance
- wiceu
- wnli_eu
- xcopa_eu
- xnli_eu_native
- xstorycloze_eu

## Galician

- belebele_glg_Latn
- galcola
- mgsm_direct_gl
- openbookqa_gl
- parafrases_gl
- paws_gl
- summarization_gl
- xnli_gl
- xstorycloze_gl

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
