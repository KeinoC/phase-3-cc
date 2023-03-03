from lib.viewer import Viewer
from lib.movie import Movie


class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating
        
        ##calling adders to initialization of reviews
        self.handle_reviews()

    # rating property goes here!
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, rating):
        if(type(rating) == int and 5 >= rating >= 0):
            self._rating = rating
        else:
            raise Exception("Invalid Rating")


    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer (self, viewer):
        from lib.viewer import Viewer
        if(isinstance(viewer, Viewer)):
            self._viewer = viewer
        else:
            raise Exception("Invalid Viewer.")

    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        from lib.movie import Movie
        if(isinstance(movie, Movie)):
            self._movie = movie
        else:
            raise Exception("Invalid Movie")
        

################# adders

    def handle_reviews(self):
        
        if self._viewer not in self._movie.reviewers:
            self._movie.reviewers.append(self._viewer)

        if self._movie not in self.viewer.reviewed_movies:
            self._viewer.reviewed_movies.append(self._movie)
        
        if self not in self.viewer.reviews:
            self.viewer.reviews.append(self)


