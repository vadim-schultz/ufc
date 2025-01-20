Table Tennis Tournament (TTT)
-----------------------------

Let's build an app to facilitate the company-wide TTT. Here are the proposed steps, as well as technologies used to implement them [in square brackets].

# Back end [Litestar]

## Implement the following routes

- individual player standing
- current ranking across all players
- past matches
- table reservation / scheduling for future matches

## Additional logic

- random matching of 4 players
- play-offs -- limit the number to X (e.g. 10)
- stretch goal: quarter-, semi-, and finals

# Database [SQLAlchemy, Pydantic, SQLite, PostgreSQL]

- define SQLAlchemy schemata
- define Pydantic models for input validation
- integrate with the backend

# Front-end [Jinja, CSS]

- server-side generation with jinja templates and Bootstrap CSS library

# Deployment [Docker, Kubernetes]

- DB container
- web app