# Jyotish Bot
Телеграм-бот для получения анализа натальной карты через OpenAI и оплату через Lava.

## Запуск:
1. Настройте `.env` на основе `.env.example`.
2. Установите зависимости:
   ```
   pip3 install -r requirements.txt
   ```
3. Инициализируйте базу данных:
   ```
   python3 init_db.py
   ```
4. Запустите сервер:
   ```
   chmod +x start.sh
   ./start.sh
   ```
