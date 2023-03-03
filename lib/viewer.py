class Viewer:


    
    def __init__(self, username):
        if (not isinstance(username, Viewer) and type(username) == str and 16 >= len(username) >= 6):
            self.username = username
        else:
            raise Exception("username must be a string")
        self.reviews = []
        self.reviewed_movies = []
        


    # username property goes here!

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if(not isinstance(username, Viewer) and type(username) == str and 16 >= len(username) >= 6):
            self._username = username
        else:
            raise Exception("Usernames must be unique strings between 6 and 16 characters")


    def reviewed_movie(self, movie):
        if(movie in self.reviewed_movies):
            return True
        else:
            return False

    def rate_movie(self, movie, rating):
        from review import Review
        # if isinstance(movie, Review.movie):
        if movie in self.reviewed_movies:
            self.reviewed_movies.rating = rating
        
        new_review = Review(self, movie, rating)
        if new_review not in self.reviews:
            self.reviews.append(new_review)
        pass