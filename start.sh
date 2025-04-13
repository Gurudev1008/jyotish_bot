#!/bin/bash

echo "🔁 Запускаю Lava Webhook-сервер..."
nohup python3 lava_webhook.py > webhook.log 2>&1 &

echo "🤖 Запускаю Telegram-бота..."
nohup python3 bot.py > bot.log 2>&1 &
