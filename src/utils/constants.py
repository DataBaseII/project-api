# Database
from sre_constants import CATEGORY


DB_URI = "mongodb://localhost/ProjectDB"

# Endpoints
API = "/api"
V1 = "/v1"
ID = "/<id>"

USERS_PATH = API + V1 + "/users"
MOVIES_PATH = API + V1 + "/movies"
CATEGORIES_PATH = API + V1 + "/categories"

# Codes
ERROR_CODE = 404
CREATED_CODE = 201
OK = 200
