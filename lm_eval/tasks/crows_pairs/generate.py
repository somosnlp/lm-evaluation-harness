import os

categories = [
    "age",
    "autre",
    "disability",
    "gender",
    "nationality",
    "physical appearance",
    "race_color",
    "religion",
    "sexual orientation",
    "socioeconomic",
]

import os

# Iterate over the files in the directory
for file in os.listdir("lm_eval/tasks/crows_pairs"):
    if file.startswith("crows_pairs_french"):
        es_file = file.replace("french", "spanish")
        os.makedirs(es_file, exist_ok=True)
        with open(os.path.join("lm_eval/tasks/crows_pairs", file), "r") as content:
            with open(
                os.path.join("lm_eval/tasks/crows_pairs", es_file), "w"
            ) as es_file:
                es_file.write(content.read().replace("french", "spanish"))
                # write in the yaml also
                # dataset_path: multilingual-crows-pairs/multilingual-crows-pairs
                # dataset_name: es_AR
                # test_split: train
