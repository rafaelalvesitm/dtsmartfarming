# Gêmeo digital para  um  sistema de irrigação.


A figura a seguir indica o modelo que foi adotado para realizar a simulação. O modelo leva em consideração uma bomba de água com vazão de 1 litro por segundo que deve irrigar duas áreas: uma denominada área de controle e a outra denominada área fuzzy. Em cada área existe um aspersor (sprinkler) que fará a dispersão da água em circulo garantindo uma melhor cobertura da irrigação. Cada área tem 8 x 22 metros sendo portanto uma área total de 176 m² por região. Em cada área, uma sonda de solo será simulada simulando assim diversos parametros como a temperatura do solo, umidade do solo em 2 níveis, temperatura do ar, umidade do ar e iluminância. 

![Modelo de sistema de irrigação adotado](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/sistemairrigacao.png)

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

## Simulação do sistema de irrigação

Para a simulação do sistema de irrigação foi desenvolvido um modelo utilizando o software [Plant Simulation](https://www.plm.automation.siemens.com/global/pt/products/manufacturing-planning/plant-simulation-throughput-optimization.html). A simulação está na pasta [/simulation](/simulation). A visualização da simulação é indicada na figura abaixo:

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



