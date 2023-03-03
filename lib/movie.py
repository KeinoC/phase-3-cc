class Movie:
    
    all = []

    def __init__(self, title):
        if(type(title) == str and len(title) > 0):
            self.title = title
        else:
            raise Exception("Movie title must be a string")
        
        self.reviews = []
        self.reviewers = []

    # title property goes here!

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title (self, title):
        if (len(title) > 0 and type(title) == str):
            self._title = title
        else:
            raise Exception("Movie title must be a string with at least one character")

    def average_rating(self):
        total_stars = 0
        for movie in self.reviews:
            total_stars += movie.rating
        average = total_stars / len(self.reviews)
        return average


    @classmethod
    def highest_rated(cls):
        top_movie = ""
        for movie in Movie.all_movies:
            if movie.average_rating() > top_movie.average_rating():
                top_movie = movie.title
        return top_movie
