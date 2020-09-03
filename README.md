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

Após a instalção do docker e do docker-compose acesse a pasta [platform](/platform)

A conexão entre os diversos componentes da plataforma é feita da seguinte forma:

![Arquitetura da plataforma](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/platform.png)

Após todos os serviços estarem funcionando nos seus devidos containers é necessário criar o modelo de dados a ser utilizado para o experimento. Navegue até a pasta dataModel e rode o script setup.py. Esse escript criará todoas as entidades no Orion, no IoT Agent Json e também o service group no ioT Agent e a subscrição no Orion. 

Com toidas as entidades criadas navegue até a pasta data e rode o script uploaddata.py. Esse script é responsável por enviar todos os dados utilizados para a siomulação para o IoT Agent. Os dados, para cada sonda de solo, podem ser conferidos na pasta soilProbeData.

A próxima etapa será a de configurar o Grafana para visualizar os dados de cada sensor bem como outras informações relevantes. Para isso utilize abre um navegador qualquer e digite localhost:3000. Coloque como login Admin e senha admin. escolha uma nova senha e salve/ 

## Servidor OPC UA

O servidor OPC UA foi desenvolvido em Python utilizando como base no python-opcua disponível em https://github.com/FreeOpcUa/python-opcua. Para o funcionamento dentro do ambiente virtual eu utilizei o docker para colocar o servidor dentro de um container e assim deixa-lo na mesma rede. Os arquivos relativos ao servidor OPC UA estão dentro da pasta /platform/OpcUAServer. Os componentes do servidor seguem a indicação da figura abaixo.  

![Componentes do servidor OPC UA](https://github.com/rafaelalvesitm/dtsmartfarming/blob/master/pictures/serverItens.png)



