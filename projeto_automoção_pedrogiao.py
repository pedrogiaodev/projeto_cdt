import pywhatkit as kit

NOME_DO_GRUPO = "Programação 2/26 B/Tarde"
MENSAGEM = "@pedrogiao"

try:
    print("Enviando mensagem instantânea...")
    
    # Envia imediatamente para o nome do grupo
    kit.sendwhatmsg_to_group_instantly(
        group_id=NOME_DO_GRUPO,
        message=MENSAGEM,
        wait_time=15,
        tab_close=True
    )
    print("Processo concluído!")

except Exception as erro:
    print(f"Ocorreu o seguinte erro: {erro}")
    