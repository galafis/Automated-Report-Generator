# Automated-Report-Generator

![GitHub last commit](https://img.shields.io/github/last-commit/galafis/Automated-Report-Generator?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/galafis/Automated-Report-Generator?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/galafis/Automated-Report-Generator?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/galafis/Automated-Report-Generator?style=for-the-badge)
![GitHub Pages](https://img.shields.io/github/actions/workflow/status/galafis/Automated-Report-Generator/pages/pages-build-deployment?label=GitHub%20Pages&style=for-the-badge)

## English

### Overview

[View GitHub Pages](https://galafis.github.io/Automated-Report-Generator/)

### 🖼️ Hero Image

![Hero Image](docs/assets/new_hero_images/new_hero_image.png)

Advanced Automated-Report-Generator with comprehensive functionality and modern technology stack. Features multiple programming languages, interactive web interfaces, and advanced analytics capabilities for professional-grade solutions.

### Author
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Technologies Used
- **Backend**: Python (Flask), R
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Analytics**: R, pandas, numpy, matplotlib, seaborn, plotly
- **Reporting**: ReportLab, Jinja2
- **Database**: SQLite
- **Scheduling**: Schedule

### Features

#### Core Functionality
- **Advanced Processing**: High-performance algorithms and data processing.
- **Real-time Analytics**: Live data analysis and visualization.
- **Interactive Interface**: Modern web interface with responsive design.
- **Statistical Analysis**: Comprehensive R-based analytics and reporting.
- **Scalable Architecture**: Built for enterprise-level performance.
- **Automated Reporting**: Generation of PDF reports and interactive dashboards.
- **Email Distribution**: Automated email sending with report attachments.

#### Web Interface
- **Modern UI**: HTML5 semantic markup with accessibility features.
- **Responsive Design**: CSS3 with Grid, Flexbox, and mobile optimization.
- **Interactive Elements**: JavaScript ES6+ with modern web APIs.
- **Real-time Updates**: Dynamic content and live data visualization.
- **Professional Styling**: Custom CSS animations and transitions.

#### Analytics & Reporting
- **R Integration**: Advanced statistical analysis and data visualization.
- **Data Processing**: Automated data cleaning and transformation using pandas and numpy.
- **Visualization**: Interactive charts (Plotly) and static plots (Matplotlib, Seaborn).
- **Performance Metrics**: Real-time monitoring and analytics.
- **Export Options**: Multiple format support for reports (PDF, HTML).

### Installation

```bash
# Clone the repository
git clone https://github.com/galafis/Automated-Report-Generator.git
cd Automated-Report-Generator

# Python setup
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# R setup (install required packages)
Rscript -e "install.packages(c(\'ggplot2\', \'dplyr\', \'corrplot\', \'plotly\'))"

# Run the application
python3 src/app.py
```

### Web Interface Usage

1. **Start the Application**
   ```bash
   python3 src/app.py
   # Open http://127.0.0.1:5000 in your browser
   ```

2. **Access Web Interface**
   - Open `index.html` in your browser for the frontend interface.
   - Interactive dashboard with real-time functionality.
   - Responsive design works on desktop and mobile devices.
   - Click the "Buscar Dados do Backend" button to fetch sample data.

### File Structure

```
Automated-Report-Generator/
├── .github/              # GitHub specific configurations (e.g., workflows)
├── config/               # Configuration files
│   └── config.json       # Main configuration for report generation
├── docs/                 # Documentation and assets
│   └── assets/           # Images, diagrams, and other media
│       ├── hero_image.jpg
│       ├── workflow_en.png
│       └── workflow_pt.png
├── src/                  # Source code for the application
│   ├── analytics.R       # R statistical analysis script
│   ├── app.js            # JavaScript for frontend interactivity
│   ├── app.py            # Main Flask application
│   ├── report_generator.py # Python script for report generation logic
│   └── styles.css        # CSS for styling the web interface
├── tests/                # Unit and integration tests
│   └── test_report_generator.py # Tests for report generation logic
├── .gitignore            # Specifies intentionally untracked files to ignore
├── CODE_OF_CONDUCT.md    # Code of Conduct guidelines
├── CONTRIBUTING.md       # Guidelines for contributing to the project
├── index.html            # Main HTML file for GitHub Pages
├── LICENSE               # Project license information
├── README.md             # Project README (this file)
└── requirements.txt      # Python dependencies
```

### Workflow

![Workflow Diagram (English)](docs/assets/workflow_en.png)

### API Endpoints

```python
# Main application endpoints
GET  /                 # Web interface (index.html)
POST /api/process      # Data processing endpoint
GET  /api/analytics    # Analytics results endpoint
POST /api/upload       # File upload endpoint
GET  /api/status       # System status endpoint
```

### Configuration

The `config.json` file, located in the `config/` directory, allows customization of report generation settings, email parameters, and report templates. A default configuration is created if the file does not exist.

```json
{
  "output_directory": "reports",
  "email_settings": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "",
    "sender_password": ""
  },
  "report_templates": {
    "sales_report": {
      "title": "Sales Performance Report",
      "frequency": "weekly",
      "recipients": []
    },
    "financial_report": {
      "title": "Financial Analysis Report",
      "frequency": "monthly",
      "recipients": []
    }
  }
}
```

### Performance Features
- **Multi-threading**: Parallel processing for improved performance.
- **Caching**: Intelligent caching for faster response times.
- **Memory Optimization**: Efficient memory usage and management.
- **Scalability**: Horizontal scaling support for enterprise use.

---

## Português

### Visão Geral

[Ver GitHub Pages](https://galafis.github.io/Automated-Report-Generator/)

### 🖼️ Imagem Hero

![Imagem Hero](docs/assets/new_hero_images/new_hero_image.png)

Gerador de Relatórios Automatizado avançado com funcionalidade abrangente e um conjunto de tecnologias modernas. Apresenta múltiplas linguagens de programação, interfaces web interativas e capacidades de análise avançadas para soluções de nível profissional.

### Autor
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Tecnologias Utilizadas
- **Backend**: Python (Flask), R
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Análises**: R, pandas, numpy, matplotlib, seaborn, plotly
- **Geração de Relatórios**: ReportLab, Jinja2
- **Banco de Dados**: SQLite
- **Agendamento**: Schedule

### Funcionalidades

#### Funcionalidade Principal
- **Processamento Avançado**: Algoritmos de alta performance e processamento de dados.
- **Análises em Tempo Real**: Análise e visualização de dados ao vivo.
- **Interface Interativa**: Interface web moderna com design responsivo.
- **Análise Estatística**: Análises abrangentes baseadas em R e relatórios.
- **Arquitetura Escalável**: Construído para performance de nível empresarial.
- **Relatórios Automatizados**: Geração de relatórios em PDF e dashboards interativos.
- **Distribuição por E-mail**: Envio automatizado de e-mails com relatórios anexados.

#### Interface Web
- **UI Moderna**: Marcação semântica HTML5 com recursos de acessibilidade.
- **Design Responsivo**: CSS3 com Grid, Flexbox e otimização para dispositivos móveis.
- **Elementos Interativos**: JavaScript ES6+ com APIs web modernas.
- **Atualizações em Tempo Real**: Conteúdo dinâmico e visualização de dados ao vivo.
- **Estilização Profissional**: Animações e transições CSS personalizadas.

#### Análises e Relatórios
- **Integração R**: Análise estatística avançada e visualização de dados.
- **Processamento de Dados**: Limpeza e transformação automatizada de dados usando pandas e numpy.
- **Visualização**: Gráficos interativos (Plotly) e gráficos estáticos (Matplotlib, Seaborn).
- **Métricas de Performance**: Monitoramento e análises em tempo real.
- **Opções de Exportação**: Suporte a múltiplos formatos para relatórios (PDF, HTML).

### Instalação

```bash
# Clonar o repositório
git clone https://github.com/galafis/Automated-Report-Generator.git
cd Automated-Report-Generator

# Configuração Python
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

# Configuração R (instalar pacotes necessários)
Rscript -e "install.packages(c(\'ggplot2\', \'dplyr\', \'corrplot\', \'plotly\'))"

# Executar a aplicação
python3 src/app.py
```

### Uso da Interface Web

1. **Iniciar a Aplicação**
   ```bash
   python3 src/app.py
   # Abrir http://127.0.0.1:5000 no seu navegador
   ```

2. **Acessar Interface Web**
   - Abrir `index.html` no seu navegador para a interface frontend.
   - Dashboard interativo com funcionalidade em tempo real.
   - Design responsivo funciona em desktop e dispositivos móveis.
   - Clique no botão "Buscar Dados do Backend" para buscar dados de exemplo.

### Estrutura de Arquivos

```
Automated-Report-Generator/
├── .github/              # Configurações específicas do GitHub (ex: workflows)
├── config/               # Arquivos de configuração
│   └── config.json       # Configuração principal para geração de relatórios
├── docs/                 # Documentação e ativos
│   └── assets/           # Imagens, diagramas e outras mídias
│       ├── hero_image.jpg
│       ├── workflow_en.png
│       └── workflow_pt.png
├── src/                  # Código fonte da aplicação
│   ├── analytics.R       # Script de análise estatística em R
│   ├── app.js            # JavaScript para interatividade frontend
│   ├── app.py            # Aplicação Flask principal
│   ├── report_generator.py # Script Python para a lógica de geração de relatórios
│   └── styles.css        # CSS para estilização da interface web
├── tests/                # Testes unitários e de integração
│   └── test_report_generator.py # Testes para a lógica de geração de relatórios
├── .gitignore            # Especifica arquivos intencionalmente não rastreados a serem ignorados
├── CODE_OF_CONDUCT.md    # Diretrizes do Código de Conduta
├── CONTRIBUTING.md       # Diretrizes para contribuição ao projeto
├── index.html            # Arquivo HTML principal para GitHub Pages
├── LICENSE               # Informações da licença do projeto
├── README.md             # README do projeto (este arquivo)
└── requirements.txt      # Dependências Python
```

### Fluxo de Trabalho

![Diagrama de Fluxo de Trabalho (Português)](docs/assets/workflow_pt.png)

### Endpoints da API

```python
# Endpoints principais da aplicação
GET  /                 # Interface web (index.html)
POST /api/process      # Endpoint de processamento de dados
GET  /api/analytics    # Endpoint de resultados de análise
POST /api/upload       # Endpoint de upload de arquivo
GET  /api/status       # Endpoint de status do sistema
```

### Configuração

O arquivo `config.json`, localizado no diretório `config/`, permite a personalização das configurações de geração de relatórios, parâmetros de e-mail e modelos de relatório. Uma configuração padrão é criada se o arquivo não existir.

```json
{
  "output_directory": "reports",
  "email_settings": {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "",
    "sender_password": ""
  },
  "report_templates": {
    "sales_report": {
      "title": "Sales Performance Report",
      "frequency": "weekly",
      "recipients": []
    },
    "financial_report": {
      "title": "Financial Analysis Report",
      "frequency": "monthly",
      "recipients": []
    }
  }
}
```

### Recursos de Performance
- **Multi-threading**: Processamento paralelo para melhor performance.
- **Cache**: Cache inteligente para tempos de resposta mais rápidos.
- **Otimização de Memória**: Uso eficiente de memória e gerenciamento.
- **Escalabilidade**: Suporte a escalonamento horizontal para uso empresarial.

### Licença
MIT License

### Contribuições
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

### Contato
Para dúvidas ou suporte, entre em contato através do email ou LinkedIn mencionados acima.

### Governança
- [Código de Conduta](CODE_OF_CONDUCT.md)
- [Diretrizes de Contribuição](CONTRIBUTING.md)


