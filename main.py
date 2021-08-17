import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred

scope = "user-read-recently-played playlist-modify-public playlist-modify-private"


class StoryCreator:



    def __init__(self):
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret=cred.client_secret,
                                                       redirect_uri=cred.redirect_url, scope=scope))

    def get_most_recent(self):
        results = self.sp.current_user_recently_played()
        for idx, item in enumerate(results['items']):
            track = item['track']
            print(idx, track['artists'][0]['name'], " – ", track['name'])


    def search(self, word, limit):
        results = self.sp.search(word, limit+1)['tracks']['items']
        print(self.sp.search(word, limit+1))
        words = list()

        for song in results:
            words.append(song['id'])

        return words


    def search_sentence(self, sentence, new_playlist_name):
        words = sentence.split()
        user_id = self.sp.current_user()['id']
        results = []

        query_length = 0
        for i in range(0, len(words)):
            #word has to contain only itself

            #in
            #if word doesnt exist,
                #increase query string
                #throw error for now
            if (words[i], self.search(words[i], query_length)) in results:
                query_length += 1
                results.append(self.search(words[i], query_length)[query_length])
            else:
                results.append(self.search(words[i], query_length)[query_length])


            #if the song is already present in the list, then take the second option
            #only take songs from certain genre
            #Only take songs from user
        #create playlist
        new_playlist_id = self.sp.user_playlist_create(user_id, new_playlist_name)['id']

        #new_playlist_id = self.sp.playlist_add_items(new_playlist_id, words)
        #add the songs to playlist
        self.sp.playlist_add_items(new_playlist_id, results)

        return results




#storyCreator = StoryCreator()
#storyCreator.get_word_id("word", 1)

#storyCreator.get_most_recent()
#print(storyCreator.search_sentence("There was something unique about them", "meta-story"))





