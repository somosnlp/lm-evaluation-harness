prompt_template="""A partir del caso clínico que se expone a continuación y su diagnóstico realizado por un médico, tu tarea es la siguiente.
Como médico experto, tu tarea es la de diseñar un tratamiento para el paciente descrito en el caso clínico en base a su diagnóstico. Responde escueta y concisamente únicamente con el tratamiento para el paciente.
Caso clínico: {caso_clinico}
Diagnóstico: {diagnostico}
"""

system_prompt = "Eres un experto en medicina que diseña tratamientos en base a casos clínicos y sus correspondientes diagnósticos."


def case_to_rawtext(sample: dict):
    text = f"""
    System: {system_prompt}

    User: {prompt_template.format(caso_clinico=sample['caso_clinico'], diagnostico=sample["Diagnostico"])}
    Assistant:"""
    return text