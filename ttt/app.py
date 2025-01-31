from litestar import Litestar, get, Response, Request, post
from litestar.static_files.config import StaticFilesConfig
from jinja2 import Environment, FileSystemLoader
from litestar.exceptions import HTTPException, ValidationException
from litestar.status_codes import HTTP_500_INTERNAL_SERVER_ERROR
from litestar.response import Redirect
from pydantic import BaseModel
from utils import schedule_from_players, standings_from_results
import typing as ty

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from database_config import init_db_with_empty_results, Match, MatchSchema

Base = declarative_base()

# Set up Jinja2 environment
template_loader = FileSystemLoader("templates")
jinja_env = Environment(loader=template_loader)

# Sample data for world standings
standings = [
    {"rank": 1, "name": "Fan Zhendong", "country": "China", "points": 15000},
    {"rank": 2, "name": "Ma Long", "country": "China", "points": 14500},
    {"rank": 3, "name": "Xu Xin", "country": "China", "points": 14000},
    {"rank": 4, "name": "Tomokazu Harimoto", "country": "Japan", "points": 13500},
    {"rank": 5, "name": "Hugo Calderano", "country": "Brazil", "points": 13000},
    # Add more players as needed
]

# Create a SQLite database in memory for demonstration purposes
engine = create_engine("sqlite:///ttt.db")

Session = sessionmaker(bind=engine)
session = Session()

players = ["Fan Zhendong", "Ma Long", "Xu Xin", "Tomokazu Harimoto", "Dummy1", "Dummy2", "Dummy3", "Dummy4"]
player_schedule = schedule_from_players(players)
# init_db_with_empty_results(player_schedule)


def app_exception_handler(request: Request, exc: HTTPException) -> Response:
    return Response(
        content={
            "error": "server error",
            "path": request.url.path,
            "detail": exc.detail,
            "status_code": exc.status_code,
        },
        status_code=500,
    )


# Define a route
@get("/")
async def index() -> Response:
    template = jinja_env.get_template("index.html")
    html_content = template.render(
        title="Table tennis tournament",
        heading="Table tennis tournament",
        message="This view is generated with Litestar and Jinja template. Styled with Bootstrap and zero JavaScript.",
        standings=standings,
    )
    return Response(content=html_content, media_type="text/html")


@get("/standings")
async def current_standings() -> Response:
    template = jinja_env.get_template("standings.html")

    all_matches = session.query(Match).all()
    standings = standings_from_results(all_matches, players)

    html_content = template.render(
        title="Current standings",
        heading="Current standings",
        message="Current standings per individual player.",
        standings=standings,
    )
    return Response(content=html_content, media_type="text/html")


# Endpoint for schedule
@get(
    "/schedule",
    exception_handlers={HTTP_500_INTERNAL_SERVER_ERROR: app_exception_handler},
)
async def schedule() -> Response:
    template = jinja_env.get_template("schedule.html")
    results = session.query(Match).all()

    results = [[result.score0, result.score1] for result in results]

    html_content = template.render(
        title="Schedule",
        heading="Schedule",
        message="Schedule for the tournament.",
        schedule=player_schedule,
        results=results,
    )
    return Response(content=html_content, media_type="text/html")


@get("/result/{match_id: int}", exception_handlers={HTTP_500_INTERNAL_SERVER_ERROR: app_exception_handler})
async def result(match_id: int) -> Response:
    template = jinja_env.get_template("result.html")

    result = session.query(Match).filter(Match.id == match_id).all()[0]  # .update({"score0": 2, "score1": 1})

    score = [result.score0, result.score1]
    # print(score)
    # result = "2:1"
    html_content = template.render(
        title="Result",
        heading="Submit result",
        message="Here you can enter the result of the match.",
        match_id=match_id,
        score=score,
    )
    return Response(content=html_content, media_type="text/html")


@post("/enter_result/{match_id: int}", exception_handlers={HTTP_500_INTERNAL_SERVER_ERROR: app_exception_handler})
async def enter_result(match_id: int, request: Request) -> Response:
    # print("Something posted")
    results = await request.form()

    result = (
        session.query(Match)
        .filter(Match.id == match_id)
        .update({"score0": results["result0"], "score1": results["result1"]})
    )

    session.commit()

    return Redirect(path="/schedule")


# Create the Litestar app
app = Litestar(route_handlers=[index, current_standings, schedule, result, enter_result])
