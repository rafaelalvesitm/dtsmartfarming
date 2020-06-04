# A digital twin for smart farming

This is a repository to contain any files from my master's degree thesis. I am including here all the scripts, models, data, files and discoveris that I made though the process of creating the thesis. The list os articles related to this work is presented below.

Articles:

R. G. Alves et al., "A digital twin for smart farming," 2019 IEEE Global Humanitarian Technology Conference (GHTC), Seattle, WA, USA, 2019, pp. 1-4. Avilable at: https://ieeexplore.ieee.org/document/9033075

This work uses FIWARE to create the cloud enviroment to collect data from sensors and to send commands to actuators. For more information about FIWARE use this link https://www.fiware.org/.

This is just a new message using visual studio code

Atualizando a nova versão do GitHub para funcionar com os sistemas previstos de envio de dados. Espero que resolva

Atividades
1. Configurei o WSL versão 1 no laptop (Ubuntu 18.04 LTS). A versão 2 do WSL só está disponível após atualizar o windows para a Build 2004. 
2. Configuração da pasta Git para contribuir para esta branch. 
3. Pasta Data criada com um csv dos dados do projeto do Gilberto e também um Script Python capaz de ler tais dados e publica-los no Fiware

Trabalhar ainda:
1. A notificação do Cygnus para o Mysql vai com o timestamp da notificação e não o timestamp que está no Orion, mesmo que o IoT Agent sobrescreva esse valor. Será que existe uma forma do Cygnus salvar tais dados no MySQL com a sobreescrição do IoT Agent?
2. Se não for possivel fazer tal modificação transformar a planilha de dados do Gilberto para a forma com que a apresentação ficaria no MySQL. 
