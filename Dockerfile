# Базовый образ
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем зависимости
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Команда по умолчанию
CMD ["python", "app/main.py"]
