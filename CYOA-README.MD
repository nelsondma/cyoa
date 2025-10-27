# Backend

## Phase 1: Application startup
This stage initializes all the backend system components and connects to the database.


1- We start the backend server by running "uv run main.py" inside the /backend folder. This triggers the execution of main.py

2- main.py first imports all referenced dependencies at the top. Among them we have (a) from core.config import settings... (b)from routers import story, job... and (c)from db.database import create_tables. When the Python interpreter executes main.py, it hits each of these lines, it basically tells Python to "go find the file core/config.py and execute the whole file (a.k.a. module). At the end of that file, there should be an object named settings. Bring that object back" ditto for imports (b) and (c).

3- main.py's "from core.config import settings" triggers the execution of core/config.py.
    3.1 - config.py defines a "Settings" class that inherits from Pydantic's BaseSettings. This class acts as the blueprint, defining the expected name and data type for every configuration variable. Pydantic is a data validation    
     library for Python.By making a class that inherits from pydant's BaseSettings (such as our class "Settings") Pydantic knows to look for a special file named .env in the project root. It then reads the key-value pairs from your 
    .env file (e.g., OPENAI_API_KEY=sk-...) and automatically maps them to the corresponding variables in your Settings class (e.g., OPENAI_API_KEY: str) while also validating the types

4- main.py's "from db.database import create_tables" triggers the execution of db/database.py
    4.1 - database.py uses sqlalchmy to create a SQLite database using python instead of having to write SQL queries. 
    4.2 - database.py uses "engine = create_engine(settings.DATABASE_URL)" to create "the engine" which is a python object that "wraps" around the database. We'll use that wrapper to securely interact with the database.
    4.3 - database.py uses "Base = declarative_base() " to create a special SQLAlchemy object named "Base" which acts as a central registry for all the database tables. Every Model in the models package (e.g., Story, StoryJob)       
    "inherits" from this Base class. Every time you define a Model (like Story or StoryJob) and have it inherit from Base, the Base object automatically registers it on its internal list of tables that need to be created, known as 
    Base.metadata.
    4.4 - database.py defines the create_table() function, with "Base.metadata.create_all(bind=engine)" inside, which uses the Engine's connection to look at all the table blueprints associated with Base.metadata through inheritance 
     and tells the database to physically build those empty tables.

5- main.py then uses create_tables() to create the database tables according to the models we have defined in the models folder

6- main.py then uses app = FastAPI() to create the FastAPI instance that will be used to create the API (a.k.a. the app)

7- main.py then uses app.add_middleware(CORSMiddleware,...) to create the middleware, which is meant to act as a security checkpoint that makes sure any requests coming into the backend from the frontend are truly from my own frontoned and not from some other random website (i.e. some attacker). The "allow_origins=settings.ALLOWED_ORIGINS" line specifies which web addresses are allowed to talk to my API by checking which addresses if authorized in my backend/core/config.py settings class.

8- main.py then uses app.include_router() to indicate to the central FastAPI application what are all the specific URL paths that users can access (aka what are all the different "routes" the suer can take). Remember, using the christmas tree analogy and APIRoute object is a christmas tree and each API endpoint is like a decoration hanging on a branch of the tree. When main.py says "app.include_router(story.router, prefix=settings.API_PREFIX)" it is telling the central FastAPI application of the existence of the APIRoute object "story.router" which in itself contains several API endpoints the central app will be using. Like telling the central app "here, you now have a christmas tree names story.route (APIRoute object) which has several decoration you can use (API endpoints / URL paths)

9- main.py then uses "uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)" as a start button for the web server, finally launching the application and making it available via the network. This code lives inside the following if statement: if __name__ == "__main__". This if statment is known as "the execution guard", its standard practice used in Python to ensure that the server start-up command (uvicorn.run(...)) only executes when you specifically tell the server to run. If another file just wants to import the app object for testing, it avoids accidentally starting the server.