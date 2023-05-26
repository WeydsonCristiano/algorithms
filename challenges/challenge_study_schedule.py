def study_schedule(periodo_permanencia, hora_alvo):
    if not hora_alvo:
        return None

    if not all(
        isinstance(periodo, tuple) and len(periodo) == 2
        for periodo in periodo_permanencia
    ):
        return None

    contador = 0
    for periodo in periodo_permanencia:
        if periodo[0] <= hora_alvo <= periodo[1]:
            contador += 1

    return contador
