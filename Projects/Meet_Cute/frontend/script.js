const storyForm = document.getElementById("storyForm");
const latestStoryDiv = document.getElementById("latestStory");
const allStoriesDiv = document.getElementById("allStories");

// Load saved stories from localStorage
let allStories = JSON.parse(localStorage.getItem("allStories") || "[]");
displayAllStories(allStories);

storyForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const storyText = document.getElementById("storyText").value;
  const city = document.getElementById("city").value;

  // Generate story title
  const title = generateTitle(storyText, city);
  // Pick a random movie
  const movie = matchMovie();

  const storyData = {
    story_text: storyText,
    city,
    story_title: title,
    matched_movie: movie,
    match_score: Math.floor(Math.random() * 20) + 80,
    match_reason: "A chance encounter followed by a long walk and conversation."
  };

  allStories.push(storyData);
  localStorage.setItem("allStories", JSON.stringify(allStories));

  displayLatestStory(storyData);
  displayAllStories(allStories);

  storyForm.reset();
});

// Title generator logic
function generateTitle(storyText, city) {
  const objects = ["coffee", "croissant", "train", "book", "umbrella", "seat"];
  let foundObject = objects.find(obj => storyText.toLowerCase().includes(obj));
  const templates = [
    "The Last {}",
    "Before the {}",
    "An Ordinary {}",
    "Just One {}",
    "The {} That Started It All"
  ];
  if (foundObject) {
    return templates[Math.floor(Math.random()*templates.length)].replace("{}", capitalize(foundObject));
  } else if (city) {
    return `A Small Moment in ${city}`;
  } else {
    return "An Ordinary Moment";
  }
}

// Movie matcher logic
function matchMovie() {
  const movies = [
    {title: "Before Sunrise", year: 1995},
    {title: "Before Sunset", year: 2004},
    {title: "La La Land", year: 2016},
    {title: "Amélie", year: 2001},
    {title: "Notting Hill", year: 1999},
    {title: "Love Actually", year: 2003},
    {title: "10 Things I Hate About You", year: 1999},
    {title: "Crazy Rich Asians", year: 2018}
  ];
  return movies[Math.floor(Math.random()*movies.length)];
}

// Helpers
function capitalize(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}

function displayLatestStory(story) {
  latestStoryDiv.innerHTML = `
    <div class="story-card">
      <div class="story-title">${story.story_title}</div>
      <div><strong>Story:</strong> ${story.story_text}</div>
      <div><strong>City:</strong> ${story.city || "N/A"}</div>
      <div><strong>Movie:</strong> <span class="movie">${story.matched_movie.title} (${story.matched_movie.year})</span></div>
      <div><strong>Score:</strong> ${story.match_score}</div>
      <div><strong>Reason:</strong> ${story.match_reason}</div>
    </div>
  `;
}

function displayAllStories(stories) {
  allStoriesDiv.innerHTML = stories
    .map(story => `
      <div class="story-card">
        <div class="story-title">${story.story_title}</div>
        <div><strong>Story:</strong> ${story.story_text}</div>
        <div><strong>City:</strong> ${story.city || "N/A"}</div>
        <div><strong>Movie:</strong> <span class="movie">${story.matched_movie.title} (${story.matched_movie.year})</span></div>
        <div><strong>Score:</strong> ${story.match_score}</div>
      </div>
    `)
    .join("");
}
