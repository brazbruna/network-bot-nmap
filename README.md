#  Bot de Monitoramento de Rede com Nmap + Telegram

Este projeto utiliza o **Nmap** para escanear redes locais e detectar dispositivos conectados ou desconectados, enviando notificações em tempo real para um bot do Telegram. A automação e a integração com o Telegram permitem um monitoramento contínuo e eficiente da rede.

##  Objetivo

O objetivo deste projeto é mostrar como é possível automatizar o monitoramento de dispositivos conectados em uma rede doméstica ou corporativa, utilizando ferramentas de código aberto. Ele é útil para:

- Garantir a segurança da rede (identificando acessos não autorizados);
- Manter o controle de quem está conectado;
- Automatizar tarefas de detecção e alerta com custo zero.

Exemplo de uso prático: Monitoramento contínuo de dispositivos em uma rede corporativa para identificar dispositivos não autorizados ou verificar a conectividade de dispositivos importantes.


---

## Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Nmap](https://nmap.org/) – Ferramenta de escaneamento de rede
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) – Envio de mensagens para o Telegram

##  Funcionalidades

✅ Escaneia a rede local usando `nmap -sn` (ping scan)  
✅ Identifica novos dispositivos e envia alertas no Telegram (ex: "Novo dispositivo detectado: 192.168.0.5")  
✅ Detecta dispositivos que saíram da rede (ex: "Dispositivo desconectado: 192.168.0.5")  
✅ Pode ser automatizado para rodar a cada X horas (via Agendador de Tarefas no Windows ou `cron` no Linux)

### Como Usar
### Instale as dependências

pip install -r requirements.txt

### Instale o Nmap
Faça o download do Nmap e instale no seu sistema:
- [Windows](https://nmap.org/download.html) – Para Windows, baixe o instalador e siga o assistente.
- [Linux/Mac](https://nmap.org/download.html) – Instale via gerenciador de pacotes (ex: `sudo apt install nmap` no Ubuntu).
Após instalar, verifique se o Nmap está funcionando corretamente no terminal:
nmap -V

### Configure o token do Bot
Crie um bot no Telegram usando o BotFather e copie o token.

Use o @userinfobot para descobrir o seu chat_id.

No código Python, substitua:
token = "SEU_TOKEN" e
chat_id = SEU_CHAT_ID

### Executando o Projeto
Execute o bot com:
python main.py

###  Automação (Opcional)
Você pode configurar esse script para rodar automaticamente a cada X horas.
No Windows (Agendador de Tarefas):

Agende para executar:
python C:\caminho\para\main.py

### Aprendizados
Este projeto reforçou conceitos importantes como:
- Sub-redes e endereçamento IP
- Varredura de rede com Nmap
- Automação de tarefas com Python
- Uso de bots para integração com serviços externos (Telegram)
- Organização de projetos para portfólio

###  Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

