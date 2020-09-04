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
    - Componentes da [plataforma FIWARE ](https://www.fiware.org/)
    - Banco de dados [MySQL DB:](https://www.mysql.com/) e [Mongo DB:](https://www.mongodb.com/)
    - [Grafana:](https://grafana.com/)
    - Componentes personalizados desenvolvidos pelo autor
- Para montar a plataforma em ambiente local
    - [Docker](https://docs.docker.com/get-docker/) e [docker-compose](https://docs.docker.com/compose/)
- Para realizar a simulação do sistema de irrigação
    - [Plant Simulation](https://www.plm.automation.siemens.com/global/pt/products/manufacturing-planning/plant-simulation-throughput-optimization.html)
    - Servidor OPC UA desenvolvido em Python pelo autor
- Para o desenvolvimento do código e outros serviços
    - [Visual Studio Code](https://code.visualstudio.com/) 
    - [Postman](https://www.postman.com/)
    - [Open Weather OneCall API](/platform/weather_handler) 
    - [Wunderground API](https://www.wunderground.com/)

## Etapas para montar a plataforma de Internet das Coisas

Primeiramente é necessário [instalar o Docker](https://docs.docker.com/get-docker/) e o [docker-compose](https://docs.docker.com/compose/). Para usuários do Windows é recomendado utilizar o WSL2 com uma versão do Ubuntu, para isso siga o [tutorial do link](https://docs.docker.com/docker-for-windows/wsl/).

Após a instalção do docker e do docker-compose acesse a pasta [Weather Handler](/platform/weather_handler) e crir um arquivo `config.py` com a com a delcaração das variáveis `api_key` e `api_key_wunder` com as chavees para as APIs do [OpenWeather](https://openweathermap.org/) (OneCall API) e [Wunderground](https://www.wunderground.com/). A API do OpenWeather é aberta para qualquer um sendo necessário apenas fazer uma conta no site e solicitar a chave da API já para a API do Wunderground é necessário ter uma estação meterológica para fazer o cadastro no site.  

Para montar as imagens dos containers utilizados acesse a pasta [platform](/platform) pelo terminal e utilize o comando `docker-compose build`. Por fim, utilize o comando `docker-compose up -d` para subir os containers para o ambiente de desenvolvimento local. 

Após tal configuração é necessário configurar o grafana para se conectar a base de dados e também para mostrar a dashboard que foi criada, para isso siga o tutorial na [Seção Grafana](#Grafana)

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

É necessário que o Cygnus esteja subscrito em uma entidade do Orion para que o Cygnus seja capaz de armazenar os dadso no banco MySQL. A subscrição é feita criando uma notificação no Orion como indicada no código JSON abaixo e que deve ser enviado através de um client REST ou código usando uma requisição HTTP do tipo POST. O Código dispoível no container data-model faz a subscrição com o código apresentado abaixo. 

```JSON
{
    "description": "Notify Cygnus of all context changes",
    "subject": {
        "entities": [
            {
                "idPattern": ".*"
            }
        ]
    },
    "notification": {
        "http": {
            "url": "http://cygnus:5050/notify"
        }
    },
    "throttling": 1
}
```

Isso significa que todas as entidades do Orion estão sobrescritas pelo Cygnus, ou seja, o Cygnus é capaz de monitorar todas as entidades do Orion e se alguma delas sofrer alguma alteração em um de seus parâmetros o Cygnus ira fazer a persistencia dos dados da entidade toda no banco MySQL.

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

Este container foi desenvolvido apenas para criar as entidades no Orion Context broker, criar as entidades  no IoT Agent JSON, e criar a subscrição do Cygnus no Orion Context Broker. Cada um dos elementos criados está dentro de suas respectivas pastas dentro da pasta [/platform/data_model](/platform/data_model). Note que da forma que o script `setup.py` está escrito qualquer arquivo .json que esteja dentro da pasta `orionEntities` tentará ser enviado para o Orion, os arquivos dentro da pasta `iotAgentJson` será enviado para o IoT Agent JSON e por fim uma subscrição para todas as entidades do Orion é feita no Cygnus. 

### Probe

Este container foi desenvolvido para simular o comportamento de uma sonda de solo. O script python `uploaddata.py` disponível na pasta [/platform/probe](/platform/probe) faz o envio dos dados contidos no arquivo `SoilProbeData.csv` localizado na mesma pasta. O Envio dos dados é feito a cada 30 minutos pelo contianer pois foi essa a taxa de coleta utilizada em um experimento realizado com uma sonda de solo real. 

É importante destacar que apesar de uma sonda de solo real ter coletado os dados que estão disponíveis no arquivo `SoilProbeData.csv`, tais dados não devem ser usados para validar recomendações de irrigação pois eles apresentam incosistencias devido a problemas no sensor e também levam em conta a chuva que ocorreu durante o periodo em que tais dados foram coletados. Esses dados server para validar a comunicação que aconteceria entre uma sonda de solo e toda a plataforma IoT montada nesta simulação.

## Simulação do sistema de irrigação

Para a simulação do sistema de irrigação foi desenvolvido um modelo utilizando o software [Plant Simulation](https://www.plm.automation.siemens.com/global/pt/products/manufacturing-planning/plant-simulation-throughput-optimization.html). A visualização da simulação é indicada na figura abaixo:

![Visualização da simulação no Plant Simulation](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/plantsimulation1.png)

A simulação é conectada a um servidor OPC UA através de um módulo OPC UA do Plant Simulation que requer uma licença especifica. O Plant Simulation tem uma [versão de estudante](https://www.plm.automation.siemens.com/plmapp/education/plant-simulation/en_us/free-software/student/) que permite visualizar o modelo mas não é possivel conectar o modelo a um servidor OPC UA. Com este modelo é possivel simular o comportamento do sistema de irrigação de acordo com os métodos que foram descritos na [seção Servidor OPC UA](#Servidor-OPC-UA).

O sistema de irrigação é composto por uma bomba de água que alimenta duas regiões: uma de denominada região Controle na qual a prescrição de irrigação é feita com base no modelo de evapotranspiração da Organização Das Nações Unidas para a Alimentação e Agricultura; e outra denominada região Fuzzy na qual a prescrição de irrigação é feita por um algoritmo de Inteligêncial Artifical chamado de lógica Fuzzy. O algortimo de lógica Fuzzy para a prescrição de irrigação foi desenvolvido por Gilberto de Souza, um dos meus colegas de trabalho.

Uma demonstração das funcionalidades da simulação pode ser visualizada no video localizado no link do Youtube

As duas áreas tem 3 sprinklers cada uma sendo eles denominados SP1,SP2 e SP3. É possivel acionar cada área de maneira independente mas os 3 sprinklers de cada área funcionam como um conjunto. É possivel operar cada sprinkler separadamente alterando o servidor OPC UA e também o IoT Agent OPC UA, essa decisão depende sismtea de irrigação a ser modelado. 

Na simulação caso a variável `manualoperation` do servidor OPC UA esteja falsa a simulação aguarda um dos métodos `irrigate_control` ou `irrigate_fuzzy` ser acionado para executar a irrigação da área de controle ou fuzzy respectivamente. O comando pode ser enviado para a simulação através do Orion (seja pelo cliente REST seja por um serviço da plataforma IoT) sendo então o caminho do comando através dos componentes o indicado na figura a seguir:

![Fluxo de comunicação entre os componetes e o Plant Simulation](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/fluxo1.png)

Assim que o comando chega na simulação, a necessidade de água em litros é calculada e a capacidade do tanque respectivo é ajustada para tal necessidade. Como exemplo se um comando `irrigate_control` é enviado paara irrigar 4mm asimulação calcula que a necessidade de irrigação da área de controle seria de 704 litros e então o tanque denominado `control_t` teria esse volume máximo. Assim as válvulas SP1,SP2 e SP3 da área de controle são abertas bem como a bomba de água é ligada com vazão de 1 l/s (definida na simulação e no servidor OPC UA de acordo com o projeto). 

Quando o tanque `control_t` atinge a capacidade máxima a simulação fecha os sprinklers da área de controle e também desliga a bomba de água caso ela não esteja irrigando a área fuzzy também. O tanque,então , libera todo o seu volume para a saida da simulação que indica quantos litros foram irrigados no total. Por fim, uma resposta dizendo que a irrigação da área de controle é enviada no sentido contrário ao expressado anteriormente, ou seja, um comando é enviado da simulação para o Orion Context Broker. 

Existe também a possibilidade da variável `manualoperation` estar ligada o que permitiria ao fazendeiro controle as áreas de irrigação e a bomba de água de maneira idependente como indicado nos métodos disponíveis na [seção Servidor OPC UA](#Servidor-OPC-UA). Neste caso cada sprinkler teria o seu próprio tanque que indicaria ao fazendeiro o volume de água que já foi irrigado durante o periodo de irrigação manual. Ao mudar novamente a variável `manualoperation` para falsa todo o volume de água é enviado para a saida da simulação e contabilizado como o volume total de água irrigado. 

No momento atual o IoT Agent OPC UA não é a capaz de dizer se um comando eviado dele para o servidor OPC UA foi executado de maneira adequada ou se ocorreu algum problema. Essa á uma função que deve ser implementada no futuro. Isso significa que caso o sistema de irrigação simulado, ou até mesmo um sistema real, não consiga executar o comando solicitado o IoT Agent OPC UA não conseguir informar ao Orion Context Broker que eu erro ocorreu e assim um possivel aplicativo não indicaria tal problema para o fazendeiro. 

Esta simulação utilizando o Plant Simulation e a uma plataforma de Internet das Coisas permite testar a comunicação de dispositivos reais e a funcionalidade dos mesmos antes de eles serem devidamente implantados nas fazendas. Isso permite que a plataforma seja previamente configurada antes de ser implanta e também permite verificar junto ao fazendeiro as funcionalidades que ele deseja que sejam implantadas. Além disso é possivel, dada a capacidade do Plant Simulation, simular um sistema de irrigação mais complexo, ou seja, tendo mais áreas de irrigação, mais sprinklers, mais bombas e mais bifurcações nas tubulações do sistema de irrigação. 

Vale ressaltar ainda que devido a possibilidade do Orion Contex Broker de se comunicar com diversos dispositivos e softwares através dos IoT Agents essa se torna uma solução capaz de integrar diversos componentes e soluções diferentes criando assim um sistema cyber-fisico de toda a fazenda. É possivel, por exemplo, conectar a plataforma a um sismtema de monitoramento de maquinário e operações permitindo que os agricultures saibam exatamente como está o comportamento de suas fazendas, garantindo assim que um gêmeo digital das fazendas possas ser criado. 



