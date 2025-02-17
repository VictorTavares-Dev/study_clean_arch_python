# Projeto de Arquitetura Limpa em Python

Este repositório representa estudos sobre a metodologia de Arquitetura Limpa de código em Python. A estrutura de pastas para este projeto está organizada da seguinte forma:
```bash
clean_arch_project/
│
├── adapters/
│   ├── __init__.py
│   ├── credentials_manager.py
│   ├── db_nosql_manager.py
│   ├── file_manager.py
│   └── workflow_manager.py
│
├── cross_cutting/
│   ├── __init__.py
│   ├── logging.py
│   └── utils.py
│
├── domains/
│   ├── __init__.py
│   ├── credential.py
│   ├── file.py
│   ├── workflow.py
│   └── db_nosql.py
│
├── use_cases/
│   ├── __init__.py
│   ├── manage_credentials.py
│   ├── manage_files.py
│   ├── manage_workflows.py
│   └── manage_nosql_db.py
│
└── main.py
```

## Explicação da estrutura
1. **adapters:** Contém classes ou funções que conectam as implementações específicas de infraestrutura ao domínio do problema, como gerenciadores de credenciais, banco de dados NoSQL, arquivos e workflows. Essas implementações são específicas da tecnologia, mas seguem uma interface comum definida no domínio.
2. **domains:** Contém as entidades e objetos de valor que representam o modelo de domínio do seu sistema. Esses arquivos devem refletir as regras de negócio, mas não devem depender de implementações específicas de infraestrutura (como banco de dados, APIs, etc.).
3. **cross_cutting:** Contém funcionalidades que são transversais a várias partes do sistema, como logging, utilitários (como validação de dados, formatação, etc.) e outras preocupações de infraestrutura que não são diretamente relacionadas ao domínio, mas necessárias para o funcionamento do sistema.
4. **use_cases:** Contém os casos de uso do sistema. Cada arquivo aqui representa uma ação que o sistema pode executar, utilizando as implementações dos adaptadores. Os casos de uso orquestram as interações entre as entidades do domínio e os adaptadores.
5. **main.py:** Este é o ponto de entrada do aplicativo. Pode ser onde você configura as dependências e inicializa os casos de uso, mas deve ser simples e não conter lógica de negócios complexa.
