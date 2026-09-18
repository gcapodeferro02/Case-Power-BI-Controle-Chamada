# Case: desenvolvimento de um Power BI de controle de chamada

> Documentação de portfólio sobre a construção de um relatório para acompanhar
> chamadas, status de presença, colaboradores e aderência ao planejamento.

> [!WARNING]
> Este é um case público e educativo. O repositório contém documentação e
> diagramas sanitizados; não há dados brutos, credenciais, arquivos PBIX/PBIP,
> cache do modelo ou conexões corporativas.

## Contexto

O controle de chamada precisa transformar registros de ocorrência e uma base de
colaboradores em uma leitura simples sobre presença, status e cobertura do
quadro planejado. O desafio envolve combinar uma fonte transacional com bases de
apoio, preservar a granularidade dos eventos e permitir filtros confiáveis por
período, colaborador, gestor e centro de custo.

Este case documenta o raciocínio de dados e de produto analítico sem reproduzir
informações do ambiente original.

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

## Resultado

O relatório foi estruturado para responder perguntas como:

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

## Próximos passos

- adicionar testes de qualidade para duplicidade de matrícula e integridade de datas;
- documentar um contrato de atualização para cada fonte;
- acompanhar duração e falha do refresh;
- evoluir indicadores de cobertura e exceção para uma camada analítica governada.
