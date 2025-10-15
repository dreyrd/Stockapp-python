# Stockapp Python

Uma API FastAPI para predições de ações usando algoritmos de Machine Learning como Random Forest e Regressão Linear.

## 📁 Estrutura do Projeto

### Arquivos Principais

- **`main.py`** - Ponto de entrada da aplicação FastAPI com configurações de CORS e inicialização do servidor
- **`core/configs.py`** - Configurações centralizadas da aplicação (porta, host, prefixos de API)
- **`schemas/prediction_schema.py`** - Schemas Pydantic para validação de dados de entrada e resposta
- **`api/v1/api.py`** - Roteador principal que agrupa todos os endpoints da API v1
- **`api/v1/routers/random_forest.py`** - Endpoints específicos para predições usando Random Forest
- **`api/v1/routers/linear_regression.py`** - Endpoints específicos para predições usando Regressão Linear

### Estrutura de Diretórios
```
stockapp-python/
├── main.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── core/
│   └── configs.py
├── schemas/
│   └── prediction_schema.py
└── api/
    └── v1/
        ├── api.py
        └── routers/
            ├── linear_regression.py
            └── random_forest.py
```

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.12.4
- pip

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd stockapp-python
   ```

2. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/macOS:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configure as variáveis de ambiente**
   
   Faça uma cópia do .env.example em um arquivo chamado .env
   ```bash
   cp .env.example .env
   ```
   Edite o arquivo `.env` com suas configurações

6. **Execute a aplicação**
   ```bash
   python main.py
   ```

7. **Acesse a aplicação**
   - API: http://{HOST}:{PORT}
   - Documentação Swagger: http://{HOST}:{PORT}/docs
   - Documentação ReDoc: http://{HOST}:{PORT}/redoc

## 📋 Mapeamento dos Endpoints

### Base URL
```
http://{HOST}:{PORT}/api/v1
```

### Endpoints Disponíveis

#### 1. Random Forest - Predição
- **URL:** `POST /api/v1/rf/prediction`
- **Descrição:** Realiza predições usando algoritmo Random Forest
- **Request Body:**
  ```json
  {
    "high": 0.0,
    "low": 0.0
  }
  ```
- **Response:**
  ```json
  {
    "high": 0.0,
    "low": 0.0
  }
  ```

#### 2. Linear Regression - Predição
- **URL:** `POST /api/v1/lr/prediction`
- **Descrição:** Realiza predições usando algoritmo de Regressão Linear
- **Request Body:**
  ```json
  {
    "high": 0.0,
    "low": 0.0
  }
  ```
- **Response:**
  ```json
  {
    "high": 0.0,
    "low": 0.0
  }
  ```

## 📝 Schemas de Dados

### PredictionCreateBase
```python
{
    "high": float,  # Valor máximo da ação
    "low": float    # Valor mínimo da ação
}
```

### PredictionResponseBase
```python
{
    "high": float,  # Predição do valor máximo
    "low": float    # Predição do valor mínimo
}
```

## 🔧 Configurações

As configurações da aplicação são gerenciadas através do arquivo `.env`:

- `PORT` - Porta onde a aplicação será executada (padrão: 8000)
- `HOST` - Host onde a aplicação será executada (padrão: 127.0.0.1)



