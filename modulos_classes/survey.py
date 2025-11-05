class AnonymousSurvey():
    """Coleta respostas anônimas para uma pergunta de uma pesquisa."""

    def __init__(self, question):
        """Armazena uma pergunta e se prepara para armazenar as
        respostas."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Mostra a pergunta da pesquisa."""
        print(self.question)

    def store_response(self, new_response):
        """Armazena uma única resposta da pesquisa."""
        self.responses.append(new_response)
        
    def show_results(self):
        """Mostra todas as respostas dadas."""
        response_aux = set(self.responses)
        response_aux = list(response_aux)
        print("Survey results:")
        for i in range (len(response_aux)):
            print(response_aux[i] + " - " + str(self.responses.count(response_aux[i])))
