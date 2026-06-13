# 1. Interoperabilidade e Padrões de Troca de Dados CAD

*(Baseado nas anotações de 27/05 e 03/06)*

Este bloco trata de como diferentes softwares conversam entre si e como as informações de projeto e manufatura são armazenadas e transportadas.

## Estratégias de Comunicação

- O objetivo é a troca de arquivos de manufatura com o melhor custo-benefício para transportar dados entre aplicativos.
- Duas opções principais: Usar um tradutor direto ou usar uma interface/arquivo neutro.
- **Trade-off**: O arquivo neutro costuma ser muito maior em tamanho.

## Padrões Clássicos e Histórico

- Programa ICAM (Integrated Computer-Aided Manufacturing).
- Padrões de mercado: IGES, SET, VDA-FS.

## O Padrão STEP (Norma ISO 10303)

- **Atenção (Questão de Prova)**: Qual a diferença do STEP para o IGES?
- Arquitetura do STEP: Protocolos STEP, Description Methods (métodos de descrição), Integrated Resources (recursos integrados).
- Linguagem e Acesso: EXPRESS Language e SDAI (Standard Data Access Interface).

## Modelos de Produto (Product Models)

- Divisão em domínios: Estrutural (Structural), Geometria (Geometry), Conhecimento (Knowledge), resultando em Integrated Product Models.

## Aplicações na Manufatura

- Benefícios advindos da verificação de conformidade.
- Integração com NC (Comando Numérico) e CNC.

---

# 2. Modelagem Paramétrica, Variacional e Restrições

*(Baseado nas anotações de 10/06 e início da página sem data)*

Aqui o foco muda da troca de arquivos para a lógica de construção do modelo e como o software entende as regras do seu projeto.

## Conceitos Fundamentais

- Intenção de Projeto (Design Intent).
- Criação de Famílias de Peças.

## Tipos de Restrições (Constraints)

- Restrições Geométricas.
- Restrições Funcionais (ex: stress, fluência).
- Restrições Variacionais.

## Métodos Matemáticos e Computacionais de Resolução

- Modelos baseados a restrições vs. Métodos procedurais.
- Uso de Grafos e Predicados.
- Sistemas de Equações Simultâneas.
- Função Implícita.

---

# 3. Modelagem Avançada CAD e Baseada em Feições (Features)

*(Baseado nas anotações da página sem data)*

Este último bloco aborda as limitações dos sistemas CAD mais antigos e a evolução para a modelagem orientada a features.

## Deficiências do CAD Tradicional

- Utiliza "dados microscópicos" (linhas, pontos) que levam à sub-especificação geométrica.
- Faltam as intenções de projeto na estrutura de dados.
- Construção tediosa para o usuário.
- A estrutura de dados é de um único nível.

## Feições Geométricas (Features)

- **Classificação Física/Abstrata**: Features Físicas vs. Features Abstratas.
- **Classificação de Aplicação**: Form Features (Feições de Forma) e Manufacturing Features (Feições de Manufatura).
- **Tipologia Geométrica**: Features Rotacionais e Prismáticas.
