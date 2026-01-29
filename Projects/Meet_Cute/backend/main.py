from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pathlib
from services.title_generator import generate_title
from services.mock import match_movie
# ----- App Setup -----
app = FastAPI()

# Allow JS frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this!
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend folder
frontend_path = pathlib.Path(__file__).parent.parent / "frontend"
app.mount("/static", StaticFiles(directory=frontend_path), name="static")

# ----- Data Storage -----
all_stories = []

# ----- Pydantic model for POST data -----
class StoryInput(BaseModel):
    story_text: str
    city: str | None = None

# ----- Routes -----
@app.get("/", response_class=HTMLResponse)
def read_index():
    """Serve HTML frontend"""
    index_file = frontend_path / "index.html"
    return index_file.read_text()

@app.post("/submit-story")
def submit_story(story: StoryInput):
    """Generate title, match a movie, store story"""
    title = generate_title(story.story_text, story.city)
    movie = match_movie(story.story_text)  # NEW

    story_data = {
        "story_text": story.story_text,
        "city": story.city,
        "story_title": title,
        "matched_movie": movie,  # dynamic movie
        "match_score": random.randint(80, 100),  # optional: random score for fun
        "match_reason": "A chance encounter followed by a long walk and conversation."
    }

    all_stories.append(story_data)
    return story_data


@app.get("/stories")
def get_stories():
    """Return all submitted stories"""
    return {"stories": all_stories}
