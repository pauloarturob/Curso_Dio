class Level:
    def __init__(self):
        self.eventos_temporais = []

    def adicionar_evento_temporal(self, id_evento, intervalo, acao):
        # Adiciona um evento temporal à lista de eventos
        evento = {'id': id_evento, 'intervalo': intervalo, 'acao': acao, 'tempo_anterior': 0}
        self.eventos_temporais.append(evento)

    def verificar_eventos_temporais(self, tempo_atual):
        for evento in self.eventos_temporais:
            # Verifica se o intervalo decorreu desde o último evento
            if tempo_atual - evento['tempo_anterior'] >= evento['intervalo']:
                # Executa a ação associada ao evento
                evento['acao']()
                # Atualiza o tempo do último evento
                evento['tempo_anterior'] = tempo_atual

    def acao_instanciar_inimigo(self):
        # Lógica para instanciar um inimigo
        pass
