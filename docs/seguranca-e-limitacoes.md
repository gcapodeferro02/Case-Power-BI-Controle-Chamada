# Segurança e limitações

## O que não deve ser publicado

O case público não contém:

- arquivos PBIX ou PBIP;
- cache do modelo ou dados brutos;
- credenciais, DSNs ou arquivos de ambiente;
- URLs e caminhos internos;
- nomes de pessoas, matrículas ou identificadores reais;
- capturas de tela com dados legíveis.

## Sanitização

O fluxo recomendado é:

```text
Material autorizado -> remoção de dados sensíveis -> revisão visual -> publicação
```

Remover é preferível a apenas desfocar. Quando a estrutura visual precisar ser
preservada, use valores e rótulos genéricos antes de publicar.

## Limitações do case

O repositório explica arquitetura e raciocínio, mas não reproduz o ambiente de
produção. Portanto:

- as fontes são descritas genericamente;
- regras operacionais foram resumidas;
- resultados numéricos não validam o negócio real;
- a agenda de refresh depende da operação responsável pelas fontes.

## Checklist antes de publicar

- [ ] nenhuma imagem original foi copiada;
- [ ] valores, nomes e matrículas não estão legíveis;
- [ ] não existem arquivos PBIX, PBIP, cache ou segredos;
- [ ] não existem URLs internas ou caminhos locais;
- [ ] o README continua compreensível sem dados reais;
- [ ] links e diagramas renderizam corretamente no GitHub.
