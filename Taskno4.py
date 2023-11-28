class MovieRecommendationSystem:

  def __init__(self):
    self.movie_features = {
        1: ['ANIMAL', 'Action'],
        2: ['HARRY POTTER', 'Sci-Fi'],
        3: ['DRISHYAM', 'Crime'],
        4: ['HOUSEFULL', 'Drama'],
        5: ['SINGHAM', 'Drama'],
        6: ['STRANGER THINGS', 'Sci-Fi'],
        7: ['WAR', 'Action'],
        # Add more movies with their genres
    }

  def recommend_movies(self, user_preferences, top_n=2):
    recommended_movies = {}

    for movie_id, features in self.movie_features.items():
      title, genre = features

      if genre in user_preferences:
        if title not in recommended_movies:
          recommended_movies[title] = 0
        recommended_movies[title] += user_preferences[genre]

    sorted_recommendations = sorted(recommended_movies.items(),
                                    key=lambda x: x[1],
                                    reverse=True)[:top_n]

    return sorted_recommendations


def main():
  recommendation_system = MovieRecommendationSystem()

  user_preferences = {
      'Action': 5,
      'Sci-Fi': 4,
      'Drama': 3,
      # Add more user preferences
  }

  recommended_movies = recommendation_system.recommend_movies(user_preferences,
                                                              top_n=3)

  print("Recommended movies based on user preferences:")
  for movie, preference_score in recommended_movies:
    print(f"Movie: {movie}, Preference Score: {preference_score}")


if __name__ == "__main__":
  main()