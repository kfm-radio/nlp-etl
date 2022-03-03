__all__ = ["DATABASE_URL", "JOBS"]

import os

# Database settings
DATABASE_URL = os.environ.get("DATABASE_URL")

JOBS = {
    "nlp": [
        "nlp",
    ],
}
