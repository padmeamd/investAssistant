Конечно, вот пример README файла для вашего проекта:

# Инвестиционный Умный Помощник

## Описание проекта
Инвестиционный умный помощник предназначен для первичной консультации инвесторов и комплексного подбора земельных участков, помещений, мер поддержки и решения системных проблем. Проект обеспечивает эффективные инструменты для подбора инвестиционных площадок, анализируя данные и предлагая релевантные варианты.

## Технологический стек
- **Backend**: Java, Spring Boot
- **Frontend**: React.js
- **Database**: PostgreSQL
- **AI**: Python (scikit-learn, TensorFlow)
- **API**: RESTful API
- **Security**: JWT для аутентификации

## Функциональность
- **Регистрация и авторизация пользователей**
- **Подбор инвестиционных площадок и мер поддержки**
- **Личный кабинет пользователя с историей запросов и результатов**
- **Сравнение различных вариантов и скачивание отчетов в формате PDF**

## Структура проекта
```
invest_assistant/
├── backend/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── com/
│   │   │   │       └── example/
│   │   │   │           └── investassistant/
│   │   │   │               ├── controllers/
│   │   │   │               │   ├── AuthController.java
│   │   │   │               │   └── RecommendationController.java
│   │   │   │               ├── models/
│   │   │   │               │   └── User.java
│   │   │   │               ├── repositories/
│   │   │   │               │   └── UserRepository.java
│   │   │   │               ├── services/
│   │   │   │               │   └── UserService.java
│   │   │   │               ├── security/
│   │   │   │               │   ├── CustomUserDetailsService.java
│   │   │   │               │   └── SecurityConfig.java
│   │   │   │               └── InvestAssistantApplication.java
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── pom.xml
│   └── README.md
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Home.js
│   │   │   ├── Register.js
│   │   │   ├── Login.js
│   │   │   └── Dashboard.js
│   │   ├── App.js
│   │   ├── index.js
│   │   └── App.css
│   ├── package.json
│   └── README.md
└── python-api/
    ├── app.py
    ├── requirements.txt
    ├── data/
    │   ├── support_measures.csv
    │   └── sites.csv
    └── models/
        └── recommendation_model.pkl
```

## Запуск проекта

### Backend
1. Перейдите в директорию проекта Spring Boot:
   ```bash
   cd backend
   ```
2. Запустите приложение:
   ```bash
   ./mvnw spring-boot:run
   ```

### Frontend
1. Перейдите в директорию проекта React:
   ```bash
   cd frontend
   ```
2. Установите зависимости и запустите приложение:
   ```bash
   npm install
   npm start
   ```

### Python API
1. Перейдите в директорию проекта Python API:
   ```bash
   cd python-api
   ```
2. Установите зависимости и запустите Flask приложение:
   ```bash
   pip install -r requirements.txt
   python app.py
   ```

## Будущие улучшения
Настоящая версия проекта является начальной моделью, которую можно со временем усовершенствовать и расширить, добавляя новые функции и улучшая существующие возможности.

## Авторы
Константинова Дарья Алексеевна (full-stack разработчик, java)
Telegram: https://t.me/imdayd

Козлов Максим Александрович (full-stack разработчик, python)
Telegram: https://t.me/Aguero_Agnis




