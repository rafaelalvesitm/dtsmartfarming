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
    - Postman
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

É importante destacar as funcionalidades de cada container utilizado na plataforma bem como os parâmetros que devem ser configurados nesses elementos para garantir que cada componente funcione de maneira adequada. A seguir tem-se as explicações de cada um dos componenetes utilizados.  

### Orion Context Broker

O [Orion Context Broker](https://fiware-orion.readthedocs.io/en/master/) é um componente oferecido pelo [FIWARE](https://www.fiware.org/). Este componente faz a gestão do ciclo de vida das informações de contexto incluindo atualizações, consultas, registros e assinaturas. Para realizar a gestão de contexto o Orion trabalha com o conceito de entidades. As entidades são escritas no formato JSON e devem conter os atributos e propriedades que descrevem estas entidades como por exemplo a entidade abaixo:

```JSON
{
  "id": "Room1",
  "type": "Room",
  "temperature": {
    "value": 23,
    "type": "Float"
  },
  "pressure": {
    "value": 720,
    "type": "Integer"
  }
}
```

Neste exemplo temos uma entidade que representa um sensor de temperatura e pressão instalados em um quarto qualquer. Nota-se que é importante que todas as entidades do Orion tenham os atributos `id` e `type` e que outros atributos devem conter as propriedades `value` e `type`. Para maiores descrições de como criar um modelo de dados podem ser conferidas na [página de modelos de dados do FIWARE](https://fiware-datamodels.readthedocs.io/en/latest/index.html)

As entidades criadas no Orion para este projeto estão definidads na pasta [orionEntities](/platform/data_model/orionEntities) e são automaticamente enviadas ao Orion quando o comando `docker-compose up -d` é utilizado. Caso queira fazer qualquer modificação nesse modelo de dados você pode criar arquivos JSON personalizados dentro da pasta indicada ou então utilizar algum cliente REST como o [RESTCLient](http://restclient.net/) ou [Postman](https://www.postman.com/).

### Mongo DB

O MongoDB é um banco de dados distribuído de propósito geral e orientado a documentos, ou seja, ele armazena os dados em forma de arquivos. O Mongo DB é utilizado na plataforma para armazenar a estrutura das entidades do Orion Context Broker e do IoT Agent JSON. Para a plataforma não é necessário configurar nada diretamente no Mongo DB, a configuração é feita no arquivo `docker-compose` localizado na pasta [plataform](/platform).

### MySQL Database

O MySQL database é um banco de dados SQL e é utilizado na plataforma para armazenar as alterações que ocorrem nos dados das entidades do Orion. Para que tal armazenamento ocorra é necessário ter o Cygnus na plataforma para enviar os dados do Orion Context Broker para serem armazenados no MySQL. 

Não é necessário realizar nenhuma configuração no MySQL diretamente, a configuração é feita no arquivo `docker-compose` localizado na pasta [plataform](/platform). É importante notar que o usuário padrão é o `root` com senha `123`. Para acessar o banco SQL através da linha de comando utilize o seguinte comando `docker exec -it  db-mysql mysql -h mysql-db -P 3306  -u root -p123`.

Para aprender como fazer requisições no banco SQL você pode acessar os [tutoriais da W3 Schools](https://www.w3schools.com/sql/). Para algumas requisições é possivel conferir o arquivo `query.txt` localizado na pasta [platform](/platform). 

### IoT Agent Json

O ioT Agent Json é um agente que faz a ponte entre um dispositivo que utiliza o protocolo JSON com brokers que utilizam o protocolo NGSI como o Orion Contex Broker. As configurações o IoT Agent JSON são escritas no arquivo `docker-compose` localizado na pasta [plataform](/platform). Essas configurações são feitas para fazer a união entre o IoT Agent Json e o Orion Context Broker para que quando uma dado seja enviado ao IoT Agent JSON ele seja encaminhado ao Orion e também para que os comandos enviados ao Orion sejam encaminhados ao IoT Agent JSON. Para maiores informações sobre as funcionalidades do IoT Agent JSON acesse a [documentação do FIWARE sobre o componente](https://fiware-iotagent-json.readthedocs.io/en/latest/stepbystep/index.html).

Para este ambiente de simulação os dispositivos cadastranos no IoT Agent JSON estão localizadas na pasta [iotAgentJson](/platform/data_model/iotAgentJson) para que o container data_model faça a envio dessas entidades para o IoT Agent Json. Nota-se também que caso você crie uma entidade no IoT Agent JSON que não existe inicialmente no Orion o próprio componente é capaz de criar uma entidade no Orion também. Caso queira fazer qualquer alteração nas entidades do IoT Agent pode ser feita diretamente na pasta [platform/data_model/iotAgentJson](/platform/data_model/iotAgentJson) ou então utilizando um cliente REST como o [RESTCLient](http://restclient.net/) ou [Postman](https://www.postman.com/).

### IoT Agent OPC UA

O componente IoT Agent OPC UA faz a comunicação entre um servidor OPC UA e a Orion Context Broker. Este componente tem como base o [código disponivel aqui](https://github.com/Engineering-Research-and-Development/iotagent-opcua). Para a configuração do IoT Agent OPC UA é necessário modificar os arquivos localizados na pasta [/platform/iotAgentOpcUa/AGECONF](/platform/iotAgentOpcUa/AGECONF). O arquivo `config.properties` contém as informações relativas ao parametros do IoT Agent OPC UA e o arquivo `config.json` contém a configuração das entidades dos dispositivos que serão criados no IoT Agent OPC UA assim que ele for montado. 

Os dois aquivos podem ser modificados de acordo com as necessidades do ambiente de desenvolvimento que esteja sendo utilizado, mas não é necessário fazer nenhuma alteração para que esta simulação funcione. É importante destacar que o mapeamento entre os nós do servidor OPC UA e as propriedades dos dispositivos no IoT Agent OPC UA deve ser feita com cautela para que os dados sejam comunicados de forma correta. Também é importante destacar que este componente ainda está em fase de desenvolvimento mas já é possivel fazer a comunicação de dados e o acionamento de comandos através do agente. 

### Cygnus

O Cygnus é um conector encarregado de persistir certas fontes de dados em certos armazenamentos de terceiros (MySQL, PosgreSQL, Kafka, CKAN, Carto etc), criando uma visão histórica de tais dados. As configurações deste componente são feitas no arquivo `docker-compose` localizado na pasta [/platform](/platform). Não é necessário fazer nenhuma alteração no documento para que essa simulação funcione mas caso seja necessário adicionar outros banco de dados ao Cygnus utilize o [manual de referência disponibilizado pelo FIWARE](https://fiware-cygnus.readthedocs.io/en/latest/cygnus-ngsi/installation_and_administration_guide/install_with_docker/index.html). 

Nesta simulação utiliza-se apenas o banco MySQL para fazer a persistencia dos dados contudo é possivel fazer o Cygnus persistir os dados em mais de um banco ao mesmo tempo utilizando a variável `CYGNUS_MULTIAGENT`.

### Grafana

Grafana é uma aplicação web de análise de código aberto multiplataforma e visualização interativa da web. Ele fornece tabelas, gráficos e alertas para a Web quando conectado a fontes de dados suportadas como o MySQL desta simulação. Com o Grafana é possivel criar painéis interativos para visualizar os dados obtidos pela plataforma. Tais painéis são configurados no próprio componente acessando, via browser, o link `localhost:3000` caso esta simulação esteja sendo criada em ambeinte local de desenvolvimento. 

Inicialmente o Grafana irá pedir um login e senha sendo eles `admin` e `admin`. Logo após será necessário alterar a senha que fica a critério do usuário. O próximo passo é fazer o cadastro do banco de dados como mostra as figuras a seguir:

![Selecione Data Sourcer para conectar um banco de dados ao Grafana ](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/grafana.png)

![Configure os parametros de acordo com o banco de dados](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/grafana2.png)

Após estes passos é possivel criar o painél interativo de acordo com as necessidades ou então utilizar o painel previamente condificado, para isso click em `import` como indicado na figura abixo e depois em `Upload JSON File` e adicione o arquivo `panel.json` disponível na pasta [/platform](/platform). 

![Importe o arquivo panel.json para o grafana](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/grafana3.png)

Após acessar a Dashboard e possivel, no menu superior direito da Dashboard, configurar o painel para mostrar os dados relativos a um determinado periodo bem como alterar a taxa de atualização do painel. 

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
