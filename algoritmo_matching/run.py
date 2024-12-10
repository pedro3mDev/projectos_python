candidatos = [
    {"nome": "Pedro Moniz", "habilidades": {"Python", "Django", "SQL"}},
    {"nome": "Ismael Correia", "habilidades": {"Java", "Spring", "SQL"}},
    {"nome": "Adelino Francelino", "habilidades": {"JavaScript", "Vue.js", "HTML"}},
    {"nome": "Celso Sousa", "habilidades": {"Java", "Spring", "SQL", "Angular"}},
]

vagas = [
    {"titulo": "Desenvolvedor Backend", "requisitos": {"Python", "Django", "SQL"}},
    {"titulo": "Engenheiro Java", "requisitos": {"Java", "Spring", "SQL"}},
    {"titulo": "Desenvolvedor Frontend", "requisitos": {"JavaScript", "Vue.js", "CSS"}},
]

def encontrar_matching(candidatos, vagas):
    resultados = []
    for vaga in vagas:
        matches = []
        for candidato in candidatos:
            matching_habilidades = vaga["requisitos"].intersection(candidato["habilidades"])
            pontuacao = len(matching_habilidades) / len(vaga["requisitos"])
            if pontuacao > 0:
                matches.append({"candidato": candidato["nome"], "pontuacao": pontuacao})
        matches = sorted(matches, key=lambda x: x["pontuacao"], reverse=True)
        resultados.append({"vaga": vaga["titulo"], "matches": matches})
    return resultados

resultados = encontrar_matching(candidatos, vagas)

for resultado in resultados:
    print(f"Vaga: {resultado['vaga']}")
    if resultado["matches"]:
        for match in resultado["matches"]:
            print(f"  - Candidato: {match['candidato']}, Pontuação: {match['pontuacao']:.2f}")
    else:
        print("  - Nenhum candidato correspondeu.")
