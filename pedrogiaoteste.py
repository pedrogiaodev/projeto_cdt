import pywhatkit as kit
import datetime
import time

# Nome exato do grupo no WhatsApp
NOME_DO_GRUPO = "Programação 2|26 B\\tarde"
MENSAGEM = "Aviso para a turma: @pedrogiao favor verificar os recados da aula!"

# Define o envio para daqui a 1 minuto
agora = datetime.datetime.now() + datetime.timedelta(minutes=1)

try:
    print("Agendando envio... O navegador abrirá em instantes.")
    
    # Envia para o grupo usando o nome e o horário programado
    kit.sendwhatmsg_to_group(
        group_id=NOME_DO_GRUPO,
        message=MENSAGEM,
        time_hour=agora.hour,
        time_min=agora.minute,
        wait_time=20,
        tab_close=True
    )
    print("Processo concluído!")

except Exception as erro:
    print(f"Ocorreu o seguinte erro: {erro}")
