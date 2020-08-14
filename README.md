# Fazenda Inteligente: Desenvolvimento de um gêmeo digital para um sistema de irrigação.

Este repositório contém os códigos e componentes utilizados para a minha dissertação entitulada "Fazenda Inteligente: Desenvolvimento de um gêmeo digital para o sistema de irrigação" ainda em andamento.

As pastas disponíveis são as seguintes:

1. Plataform - Contém or arquivos necessários para subir uma plataforma IoT com base no FIWARE.
2. DataModel - Contém os arquivos .json utilizados para modelar as entidades nos diversos componentes utilizados na plataforma IoT. 
3. Data - Dados coletados ao longo do desenvolvimento do mestrado. 

Caso queira entrar em contato utilize o e-mail ralves@fei.edu.br
Verifique o meu curriculo lattes através do link: http://lattes.cnpq.br/6950937359307635
Para visualizar o meu perfil no Google Schoolar utilize o link: https://scholar.google.com.br/citations?user=swKME70AAAAJ&hl=pt-BR

## Projeto SWAMP

Este trabalha faz parte do projeto "Smart Water Management Platform" (SWAMP) desenvolvindo em parceria com universidades no Braisl, Espanha, Itália e Finlândia. 

Link para o site do projeto SWAMP: http://swamp-project.org/.
Link para o edital do projeto na comissão européria: https://cordis.europa.eu/project/id/777112

## Artigos interessantes. 

R. G. Alves et al., "A digital twin for smart farming," 2019 IEEE Global Humanitarian Technology Conference (GHTC), Seattle, WA, USA, 2019, pp. 1-4. Avilable at: https://ieeexplore.ieee.org/document/9033075

## Ferramentas utilizadas

Este trabalho utiliza o FIWARE para criar os serviços e compoentes a serem utilizados em nuvem para coletar dados dos sensores e enviar comandos para os atuadores. 

Para mais informações sobre o FIWARE utilize o link: https://www.fiware.org/.

## Lista de entidades do modelo de dados

Lista de entidades (Todas as entidades estão dentro da pasta Data Model -> Orion Entities):
1. 1 Irrigation System
2. 2 Management zones 
3. 2 Soil Probes
4. 1 Fuzzy Needs
5. 2 Irrigation recomendation
6. 1 Weather Observed
7. 1 Weather Forecast

## Etapas para funcionamento da simulação. 

Primeiramente é necessário instalar o Docker e o docker-compose. Siga os passos no link https://www.docker.com/ para o seu sistema operacional. Para usuários do Windows é recomendado utiliza o WSL2 um a versão do Ubunto 20.04LTS para isso siga o tutorial do link https://docs.docker.com/docker-for-windows/wsl/.

Após a instalação do docker e do docker-compose você pode acessar a pasta platform e utilizado o comando 'docker-compose up -d' para construir os componentes da plataforma. Caso seja a primeira vez que você esteja fazendo isso você verá, na linha de comando, as imagens de cada serviço sendo baixadas do docker-hub. 

A conexão entre os diversos componentes da plataforma é feita da seguinte forma:

![Arquitetura da plataforma](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/platform.png)

Após todos os serviços estarem funcionando nos seus devidos containers é necessário criar o modelo de dados a ser utilizado para o experimento. Navegue até a pasta dataModel e rode o script setup.py. Esse escript criará todoas as entidades no Orion, no IoT Agent Json e também o service group no ioT Agent e a subscrição no Orion. 

Com toidas as entidades criadas navegue até a pasta data e rode o script uploaddata.py. Esse script é responsável por enviar todos os dados utilizados para a siomulação para o IoT Agent. Os dados, para cada sonda de solo, podem ser conferidos na pasta soilProbeData.

A próxima etapa será a de configurar o Grafana para visualizar os dados de cada sensor bem como outras informações relevantes. Para isso utilize abre um navegador qualquer e digite localhost:3000. Coloque como login Admin e senha admin. escolha uma nova senha e salve/ 

## Servidor OPC UA

O servidor OPC UA foi desenvolvido em Python utilizando como base no python-opcua disponível em https://github.com/FreeOpcUa/python-opcua. Para o funcionamento dentro do ambiente virtual eu utilizei o docker para colocar o servidor dentro de um container e assim deixa-lo na mesma rede. Os arquivos relativos ao servidor OPC UA estão dentro da pasta /platform/OpcUAServer. Os componentes do servidor seguem a indicação da figura abaixo.  

