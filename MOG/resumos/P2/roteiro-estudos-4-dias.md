# Roteiro de estudos para 4 dias — P2

Este cronograma cobre os três blocos da P2 em 4 dias, com o último dia focado em consolidação.

Objetivo:
- cobrir os três blocos de tópicos da P2
- revisar teoria com foco em explicar e comparar conceitos (a prova é mais teórica que matemática)
- deixar o último dia para revisão ativa e simulado

Sugestão de ritmo diário:
- Bloco 1: 1h30 a 2h de leitura do roteiro
- Bloco 2: 1h a 1h30 de resumo próprio e mapa mental
- Bloco 3: 45min a 1h de autoexplicação ou questões

Se tiver menos tempo, priorize:
1. Bloco 1 (Interoperabilidade/STEP): é o mais extenso e com mais conceitos para decorar
2. Bloco 2 (Paramétrico): entender a diferença paramétrico vs. variacional
3. Bloco 3 (Features): classificação e deficiências do CAD tradicional

---

## Dia 1: Interoperabilidade e Padrões de Troca de Dados

### Objetivo do dia

Entender como softwares CAD trocam dados, os padrões históricos e o padrão STEP como evolução.

### Estudar

Ler no `roteiro-estudo-prova.md` as seções:
- 1.1 Estratégias de Comunicação
- 1.2 Padrões Clássicos e Histórico
- 1.3 O Padrão STEP (Norma ISO 10303)

### Foco principal

- Tradutor direto vs. arquivo neutro (trade-off)
- IGES: o que é, limitações (só geometria, sem semântica)
- STEP: diferença crucial em relação ao IGES (dado de produto vs. geometria)
- Arquitetura STEP em três camadas (Description Methods, Integrated Resources, Application Protocols)
- EXPRESS e SDAI: para que servem

### O que você precisa sair sabendo

- **Explicar a diferença STEP vs. IGES** (questão certa de prova)
- Descrever as três camadas da arquitetura STEP
- Explicar por que o modelo de arquivo neutro é mais escalável
- Dizer o que é e para que serve a EXPRESS e o SDAI
- Citar ao menos 3 exemplos de Application Protocols (AP203, AP214, AP242)

### Revisão ativa do dia

Responda sem consultar:
- Qual a grande diferença entre IGES e STEP?
- O que é um Application Protocol? Dê dois exemplos.
- Para que serve a linguagem EXPRESS?
- Por que N tradutores diretos não escalam bem?
- Qual o papel do SDAI?

### Entrega do dia

Escreva uma folha-resumo com:
- Desenho comparativo: tradutor direto (N*(N-1)) vs. arquivo neutro (2N)
- Diagrama da arquitetura STEP (3 camadas)
- Tabela STEP vs. IGES (colunas: o que troca, semântica, ciclo de vida, formato)

---

## Dia 2: Modelos de Produto, Manufatura + Modelagem Paramétrica (parte 1)

### Objetivo do dia

Fechar o Bloco 1 (Product Models e STEP-NC) e começar o Bloco 2 com os conceitos fundamentais de modelagem paramétrica.

### Estudar

Ler no `roteiro-estudo-prova.md` as seções:
- 1.4 Modelos de Produto (Product Models)
- 1.5 Aplicações na Manufatura
- 2.1 Conceitos Fundamentais de Paramétrico
- 2.2 Tipos de Restrições

### Foco principal

- Três domínios do modelo de produto (Estrutural, Geométrico, Conhecimento)
- STEP-NC: o que muda em relação ao código G tradicional
- Design Intent: o que é, por que importa
- Famílias de peças e relação com instancing (Mortenson Cap. 10)
- Paramétrico vs. Variacional: diferença fundamental
- Restrições geométricas, funcionais e variacionais

### O que você precisa sair sabendo

- Explicar os três domínios do product model
- Dizer por que STEP-NC é mais inteligente que código G
- Definir design intent com exemplo
- Diferenciar paramétrico de variacional com exemplo concreto
- Dar exemplo de cada tipo de restrição (geométrica, funcional, variacional)

### Revisão ativa do dia

