import webbrowser

class Movie:
    def __init__(self,title,duration,poster_image_url,trailer_youtube_url):
        self.title=title
        self.duration=duration
        self.poster_image_url=poster_image_url
        self.trailer_youtube_url=trailer_youtube_url

     # print (self.title)

    def displayCount(self):
        print "Name of Movie is" + self.title

    def displayTrailer(self):
        webbrowser.open(self.trailer_youtube_url)


