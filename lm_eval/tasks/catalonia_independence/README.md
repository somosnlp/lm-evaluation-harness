# CATALONIA INDEPENDENCE CORPUS

### Dataset Summary

This dataset contains two corpora in Spanish and Catalan that consist of annotated Twitter messages for automatic stance detection. The data was collected over 12 days during February and March of 2019 from tweets posted in Barcelona, and during September of 2018 from tweets posted in the town of Terrassa, Catalonia.

Each corpus is annotated with three classes: **AGAINST**, **FAVOR**, and **NEUTRAL**, which express the stance towards the target—independence of Catalonia.

### Tasks

The following task evaluates the ability of models to perform stance detection on Spanish and Catalan tweets using the Catalonia Independence Corpus:

* `catalonia_independence`: Classifies tweets into three classes—**AGAINST**, **FAVOR**, or **NEUTRAL**—indicating stance towards the independence of Catalonia.

### Checklist

For adding novel benchmarks/datasets to the library:
* [ ] Is the task an existing benchmark in the literature?
  * [ ] Have you referenced the original paper that introduced the task?
  * [ ] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?

If other tasks on this dataset are already supported:
* [X] Is the "Main" variant of this task clearly denoted?
* [x] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [x] Have you noted which, if any, published evaluation setups are matched by this variant?

