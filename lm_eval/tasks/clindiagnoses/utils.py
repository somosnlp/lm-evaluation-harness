prompt_template="""A partir del caso clínico que se expone a continuación, tu tarea es la siguiente.
Como médico experto, tu tarea es la de diagnosticar al paciente en base al caso clínico. Responde únicamente con el diagnóstico para el paciente de forma concisa.
Caso clínico: {caso_clinico}
"""

system_prompt = "Eres un experto en medicina que realiza diagnósticos en base a casos clínicos."


def case_to_rawtext(sample: dict):
    text = f"""
    System: {system_prompt}

    User: {prompt_template.format(caso_clinico=sample['caso_clinico'])}
    Assistant:"""
    return text
