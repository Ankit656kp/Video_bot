import json
import os

DATA_DIR = "data"
USERS_FILE = os.path.join(DATA_DIR, "users.json")
SOURCES_FILE = os.path.join(DATA_DIR, "sources.json")


def load_users():
    if not os.path.exists(USERS_FILE):
        return []
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_user(user):
    users = load_users()
    if user["id"] not in [u["id"] for u in users]:
        users.append(user)
        with open(USERS_FILE, "w") as f:
            json.dump(users, f, indent=2)


def load_sources():
    if not os.path.exists(SOURCES_FILE):
        return []
    with open(SOURCES_FILE, "r") as f:
        return json.load(f)


def add_source(group_id):
    sources = load_sources()
    if group_id not in sources:
        sources.append(group_id)
        with open(SOURCES_FILE, "w") as f:
            json.dump(sources, f, indent=2)


def remove_source(group_id):
    sources = load_sources()
    if group_id in sources:
        sources.remove(group_id)
        with open(SOURCES_FILE, "w") as f:
            json.dump(sources, f, indent=2)