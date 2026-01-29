@app.post("/submit-story")
def submit_story(story: StoryInput):
    # Generate title
    title = generate_title(story.story_text, story.city)
    
    # Match a movie
    movie_match = match_movie(story.story_text, story.city)
    
    # Build the story object
    story_data = {
        "story_title": title,
        "story_text": story.story_text,
        "city": story.city,
        "matched_movie": {
            "title": movie_match["title"],
            "year": movie_match["year"]
        },
        "match_score": movie_match["match_score"],
        "match_reason": movie_match["match_reason"]
    }
    
    # Save it to the in-memory list
    submitted_stories.append(story_data)
    
    return story_data

#GET/stories will return all submitted storeis in JSON array
@app.get("/stories")
def get_stories():
    return {"stories": submitted_stories}