![Componentes do servidor OPC UA](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/serverItens.png)


## Atividades desenvolvidas
1. Configurei o WSL versão 1 no laptop (Ubuntu 18.04 LTS). A versão 2 do WSL só está disponível após atualizar o windows para a Build 2004. 
2. Configuração da pasta Git para contribuir para esta branch. 
3. Pasta Data criada com um csv dos dados do projeto do Gilberto e também um Script Python capaz de ler tais dados e publica-los no Fiware
4. Configurei o WSL 2 no desktop (Ubuntu 20.04 LTS). A versão 2 tem melhor compatibilidade junto ao docker e também aos módulos do Linux. Também configurei o Visual Studio Code para trabalhar no WSL2. 
5. Comecei a trabalhar na construção do script python para rodar dentro do docker. Assim sendo é possivel deixar um script python rodando automaticamente dentro da arquitetura da plataforma. 
6. O componente Cygnus salva no banco de dados o Timestamp de quando ele recebe a notificação e não de quando o dado foi coletado. É necessário, portanto, fazer a query adequada no banco SQL para que seja possível resgatar o Timestamp desejado.Para utilizar o tempo em que o dado é enviado é necessário filtrar a tabela para apresentar o AttrName = TimeInstante como o Timestamp.
7. Realizado testes para elementos simples. Possivel ligar e desligar as áreas de irrigação de acordo com a simulação do Plant Simulation. 
8. É possivel conectar o Fiware e o servidor OPC UA através do IoT Agent OPC UA. Eu consegui fazer a conexão do IoT Agent OPC UA com um servidor OPC UA escrito em Python. Alteraçõa de variáveis e o envio de comandos (métodos) está funcionando. 
9. Realizada a conexão do Plant Simulation com o servidor OPC UA escrito em Python. É possivel alterar as variáveis do servidor e ver tal alteração refletida no Plant Simulation bem como realizar alterações no Plant SImulation e ver tal modificação refletida no servidor OPC UA. 
10. A modelagem de uma duas pequenas áreas de irrigação foi feita com 3 sprinklers para cada uma. Uma mesma bomba alimenta os dois sistemas e é possivel ligar e desligar cada área individualmente. 
11. Para a simulação foi necessário adaptar a mesma para ser capaz de assim que a recomendação de irrigação fosse feita a simulaçao desligaria o sistema. Isso foi feito através do compomente "Tanque" do Plant Simulation em que a recomendação de irrigação é convertida de mm para litros. Asism quando o tanque está cheio um comendo é enviado para fechar o sistema de irrigação e depois é feito o esvaziamento do tanque. 


## Etapas a realizar:

1. Desenvolver a planilha do Gilberto para 2 zonas de manejo. Para isso será necessário modificar os cálculos realizados na planilha dele de forma a criar 2 zonas de manejo com comportamentos de irrigação diferentes (1 pelo método Fuzzy e outro pelo método FAO, que será a área de controle). 

2. Conectar o process simulate e o simulador de PLC com um servidor OPC UA. Até o momento eu não consegui fazer a conexão do Process com um servidor OPC UA. Possiveis problemas são a versão do mesmo que no laboratório é a 14 e também algo que falta ser codificado no servidr Python para funcionar. Contudo mesmo em um servidor de exemplos que existe disponível gratuitamente na internet não foi possível fazer tal conexão. 

3. Ingluir o odelo Fuzzy feito pelo Gilberto para dentro da Plataforma IoT de modo que seja possivel deixar o script rodando e assim que uma recomendação de irrigaçõa for possível ele envie uma recomendação de irrigação para o IoT Agent OPC UA executar. Se eu conseguir fazer essa roda toda vai ser bem interessante. 

4. Testar a possibilidade de acionar os sistemas de irrigação através das plataformas IoT para assim automatizar completamente os sistemas e fazer a integração final criando assim o gêmeo digital do sistema. No momento eu consigo subir o FIWARE e fazer o mesmo enviar comandos para para o IoT Agent OPC UA e executá-los na simulação. É uma pena eu não poder construir o sistema real mas até que soluação está ficando bem bacana. 

## Estrutura Final para o ambiente do GitHub

1. Instalação do Docker e Docker-compose. [Windows](https://docs.docker.com/docker-for-windows/install/) or [MAC](https://docs.docker.com/docker-for-mac/install/) or [Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
2. Instalação do Docker-compose caso esteja no [Ubuntu ou outra distribuição Linux](https://docs.docker.com/compose/install/)
3.
