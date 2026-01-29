import random

# A small mock database of movies
MOVIES = [
    {"title": "Before Sunrise", "year": 1995, "keywords": ["train", "vienna", "meeting", "love"]},
    {"title": "Before Sunset", "year": 2004, "keywords": ["paris", "walk", "conversation", "love"]},
    {"title": "Amélie", "year": 2001, "keywords": ["paris", "coffee", "romance", "quirky"]},
    {"title": "Lost in Translation", "year": 2003, "keywords": ["tokyo", "hotel", "lonely", "connection"]},
    {"title": "Midnight in Paris", "year": 2011, "keywords": ["paris", "time travel", "romance"]},
]

def match_movie(story_text: str, city: str | None = None):
    story_text_lower = story_text.lower()
    
    # Score each movie based on keyword matches
    scored_movies = []
    for movie in MOVIES:
        score = 0
        for kw in movie["keywords"]:
            if kw.lower() in story_text_lower:
                score += 25  # arbitrary scoring per match
        if city and city.lower() in [k.lower() for k in movie["keywords"]]:
            score += 25  # extra for city match
        if score > 0:
            scored_movies.append((movie, score))
    
    # Pick the highest scoring movie
    if scored_movies:
        scored_movies.sort(key=lambda x: x[1], reverse=True)
        best_match, best_score = scored_movies[0]
        return {
            "title": best_match["title"],
            "year": best_match["year"],
            "match_score": best_score,
            "match_reason": f"Keywords matched in your story: {', '.join([kw for kw in best_match['keywords'] if kw in story_text_lower])}"
        }
    else:
        # fallback
        return {
            "title": "Some Movie",
            "year": 2000,
            "match_score": 50,
            "match_reason": "Couldn't find a perfect match, but we still wanted to suggest something fun!"
        }
