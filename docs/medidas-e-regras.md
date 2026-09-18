# Medidas e regras de negócio

## Organização das medidas

As medidas são centralizadas para que os cálculos possam ser reutilizados em
cards, tabelas e gráficos:

| Grupo | Finalidade |
| --- | --- |
| Ocorrências | Contar chamadas e registros no contexto selecionado |
| Status | Distribuir ocorrências por situação |
| Cobertura | Comparar planejamento e chamada por colaborador |
| Tempo | Filtrar mês, período e data de atualização |
| Indicadores | Retornar valor, rótulo ou estado visual |

## Regra de contexto

Uma medida não representa um número fixo. Ela responde aos filtros ativos:

```text
Medida = regra DAX + filtros ativos + relacionamentos do modelo
```

Por isso, o mesmo indicador pode mudar quando o usuário seleciona um período,
gestor, função, centro de custo ou colaborador.

## Regra de aderência

O cadastro de colaboradores calcula referências de mês para planejamento e
chamada. A comparação dessas referências produz um status de aderência,
permitindo identificar quando as duas visões estão alinhadas ou quando existe
uma exceção para investigação.

Essa regra é um apoio analítico: ela não substitui a validação operacional da
fonte nem deve ser interpretada sem o filtro de período correspondente.

## Cuidados

- contar ocorrências na granularidade correta;
- não misturar data de chamada com data de cadastro;
- tratar ausência de correspondência como exceção explícita;
- testar os indicadores com filtros de mês e colaborador;
- validar se o status visual representa a regra documentada.
