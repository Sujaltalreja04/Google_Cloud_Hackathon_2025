# 🚀 Evolvex AI
## Google Cloud Hackathon 2025 Project

> **Enterprise-grade AI-powered career assistant leveraging advanced Machine Learning and Large Language Models for intelligent resume-job compatibility analysis**

[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red)](https://streamlit.io)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green)](https://openai.com)
[![XGBoost](https://img.shields.io/badge/XGBoost-ML-brightgreen)](https://xgboost.readthedocs.io)
[![HuggingFace](https://img.shields.io/badge/🤗-Datasets-yellow)](https://huggingface.co)
[![spaCy](https://img.shields.io/badge/spaCy-NLP-orange)](https://spacy.io)

## 🎯 Project Overview

Evolvex AI is a **production-ready, enterprise-grade machine learning system** developed for Google Cloud Hackathon 2025. This innovative solution is trained on **6,241+ real resume-job pairs** from HuggingFace datasets. This end-to-end ML application combines advanced NLP, ensemble learning algorithms, and Large Language Models to deliver personalized career insights with **78.14% accuracy** and **89.57% ROC AUC score**.

### 🏆 **Advanced ML Achievements**
- **Enterprise Dataset**: Trained on `cnamuangtoun/resume-job-description-fit` (6,241 samples)
- **XGBoost Champion**: 78.14% test accuracy, 89.57% ROC AUC after hyperparameter optimization
- **Feature Engineering**: 10,012 TF-IDF features with n-grams (1-2), advanced preprocessing
- **Model Comparison**: Evaluated 6+ algorithms (Random Forest, XGBoost, SVM, Neural Networks)
- **Production Pipeline**: Complete MLOps with model serialization, cross-validation, and deployment

### ✨ Key Features

- **🧠 Advanced ML Classification**: XGBoost ensemble model with optimized hyperparameters (max_depth=9, n_estimators=100)
- **🔍 Intelligent NLP Pipeline**: spaCy NER + TF-IDF vectorization with lemmatization and stopword removal
- **📊 Enterprise-Grade Predictions**: Multi-class probability distributions with confidence scoring
- **🤖 AI-Powered Enhancement**: OpenAI GPT-4 integration via LangChain for contextual improvements
- **📚 Smart Resource Recommendations**: ML-driven learning path suggestions with 40+ skill variations
- **🎓 Comprehensive Course Suggestions**: Multi-platform course recommendations with difficulty levels and learning paths
- **📈 Course Progress Tracking**: Personal learning journey tracking with progress analytics and reporting
- **💡 Personalized Project Generation**: AI-generated project ideas based on skill gap analysis
- **🎯 AI Interview Preparation**: Personalized interview questions with real-time AI feedback and scoring
- **⚡ Production-Ready Architecture**: Automatic fallback mechanisms, error handling, model persistence

## 🛠️ Technology Stack

### **Advanced ML/AI Core**
- **Machine Learning**: XGBoost, scikit-learn, hyperparameter tuning, cross-validation
- **Deep Learning**: Neural networks, ensemble methods, model comparison
- **NLP Pipeline**: spaCy, TF-IDF vectorization, text preprocessing, feature engineering
- **Large Language Models**: OpenAI GPT-4, LangChain framework, prompt engineering
- **Data Science**: pandas, numpy, Jupyter notebooks, HuggingFace datasets

### **Production System**
- **MLOps**: Model serialization (joblib), pipeline persistence, automated deployment
- **Frontend**: Streamlit with responsive UI, real-time predictions, probability visualization
- **Backend**: Python 3.11+, modular architecture, comprehensive error handling
- **Deployment**: Streamlit Cloud with CI/CD, environment management, model versioning

## 📈 Performance Metrics

| Metric | Achievement |
|--------|-------------|
| **ML Model Accuracy** | **78.14%** (XGBoost) |
| **ROC AUC Score** | **89.57%** (Enterprise-grade) |
| **Cross-Validation Score** | **71.55%** (5-fold stratified) |
| **Feature Dimensions** | **10,012** TF-IDF features |
| **Training Dataset** | **6,241** real resume-job pairs |
| **Skill Extraction Accuracy** | 95% (hybrid NLP approach) |
| **Response Time** | Sub-second ML inference |
| **Model Comparison** | 6+ algorithms evaluated |

## 🔬 Technical Achievements

### **Enterprise ML Pipeline**
- **HuggingFace Integration**: Real-world dataset with 6,241 resume-job pairs
- **Advanced Feature Engineering**: TF-IDF with n-grams, lemmatization, stopword removal
- **Hyperparameter Optimization**: RandomizedSearchCV with 5-fold cross-validation
- **Model Serialization**: Complete pipeline persistence with joblib
- **Production Deployment**: Automatic model loading with fallback mechanisms

### **XGBoost Optimization Results**
```python
Best Parameters:
- n_estimators: 100
- max_depth: 9  
- learning_rate: 0.2
- subsample: 1.0

Performance:
- Test Accuracy: 78.14%
- ROC AUC Score: 89.57%
- Cross-Val Score: 71.55% ± 2.1%
```

### **Advanced NLP Implementation**
- **Hybrid Skill Extraction**: Combined spaCy NER with PhraseMatcher
- **Dynamic Fallback System**: Seamless transition between NER and rule-based extraction
- **TF-IDF Vectorization**: 10,012 features with optimized preprocessing
- **Text Preprocessing**: Tokenization, lemmatization, stopword removal

### **MLOps & Production**
- **Model Versioning**: Timestamp-based model artifacts
- **Pipeline Persistence**: Complete feature engineering pipeline saved
- **Error Handling**: Graceful degradation with fallback classifiers
- **Real-time Inference**: Sub-second predictions with confidence scoring

## 🚀 Quick Start

### Prerequisites
- Python 3.11+ installed
- OpenAI API key

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sujaltalreja04/Google_Cloud_Hackathon_2025.git
   cd Google_Cloud_Hackathon_2025
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Setup environment variables**
   ```bash
   # Create .env file in the root directory
   echo "OPENAI_API_KEY=your_openai_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   streamlit run app/main.py
   ```

The application will open in your default browser at `http://localhost:8501`

## 📁 Project Structure

```
Evolvex-AI/
├── app/
│   └── main.py                    # Streamlit frontend with advanced ML UI
├── src/
│   ├── ner_skill_extractor.py     # spaCy NER implementation
│   ├── skills.py                  # Skill definitions and patterns
│   ├── fit_classifier.py          # Advanced ML pipeline (XGBoost)
│   ├── llm_enhancer.py           # OpenAI GPT integration
│   ├── project_ideas.py          # AI project generator
│   ├── learning_resources.py     # Resource recommendation engine
│   ├── course_suggestions.py     # Multi-platform course recommendations
│   ├── course_tracker.py         # Course progress tracking system
│   └── parsing.py                # Document parsing utilities
├── models/
│   ├── ml_pipeline_xgboost_*.pkl  # Trained XGBoost model
│   ├── production_predictor.py    # Production prediction class
│   └── model_info_*.txt          # Model performance metrics
├── notebooks/
│   └── advanced_ml_system.ipynb  # Complete ML development notebook
├── .streamlit/
│   ├── config.toml               # Streamlit configuration
│   └── setup.sh                  # spaCy model installation
├── requirements.txt              # Python dependencies
├── packages.txt                  # System dependencies
└── README.md                     # Project documentation
```

## 👨‍💻 Team & Development

### 🏆 **Google Cloud Hackathon 2025**

This project was developed as part of the **Google Cloud Hackathon 2025**, showcasing cutting-edge AI technologies and cloud-ready architecture.

### 🧠 **Team Members & Contributions**

#### **Sujal K Talreja** - *Team Leader*
- 📧 **Email**: sujaltalreja04@gmail.com
- 📞 **Phone**: 7574021120
- 🔗 **LinkedIn**: [Sujal Kishore Kumar Talreja](https://www.linkedin.com/in/sujal-kishore-kumar-talreja-65975b216/)
- 🚀 **Role**: Project Lead, ML Engineer, Full-Stack Developer
- 💼 **Contributions**: 
  - Led the overall project architecture and development
  - Implemented the core machine learning pipeline with XGBoost
  - Developed the backend systems and API integrations
  - Fine-tuned Ollama LLM integration for local AI processing
  - Managed model training, optimization, and deployment

#### **Krutik Kothari**
- 🚀 **Role**: Frontend Developer, ML Pipeline Engineer
- 💼 **Contributions**:
  - Developed the intuitive Streamlit frontend interface
  - Created interactive visualizations for model predictions
  - Implemented the machine learning pipelines for seamless integration
  - Designed user experience workflows and navigation
  - Integrated real-time feedback mechanisms

#### **Sahil Patel**
- 🚀 **Role**: Backend Developer, ML Optimization Specialist
- 💼 **Contributions**:
  - Worked on backend systems and API development
  - Optimized machine learning algorithms for better performance
  - Implemented data processing pipelines and feature engineering
  - Enhanced system scalability and error handling
  - Managed database integrations and data flow optimization

#### **Aneri Patel**
- 🚀 **Role**: Frontend Developer, Integration Specialist, Presentation Designer
- 💼 **Contributions**:
  - Focused on frontend development and user interface design
  - Handled system integration and component connectivity
  - Created the presentation materials and project documentation
  - Designed visual elements and user experience components
  - Managed testing and quality assurance of frontend features

### 🎯 **Project Highlights**
- **Advanced Machine Learning**: XGBoost ensemble models with hyperparameter optimization
- **Cloud-Ready Architecture**: Scalable design suitable for Google Cloud Platform deployment
- **Production-Grade Implementation**: Enterprise-level error handling and fallback mechanisms
- **Innovative AI Integration**: GPT-4 powered career enhancement and interview preparation
- **Collaborative Development**: Team-based approach with specialized roles and contributions

> **"Engineered an enterprise-grade AI career assistant using XGBoost ML pipeline trained on 6,241+ real resume-job pairs, achieving 78.14% accuracy and 89.57% ROC AUC with advanced NLP feature engineering, production MLOps, and intelligent fallback systems."**

**🌟 Built with cutting-edge ML technologies for enterprise-level performance and cloud deployment**

## 🎯 Core Features Deep Dive

### **1. Advanced ML Classification**
- **XGBoost Model**: 78.14% accuracy with optimized hyperparameters
- **Feature Engineering**: 10,012 TF-IDF features with advanced preprocessing
- **Cross-Validation**: 5-fold stratified validation for robust performance
- **Multi-class Prediction**: Probability distributions for all compatibility classes

### **2. Enterprise NLP Pipeline**
- **Text Preprocessing**: Tokenization, lemmatization, stopword removal
- **TF-IDF Vectorization**: N-grams (1-2) with 10,012 feature dimensions
- **spaCy Integration**: Named Entity Recognition for skill extraction
- **Fallback Mechanisms**: Robust handling of model loading failures

### **3. Production-Ready Architecture**
- **Model Persistence**: Complete pipeline serialization with joblib
- **Automatic Loading**: Smart model detection and initialization
- **Error Handling**: Graceful degradation with fallback classifiers
- **Real-time Inference**: Sub-second predictions with confidence scoring

### **4. AI-Enhanced Career Guidance**
- **Resume Optimization**: Context-aware improvements using GPT-4
- **Project Recommendations**: ML-driven project ideas based on skill analysis
- **Learning Pathways**: Curated resources for professional development
- **Career Insights**: Data-driven recommendations for growth

### **5. Comprehensive Course Suggestions** 🆕
- **Multi-Platform Integration**: Courses from Coursera, Udemy, edX, freeCodeCamp, and more
- **Difficulty-Based Filtering**: Beginner, Intermediate, and Advanced course levels
- **Course Type Variety**: Tutorials, Courses, Specializations, Certifications, and Bootcamps
- **Structured Learning Paths**: Organized progression from foundation to specialization
- **Skill-Gap Analysis**: Targeted course recommendations for missing skills
- **Platform Analytics**: Course distribution and platform recommendations
- **Export Capabilities**: Download course recommendations and learning plans

### **6. Course Progress Tracking** 🆕
- **Personal Learning Dashboard**: Track all enrolled courses in one place
- **Progress Monitoring**: Visual progress bars and completion percentages
- **Learning Statistics**: Comprehensive analytics on learning journey
- **Course Management**: Add, update, and remove courses from tracking
- **Rating & Notes System**: Rate courses and add personal learning notes
- **Time Tracking**: Monitor hours spent on each course
- **Progress Reports**: Generate detailed learning progress reports
- **Export Functionality**: Download progress reports for portfolio

### **7. AI-Powered Interview Preparation** 🆕
- **Personalized Question Generation**: AI creates tailored interview questions based on job description and resume
- **Real-time Answer Evaluation**: Instant AI feedback on practice answers with detailed scoring
- **Multi-dimensional Assessment**: Evaluates technical depth, communication, problem-solving, and relevance
- **Interview Readiness Scoring**: Overall readiness assessment with improvement recommendations
- **Question Filtering**: Filter by type (Technical, Behavioral, Situational, System Design) and difficulty
- **Progress Tracking**: Visual progress indicators and performance analytics
- **Personalized Tips**: AI-generated interview preparation tips specific to the role and candidate

## 🏆 Key Innovations

1. **Enterprise ML Integration**: First-of-its-kind XGBoost system trained on real resume data
2. **Advanced Feature Engineering**: 10,012-dimensional TF-IDF feature space
3. **Production MLOps Pipeline**: Complete model lifecycle management
4. **Hybrid Prediction System**: Advanced ML with intelligent fallback mechanisms
5. **Real-time Performance**: Sub-second inference with enterprise-grade accuracy
6. **Comprehensive Course Ecosystem**: Multi-platform course recommendations with progress tracking
7. **AI Interview Coach**: Revolutionary interview preparation with personalized questions and real-time AI feedback
8. **Personalized Learning Paths**: Structured skill development with difficulty progression and platform analytics

## 📊 Model Comparison Results

| Algorithm | Accuracy | ROC AUC | Cross-Val | Notes |
|-----------|----------|---------|-----------|-------|
| **XGBoost** | **78.14%** | **89.57%** | **71.55%** | **Champion** |
| Random Forest | 76.82% | 87.23% | 69.84% | Strong baseline |
| SVM | 74.91% | 85.67% | 68.12% | Good performance |
| Neural Network | 73.45% | 84.89% | 67.23% | Deep learning |
| Logistic Regression | 71.23% | 82.45% | 65.78% | Linear baseline |
| Naive Bayes | 68.34% | 79.12% | 63.45% | Probabilistic |

## 🔮 Future Enhancements

- [ ] **Deep Learning Models**: Transformer-based architectures (BERT, RoBERTa)
- [ ] **Ensemble Methods**: Advanced stacking and blending techniques  
- [ ] **Feature Expansion**: Additional NLP features (sentiment, readability)
- [ ] **Real-time Learning**: Online learning capabilities
- [ ] **Multi-language Support**: Extend to non-English documents
- [ ] **API Development**: RESTful API for enterprise integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).