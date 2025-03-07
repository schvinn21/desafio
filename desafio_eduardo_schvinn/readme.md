# Calculadora de IMC

## Sobre o Projeto

A **Calculadora de IMC** é uma aplicação web simples e funcional desenvolvida em **Python (Flask)**. Ela permite que os usuários calculem o Índice de Massa Corporal (IMC) e verifiquem sua classificação com base em categorias padrão, além de armazenar os resultados em uma planilha do **Google Sheets** para consulta e acompanhamento.

---

## Funcionalidades

- **Cálculo do IMC**:
  - Permite entrada do nome, peso (kg) e altura (m).
- **Classificação Automática**:
  - Abaixo do peso.
  - Peso normal.
  - Sobrepeso.
  - Obesidade (grau 1 e 2).
- **Armazenamento em Google Sheets**:
  - Os dados são enviados automaticamente para uma planilha conectada via API.
- **Interface Amigável**:
  - Design responsivo, educativo e com ícones integrados.

---

## Requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu sistema:
- **Python 3.8+**
- **Google Cloud Account** com acesso configurado para a API do Google Sheets.
- Ambiente virtual (opcional, mas recomendado).

Para instalar todos os requerimentos necessários digite o seguinte comando:

pip install -r requeriments.txt

## Tecnologias Utilizadas
**Backend**
- Python
- Flask
- Google Sheets API

**Frontend**
- HTML5
- CSS3
- Font Awesome (ícones)

**Armazenameno**
- Google Sheets
