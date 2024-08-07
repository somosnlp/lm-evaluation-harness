system_prompt = "Eres un cómico español experto en humor blanco cuya tarea consiste en identificar el tipo al que pertenecen las bromas planteadas."

prompt_template="""Como experto en humor, tu tarea es la siguiente.
A partir de la broma que se muestra a continuación y las opciones tipo test que se te presentan, tu tarea consiste en responder únicamente con el número correspondiente a la opción correcta del tipo de broma.
Es decir, si la broma es de comparación-exageración, responde 0; si la broma es de juego de palabras, responde 1; si la broma es de animar lo inanimado, responde 2 y si la broma es de regla de tres, responde 3. Recuerda responder sólo con el número correspondiente a la opción del tipo de broma.
Broma: {broma}
Opciones: {opciones}
"""

def doc_to_text(sample: dict):
    options = "\n".join([f"{i}: {choice}" for i, choice in enumerate(sample["choices"])])
    text = f"""
    System: {system_prompt}

    User: {prompt_template.format(broma=sample["question"], opciones=options)}
    Assistant:"""
    return text

def doc_to_target(sample):
    letter_to_num = {"A": 0, "B": 1, "C": 2, "D": 3}
    answer = letter_to_num[sample["answer"]]
    return answer

def doc_to_choice(sample):
    return sample["choices"]
