system_prompt = "Eres un abogado español experto en las leyes de España y su sistema legal y jurídico."

prompt_template="""Como experto en derecho español y el sistema legal y jurídico de España, debes hacer lo siguiente.
A partir de la pregunta tipo test que se plantea a continuación y las opciones que se te presentan, tu tarea consiste en responder únicamente con el número que corresponde a la respuesta correcta: 0, 1, 2 o 3. Sólo responde con el número, la respuesta no debe incluir nada más que el número. Por tanto las únicas respuestas posibles son: 0, 1, 2 o 3.
## Pregunta: {pregunta}
## Opciones: {opciones}
"""

def doc_to_text(sample: dict):
    options = "\n".join([f"{i}: {choice}" for i, choice in enumerate(sample["choices"])])
    text = f"""
    System: {system_prompt}

    User: {prompt_template.format(pregunta=sample["question"], opciones=options)}
    Assistant:"""
    return text

def doc_to_target(sample):
    letter_to_num = {"A": 0, "B": 1, "C": 2, "D": 3}
    answer = letter_to_num[sample["answer"]]
    return answer

def doc_to_choice(sample):
    return sample["choices"]
