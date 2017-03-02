import media
import Fresh_tomatoes


m1 = media.Movie("Avatar", 2000 ,"https://commons.wikimedia.org/wiki/Category:Movie_posters_of_experimental_films#/media/File:Eraserhead.jpg",
                  "https://www.youtube.com/watch?v=5PSNL1qE6VY")



m2 = media.Movie("Aviator", 200 ,"https://commons.wikimedia.org/wiki/Category:Movie_posters_of_experimental_films#/media/File:Man_with_a_movie_camera-1.jpg",
                  "https://www.youtube.com/watch?v=cX0R3mXaod8")


m3 = media.Movie("New moon", 1200 ,"https://commons.wikimedia.org/wiki/Category:Movie_posters_of_experimental_films#/media/File:File_Ce_qui_me_perd_me_sauvera_ver1.jpg",
                  "https://www.youtube.com/watch?v=cX0R3mXaod8")


m4 = media.Movie("First laugh", 500 ,"https://commons.wikimedia.org/wiki/Category:Movie_posters_of_experimental_films#/media/File:Man_with_a_movie_camera-1.jpg",
                  "https://www.youtube.com/watch?v=cX0R3mXaod8")
#"This would create second object of Employee class"
#emp2 = Employee("Manni", 5000)
#m1.displayCount()
#m1.displayTrailer()
#print m1.trailer_youtube_url
movies_list=[m1,m2,m3,m4]
Fresh_tomatoes.open_movies_page(movies_list)