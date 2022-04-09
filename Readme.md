# Запустить сервер
```bash
docker-compose up -d postgresql  backend traefik # pgadmin
```

## Добавить данные в бд (параллельно с верхней командой)
```bash
docker-compose up preinsert_data
```
