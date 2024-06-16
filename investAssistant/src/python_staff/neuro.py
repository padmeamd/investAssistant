import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization
from tensorflow.keras.regularizers import l2
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from transformers import pipeline

# Загрузка данных
oez_technoparks = pd.read_excel('1.xlsx')
premises_buildings = pd.read_excel('2.xlsx')
regional_support_measures = pd.read_excel('3.xlsx')

# Обработка данных
def preprocess_data(df, fit=True, columns=None):
    df = df.copy()
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].median(), inplace=True)
    df = pd.get_dummies(df)
    if fit:
        return df
    else:
        missing_cols = set(columns) - set(df.columns)
        for col in missing_cols:
            df[col] = 0
        return df[columns]

# Подготовка данных и обучение модели для каждого типа данных
def prepare_model(data, target_column='target'):
    data[target_column] = np.random.randint(0, 2, data.shape[0])  # Пример случайной целевой переменной
    X = data.drop(target_column, axis=1)
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = Sequential([
        Dense(256, input_dim=X_train.shape[1], activation='relu', kernel_regularizer=l2(0.001)),
        Dropout(0.5),
        BatchNormalization(),
        Dense(128, activation='relu', kernel_regularizer=l2(0.001)),
        Dropout(0.5),
        BatchNormalization(),
        Dense(64, activation='relu', kernel_regularizer=l2(0.001)),
        Dropout(0.5),
        BatchNormalization(),
        Dense(32, activation='relu', kernel_regularizer=l2(0.001)),
        Dropout(0.5),
        BatchNormalization(),
        Dense(1, activation='sigmoid')
    ])

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_test, y_test))

    loss, accuracy = model.evaluate(X_test, y_test)
    print(f'Test Accuracy: {accuracy * 100:.2f}%')

    return model, scaler, X.columns

model_oez, scaler_oez, columns_oez = prepare_model(preprocess_data(oez_technoparks))
model_premises, scaler_premises, columns_premises = prepare_model(preprocess_data(premises_buildings))
model_support, scaler_support, columns_support = prepare_model(preprocess_data(regional_support_measures))

# Инициализация модели GPT-2 для генерации текстов
generator = pipeline('text-generation', model='gpt2')

# Функция для предсказания с учетом гибкости критериев
def recommend_investment_sites(user_input, model, scaler, columns, flexibility=0.1):
    try:
        user_input = preprocess_data(user_input, fit=False, columns=columns)
        user_input = scaler.transform(user_input)

        predictions = model.predict(user_input)
        results = (predictions > 0.5).astype(int)

        if np.random.rand() < flexibility:
            results = 1 - results

        distances = np.abs(predictions - 0.5)
        sorted_indices = np.argsort(distances, axis=0)
        closest_indices = sorted_indices[:5].flatten()

        return results, closest_indices
    except Exception as e:
        print(f"Ошибка при предсказании: {e}")
        return None, None

# Интерактивный диалог
def interactive_dialog():
    print("Здравствуйте! Я помогу вам подобрать инвестиционные площадки.")

    while True:
        try:
            user_input = {}

            object_type = input("Какой тип объекта вас интересует? (ОЭЗ, Помещение, Меры поддержки): ").strip().lower()
            if object_type == 'оэз':
                model, scaler, columns = model_oez, scaler_oez, columns_oez
            elif object_type == 'помещение':
                model, scaler, columns = model_premises, scaler_premises, columns_premises
            elif object_type == 'меры поддержки':
                model, scaler, columns = model_support, scaler_support, columns_support
            else:
                print("Неверный тип объекта. Попробуйте снова.")
                continue

            # Запрашиваем критерии у пользователя
            region = input("Введите регион: ")
            user_input['Регион'] = region

            category = input("Введите категорию объекта (например, ОЭЗ, Технопарк): ")
            user_input['Категория объекта'] = category

            area = input("Введите минимальную площадь объекта (в кв.м): ")
            user_input['Площадь'] = float(area)

            rent_cost = input("Введите максимальную стоимость аренды (в руб.): ")
            user_input['Стоимость аренды'] = float(rent_cost)

            buy_cost = input("Введите максимальную стоимость покупки (в руб.): ")
            user_input['Стоимость покупки'] = float(buy_cost)

            infrastructure = input("Наличие инфраструктуры (да/нет): ")
            user_input['Инфраструктура'] = 1 if infrastructure.lower() == 'да' else 0

            transport_accessibility = input("Транспортная доступность (да/нет): ")
            user_input['Транспортная доступность'] = 1 if transport_accessibility.lower() == 'да' else 0

            activity_type = input("Тип деятельности (производственная, офисная, складская и т.д.): ")
            user_input['Тип деятельности'] = activity_type

            num_residents = input("Минимальное количество резидентов: ")
            user_input['Количество резидентов'] = int(num_residents)

            construction_year = input("Минимальный год постройки или последней реконструкции: ")
            user_input['Год постройки'] = int(construction_year)

            tax_benefits = input("Налоговые льготы (да/нет): ")
            user_input['Налоговые льготы'] = 1 if tax_benefits.lower() == 'да' else 0

            pref_modes = input("Преференциальные режимы (да/нет): ")
            user_input['Преференциальные режимы'] = 1 if pref_modes.lower() == 'да' else 0

            key_objects = input("Близость к ключевым объектам (да/нет): ")
            user_input['Близость к ключевым объектам'] = 1 if key_objects.lower() == 'да' else 0

            eco_conditions = input("Экологические условия (да/нет): ")
            user_input['Экологические условия'] = 1 if eco_conditions.lower() == 'да' else 0

            support_measures = input("Меры поддержки (да/нет): ")
            user_input['Меры поддержки'] = 1 if support_measures.lower() == 'да' else 0

            legal_status = input("Юридический статус (арендное, собственное): ")
            user_input['Юридический статус'] = legal_status

            # Создаем DataFrame из пользовательского ввода
            user_input_df = pd.DataFrame([user_input])

            # Предоставляем рекомендации
            recommendations, closest_indices = recommend_investment_sites(user_input_df, model, scaler, columns)
            if recommendations is not None:
                # Генерация описания с помощью GPT-2
                description = generator(f"Рекомендованные инвестиционные площадки для {region}, категория {category}, минимальная площадь {area} кв.м:", max_length=100, truncation=True)[0]['generated_text']
                print(description)

                # Показ ближайших вариантов и объяснений
                for i in closest_indices:
                    reason = generator(f"Объект {i} не полностью соответствует критериям, потому что...", max_length=50, truncation=True)[0]['generated_text']
                    print(f"Вариант {i}: {reason}")
            else:
                print("Не удалось предоставить рекомендации. Попробуйте снова.")

        except ValueError as ve:
            print(f"Ошибка значения: {ve}. Попробуйте снова.")
        except Exception as e:
            print(f"Произошла ошибка: {e}. Попробуйте снова.")

        retry = input("Хотите ввести данные еще раз? (да/нет): ").strip().lower()
        if retry != 'да':
            break

# Запуск интерактивного диалога
interactive_dialog()
