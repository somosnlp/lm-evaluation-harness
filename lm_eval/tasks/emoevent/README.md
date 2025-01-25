# EMOEVENT

### Paper

Title: `EmoEvent: A Multilingual Emotion Corpus based on different Events`

Abstract: `In recent years, emotion detection in text has become more popular due to its potential applications in fields such as psychology, marketing, political science, and artificial intelligence, among others. While opinion mining is a well-established task with many standard datasets and well-defined methodologies, emotion mining has received less attention due to its complexity. In particular, the annotated gold standard resources available are not enough. In order to address this shortage, we present a multilingual emotion dataset based on different events that took place in April 2019. We collected tweets from the Twitter platform. Then one of seven emotions, six Ekman’s basic emotions plus the “neutral or other emotions,” was labeled on each tweet by 3 Amazon MTurkers. A total of 8,409 in Spanish and 7,303 in English were labeled.`

Conference Proceedings: [LREC 2020 Proceedings](https://www.aclweb.org/anthology/2020.lrec-1.186)

### Citation

```
@inproceedings{plaza-del-arco-etal-2020-emoevent,
    title = "{{E}mo{E}vent: A Multilingual Emotion Corpus based on different Events}",
    author = "{Plaza-del-Arco}, {Flor Miriam} and Strapparava, Carlo and {Ure{\~n}a-L{\’o}pez}, L. Alfonso and {Mart{\’i}n-Valdivia}, M. Teresa",
    booktitle = "Proceedings of the 12th Language Resources and Evaluation Conference",
    month = may,
    year = "2020",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://www.aclweb.org/anthology/2020.lrec-1.186",
    pages = "1492--1498",
    language = "English",
    ISBN = "979-10-95546-34-4"
}
```

### Source Data

Twitter

### Groups and Tasks

The following task evaluates the ability of models to perform emotion detection on Spanish and English tweets using the EmoEvent dataset:

* `emoevent`: Classifies tweets into one of seven emotions—**Anger**, **Disgust**, **Fear**, **Joy**, **Sadness**, **Surprise**, or **Neutral/Other**—based on the content of the tweet. Each entry consists of a tweet, seven classification options, and the correct label.

### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [X] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:
* [X] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?
