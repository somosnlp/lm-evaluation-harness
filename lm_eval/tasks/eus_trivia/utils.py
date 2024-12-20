from typing import List


letters = ["A", "B", "C", "D"]


def doc_to_text(doc) -> str:
    """
    Converts a document to a formatted string.

    Args:
        doc (dict): A dictionary containing the document information.

    Returns:
        str: A formatted string containing the question and answer choices.
    """
    candidates = doc["candidates"]
    num_choices = len(candidates)
    if num_choices < 2:
        raise ValueError("Invalid number of candidates")
    choices = letters[:num_choices]
    formatted_choices = "\n".join(
        [f"{choice}: {candidates[i]}" for i, choice in enumerate(choices)]
    )
    return f"Galdera: {doc['question']}\n{formatted_choices}\nErantzuna:"


def doc_to_choice(doc) -> List[str]:
    """
    Returns the answer choices for a document.

    Args:
        doc (dict): A dictionary containing the document information.

    Returns:
        list: A list of strings containing the answer choices.
    """
    num_choices = len(doc["candidates"])
    if num_choices < 2:
        raise ValueError("Invalid number of candidates")
    return letters[:num_choices]

def list_fewshot_samples() -> list[dict]:
    return [
        {
        "problem": "Galdera: Nola bota behar dira honakoak ontzi horietara?\nA: Apurturik\nB: Denak lotuta\nC: Tapoia kendu gabe\nD: Tapoirik gabe\nErantzuna:",
        "solution": "Tapoirik gabe",
        "few-shot": "1"
},
        {
        "problem": "Galdera: Zein da 69 zenbakiaren hurrengoa?\nA: 96\nB: 86\nC: 70\nC: 68\nErantzuna:",
        "solution": "70",
        "few-shot": "1"
},
        {
        "problem": "Galdera: Lau sagarrek 400 gr pisatzen badute, zenbat pisatzen du sagar batek?\nA: Ez dakigu\nB: 150 gr\nC: 75 gr\nD: 100 gr\nErantzuna:",
        "solution": "Ez dakigu",
        "few-shot": "1"
},
        {
        "problem": "Galdera: Zein da Bizkaian topa dezakegun sugerik handiena?\nA: Boa sugea\nB: Eskolapioren sugea\nC: Sugegorria\nD: Zirauna\nErantzuna:",
        "solution": "Eskolapioren sugea",
        "few-shot": "1"
},
    ]
