# Case: desenvolvimento de um Power BI de controle de chamada

> Documentação pública e sanitizada de uma solução operacional e analítica para
> registrar presença, consolidar chamadas e acompanhar a operação.

> [!WARNING]
> Esta é uma documentação pública e sanitizada de uma solução desenvolvida em
> ambiente corporativo. Dados, identificadores, credenciais e informações
> sensíveis foram removidos ou substituídos; não há dados brutos, arquivos
> PBIX/PBIP, cache do modelo ou conexões corporativas.

## Contexto e problema

O controle de chamada precisa transformar registros de ocorrência e uma base de
colaboradores em uma leitura simples sobre presença, status e cobertura do
quadro planejado. O desafio envolve combinar uma fonte transacional com bases de
apoio, preservar a granularidade dos eventos e permitir filtros confiáveis por
período, colaborador, gestor e centro de custo.

Sem uma entrada padronizada, os registros de presença e falta ficam sujeitos a
lançamentos dispersos, interpretações diferentes e dificuldade de consolidação.
Isso reduz a visibilidade dos gestores sobre a situação diária da operação.

Este case documenta como a entrada operacional foi conectada a um modelo
analítico, sem reproduzir informações do ambiente original.

## Solução

A solução combina um aplicativo de lançamento, uma planilha operacional e um
relatório Power BI. Os gestores registram as ocorrências, os dados são
organizados para tratamento e o modelo semântico transforma os lançamentos em
indicadores de presença, falta, status e aderência ao planejamento.

## Minha atuação

Atuei nas frentes documentadas neste repositório:

- estruturação da solução de entrada e acompanhamento operacional;
- organização das fontes e do fluxo de integração;
- modelagem de fatos, dimensões, calendário e relacionamentos;
- definição de medidas e regras de acompanhamento;
- organização das páginas e evidências do relatório;
- validação da carga e documentação sanitizada da solução.

## O que este case demonstra

- ingestão de registros de chamada a partir de uma fonte relacional;
- integração com uma base de colaboradores e planejamento;
- uso de atualização incremental para a tabela de ocorrências;
- separação entre fatos, dimensões, calendário e medidas;
- relacionamentos por matrícula, status e data;
- medidas para contagem, acompanhamento e comparação de status;
- navegação entre visão executiva e detalhamento operacional;
- publicação segura de evidências e documentação.

[Diagrama da arquitetura do relatório](assets/arquitetura-dados.mmd)

![Fluxo de arquitetura de referência](assets/fluxo-arquitetura-referencia.png)

> A imagem acima é uma referência visual de arquitetura de dados e não
> representa literalmente todas as fontes ou ferramentas deste case.

## Como funciona

```text
Gestor
  ↓
Aplicativo de presença
  ↓
Google Sheets
  ↓
Tratamento e integração
  ↓
Modelo Power BI
  ↓
Indicadores operacionais
```

## Aplicativo de lançamento de presença

![Aplicativo de controle de presença](assets/app-controle-presenca.png)

O aplicativo de lançamento de presença foi criado com **Google Apps Script** e
integrado a uma planilha do **Google Sheets**. Os gestores da operação realizam
o input diário dos dados de presença, falta e demais ocorrências dos
colaboradores.

Esses lançamentos alimentam a planilha, que funciona como base operacional para
gerar os dados de presença e falta consumidos pelo Power BI. Dessa forma, o
relatório transforma o input realizado na operação em uma visão consolidada
para acompanhamento e análise.

## Índice da documentação

| Documento | O que explica |
| --- | --- |
| [Arquitetura](docs/arquitetura.md) | Camadas e responsabilidades da solução |
| [Atualização e fontes](docs/atualizacao-e-fontes.md) | Entrada, tratamento e refresh |
| [Modelo e relacionamentos](docs/modelo-e-relacionamentos.md) | Fatos, dimensões, chaves e filtros |
| [Medidas e regras](docs/medidas-e-regras.md) | Regras de acompanhamento e status |
| [Páginas do relatório](docs/paginas-do-relatorio.md) | Organização da experiência de análise |
| [Segurança e limitações](docs/seguranca-e-limitacoes.md) | Sanitização e limites do case público |

## Stack utilizada

| Camada | Tecnologia | Finalidade |
| --- | --- | --- |
| Origem | Banco relacional e arquivos corporativos | Disponibilizar ocorrências e bases de apoio |
| Ingestão | Power Query | Conectar, filtrar, combinar e tipar dados |
| Modelagem | Power BI Semantic Model | Organizar fatos, dimensões e relacionamentos |
| Cálculo | DAX | Criar indicadores e regras de status |
| Apresentação | Power BI Report | Exibir o acompanhamento executivo e operacional |
| Documentação | Markdown + Mermaid | Explicar decisões, fluxos e limitações |

## Impacto / resultado

Com a solução, a operação passou a contar com:

- uma entrada mais padronizada para ocorrências de presença e falta;
- uma base centralizada para acompanhamento diário;
- filtros consistentes por período, colaborador e estrutura operacional;
- uma visão analítica que conecta o lançamento do gestor ao indicador.

O relatório responde perguntas como:

- quantas chamadas foram registradas no período;
- como os registros se distribuem por status;
- quais colaboradores possuem correspondência entre planejamento e chamada;
- como filtrar a análise por gestor, função, centro de custo ou período;
- quando ocorreu a última atualização da base.

Os dados e identificadores exibidos no ambiente original não são publicados. O
foco do case é explicar a construção do modelo e da análise.

## Segurança por padrão

O repositório foi desenhado para publicar documentação e evidências
sanitizadas. Antes de qualquer publicação, devem ser verificados arquivos
proibidos, segredos, caminhos locais, URLs internas e dados identificáveis.

## Estratégia de atualização

A tabela de ocorrências foi preparada para atualização incremental. O princípio
é atualizar a janela recente de eventos sem recarregar desnecessariamente todo o
histórico, mantendo o modelo mais adequado ao crescimento da operação.

Os parâmetros internos não são publicados. Antes do consumo, devem ser
validados volume, período carregado, correspondência de matrículas e data da
última atualização.

## Próximos passos

- adicionar testes de qualidade para duplicidade de matrícula e integridade de datas;
- documentar um contrato de atualização para cada fonte;
- acompanhar duração e falha do refresh;
- evoluir indicadores de cobertura e exceção para uma camada analítica governada.
