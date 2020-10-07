# Gêmeo digital para  um  sistema de irrigação.

Este repositório contém os códigos e componentes utilizados para a minha dissertação entitulada "Fazenda Inteligente: Desenvolvimento de um gêmeo digital para o sistema de irrigação" ainda em andamento. O projeto visa desenvolver uma simulação computacional de um sistema de irrigação utilizando o software Plant Simulation e realizar a conexão da simulação com uma plataforma de Internet das Coisas para validar, digitalmente, um processo de irrigação dado uma prescrição de irrigação obtida pela plataforma de internet das coisas.

A figura a seguir indica o modelo que foi adotado para realizar a simulação. O modelo leva em consideração uma bomba de água com vazão de 1 litro por segundo que deve irrigar duas áreas: uma denominada área de controle e a outra denominada área fuzzy. Em cada área existe um aspersor que fará a dispersão da água em circulo garantindo uma melhor cobertura da irrigação. Cada área tem 8 x 22 metros sendo portanto uma área total de 176 m² por região. Em cada área, uma sonda de solo será simulada para enviar diversos parametros como a temperatura do solo, umidade do solo em 2 níveis, temperatura do ar, umidade do ar e iluminância. 

![Modelo de sistema de irrigação adotado](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/sistemairrigacao.png)

Para maiores detalhes sobre os componentes utilizados, artigos relevantes, etc acesse a [WIKI](https://github.com/rafaelalvesitm/dtsmartfarming/wiki)

## Etapas para montar a plataforma de Internet das Coisas

Primeiramente é necessário [instalar o Docker](https://docs.docker.com/get-docker/) e o [docker-compose](https://docs.docker.com/compose/). Para usuários do Windows é recomendado utilizar o WSL2 com uma versão do Ubuntu, para isso siga o [tutorial do link](https://docs.docker.com/docker-for-windows/wsl/).

Após a instalção do docker e do docker-compose acesse a pasta [Weather Handler](/platform/weather_handler) e crie um arquivo `config.py` com a delcaração das variáveis `api_key` e `api_key_wunder` com as chaves para as APIs do [OpenWeather](https://openweathermap.org/) (OneCall API) e [Wunderground](https://www.wunderground.com/). A API do OpenWeather é aberta para qualquer um sendo necessário apenas fazer uma conta no site e solicitar a chave da API já para a API do Wunderground é necessário ter uma estação meterológica para fazer o cadastro no site.  

Para montar as imagens dos containers utilizados acesse a pasta [platform](/platform) pelo terminal e utilize o comando `docker-compose build` para construir os componentes que foram desenvolvidos por min. Por fim, utilize o comando `docker-compose up -d` para subir os containers para o ambiente de desenvolvimento local (localhost). Este comando baixará as imagens dos componentes descritos no arquivo "docker-compose" no [Docker HUB](https://hub.docker.com/).

Após tal configuração é necessário configurar o grafana para se conectar a base de dados e também para mostrar a dashboard que foi criada. Acesse via browser, o link `localhost:3000` caso esta simulação esteja sendo criada em ambiente local de desenvolvimento. 

Inicialmente o Grafana irá pedir um login e senha sendo eles `admin` e `admin`. Logo após será necessário alterar a senha que fica a critério do usuário. O próximo passo é fazer o cadastro do banco de dados como mostra as figuras a seguir:

![Selecione Data Sourcer para conectar um banco de dados ao Grafana ](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/grafana.png)

![Configure os parametros de acordo com o banco de dados](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/grafana2.png)

Após estes passos é possivel criar o painél interativo de acordo com as necessidades ou então utilizar o painel previamente condificado, para isso click em `import` como indicado na figura abaixo e depois em `Upload JSON File` e adicione o arquivo `FEI panel.json` disponível na pasta [/platform](/platform). 

![Importe o arquivo FEI panel.json para o grafana](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/grafana3.png)

Após acessar a Dashboard e possível, no menu superior direito da Dashboard, configurar o painel para mostrar os dados relativos a um determinado periodo bem como alterar a taxa de atualização do painel. 

A conexão entre os diversos componentes da plataforma é feita da seguinte forma:

![Arquitetura da plataforma](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/platform.png)

## Simulação do sistema de irrigação

Para a simulação do sistema de irrigação foi desenvolvido um modelo utilizando o software [Plant Simulation](https://www.plm.automation.siemens.com/global/pt/products/manufacturing-planning/plant-simulation-throughput-optimization.html). A simulação está na pasta [/simulation](/simulation). A visualização da simulação é indicada na figura abaixo:

![Visualização da simulação no Plant Simulation](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/plantsimulation1.png)

A simulação é conectada a um servidor OPC UA através de um módulo OPC UA do Plant Simulation que requer uma licença especifica. O Plant Simulation tem uma [versão de estudante](https://www.plm.automation.siemens.com/plmapp/education/plant-simulation/en_us/free-software/student/) que permite visualizar o modelo mas não é possivel conectar o modelo a um servidor OPC UA. Com este modelo é possivel simular o comportamento do sistema de irrigação de acordo com os métodos que foram descritos na [seção Servidor OPC UA](#Servidor-OPC-UA).

Uma demonstração das funcionalidades da simulação pode ser visualizada no video [Plant Simulation e servidor OPC UA](https://www.youtube.com/watch?v=Ixm5KTdeVqs). 


