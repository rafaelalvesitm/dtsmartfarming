# Fazenda Inteligente: Desenvolvimento de um gêmeo digital para um sistema de irrigação.

Este repositório contém os códigos e componentes utilizados para a minha dissertação entitulada "Fazenda Inteligente: Desenvolvimento de um gêmeo digital para o sistema de irrigação" ainda em andamento.

Este trabalho faz parte do projeto ["Smart Water Management Platform"](http://swamp-project.org/) (SWAMP) desenvolvindo em parceria com universidades no Brasil, Espanha, Itália e Finlândia. O projeto é financiado pela [Comissão Europeia dentro do H2020-EU.2.1.1](https://cordis.europa.eu/project/id/777112)

Verifique o meu [curriculo lattes](http://lattes.cnpq.br/6950937359307635) ou então o meu perfil no [Google Schoolar](https://scholar.google.com.br/citations?user=swKME70AAAAJ&hl=pt-BR)

Caso queira entrar em contato utilize o e-mail ralves@fei.edu.br ou rgomesal@hotmail.com

## Artigos interessantes. 

Aqui você encontra artigos sobre o desenvolvimento deste trabalho, artigos sobre autores parceiros ou então artigos importantes sobre a aplicação de tecnologia na agricultura. 

- R. G. Alves et al., "A digital twin for smart farming," 2019 IEEE Global Humanitarian Technology Conference (GHTC), Seattle, WA, USA, 2019, pp. 1-4. Available at: https://ieeexplore.ieee.org/document/9033075

- Kamienski, C.; Soininen, J.-P.; Taumberger, M.; Dantas, R.; Toscano, A.; Salmon Cinotti, T.; Filev Maia, R.; Torre Neto, A. Smart Water Management Platform: IoT-Based Precision Irrigation for Agriculture. Sensors 2019, 19, 276. Available at: http://www.mdpi.com/1424-8220/19/2/276.

- S. Monteleone, E. A. de Moraes and R. F. Maia, "Analysis of the variables that affect the intention to adopt Precision Agriculture for smart water management in Agriculture 4.0 context," 2019 Global IoT Summit (GIoTS), Aarhus, Denmark, 2019, pp. 1-6, Available at: https://ieeexplore.ieee.org/document/8766384.

## Ferramentas utilizadas

Este trabalho utiliza as seguintes ferramentas:

- Para as funcionaldiades da plataforma
    -  Componentes da plataforma FIWARE 
    - Banco de dados MySQL e MongoDB
- Para montar a plataforma em ambiente local
    - Docker e docker-compose
- Para realizar a simulação do sistema de irrigação
    - Plant Simulation
    - Servidor OPC UA
- Para o desenvolvimento do código e outros serviços
    - Visual Studio Code 
    - Open Weather API
    - Wunderground API

## Etapas para montar a plataforma de Internet das Coisas

Primeiramente é necessário instalar o Docker e o docker-compose. Siga os passos no link https://www.docker.com/ para o seu sistema operacional. Para usuários do Windows é recomendado utilizar o WSL2 com uma versão do Ubuntu, para isso siga o tutorial do link https://docs.docker.com/docker-for-windows/wsl/.

Após a instalção do docker e do docker-compose acesse a pasta [Weather Handler](/platform/weather_handler) e crir um arquivo `config.py` com a com a delcaração das variáveis `api_key` e `api_key_wunder` com as cahves para as APIs do [OpenWeather](https://openweathermap.org/) (OneCall API) e [Wunderground](https://www.wunderground.com/). 

Para montar as imagens dos containers utilizados acesse a pasta [platform](/platform) pelo terminal e utilize o comando `docker-compose build`. Por fim, utilize o comando `docker-compose up -d` para subir os containers para o ambiente de desenvolvimento local. 

Os containers utilizados neste ambiente são os seguintes:

Elementos desenvolvidos por terceiros e apenas configurados para utilização neste projeto. 

- [Orion Context Broker:](https://fiware-orion.readthedocs.io/en/master/) O Orion Context Broker permite que você gerencie todo o ciclo de vida das informações de contexto, incluindo atualizações, consultas, registros e assinaturas
- [Mongo DB:](https://www.mongodb.com/) O MongoDB é um banco de dados distribuído de propósito geral, baseado em documento, criado para desenvolvedores de aplicativos modernos e para a era da nuvem.
- [MySQL DB:](https://www.mysql.com/) O MySQL é um sistema de gerenciamento de banco de dados, que utiliza a linguagem SQL como interface.
- IoT Agent Ultralight
- [IoT Agent Json:](https://fiware-iotagent-json.readthedocs.io/en/latest/) O ioT Agent Json é um agente que faz a ponte entre um dispositivo que utilizam o protocolo JSON com brokers que utilizam o protocolo NGSI como o Orion Contex Broker
- [IoT Agent OPC UA:](https://iotagent-opcua.readthedocs.io/en/latest/) O IoT Agent OPC UA é um agente que faz a ponte entre dispositivos que utilizam um servidor OPC UA e o Orion Contex Broker. 
- [Cygnus:](https://fiware-cygnus.readthedocs.io/en/latest/) O Cygnus é um conector encarregado de persistir certas fontes de dados em certos armazenamentos de terceiros (MySQL, PosgreSQL, Kafka, CKAN, Carto etc), criando uma visão histórica de tais dados.
- [Grafana:](https://grafana.com/) Grafana é uma aplicação web de análise de código aberto multiplataforma e visualização interativa da web. Ele fornece tabelas, gráficos e alertas para a Web quando conectado a fontes de dados suportadas

Elementos desenvolvidos pelo autor deste projeto. 

- Opc UA Server: Servidor OPC UA contendo os elementos que compoe o sistema de irrigação proposto.  
- Weather Handler: O Weather Handler faz a coleta de parametros climáticos com base nas APIs do OpenWeather e também do Wundergorund. 
- Data Model: o Data Model faz a publicação das entidades a serem utilizadas no Orion, IoT Agent JSON e Cygnus para que o ambeinte virtual esteja configurado de acordo com a proposta do autor. 
- Probe: O Probe faz o envio dos dados de uma sonda de solo hipotética. Estes dados foram coletados de uma sonda de solo real que ficou em operação durante 3 meses, contudo não devem ser usados para validar modelos de irrigação mas apenas como validação da comunicação real que aconteceria entre a sonda e a plataforma. 

A conexão entre os diversos componentes da plataforma é feita da seguinte forma:

![Arquitetura da plataforma](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/platform.png)

## Descrição da atuação de cada componente na plataforma, sua configuração e outras informações importantes. 

### Orion Context Broker

### Mongo DB

### MySQL Database

### IoT Agent Json

### IoT Agent OPC UA

### Cygnus

### Grafana

### Servidor OPC UA

O servidor OPC UA foi desenvolvido em Python utilizando como base no [python-opcua](https://github.com/FreeOpcUa/python-opcua). Os arquivos relativos ao servidor OPC UA estão dentro da pasta [/platform/OpcUAServer](/platform/OpcUAServer). Os componentes do servidor seguem a indicação da figura abaixo.  

![Componentes do servidor OPC UA](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/serverItens.png)

Nota-se que o servidor tem 3 objetos sendo eles a bomba de água, a zona de controle e a zona Fuzzy. Para cada zona tem-se 3 sprinklers que fazem a irrigação de cada área. As variáveis das zonas sõa denominadas "Open" para saber se os sprinklers estão ou não abertos, "q"para indicar a vazão de cada sprinkler e da zona como um todo, "v" para o volume irrigado por cada sprinkler caso a operação manual esteja ativa e "ir" para a recomendação de irrigação para a área. 

Existe também duas pastas: uma para os comandos da operação manual e uma para os comandos das operações automáticas. Entende-se por automáticas as ações que vão irrigar a zona de controle e/ou a zona fuzzy de acordo com o que for determinado pela plataforma IoT e por ações manuais as ações que podem ser utilizadas pelo fazendeiro. As ações manuais são capazes de ligar e desligar a bomba de água, abrir e fechar as zonas de irrigação e ligar e desligar todos os componentes de uma vez. 

É possivel adicionar outras variáveis e métodos de acordo com as necessidades de projeto alterando o script [server.py](/platform/OpcUAServer/server.py)

### Weather Handler

O [Weather Handler](/platform/weather_handler) é responsável por coletar as variáveis climáticas das APIs [OpenWeather](https://openweathermap.org/) (OneCall API)  e [Wunderground](https://www.wunderground.com/) e posta-las no Orion Context Broker nas entidades Weather Current e Weather Forecast relativas a cada API. Nota-se que na pasta falta um arquivo config.py com a delcaração das variáveis `api_key` e `api_key_wunder` que devem ser incluidas na pasta antes de montar e subir os containers localmente. 

O código [weather.py](/platform/weather_handler/weater.py) coleta os parametros climáticos de São Bernardo do Campo de hora em hora. É possivel alterar o local em que as variáveis climáticas são coletadas bem como o intervalo de tempo dessa coleta. Também é importante notar que a previsão climática pela API do OpenWeather é de 7 dias enquanto que a previsão do Wunderground é de 5 dias.  

o Weather handler coleta os seguintes parâmetros:

![Parametros coletados pelo Weather Handler](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/weatherHandler.png)

### Data Model

### Probe
