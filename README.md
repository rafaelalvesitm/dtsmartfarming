# Um gemêo digital para uma fazenda inteligente

Este repositório contém os arquivos utilizados para a minha dissertação de mestrado. Estão incuidos os arquivos, modelos, dados e descobertas que eu fiz ao longo do processo de criação da dissertação. Também incluirei links importantes para saber mais sobre o projto desenvolvido e teiorias utilizadas. 

Caso queira entrar em contato utilize o e-mail ralves@fei.edu.br
Verifique o meu curriculo lattes através do link: http://lattes.cnpq.br/6950937359307635
Para visualizar o meu perfil no Google Schoolar utilize o link: https://scholar.google.com.br/citations?user=swKME70AAAAJ&hl=pt-BR

## Projeto SWAMP

Este trabalha faz parte do projeto "Smart Water Management Platform" (SWAMP) desenvolvindo em parceria com universidades no Braisl, Espanha, Itália e Finlândia. 

Link para o site do projeto SWAMP: http://swamp-project.org/.
Link para o edital do projeto na comissão européria: https://cordis.europa.eu/project/id/777112

## Artigos do autor

R. G. Alves et al., "A digital twin for smart farming," 2019 IEEE Global Humanitarian Technology Conference (GHTC), Seattle, WA, USA, 2019, pp. 1-4. Avilable at: https://ieeexplore.ieee.org/document/9033075

## Ferramentas utilizadas

Este trabalho utiliza o FIWARE para criar os serviços e compoentes a serem utilizados em nuvem para coletar dados dos sensores e enviar comandos para os atuadores. 

Para mais informações sobre o FIWARE utilize o link: https://www.fiware.org/.

## Lista de entidades do modelo de dados

Lista de entidades (Todas as entidades estão dentro da pasta Data Model -> Orion Entities):
1. 10 Sprinklers
2. 1 Central Pivot
3. 8 Management zones 
4. 8 Soil Probes
5. 8 Fuzzy Needs
6. 8 Irrigation recomendation
7. 1 Weather Observed
8. 1 Weather Forecast

## Etapas para funcionamento da simulação. 

Primeiramente é necessário instalar o Docker e o docker-compose. Siga os passos no link https://www.docker.com/ para o seu sistema operacional. Para usuários do Windows é recomendado utiliza o WSL2 um a versão do Ubunto 20.04LTS para isso siga o tutorial do link https://docs.docker.com/docker-for-windows/wsl/.

Após a instalação do docker e do docker-compose você pode acessar a pasta platform e utilizado o comando 'docker-compose up -d' para construir os componentes da plataforma. Caso seja a primeira vez que você esteja fazendo isso você verá, na linha de comando, as imagens de cada serviço sendo baixadas do docker-hub. 

A conexão entre os diversos componentes da plataforma é feita da seguinte forma:

![Arquitetura da plataforma](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/platform.png)

## Atividades
1. Configurei o WSL versão 1 no laptop (Ubuntu 18.04 LTS). A versão 2 do WSL só está disponível após atualizar o windows para a Build 2004. 
2. Configuração da pasta Git para contribuir para esta branch. 
3. Pasta Data criada com um csv dos dados do projeto do Gilberto e também um Script Python capaz de ler tais dados e publica-los no Fiware
4. Configurei o WSL 2 no desktop (Ubuntu 20.04 LTS). A versão 2 tem melhor compatibilidade junto ao docker e também aos módulos do Linux. Também configurei o Visual Studio Code para trabalhar no WSL2. 
5. Comecei a trabalhar na construção do script python para rodar dentro do docker. Assim sendo é possivel deixar um script python rodando automaticamente dentro da arquitetura da plataforma. 

Trabalhar ainda:
1R. A notificação do Cygnus para o MySQL sempre salva as colunas de TImestamp como o tempo em que a notificação é recebida e não o tempo em que o dado é enviado. Para utilizar o tempo em que o dado é enviado é necessário filtrar a tabela para apresentar o AttrName = TimeInstante como o Timestamp. 

2. Desenvolver a planilha do Gilberto para outras zonas de manejo. Para isso será necessário modificar os cálculos realizados na planilha dele de forma a criar zonas de manejo com comportamentos diferentes como por exemplo ambiente mais seco, mais umido, totalmente molhado etc. Também é possivel criar uma irrigação com o modelo Fuzzy e outra apenas com o modelo FAO etc. 

3R. O modelo de dados de entidades foi criado levando em consideração as entidades apresentadas anterioremente. Esse modelo de dados leva em consideração 8 áreas diferentes com recomendações de irrigação diferentes. 

4. Criar a simulacão do pivô central no Process Simualte e realizar a configuração de movimentações difernetes para o pivô central. Testes devem ser realizados em elementos simples. 

5. Realizar a conexão do process simulate com um simulador de PLC para verificar as funcionalidades dos elementos e possivelmente conectar de maneira automática todos os elementos. 

6. Conectar o process simulate e o simulador de PLC com um servidor OPC UA. Essa intergração ainda está nebulosa para min mas acredito ser possivel de realizar. 

7. Realizar a integração o servidor OPC UA com o Fiware através do IoT Agent. E também do Mindsphere através do MindConnect. 

8. Testar a possibilidade de acionar os sismtemas de irrigação através das plataformas IoT para assim automatizar completamente os sismteas e fazer a integração final criando assim o gêmeo digital do sistema. 
