import media
import fresh_tomatoes


mississippi_grind = media.Movie('Mississippi Grind',
                        'Down on his luck, Gerry teams up with younger poker player in an attempt to change'
                        'his luck. The two set off on a road trip through the South.',
                        r'https://trailers.apple.com/trailers/independent/mississippigrind/images/poster-large.jpg?lastmod=1',
                        r'https://www.youtube.com/watch?v=Ooca5idaNSk',
                        'Blackjack'
                        )

the_divine_move = media.Movie('The Divine Move',
                              'A professional baduk (go) player infiltrates his local underground gambling scene to avenge his brother\'s death.',
                              r'https://lh3.googleusercontent.com/-K8yfS9t7Qfs/VVmTknDQOyI/AAAAAAAAABs/7XV5ZIZNQuQ/s0/The_Divine_Move.jpg',
                              r'https://www.youtube.com/watch?v=cNe2QKOYqjU',
                              'Go'
                              )

owning_mahowny = media.Movie('Owning Mahowny',
                             'A bank manager with a gambling problem and access to a multimillion dollar account gets into a messy situation.'
                             'in the largest bank fraud in Canadian history.',
                             r'http://images.moviepostershop.com/owning-mahowny-movie-poster-2003-1020230351.jpg',
                             r'https://www.youtube.com/watch?v=YH8mh8e8L_c',
                             'Craps'
                             )

rounders = media.Movie('Rounders',
                       'A young man is a reformed gambler who must return to playing big stakes poker to help a friend pay off loan sharks.',
                       r'http://www.flickeringmyth.com/wp-content/uploads/2014/08/Rounders-movie-poster-1020349804.jpg',
                       r'https://www.youtube.com/watch?v=-Qv4K-4-FZM',
                       'Poker'
                       )

god_of_gamblers = media.Movie('God of Gamblers',
                              'A master gambler loses his memory, and is befriended by a street hustler who discovers his supernatural gambling abilities.',
                              r'http://ilarge.lisimg.com/image/4859588/953full-god-of-gamblers-poster.jpg',
                              r'https://www.youtube.com/watch?v=4o6y0g8adho',
                              'Mahjong'
                              )

casino_royale = media.Movie('Casino Royale',
                             'James Bond must defeat a weapons dealer in a high stakes game of poker at Casino Royale,'
                             ' but things are not what they seem..',
                             r'http://wdl.tmimgcdn.com/img_articles/10365/_casino-royale-final.jpg',
                             r'https://www.youtube.com/watch?v=xK7PbujRUOk',
                            'Poker'
                            )

movies = [mississippi_grind, the_divine_move, owning_mahowny, rounders, god_of_gamblers, casino_royale]

fresh_tomatoes.open_movies_page(movies)