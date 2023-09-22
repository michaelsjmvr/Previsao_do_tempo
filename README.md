# Aplicação de Previsão do Tempo

## Autor: Michael Douglas P Lima
## Contato: michaelsjmvr@hotmail.com
## LinkedIn: [michael-douglas-640a11180](https://www.linkedin.com/in/michael-douglas-640a11180/)

## Projeto
Este é um projeto que cria uma aplicação de previsão do tempo usando PySide6 e a API OpenWeatherMap. A aplicação permite que os usuários obtenham informações atualizadas sobre o clima para uma cidade específica.

## Descrição
O projeto consiste em uma interface gráfica simples que permite aos usuários inserir o nome de uma cidade e, em seguida, clicar em um botão para obter a previsão do tempo atualizada para essa cidade. A aplicação usa a API OpenWeatherMap para buscar dados de previsão do tempo.

## Componentes Principais
- **Janela Principal:**
  - A janela principal da aplicação exibe o título "Previsão do Tempo".
  - A janela tem um tamanho fixo de 400x200 pixels e é posicionada na tela.

- **Interface de Usuário:**
  - A interface de usuário consiste em uma caixa de entrada de texto onde o usuário pode inserir o nome da cidade.
  - Há um botão "Obter Previsão" que, quando clicado, solicita a previsão do tempo para a cidade inserida.
  - Abaixo da caixa de entrada e do botão, uma etiqueta exibe a previsão do tempo.

## Funcionalidades
- A aplicação faz uma solicitação à API OpenWeatherMap quando o botão "Obter Previsão" é clicado.
- A API é acessada usando uma chave de API (api_key) fornecida pelo usuário.
- Os dados da previsão do tempo retornados pela API são analisados e exibidos na interface gráfica.
- A temperatura é exibida em graus Celsius (°C) e a descrição do tempo é exibida em português.

## Tratamento de Erros
- A aplicação lida com erros possíveis, como cidade não encontrada ou falha na solicitação à API.
- Em caso de erro, a aplicação exibe uma mensagem de erro em uma caixa de diálogo.

## Executando a Aplicação
- Para executar a aplicação, é necessário fornecer uma chave de API válida do OpenWeatherMap.
- A chave de API deve ser inserida na variável api_key no código antes de executar o programa.
- Após a execução, a janela da aplicação será exibida e o usuário poderá usá-la para obter previsões do tempo.

## Requisitos
- Python com PySide6 instalado.
- Uma chave de API válida do OpenWeatherMap (substituir 'SUA_API_KEY_AQUI' pela chave).

## Contribuição
Este projeto é de código aberto e está aberto a contribuições. Sinta-se à vontade para melhorar a aplicação ou adicionar novos recursos.
