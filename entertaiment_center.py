import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story', 'A story of a boy and his toys that come to life', 'https://upload.wikimedia.org/wikipedia/ru/a/a6/Toy_Story_1995_Poster.jpg', 'https://www.youtube.com/watch?v=KYz2wyBy3kc')
#print toy_story.storyline

avatar = media.Movie('Avatar', 'A marine on alien planet', 'https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg', 'https://www.youtube.com/watch?v=5PSNL1qE6VY')
#print avatar.storyline
#avatar.show_trailer()

the_green_mile = media.Movie('The Green Mile', 'A story about innocent prisoner', 'https://upload.wikimedia.org/wikipedia/en/thumb/c/ce/Green_mile.jpg/220px-Green_mile.jpg', 'https://www.youtube.com/watch?v=Ki4haFrqSrw')
#the_green_mile.show_trailer()

terminator_2 = media.Movie('Terminator 2: Judgement Day', 'A story about robot who came in past to save the life of one boy', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/85/Terminator2poster.jpg/220px-Terminator2poster.jpg', 'https://www.youtube.com/watch?v=z6PowtQLGoU')

x_men = media.Movie('X-Men', 'The mutants trying to save the world', 'https://upload.wikimedia.org/wikipedia/en/thumb/8/8c/XMen1poster.jpg/220px-XMen1poster.jpg', 'https://www.youtube.com/watch?v=Iy5R5_T243w')

movies = [toy_story, avatar, the_green_mile, terminator_2, x_men]
fresh_tomatoes.open_movies_page(movies)