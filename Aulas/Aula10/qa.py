from transformers import pipeline


qa_model = pipeline("question-answering", model="lfcc/bert-portuguese-squad")

context = """Resumo Introdução: A plasmaferese terapêutica é um procedimento em que o sangue passa por um circuito extracorpóreo que separa o plasma dos outros componentes do sangue. O plasma removido é substituído por soluções de reposição. Os estudos sobre a utilização de plasmaferese terapêutica no doente crítico são escassos. O objetivo do estudo foi rever todas as sessões de plasmaferese realizadas no serviço de Medicina Intensiva do Hospital Beatriz Ângelo.Material e Métodos: Estudo observacional retrospetivo de todos os doentes admitidos no serviço de Medicina Intensiva entre abril de 2012 e março de 2019. Foram selecionados os doentes submetidos a plasmaferese e excluídas as sessões realizadas fora do serviço de Medicina Intensiva.Resultados: No período de estudo foram incluídos 46 doentes. A maioria eram homens (n = 29; 63%) com uma idade mediana de 53 anos. Os diagnósticos mais frequentes foram pancreatite secundária a hipertrigliceridemia, vasculite, anemia hemolítica autoimune e síndrome hemolítica urémica atípica. Foram realizadas 198 sessões de plasmaferese no serviço de Medicina Intensiva. As soluções de substituição mais utilizadas foram plasma fresco congelado (34,4%), albumina/cristalóide (24,2%) e albumina/plasma (19,2%). As complicações mais comuns foram alterações hidroeletrolíticas (84; 42,4%), e distúrbios da coagulação/plaquetas (65; 32,8%). Emnenhum dos casos a técnica teve que ser interrompida por complicações relacionadas com o doente.Conclusão: A plasmafere terapêutica é uma técnica complexa que requer treino específico. As indicações são diversas e algumas não consensuais. As complicações foram frequentes, mas não condicionaram morbilidade associada.
"""

questions = ["Em que hospital foi realizada a pesquisa?",
            "Qual é a conclusão da pesquisa?",
            "Qual é o objetivo da pesquisa?",
            "Qual é a metodologia usada na pesquisa?"]


for question in questions:
    print(question)
    print(qa_model(question = question, context = context))
## {'answer': 'İstanbul', 'end': 39, 'score': 0.953, 'start': 31}
