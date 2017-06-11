import media
import fresh_tomatoes

# A list of movies created by creating objects of the class Movie.
goonies = media.Movie("The Goonies",
                        "http://keyassets-p2.timeincuk.net/wp/prod/wp-content/uploads/sites/30/2014/11/00002a732-TheGooniePoster-300x400.jpg",
                        "https://www.youtube.com/watch?v=5qA2s_Vh0uE")

big_fish = media.Movie("Big Fish",
                        "http://orig04.deviantart.net/b94b/f/2011/283/7/6/big_fish_poster_by_adamrabalais-d4cfntt.jpg",
                        "https://www.youtube.com/watch?v=M3YVTgTl-F0")

harry_sally = media.Movie("When Harry Met Sally",
                        "https://s-media-cache-ak0.pinimg.com/236x/bb/c1/6e/bbc16e53fb10bdbd481dda69667ad910.jpg",
                        "https://www.youtube.com/watch?v=V8DgDmUHVto")

ferris_bueller = media.Movie("Ferris Bueller's Day Off",
                        "http://pillowcinema.com/wp-content/uploads/2015/06/Ferris-Bueller-poster.jpg",
                        "https://www.youtube.com/watch?v=D6gABQFR94U")

jason_and_the_argonauts = media.Movie("Jason and the Argonauts",
                        "http://2.bp.blogspot.com/-q0iJ2XCAt-M/ToErq9sb4ZI/AAAAAAAAAEI/5MsocUfS6Bo/s1600/jason%2Band%2Bthe%2Bargonauts.jpg",
                        "https://www.youtube.com/watch?v=Sg1v5HkpdEA")

forrest_gump = media.Movie("Forrest Gump",
			"https://1.bp.blogspot.com/-_fPu93EHH7I/V0vhv2m9ZtI/AAAAAAABG0k/VrMMAeJ9nVE0-dIv8V_icOlcN_bddMN4wCKgB/s1600/Forrest-Gump-movie_poster.jpg",
                        "https://www.youtube.com/watch?v=eYSnxZKTZzU")

rogue_one = media.Movie("Star Wars: Rogue One",
                        "https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/4f168747265541.58754b3566d88.jpg",
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")

force_awakens = media.Movie("Star Wars: The Force Awakens",
                        "https://s-media-cache-ak0.pinimg.com/originals/9f/fc/d0/9ffcd044545444a62c8ab46eca93154f.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

wonder_woman = media.Movie("Wonder Woman",
                        "http://www.cineavatar.it/wp-content/uploads/2017/05/wonder_woman_ver6.jpg",
                        "https://www.youtube.com/watch?v=1Q8fG0TtVAY")

# A list of movies to be used by fresh_tomatoes to display on the webpage
movies = [goonies, big_fish, harry_sally, ferris_bueller, jason_and_the_argonauts, forrest_gump, rogue_one, force_awakens, wonder_woman]

# Call the open_movies_page method to create the webpage and display the movies on the list
fresh_tomatoes.open_movies_page(movies)