Responda sem consultar:
- Quais os três domínios de um product model? O que cada um contém?
- O que é STEP-NC e como difere do código G tradicional?
- O que é Design Intent? Dê um exemplo.
- Qual a diferença entre modelagem paramétrica e variacional?
- Dê um exemplo de restrição funcional.

### Entrega do dia

Escreva uma folha-resumo com:
- Diagrama dos três domínios do product model
- Tabela: paramétrico vs. variacional (critério: ordem de resolução, dependências, flexibilidade)
- Tabela dos 3 tipos de restrições com exemplos

---

## Dia 3: Métodos de Resolução + Features

### Objetivo do dia

Fechar o Bloco 2 (métodos matemáticos/computacionais) e cobrir o Bloco 3 inteiro (features).

### Estudar

Ler no `roteiro-estudo-prova.md` as seções:
- 2.3 Métodos Matemáticos e Computacionais de Resolução
- 3.1 Deficiências do CAD Tradicional
- 3.2 Feições Geométricas (Features)

### Foco principal

- Procedural vs. baseado em restrições (declarativo)
- Grafos de restrições (nós = geometria, arestas = restrições)
- Sistemas sub-restritos e sobre-restritos
- Função implícita: quando usar
- 4 deficiências do CAD tradicional
- Classificações de features: física/abstrata, forma/manufatura, rotacional/prismática
- Feature recognition vs. feature-based design

### O que você precisa sair sabendo

- Comparar abordagem procedural com constraint-based
- Explicar o que acontece com sistemas sub-restritos e sobre-restritos
- Listar as 4 deficiências do CAD tradicional e explicar cada uma
- Classificar features nos três eixos de classificação
- Diferenciar feature recognition de feature-based design
- Explicar por que o mapeamento design ↔ manufatura não é 1:1

### Revisão ativa do dia

Responda sem consultar:
- Qual a diferença entre uma abordagem procedural e uma baseada em restrições?
- O que é um sistema sub-restrito? E sobre-restrito?
- Quais as 4 deficiências do CAD tradicional?
- Qual a diferença entre feature física e abstrata?
- Por que uma form feature e uma manufacturing feature podem ser diferentes para a mesma geometria?
- O que caracteriza uma feature rotacional? E uma prismática?

### Entrega do dia

Escreva uma folha-resumo com:
- Tabela comparativa: CAD tradicional vs. CAD baseado em features
- Diagrama de classificação de features (3 eixos)
- Mapa mental: deficiências do CAD tradicional → como features resolvem

---

## Dia 4: Consolidação e Simulado

### Objetivo do dia

Revisar tudo, fazer o simulado e identificar pontos fracos para reforçar.

### Atividades

1. **Revisão rápida (1h):** Reler as folhas-resumo que você produziu nos dias 1-3
2. **Simulado (1h30):** Resolver o arquivo `simulado-teorico-50-questoes.md` sem consultar
3. **Correção e reforço (1h):** Corrigir pelo gabarito e voltar ao roteiro nos tópicos em que errou

### Checklist de prontidão para a prova

Antes de dormir no dia 4, você deve conseguir responder estas 10 perguntas sem consultar:

1. Qual a diferença fundamental entre STEP e IGES?
2. O que é um Application Protocol? Cite dois.
3. Para que servem EXPRESS e SDAI?
4. Quais são os três domínios de um product model?
5. O que é Design Intent? Dê um exemplo.
6. Qual a diferença entre modelagem paramétrica e variacional?
7. O que são restrições funcionais? Diferencie das geométricas.
8. Quais são as quatro deficiências do CAD tradicional?
9. Qual a diferença entre form feature e manufacturing feature?
10. O que caracteriza uma feature como rotacional ou prismática?

Se travar em alguma, volte ao roteiro e revise a seção correspondente.

### Dica final

A prova é teórica — foque em **explicar conceitos com suas palavras**, **comparar ideias** (IGES vs. STEP, paramétrico vs. variacional, form vs. manufacturing features), e **justificar por que certas evoluções foram necessárias** (STEP depois do IGES, features depois do CAD tradicional).
