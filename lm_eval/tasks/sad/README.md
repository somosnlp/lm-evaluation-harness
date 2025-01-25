# SPANISH ANOREXIA DATASET

### Paper

Title: `Detecting Anorexia in Spanish Tweets`

Abstract: `Mental health is one of the main concerns of today’s society. Early detection of symptoms can greatly help people with mental disorders. People are using social networks more and more to express emotions, sentiments, and mental states. Thus, the treatment of this information using NLP technologies can be applied to the automatic detection of mental problems such as eating disorders. However, the first step for solving the problem should be to provide a corpus in order to evaluate our systems. In this paper, we specifically focus on detecting anorexia messages on Twitter. Firstly, we have generated a new corpus of tweets extracted from different accounts including anorexia and non-anorexia messages in Spanish. The corpus is called SAD: Spanish Anorexia Detection corpus. In order to validate the effectiveness of the SAD corpus, we also propose several machine learning approaches for automatically detecting anorexia symptoms in the corpus. The good results obtained show that the application of textual classification methods is a promising option for developing this kind of system demonstrating that these tools could be used by professionals to help in the early detection of mental problems.`

Conference Proceedings: [RANLP 2019 Proceedings](http://lml.bas.bg/ranlp2019/proceedings-ranlp-2019.pdf)

### Citation

```
@inproceedings{lopez-ubeda-etal-2019-detecting,
    title = "Detecting Anorexia in {S}panish Tweets",
    author = "L{\'o}pez {\'U}beda, Pilar  and
      Plaza del Arco, Flor Miriam  and
      D{\'\i}az Galiano, Manuel Carlos  and
      Urena Lopez, L. Alfonso  and
      Martin, Maite",
    booktitle = "Proceedings of the International Conference on Recent Advances in Natural Language Processing (RANLP 2019)",
    month = sep,
    year = "2019",
    address = "Varna, Bulgaria",
    publisher = "INCOMA Ltd.",
    url = "https://www.aclweb.org/anthology/R19-1077",
    doi = "10.26615/978-954-452-056-4_077",
    pages = "655--663",
    abstract = "Mental health is one of the main concerns of today{'}s society. Early detection of symptoms can greatly help people with mental disorders. People are using social networks more and more to express emotions, sentiments and mental states. Thus, the treatment of this information using NLP technologies can be applied to the automatic detection of mental problems such as eating disorders. However, the first step to solving the problem should be to provide a corpus in order to evaluate our systems. In this paper, we specifically focus on detecting anorexia messages on Twitter. Firstly, we have generated a new corpus of tweets extracted from different accounts including anorexia and non-anorexia messages in Spanish. The corpus is called SAD: Spanish Anorexia Detection corpus. In order to validate the effectiveness of the SAD corpus, we also propose several machine learning approaches for automatically detecting anorexia symptoms in the corpus. The good results obtained show that the application of textual classification methods is a promising option for developing this kind of system demonstrating that these tools could be used by professionals to help in the early detection of mental problems.",
}
```

### Tasks

The following task evaluate the ability of models to detect anorexia-related content in Spanish tweets using the SAD dataset:

* `sad`: Classifies tweets as either anorexia-related or non-anorexia-related using binary classification. Each entry consists of a tweet, three classification options, and the correct label.


### Checklist

For adding novel benchmarks/datasets to the library:
* [X] Is the task an existing benchmark in the literature?
  * [X] Have you referenced the original paper that introduced the task?
  * [X] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:
* [X] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?