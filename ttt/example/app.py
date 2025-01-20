from litestar import Litestar, get, Response
from litestar.static_files.config import StaticFilesConfig
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
template_loader = FileSystemLoader('templates')
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

# Define a route
@get("/")
async def index() -> Response:
    template = jinja_env.get_template('index.html')
    html_content = template.render(
        title="Table tennis tournament",
        heading="Table tennis tournament",
        message="This view is generated with Litestar and Jinja template. Styled with Bootstrap and zero JavaScript.",
        standings=standings
    )
    return Response(content=html_content, media_type="text/html")

# Create the Litestar app
app = Litestar(route_handlers=[index])