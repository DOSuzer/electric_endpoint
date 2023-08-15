# Electric Endpoint
## Описание
Проект эмуляции электросчетчиков для [electric_meter](https://github.com/DOSuzer/electric_meter).
## Запуск проекта
1. клонировать репозиторий
   ```
   git clone git@github.com:DOSuzer/electric_endpoint.git
   ```
2. Cоздать и активировать виртуальное окружение:
   ```
   cd electric_endpoint
   py -3.10 -m venv env
   ```
   ```
   . venv/Scripts/activate - Windows
   . venv/bin/activate     - Linux
   ```
3. Установить зависимости из файла requirements.txt:
   ```
   python -m pip install --upgrade pip
   ```
   ```
   pip install -r requirements.txt
   ```
4. Запустить сервер:
   ```
   uvicorn main:app --reload --port 8001
   ```
