# 🎉 MercadoPago-API-PIX-Event-Collector 🚀

## 📖 Introdução

O **MercadoPago-API-PIX-Event-Collector** é um coletor de eventos PIX desenvolvido em Python, utilizando a arquitetura MVC (Model-View-Controller). Este projeto é o culminar de uma jornada de 8 anos de aprendizado em Python, onde inicialmente me concentrei em APIs e prototipagem, mas agora estou voltando meu foco para práticas mais robustas de arquitetura de software, incluindo DDD (Domain-Driven Design) e Clean Architecture.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍: Linguagem principal do projeto, conhecida por sua simplicidade e versatilidade.
- **Flask** 🔥: Framework utilizado para construir a API de forma leve e eficaz.
- **SQLAlchemy** 🗄️: ORM (Object-Relational Mapping) para facilitar a interação com o banco de dados.
- **Mercado Pago API** 💳: Integração com a API do Mercado Pago para coletar eventos de transações PIX.

## 🚧 Status do Desenvolvimento

![Status do Projeto](https://img.shields.io/badge/Status-Em%20Desenvolvimento-orange.svg) ![Versão](https://img.shields.io/badge/Vers%C3%A3o-0.1.0-blue.svg) ![API Key](https://img.shields.io/badge/API%20Key-N%C3%A3o%20Dispon%C3%ADvel-red.svg)

Este projeto está atualmente em **desenvolvimento**. ✨ Novas funcionalidades estão sendo planejadas e implementadas, e esperamos expandir as capacidades do coletor de eventos PIX em breve! 

🔍 **Atenção**: O projeto não é funcional neste momento, pois as **API Key** 🔑 e a **chave criptografada** 🔒 necessárias para a integração com a API do Mercado Pago **não estão disponíveis** neste repositório. 

![Code_6s64MFZBZb](https://github.com/user-attachments/assets/8df0cbbf-ea2b-4707-96e5-9da7d103d2cd)

---

### 🔔 O que vem a seguir?
- Novas funcionalidades
- Melhorias na documentação
- Implementação de testes automatizados 🧪

🔗 **Siga-nos para atualizações!** Fique atento às mudanças e melhorias que estão por vir! 🛠️


## 🚀 Objetivo do Projeto

O principal objetivo do projeto é fornecer uma solução confiável e escalável para coletar e processar eventos de transações PIX através da API do Mercado Pago. Esta ferramenta é essencial para empresas que desejam monitorar suas transações financeiras em tempo real e reagir rapidamente a eventos críticos.

## 📈 Benefícios do Projeto

- **Eficiência** ⚡: Coleta e processamento de eventos em tempo real.
- **Escalabilidade** 📊: Arquitetura projetada para crescer com suas necessidades.
- **Manutenibilidade** 🔧: Código organizado e bem estruturado, facilitando futuras atualizações e melhorias.

## 🏆 Sobre Mim

Sou **Elias Andrade**, um profissional de TI com mais de 14 anos de experiência em infraestrutura e mais de 8 anos de aprendizado em Python. Meu foco atual está em desenvolver habilidades em **arquitetura de software**, **DDD**, e **Clean Architecture**, sempre buscando aprimorar a forma como construo aplicações e sistemas.


# 🌳 Estrutura da Arquitetura do Projeto PixHub MVC V2 

![heatmap_total_tipo_pagamento_moeda](https://github.com/user-attachments/assets/3a0157d9-1f32-4e21-82f9-1fcc48bc6bff)
![heatmap_7_payment_type_id_date_created](https://github.com/user-attachments/assets/e4ac12b5-de9e-44b5-801f-8997c92076f9)
![heatmap_8_currency_id_date_created](https://github.com/user-attachments/assets/ca6e84e4-5629-4897-bee2-834712880ea7)
![heatmap_payment_type_account_money](https://github.com/user-attachments/assets/168c1ba2-57d2-4cdf-a9c9-c2cdd32d4612)


## 📁 Projeto Principal
![Projeto Principal](https://img.shields.io/badge/Projeto%20Principal-blue?style=flat-square)

- **`\projeto-pixhub-mvc-v2-melhorado`**  
  O diretório raiz do projeto, que contém todos os componentes do aplicativo.

### 📁 My Flask App
![My Flask App](https://img.shields.io/badge/My%20Flask%20App-orange?style=flat-square)

- **`\projeto-pixhub-mvc-v2-melhorado\my_flask_app`**  
  O diretório principal do aplicativo Flask, contendo todos os módulos e funcionalidades.

#### 📁 App
![App](https://img.shields.io/badge/App-red?style=flat-square)

- **`\projeto-pixhub-mvc-v2-melhorado\my_flask_app\app`**  
  Este diretório contém os componentes principais do aplicativo.

  - **📊 `analytics`**  
    ![Analytics](https://img.shields.io/badge/analytics-green?style=flat-square)
    Módulo responsável por coletar e processar dados analíticos.
    - **📁 `__pycache__`**  
      ![Pycache](https://img.shields.io/badge/__pycache__-lightgrey?style=flat-square)  
      Cache dos arquivos compilados de Python.
    - **📄 `data_processorv1.py`**  
      ![data_processorv1](https://img.shields.io/badge/data_processorv1.py-lightblue?style=flat-square)  
      Processador de dados versão 1.
    - **📄 `data_processorv2.py`**  
      ![data_processorv2](https://img.shields.io/badge/data_processorv2.py-lightblue?style=flat-square)  
      Processador de dados versão 2.

  - **🌐 `api`**  
    ![API](https://img.shields.io/badge/api-yellow?style=flat-square)  
    Interfaces de programação para interagir com serviços externos.
    - **📁 `__pycache__`**  
      ![Pycache](https://img.shields.io/badge/__pycache__-lightgrey?style=flat-square)  
      Cache dos arquivos compilados de Python.
    - **📄 `event_sender.py`**  
      ![event_sender](https://img.shields.io/badge/event_sender.py-lightblue?style=flat-square)  
      Enviador de eventos para serviços externos.

  - **🔒 `auth`**  
    ![Auth](https://img.shields.io/badge/auth-red?style=flat-square)  
    Módulo de autenticação e gerenciamento de usuários.
    - **📁 `__pycache__`**  
      ![Pycache](https://img.shields.io/badge/__pycache__-lightgrey?style=flat-square)  
      Cache dos arquivos compilados de Python.
    - **📄 `authentication.py`**  
      ![authentication](https://img.shields.io/badge/authentication.py-lightblue?style=flat-square)  
      Implementação da lógica de autenticação.

  - **⚙️ `config`**  
    ![Config](https://img.shields.io/badge/config-orange?style=flat-square)  
    Arquivos de configuração do aplicativo.
    - **📁 `__pycache__`**  
      ![Pycache](https://img.shields.io/badge/__pycache__-lightgrey?style=flat-square)  
      Cache dos arquivos compilados de Python.
    - **📄 `config.py`**  
      ![config](https://img.shields.io/badge/config.py-lightblue?style=flat-square)  
      Configurações principais do aplicativo.
    - **📄 `config.yaml`**  
      ![config_yaml](https://img.shields.io/badge/config.yaml-lightblue?style=flat-square)  
      Configurações em formato YAML para leitura fácil.
    - **🔑 `api.key`**  
      ![api.key](https://img.shields.io/badge/api.key-yellow?style=flat-square)  
      Chave de API para serviços externos.
    - **🔑 `chave_secreta.key`**  
      ![chave_secreta](https://img.shields.io/badge/chave_secreta.key-yellow?style=flat-square)  
      Chave secreta para criptografia de dados.

  - **👥 `controllers`**  
    ![Controllers](https://img.shields.io/badge/controllers-purple?style=flat-square)  
    Controladores que gerenciam a lógica de negócios.
    - **📁 `__pycache__`**  
      ![Pycache](https://img.shields.io/badge/__pycache__-lightgrey?style=flat-square)  
      Cache dos arquivos compilados de Python.
    - **📄 `user_controller.py`**  
      ![user_controller](https://img.shields.io/badge/user_controller.py-lightblue?style=flat-square)  
      Controlador para gerenciar usuários.

  - **🗄️ `db`**  
    ![DB](https://img.shields.io/badge/db-brown?style=flat-square)  
    Módulo de gerenciamento de banco de dados.
    - **📄 `controle_usuarios.db`**  
      ![controle_usuarios.db](https://img.shields.io/badge/controle_usuarios.db-lightblue?style=flat-square)  
      Banco de dados para controle de usuários.
    - **📄 `database_manager.py`**  
      ![database_manager](https://img.shields.io/badge/database_manager.py-lightblue?style=flat-square)  
      Gerenciador de conexões e operações no banco de dados.

  - **🎉 `events`**  
    ![Events](https://img.shields.io/badge/events-lightgreen?style=flat-square)  
    Módulo para coleta e gerenciamento de eventos.
    - **📁 `__pycache__`**  
      ![Pycache](https://img.shields.io/badge/__pycache__-lightgrey?style=flat-square)  
      Cache dos arquivos compilados de Python.
    - **📄 `event_collector.py`**  
      ![event_collector](https://img.shields.io/badge/event_collector.py-lightblue?style=flat-square)  
      Coletor de eventos para análise.

  - **🌍 `hostname`**  
    ![Hostname](https://img.shields.io/badge/hostname-orange?style=flat-square)  
    Gerenciamento de nomes de host.
    - **📄 `hostname_manager.py`**  
      ![hostname_manager](https://img.shields.io/badge/hostname_manager.py-lightblue?style=flat-square)  
      Gerenciador de nomes de host.

  - **📝 `models`**  
    ![Models](https://img.shields.io/badge/models-lightyellow?style=flat-square)  
    Definições de modelos para interação com o banco de dados.
    - **📁 `__pycache__`**  
      ![Pycache](https://img.shields.io/badge/__pycache__-lightgrey?style=flat-square)  
      Cache dos arquivos compilados de Python.
    - **📄 `app.py`**  
      ![app](https://img.shields.io/badge/app.py-lightblue?style=flat-square)  
      Modelo principal do aplicativo.
    - **📄 `payment.py`**  
      ![payment](https://img.shields.io/badge/payment.py-lightblue?style=flat-square)  
      Modelo para gerenciamento de pagamentos.
    - **📄 `user.py`**  
      ![user](https://img.shields.io/badge/user.py-lightblue?style=flat-square)  
      Modelo para gerenciamento de usuários.

  - **📤 `output`**  
    ![Output](https://img.shields.io/badge/output-lightgreen?style=flat-square)  
    Saídas geradas pelo aplicativo.
    - **📁 `events`**  
      ![Events](https://img.shields.io/badge/events-blue?style=flat-square)  
      Eventos processados e armazenados.
      - **📄 `payment_87384495287.json`**  
        ![payment_1](https://img.shields.io/badge/payment_87384495287.json-lightblue?style=flat-square)  
        Exemplo de pagamento registrado.
      - **📄 `payment_87384615501.json`**  
        ![payment_2](https://img.shields.io/badge/payment_87384615501.json-lightblue?style=flat-square)  
        Outro exemplo de pagamento registrado.

  - **📊 `reports`**  
    ![Reports](https://img.shields.io/badge/reports-purple?style=flat-square)  
    Relatórios gerados pelo aplicativo.
    - **📄 `bar_chart_payments_account_money.png`**  
      ![bar_chart](https://img.shields.io/badge/bar_chart_payments_account_money.png-lightblue?style=flat-square)  
      Gráfico de barras de pagamentos por conta.
    - **📄 `heatmap_payment_type.png`**  
      ![heatmap](https://img.shields.io/badge/heatmap_payment_type.png-lightblue?style=flat-square)  
      Mapa de calor mostrando tipos de pagamento.

  - **🛠️ `services`**  
    ![Services](https://img.shields.io/badge/services-gray?style=flat-square)  
    Serviços auxiliares que suportam o funcionamento do aplicativo.

  - **🛠️ `utils`**  
    ![Utils](https://img.shields.io/badge/utils-lightgrey?style=flat-square)  
    Funções utilitárias que podem ser usadas em diferentes partes do aplicativo.

  - **📄 `__init__.py`**  
    ![init](https://img.shields.io/badge/__init__.py-lightblue?style=flat-square)  
    Inicializador do módulo Flask.

  - **📄 `main.py`**  
    ![main](https://img.shields.io/badge/main.py-lightblue?style=flat-square)  
    Ponto de entrada do aplicativo.

  - **📄 `requirements.txt`**  
    ![requirements](https://img.shields.io/badge/requirements.txt-lightblue?style=flat-square)  
    Lista de dependências do projeto.

  - **📄 `run.py`**  
    ![run](https://img.shields.io/badge/run.py-lightblue?style=flat-square)  
    Script para iniciar o servidor Flask.

### 📄 Scripts e Utilitários
![Scripts e Utilitários](https://img.shields.io/badge/Scripts%20e%20Utilitários-purple?style=flat-square)

- **`projeto-pixhub-mvc-v2-melhorado\lista-diretorio-projeto.py`**  
  Script para listar o diretório do projeto, útil para verificação rápida da estrutura.

## 🔗 Recursos Adicionais
![Recursos Adicionais](https://img.shields.io/badge/Recursos%20Adicionais-yellowgreen?style=flat-square)

- 📖 [Documentação do Flask](https://flask.palletsprojects.com/)
- 📖 [Documentação de APIs REST](https://restfulapi.net/)
- 📖 [Documentação sobre Banco de Dados SQLite](https://www.sqlite.org/docs.html)

## 🎯 Conclusão
![Conclusão](https://img.shields.io/badge/Conclusão-red?style=flat-square)

A arquitetura do projeto PixHub MVC V2 é projetada para ser modular e escalável, permitindo fácil manutenção e adição de novas funcionalidades. Cada módulo é cuidadosamente organizado para facilitar a navegação e a compreensão do código.

---

### 🛡️ Este documento é um guia para desenvolvedores que desejam entender a estrutura e o funcionamento do projeto.
