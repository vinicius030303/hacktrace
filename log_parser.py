# log_parser.py

def parse_logs(log):
    if 'falha' in log.lower():
        return 'STATUS: ALERTA - Atividade suspeita detectada.'
    elif 'acesso concedido' in log.lower():
        return 'STATUS: OK - Invasão ética simulada bem-sucedida.'
    elif 'payload' in log.lower():
        return 'STATUS: EM ANÁLISE - Payload detectado.'
    else:
        return 'STATUS: MONITORAMENTO - Nenhum incidente crítico.'

if __name__ == '__main__':
    print("=== HackTrace Log Analyzer ===")
    print("Cole aqui a saída do terminal para análise simbólica.\n")
    
    entrada = input("Log> ")
    resultado = parse_logs(entrada)
    print(f"\n{resultado}")
