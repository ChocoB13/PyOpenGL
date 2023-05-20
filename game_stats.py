class GameStats():
    def __init__(self, gm_settings):
        self.gm_settings = gm_settings
        self.reset_stats()
        self.game_ative = True


    def reset_stats(self):
        """inicializa os dados estatisticos que podem mudar durante o jogo"""
        self.vidas_left = self.gm_settings.max_vida       