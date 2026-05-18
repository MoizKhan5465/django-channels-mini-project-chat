# Django Channels WebSocket Mini Project

A small chat application built with Django and Django Channels (WebSockets), demonstrating real-time messaging between clients using Channels, Daphne, and Redis.

## Features

- Real-time chat using WebSocket connections
- Simple room-based chat (room name provided in URL)
- Frontend UI with message bubbles; your messages appear on the right in green, others on the left in white
- Uses Redis as channel layer backing store (local or Docker)

## Project structure

- `Chat/` — Django app with consumer, routing, templates, and views
- `chatwebsocket/` — Django project settings and ASGI entrypoint
- `myenv/` — Python virtual environment (not committed)
- `db.sqlite3` — SQLite database

## Setup (development)

1. Clone the repo:

```bash
git clone https://github.com/MoizKhan5465/django-channels-mini-project-chat.git
cd django-channels-mini-project-chat
```

2. Create and activate a virtual environment (Windows example):

```powershell
python -m venv myenv
myenv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run Redis. Easiest with Docker:

```bash
docker run -d --name my-redis -p 6379:6379 redis
```

Or install Redis locally and ensure it's running on the default port.

5. Apply migrations and create a superuser (optional):

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Run the ASGI server (Daphne):

```bash
daphne chatwebsocket.asgi:application
```

7. Open the chat UI in your browser. Example room URL:

```
http://localhost:8000/chat/friends%20group/
```

The client will open a WebSocket to `ws://<host>/ws/chat/<room>/`.

## Notes

- Room names are accepted with spaces (the routing allows any name without `/`). It's recommended to URL-encode room names (e.g., `friends%20group`) when linking.
- If pushing to GitHub from this machine, make sure `git` is configured with your credentials (HTTPS) or an SSH key is added to your account.

## How I pushed (example)

From the project root:

```bash
git add README.md
git commit -m "Add README"
# If remote origin not set, add it:
# git remote add origin https://github.com/MoizKhan5465/django-channels-mini-project-chat.git
git push origin main
```

If `git push` asks for credentials or fails, follow GitHub hints to authenticate (PAT or SSH key).

---

If you want, I can:
- Normalize room names automatically (replace spaces with `-`) and update the client/consumer accordingly
- Add more setup examples (systemd, Windows service) or a Docker Compose file
- Attempt the git commit & push from this environment now

Tell me which of the above you'd like me to do next.