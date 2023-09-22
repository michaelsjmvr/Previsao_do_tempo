import sys
import requests
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox

class PrevisaoDoTempo(QMainWindow):
    def __init__(self, api_key):
        super().__init__()

        self.api_key = api_key  # Armazena a chave da API OpenWeatherMap
        self.setWindowTitle("Previsão do Tempo")  # Define o título da janela
        self.setGeometry(100, 100, 400, 200)  # Define a posição e o tamanho da janela

        central_widget = QWidget(self)  # Cria um widget central para a janela
        self.setCentralWidget(central_widget)  # Define o widget central

        layout = QVBoxLayout(central_widget)  # Cria um layout de grade vertical para organizar os elementos

        self.cidade_input = QLineEdit(self)  # Cria uma caixa de entrada para a cidade
        self.obter_button = QPushButton("Obter Previsão", self)  # Cria um botão para obter a previsão do tempo
        self.obter_button.clicked.connect(self.obter_previsao)  # Conecta o botão a um método

        self.result_label = QLabel(self)  # Cria uma etiqueta para exibir o resultado

        layout.addWidget(self.cidade_input)  # Adiciona a caixa de entrada ao layout
        layout.addWidget(self.obter_button)  # Adiciona o botão ao layout
        layout.addWidget(self.result_label)  # Adiciona a etiqueta ao layout

    def obter_previsao(self):
        cidade = self.cidade_input.text()  # Obtém o nome da cidade da caixa de entrada

        if cidade:
            try:
                # Faz uma solicitação à API OpenWeatherMap com idioma em português
                url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={self.api_key}&units=metric&lang=pt"  # Use 'lang=pt' para obter a descrição em português
                response = requests.get(url)
                data = response.json()  # Analisa a resposta JSON

                if data["cod"] == 200:  # Verifica se a resposta é bem-sucedida
                    # Obtém informações relevantes sobre o clima
                    temperatura = data["main"]["temp"]
                    descricao = data["weather"][0]["description"]

                    # Exibe as informações na interface
                    mensagem = f"Previsão para {cidade}:\nTemperatura: {temperatura}°C\nDescrição: {descricao.capitalize()}"
                    self.result_label.setText(mensagem)
                else:
                    self.result_label.setText("Cidade não encontrada")
            except Exception as e:
                self.result_label.setText("Erro ao obter previsão do tempo")
                QMessageBox.critical(self, "Erro", str(e))  # Exibe um diálogo de erro em caso de exceção
        else:
            self.result_label.setText("Digite o nome da cidade")  # Exibe uma mensagem se o campo estiver vazio

if __name__ == "__main__":
    # Substitua 'SUA_API_KEY_AQUI' pela sua chave de API do OpenWeatherMap
    api_key = 'sua_api_key_aqui'
    
    app = QApplication(sys.argv)  # Inicializa a aplicação Qt
    previsao_tempo = PrevisaoDoTempo(api_key)  # Cria uma instância da classe 'PrevisaoDoTempo'
    previsao_tempo.show()  # Exibe a janela
    sys.exit(app.exec())  # Executa o loop de eventos da aplicação
