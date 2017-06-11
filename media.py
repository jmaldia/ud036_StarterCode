# This file defines the class Movie that contains the attributes that a movie object needs. It helps stores movie related information. 

class Movie():
	# Constructor for Movie class. Initializes the variables needed to instantiate an object. 
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
