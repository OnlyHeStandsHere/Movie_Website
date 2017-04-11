###########################################################
# Udacity Full Stack Nanodegree Project 1 - Movie Website
# Name: Jesse Maitland
# Date: 2017-April-08
#
# Operation
#   1. Make a 6 movie objects
#   2. Add the 6 movie objects to a list
#   3. Pass the list of movie objects to fresh tomatoes for rendering in web browser
#   4. Enjoy some movie trailers!
###########################################################

import fresh_tomatoes   #from Udacity, used to create and display webpage
import movie

#Make some movies
ghost_in_the_shell = movie.Movie('Ghost in the Shell',
                                 '1h 47min',
                                 'In the near future, Major is the first of her kind: '
                                 'A human saved from a terrible crash, who is cyber-enhanced',
                                 'Sci-Fi',
                                 'https://images-na.ssl-images-amazon.com/images/M/MV5BMzJiNTI3MjItMGJiMy00YzA1LTg2MTItZmE1ZmRhOWQ0NGY1XkEyXkFqcGdeQXVyOTk4MTM0NQ@@._V1_SY1000_CR0,0,675,1000_AL_.jpg',
                                 'https://www.youtube.com/watch?v=G4VmJcZR0Yg',
                                 'PG-13')

alien_covenant = movie.Movie('Alien Covenant',
                             '2h 3min',
                             'The crew of the colony ship Covenant, bound '
                             'for a remote planet on the far side of the galaxy, '
                             'discovers what they think is an uncharted paradise.',
                             'Sci-Fi Thriller',
                             'https://images-na.ssl-images-amazon.com/images/M/MV5BNzI5MzM3MzkxNF5BMl5BanBnXkFtZTgwOTkyMjI4MTI@._V1_SY1000_CR0,0,673,1000_AL_.jpg',
                             'https://www.youtube.com/watch?v=H0VW6sg50Pk',
                             'R')

blade_runner = movie.Movie('Blade Runner 2049',
                           '1h 47min',
                           'Thirty years after the events of the first film, a new blade runner, '
                           'LAPD Officer K (Ryan Gosling), unearths a long-buried secret',
                           'Sci-Fi',
                           'https://images-na.ssl-images-amazon.com/images/M/MV5BNDIxMDE3NzcxN15BMl5BanBnXkFtZTgwNzQyMzE5MDI@._V1_.jpg',
                           'https://www.youtube.com/watch?v=6T2b0mp2hco',
                           'R')

guardians_of_the_galaxy2 = movie.Movie('Guardians of the Galaxy Vol.2',
                                       '2h 12min',
                                       'Set to the backdrop of Awesome Mixtape #2, '
                                       'Guardians of the Galaxy Vol. 2 continues the team''s '
                                       'adventures as they unravel the mystery of Peter Quill''s true parentage.',
                                       'Sci-Fi',
                                       'https://images-na.ssl-images-amazon.com/images/M/MV5BMTg2MzI1MTg3OF5BMl5BanBnXkFtZTgwNTU3NDA2MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                                       'https://www.youtube.com/watch?v=2cv2ueYnKjg',
                                       'PG-13')

wonder_woman = movie.Movie('Wonder Woman',
                           '2h',
                           'Before she was Wonder Woman she was Diana, princess of the Amazons, '
                           'trained warrior. When a pilot crashes and tells of conflict in the outside world, '
                           'she leaves home to fight a war to end all wars, '
                           'discovering her full powers and true destiny. ',
                           'Adventure, Fantasy',
                           'https://images-na.ssl-images-amazon.com/images/M/MV5BNDFmZjgyMTEtYTk5MC00NmY0LWJhZjktOWY2MzI5YjkzODNlXkEyXkFqcGdeQXVyMDA4NzMyOA@@._V1_SY1000_SX675_AL_.jpg',
                           'https://www.youtube.com/watch?v=5lGoQhFb4NM',
                           'PG-13')

the_circle = movie.Movie('The Circle',
                         '1h 50min',
                         'A woman lands a dream job at a powerful tech company called the Circle, only to uncover a nefarious agenda that will affect the lives of her friends, family and that of humanity. ',
                         'Drama, Sci-Fi',
                         'https://images-na.ssl-images-amazon.com/images/M/MV5BMjY2OTM2Njc3Ml5BMl5BanBnXkFtZTgwNDgzODU3MTI@._V1_SY1000_CR0,0,674,1000_AL_.jpg',
                         'https://www.youtube.com/watch?v=GxEzUgoCF3w',
                         'PG-13')

#Add movies to a list
movies = [ghost_in_the_shell, alien_covenant, blade_runner, guardians_of_the_galaxy2, wonder_woman, the_circle]

#render movies website
fresh_tomatoes.open_movies_page(movies)

