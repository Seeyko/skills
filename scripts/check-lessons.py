#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

LIMITS = {"topic": 60, "rule": 1000, "when": 200, "why": 400, "check": 300, "source": 200}
TOPIC = re.compile(r"^[a-z][a-z0-9-]*(\.[a-z][a-z0-9-]*)*$")


def problems(path):
    data = json.loads(Path(path).read_text())
    seen = set()
    for lesson in data["lessons"]:
        key = lesson.get("key", "?")
        if key in seen:
            yield f"{key}: clé en double"
        seen.add(key)
        if not TOPIC.match(lesson.get("topic", "")):
            yield f"{key}: topic invalide"
        if not lesson.get("rule"):
            yield f"{key}: rule manquante"
        for field, limit in LIMITS.items():
            if len(lesson.get(field, "")) > limit:
                yield f"{key}: {field} dépasse {limit} caractères"
        if not lesson.get("source", "").startswith(f"playbook:{key}"):
            yield f"{key}: source doit commencer par playbook:{key}"
        if lesson.get("status") not in (None, "active", "retired"):
            yield f"{key}: status inconnu"


if __name__ == "__main__":
    found = list(problems(sys.argv[1] if len(sys.argv) > 1 else "memory/lessons.json"))
    print("\n".join(found) or "lessons.json ok")
    sys.exit(1 if found else 0)
