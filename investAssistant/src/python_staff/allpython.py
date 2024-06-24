import pandas as pd
import spacy
from flask import Flask, request, jsonify
# import openai

# Установите свой API-ключ OpenAI здесь
# openai.api_key = ''

# Загрузка модели spaCy для русского языка
try:
    nlp = spacy.load("ru_core_news_sm")
except OSError:
    from spacy.cli import download
    download("ru_core_news_sm")
    nlp = spacy.load("ru_core_news_sm")

# Загрузка данных из файлов
file1_path = '1.xlsx'
file2_path = '2.xlsx'
file3_path = '3.xlsx'

df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)
df3 = pd.read_excel(file3_path)

# Объединение данных из всех таблиц
df_combined = pd.concat([df1, df2, df3], ignore_index=True)

def get_average_values(data):
    averages = {}
    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            averages[column] = data[column].mean()
    return averages

def filter_objects(data, params):
    filtered_data = data.copy()
    averages = get_average_values(data)

    for key, value in params.items():
        if key in data.columns:
            if pd.api.types.is_numeric_dtype(data[key]):
                if value is not None:
                    filtered_data = filtered_data[filtered_data[key] <= value]
                else:
                    filtered_data[key] = averages[key]
            else:
                if value is not None:
                    filtered_data = filtered_data[filtered_data[key] == value]
                else:
                    filtered_data[key] = 'Да'

    return filtered_data

def extract_parameters(user_input):
    doc = nlp(user_input)
    investment_amount = None
    object_type = None

    for ent in doc.ents:
        if ent.label_ == "MONEY":
            investment_amount = float(ent.text.replace("миллион", "").replace(" ", "")) * 1000000
        elif ent.label_ == "OBJECT_TYPE":
            object_type = ent.text

    return {
        'Минимальная сумма инвестиций': investment_amount,
        'Категория объекта': object_type
    }

def display_object_info(object):
    return {
        "Наименование объекта": object['Наименование объекта'],
        "Расположение": object['Ближайший город'],
        "Количество резидентов": object['Количество резидентов'],
        "Фотографии объекта": object['Фотографии объекта'],
        "Документы по объекту": object['Документы по объекту']
    }

# def get_openai_argumentation(object):
#     prompt = (
#         f"Объект: {object['Наименование объекта']}\n"
#         f"Расположение: {object['Ближайший город']}\n"
#         f"Количество резидентов: {object['Количество резидентов']}\n"
#         f"Почему этот объект идеален для инвестиций?\n"
#     )
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=prompt,
#         max_tokens=150
#     )
#     return response.choices[0].text.strip()

app = Flask(__name__)

@app.route('/api/invest', methods=['POST'])
def invest():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    params = extract_parameters(user_input)
    filtered_objects = filter_objects(df_combined, params)

    if filtered_objects.empty:
        return jsonify({"message": "Нет подходящих объектов по заданным параметрам."})

    used_indices = set()
    while not filtered_objects.empty:
        random_index = filtered_objects.sample(n=1).index[0]
        if random_index not in used_indices:
            used_indices.add(random_index)
            random_object = filtered_objects.loc[random_index]
            object_info = display_object_info(random_object)
            # argumentation = get_openai_argumentation(random_object)
            # object_info["Аргументация"] = argumentation
            return jsonify({"object_info": object_info})
        filtered_objects = filtered_objects.drop(random_index)

if __name__ == '__main__':
    app.run(host='localhost', port=5001)
