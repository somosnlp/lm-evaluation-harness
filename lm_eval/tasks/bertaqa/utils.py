def list_fewshot_samples() -> dict[str, list[dict]]:
    return {
        "bertaqa_en": [
            {
            "problem": "Question: Who was imprisoned in 1964?\nA: Nelson Mandela\nB: Mumia Abu Jamal\nC: Charles Ghankay\nAnswer:",
            "solution": "Nelson Mandela",
            "few-shot": "1"
},
            {
            "problem": "Question: What's the name of the film based on Bernardo Atxaga's novel \"Obabakoak\"?\nA: \"Obabakoak\"\nB: \"Obaba\"\nC: \"Obabako istorioak\"\nAnswer:",
            "solution": "\"Obaba\"",
            "few-shot": "1"
},
            {
            "problem": "Question: How long, more or less, did the episodes of \"Bertan zoro\" last?\nA: 90 minutes\nB: 60 minutes\nC: 30 minutes\nAnswer:",
            "solution": "30 minutes",
            "few-shot": "1"
},
        ],
        "bertaqa_eu": [
            {
            "problem": "Galdera: Nor kartzelaratu zuten 1964an?\nA: Nelson Mandela\nB: Mumia Abu Jamal\nC: Charles Ghankay\nErantzuna:",
            "solution": "Nelson Mandela",
            "few-shot": "1"
},
            {
            "problem": "Galdera: Nola du izena Bernardo Atxagaren \"Obabakoak\" eleberrian oinarritutako filmak?\nA: \"Obabakoak\"\nB: \"Obaba\"\nC: \"Obabako istorioak\"\nErantzuna:",
            "solution": "\"Obaba\"",
            "few-shot": "1"
},
            {
            "problem": "Galdera: Zenbat irauten zuten, gutxi gorabehera, \"Bertan zoro\" telesaileko kapituluek?\nA: 90 minutu\nB: Ordubete\nC: 30 minutu\nErantzuna:",
            "solution": "30 minutu",
            "few-shot": "1"
},
        ],
    }