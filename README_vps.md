# 🌟 JyotishBot для VPS (Ubuntu + systemd)

## Установка

```bash
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install -r requirements.txt
```

## Настройка

- Скопируйте `.env.example` → `.env`
- Впишите токены.

## Systemd автозапуск

1. Поместите `jyotishbot.service` в `/etc/systemd/system/`:

```bash
sudo cp jyotishbot.service /etc/systemd/system/
```

2. Активируйте и запустите:

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable jyotishbot
sudo systemctl start jyotishbot
```
