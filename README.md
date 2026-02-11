# Automated-Report-Generator

![GitHub last commit](https://img.shields.io/github/last-commit/galafis/Automated-Report-Generator?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/galafis/Automated-Report-Generator?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/galafis/Automated-Report-Generator?style=for-the-badge)
![GitHub license](https://img.shields.io/github/license/galafis/Automated-Report-Generator?style=for-the-badge)

## English

### Overview

[View GitHub Pages](https://galafis.github.io/Automated-Report-Generator/)

### 🖼️ Hero Image

![Hero Image](docs/assets/hero_image.jpg)

This project presents an **Advanced Automated Report Generator** designed to streamline data analysis and reporting processes. It leverages a modern technology stack, integrating multiple programming languages to deliver comprehensive functionality, interactive web interfaces, and advanced analytics capabilities. The solution is crafted for professional-grade performance and scalability, making it suitable for various enterprise-level applications.

### Author
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Technologies Used

| Category         | Technologies                                    |
| :--------------- | :---------------------------------------------- |
| **Backend**      | Python (Flask), R                               |
| **Frontend**     | HTML5, CSS3, JavaScript (ES6+)                  |
| **Analytics**    | R, pandas, numpy, matplotlib, seaborn, plotly   |
| **Reporting**    | ReportLab, Jinja2                               |
| **Database**     | SQLite                                          |
| **Scheduling**   | Schedule                                        |

### Features

#### Core Functionality
- **Advanced Processing**: Utilizes high-performance algorithms for efficient data processing and transformation.
- **Real-time Analytics**: Provides live data analysis and visualization for immediate insights.
- **Interactive Interface**: Features a modern, responsive web interface for intuitive user interaction.
- **Statistical Analysis**: Incorporates comprehensive R-based analytics for in-depth statistical reporting.
- **Scalable Architecture**: Designed for enterprise-level performance and easy scalability.
- **Automated Reporting**: Generates professional PDF reports and interactive dashboards automatically.
- **Email Distribution**: Supports automated email sending with attached reports for seamless distribution.

#### Web Interface
- **Modern UI**: Built with HTML5 semantic markup, ensuring accessibility and best practices.
- **Responsive Design**: Employs CSS3 with Grid and Flexbox for optimal viewing across all devices.
- **Interactive Elements**: Enhanced with JavaScript ES6+ and modern web APIs for dynamic content.
- **Real-time Updates**: Delivers dynamic content and live data visualization for up-to-the-minute information.
- **Professional Styling**: Custom CSS animations and transitions provide a polished user experience.

#### Analytics & Reporting
- **R Integration**: Seamless integration with R for advanced statistical analysis and data visualization.
- **Data Processing**: Automated data cleaning and transformation using powerful Python libraries like pandas and numpy.
- **Visualization**: Offers both interactive charts (Plotly) and static plots (Matplotlib, Seaborn) for diverse reporting needs.
- **Métricas de Performance**: Real-time monitoring and analytics to track key performance indicators.
- **Export Options**: Multiple format support for reports, including PDF and HTML.

### Installation

To set up the Automated Report Generator, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/galafis/Automated-Report-Generator.git
cd Automated-Report-Generator

# 2. Python setup
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. R setup (install required packages)
# Note: R and its packages can be complex to install. Ensure R is installed on your system.
# For Debian/Ubuntu: sudo apt-get update && sudo apt-get install -y r-base
# Then, run the following in an R console or Rscript:
# install.packages(c(\'ggplot2\', \'dplyr\', \'corrplot\', \'plotly\'), repos=\'http://cran.us.r-project.org\')

# 4. Run the application
python3 src/app.py
```

### Web Interface Usage

1. **Start the Application**
   ```bash
   python3 src/app.py
   # Open http://127.0.0.1:5000 in your browser
   ```

2. **Access Web Interface**
   - Open `index.html` (located in the `templates` folder) in your browser for the frontend interface.
   - Explore the interactive dashboard with real-time functionality.
   - The responsive design ensures compatibility across desktop and mobile devices.
   - Click the "Buscar Dados do Backend" button to fetch sample data and observe dynamic updates.

### File Structure

```
Automated-Report-Generator/
├── .github/              # GitHub specific configurations (e.g., workflows)
├── config/               # Configuration files
│   └── config.json       # Main configuration for report generation
├── docs/                 # Documentation and assets
│   └── assets/           # Images, diagrams, and other media
│       ├── hero_image.jpg
│       ├── workflow_en.mmd
│       └── workflow_pt.mmd
├── src/                  # Source code for the application
│   ├── analytics.R       # R statistical analysis script
│   ├── app.js            # JavaScript for frontend interactivity
│   ├── app.py            # Main Flask application
│   ├── report_generator.py # Python script for report generation logic
│   └── styles.css        # CSS for styling the web interface
├── templates/            # HTML templates for Flask application
│   └── index.html        # Main HTML file for GitHub Pages and Flask rendering
├── tests/                # Unit and integration tests
│   └── test_report_generator.py # Tests for report generation logic
├── .gitignore            # Specifies intentionally untracked files to ignore
├── CODE_OF_CONDUCT.md    # Code of Conduct guidelines
├── CONTRIBUTING.md       # Guidelines for contributing to the project
├── LICENSE               # Project license information
├── README.md             # Project README (this file)
└── requirements.txt      # Python dependencies
```

### Workflow

[Workflow Diagram (English)](docs/assets/workflow_en.mmd)

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
- **Multi-threading**: Implementa processamento paralelo para melhor desempenho e responsividade.
- **Cache**: Utiliza mecanismos de cache inteligentes para tempos de resposta mais rápidos e carga reduzida.
- **Otimização de Memória**: Emprega técnicas eficientes de uso e gerenciamento de memória.
- **Escalabilidade**: Suporta escalonamento horizontal para atender às demandas de aplicações de nível empresarial.

---

## Português

### Visão Geral

[Ver GitHub Pages](https://galafis.github.io/Automated-Report-Generator/)

### 🖼️ Imagem Hero

![Imagem Hero](docs/assets/hero_image.jpg)

Este projeto apresenta um **Gerador de Relatórios Automatizado Avançado** projetado para otimizar os processos de análise e geração de relatórios. Ele utiliza um conjunto de tecnologias modernas, integrando múltiplas linguagens de programação para oferecer funcionalidade abrangente, interfaces web interativas e capacidades de análise avançadas. A solução é desenvolvida para desempenho e escalabilidade de nível profissional, tornando-a adequada para diversas aplicações empresariais.

### Autor
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Tecnologias Utilizadas

| Categoria        | Tecnologias                                     |
| :--------------- | :---------------------------------------------- |
| **Backend**      | Python (Flask), R                               |
| **Frontend**     | HTML5, CSS3, JavaScript (ES6+)                  |
| **Análises**     | R, pandas, numpy, matplotlib, seaborn, plotly   |
| **Geração de Relatórios** | ReportLab, Jinja2                               |
| **Banco de Dados** | SQLite                                          |
| **Agendamento**  | Schedule                                        |

### Funcionalidades

#### Funcionalidade Principal
- **Processamento Avançado**: Utiliza algoritmos de alta performance para processamento e transformação eficiente de dados.
- **Análises em Tempo Real**: Fornece análise e visualização de dados ao vivo para insights imediatos.
- **Interface Interativa**: Apresenta uma interface web moderna e responsiva para interação intuitiva do usuário.
- **Análise Estatística**: Incorpora análises abrangentes baseadas em R para relatórios estatísticos aprofundados.
- **Arquitetura Escalável**: Projetado para desempenho de nível empresarial e fácil escalabilidade.
- **Relatórios Automatizados**: Gera automaticamente relatórios PDF profissionais e dashboards interativos.
- **Distribuição por E-mail**: Suporta o envio automatizado de e-mails com relatórios anexados para distribuição contínua.

#### Interface Web
- **UI Moderna**: Construída com marcação semântica HTML5, garantindo acessibilidade e melhores práticas.
- **Design Responsivo**: Emprega CSS3 com Grid e Flexbox para visualização otimizada em todos os dispositivos.
- **Elementos Interativos**: Aprimorada com JavaScript ES6+ e APIs web modernas para conteúdo dinâmico.
- **Atualizações em Tempo Real**: Oferece conteúdo dinâmico e visualização de dados ao vivo para informações atualizadas.
- **Estilização Profissional**: Animações e transições CSS personalizadas proporcionam uma experiência de usuário refinada.

#### Análises e Relatórios
- **Integração R**: Integração perfeita com R para análise estatística avançada e visualização de dados.
- **Processamento de Dados**: Limpeza e transformação automatizada de dados usando poderosas bibliotecas Python como pandas e numpy.
- **Visualização**: Oferece gráficos interativos (Plotly) e gráficos estáticos (Matplotlib, Seaborn) para diversas necessidades de relatórios.
- **Métricas de Performance**: Monitoramento e análises em tempo real para acompanhar os principais indicadores de desempenho.
- **Opções de Exportação**: Suporte a múltiplos formatos para relatórios, incluindo PDF e HTML.

### Instalação

Para configurar o Gerador de Relatórios Automatizado, siga estes passos:

```bash
# 1. Clonar o repositório
git clone https://github.com/galafis/Automated-Report-Generator.git
cd Automated-Report-Generator

# 2. Configuração Python
python3 -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. R setup (install required packages)
# Nota: R e seus pacotes podem ser complexos de instalar. Certifique-se de que o R esteja instalado em seu sistema.
# Para Debian/Ubuntu: sudo apt-get update && sudo apt-get install -y r-base
# Em seguida, execute o seguinte em um console R ou Rscript:
# install.packages(c(\'ggplot2\', \'dplyr\', \'corrplot\', \'plotly\'), repos=\'http://cran.us.r-project.org\')

# 4. Executar a aplicação
python3 src/app.py
```

### Uso da Interface Web

1. **Iniciar a Aplicação**
   ```bash
   python3 src/app.py
   # Abrir http://127.0.0.1:5000 no seu navegador
   ```

2. **Acessar Interface Web**
   - Abra `index.html` (localizado na pasta `templates`) em seu navegador para a interface frontend.
   - Explore o dashboard interativo com funcionalidade em tempo real.
   - O design responsivo garante compatibilidade em desktops e dispositivos móveis.
   - Clique no botão "Buscar Dados do Backend" para buscar dados de exemplo e observar as atualizações dinâmicas.

### File Structure

```
Automated-Report-Generator/
├── .github/              # Configurações específicas do GitHub (ex: workflows)
├── config/               # Arquivos de configuração
│   └── config.json       # Configuração principal para geração de relatórios
├── docs/                 # Documentação e ativos
│   └── assets/           # Imagens, diagramas e outras mídias
│       ├── hero_image.jpg
│       ├── workflow_en.mmd
│       └── workflow_pt.mmd
├── src/                  # Código fonte da aplicação
│   ├── analytics.R       # R statistical analysis script
│   ├── app.js            # JavaScript para interatividade frontend
│   ├── app.py            # Aplicação Flask principal
│   ├── report_generator.py # Script Python para a lógica de geração de relatórios
│   └── styles.css        # CSS para estilização da interface web
├── templates/            # HTML templates para a aplicação Flask
│   └── index.html        # Arquivo HTML principal para GitHub Pages e renderização Flask
├── tests/                # Testes unitários e de integração
│   └── test_report_generator.py # Testes para a lógica de geração de relatórios
├── .gitignore            # Especifica arquivos intencionalmente não rastreados a serem ignorados
├── CODE_OF_CONDUCT.md    # Diretrizes do Código de Conduta
├── CONTRIBUTING.md       # Diretrizes para contribuição ao projeto
├── LICENSE               # Informações da licença do projeto
├── README.md             # Project README (este arquivo)
└── requirements.txt      # Dependências Python
```

### Workflow

[Diagrama de Fluxo de Trabalho (Português)](docs/assets/workflow_pt.mmd)

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
- **Multi-threading**: Implementa processamento paralelo para melhor desempenho e responsividade.
- **Cache**: Utiliza mecanismos de cache inteligentes para tempos de resposta mais rápidos e carga reduzida.
- **Otimização de Memória**: Emprega técnicas eficientes de uso e gerenciamento de memória.
- **Escalabilidade**: Suporta escalonamento horizontal para atender às demandas de aplicações de nível empresarial.

### Licença
MIT License

### Contribuições
Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request.

### Contato
Para dúvidas ou suporte, entre em contato através do email ou LinkedIn mencionados acima.

### Governança
- [Código de Conduta](CODE_OF_CONDUCT.md)
- [Diretrizes de Contribuição](CONTRIBUTING.md)

