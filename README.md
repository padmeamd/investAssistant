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
investAssistant/
├── .idea/
├── investAssistant/
│   ├── .mvn/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/
│   │   │   │   └── com/
│   │   │   │       └── investAssistant/
│   │   │   │           ├── controller/
│   │   │   │           │   ├── AuthController.java
│   │   │   │           │   ├── RecommendationController.java
│   │   │   │           ├── entity/
│   │   │   │           │   ├── Criteria.java
│   │   │   │           │   ├── Recommendation.java
│   │   │   │           │   ├── User.java
│   │   │   │           ├── repository/
│   │   │   │           │   ├── RecommendationRepository.java
│   │   │   │           │   ├── UserRepository.java
│   │   │   │           ├── security/
│   │   │   │           │   ├── SecurityConfig.java
│   │   │   │           ├── service/
│   │   │   │           │   ├── CustomUserDetailsService.java
│   │   │   │           │   ├── RecommendationService.java
│   │   │   │           │   ├── UserService.java
│   │   │   │           ├── util/
│   │   │   │           │   ├── DialogManager.java
│   │   │   │           │   ├── DialogState.java
│   │   │   │           └── InvestAssistantApplication.java
│   │   ├── webapp/
│   │   │   ├── home.jsp
│   │   ├── resources/
│   │   │   ├── static/
│   │   │   │   ├── css/
│   │   │   │   │   ├── styles.css
│   │   │   │   ├── js/
│   │   │   │   │   ├── scripts.js
│   │   │   ├── templates/
│   │   │   ├── application.properties
│   │   │   ├── application-dev.properties
├── python_staff/
│   ├── data/
│   │   ├── file.txt
│   ├── myenv/
│   │   ├── bin/
│   │   │   ├── activate
│   │   │   ├── activate.csh
│   │   │   ├── activate.fish
│   │   │   ├── Activate.ps1
│   │   │   ├── flask
│   │   │   ├── pip
│   │   │   ├── pip3
│   │   │   ├── pip3.12
│   │   │   ├── python
│   │   │   ├── python3
│   │   │   ├── python3.12
│   │   ├── lib/
│   │   ├── pyvenv.cfg
│   ├── 1.xlsx
│   ├── 2.xlsx
│   ├── 3.xlsx
│   ├── allypython.py
│   ├── app.py
│   ├── neuro.py
│   ├── requirements.txt
├── test/
│   ├── java/
│   │   └── com/
│   │       └── investAssistant/
│   │           ├── InvestAssistantApplicationTests.java
├── target/
├── .gitignore
├── mvnw
├── mvnw.cmd
├── pom.xml
├── README.md

```

### Объяснение структуры проекта

- **.idea/** - Директория настроек проекта IntelliJ IDEA.
- **investAssistant/** - Основная директория проекта:
  - **.mvn/** - Maven Wrapper файлы.
  - **src/main/java/com/investAssistant/investAssistant/** - Исходный код проекта:
    - **controller/** - Контроллеры для обработки HTTP-запросов:
      - `AuthController.java`
      - `RecommendationController.java`
    - **entity/** - Сущности, отображаемые в базе данных:
      - `Criteria.java`
      - `Recommendation.java`
      - `User.java`
    - **repository/** - Репозитории для доступа к данным:
      - `RecommendationRepository.java`
      - `UserRepository.java`
    - **security/** - Классы, связанные с безопасностью:
      - `SecurityConfig.java`
    - **service/** - Сервисы для бизнес-логики:
      - `CustomUserDetailsService.java`
      - `RecommendationService.java`
      - `UserService.java`
    - **util/** - Утилитарные классы:
      - `DialogManager.java`
      - `DialogState.java`
    - `InvestAssistantApplication.java` - Основной класс приложения Spring Boot.
  - **src/main/webapp/** - Веб-ресурсы:
    - `home.jsp` - Главная страница JSP.
  - **src/main/resources/** - Ресурсы приложения:
    - **static/** - Статические ресурсы (CSS, JS):
      - `styles.css`
      - `scripts.js`
    - **templates/** - Шаблоны (например, Thymeleaf, FreeMarker).
    - `application.properties` - Файл настроек Spring Boot.
    - `application-dev.properties` - Файл настроек для разработки.
- **python_staff/** - Директория с Python-скриптами и виртуальной средой:
  - **data/** - Данные для обработки.
    - `file.txt`
  - **myenv/** - Виртуальная среда Python.
  - `app.py` - Основной файл Flask приложения.
  - `requirements.txt` - Файл зависимостей для Python.
- **test/** - Тесты проекта:
  - **java/com/investAssistant/investAssistant/** - Тесты для Java:
    - `InvestAssistantApplicationTests.java`
- **target/** - Директория сборки Maven.
- `.gitignore` - Файл настроек Git для исключения файлов из контроля версий.
- `mvnw`, `mvnw.cmd` - Maven Wrapper для запуска Maven без установки.
- `pom.xml` - Основной файл конфигурации Maven.
- `README.md` - Файл документации проекта.


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




