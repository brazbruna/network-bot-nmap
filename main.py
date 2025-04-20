import subprocess
import os
from telegram import Bot
import asyncio

#Função realiza a varredura da rede com o NMAP
def scan_rede():
    comando = ["nmap", "-sn", "SUA_REDE/24"] #Substitua pelo seu número de rede
    resultado = subprocess.run(comando, capture_output=True, text=True)
    saida = resultado.stdout

    dispositivos = []

    for linha in saida.splitlines():
        if "Nmap scan report for" in linha:
            ip = linha.split()[-1]
            dispositivos.append(ip)

    return dispositivos

def salvar_txt(lista_ips, nome_arquivo):
    with open(nome_arquivo, "w") as f:
        for ip in lista_ips:
            f.write(ip + "\n")

def carregar_ips(nome_arquivo):
    if not os.path.exists(nome_arquivo):
        return []
    with open(nome_arquivo, "r") as f:
        return [linha.strip() for linha in f.readlines()]

async def enviar_mensagem(token, chat_id, mensagem):
    bot = Bot(token=token)
    await bot.send_message(chat_id=chat_id, text=mensagem)

#Função inicia o monitoramento
def monitorar():
    ip_atuais = scan_rede()
    ip_anteriores = carregar_ips("scan_anterior.txt")

    novos = [ip for ip in ip_atuais if ip not in ip_anteriores]
    removidos = [ip for ip in ip_anteriores if ip not in ip_atuais]

    mensagens = []

    if novos:
        mensagens.append(" Novos dispositivos conectados:")
        for ip in novos:
            mensagens.append(f" + {ip}")

    if removidos:
        mensagens.append(" Dispositivos desconectados:")
        for ip in removidos:
            mensagens.append(f" - {ip}")

    if mensagens:
        token = "SEU_TOKEN" #Substitua pelo seu token (com aspas)
        chat_id = SEU_CHAT_ID #Substitua pelo seu chat_id (sem aspas)
        asyncio.run(enviar_mensagem(token, chat_id, "\n".join(mensagens)))

    salvar_txt(ip_atuais, "scan_anterior.txt")
    print("Scan atualizado!")

monitorar()
