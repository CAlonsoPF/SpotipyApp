# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:28:42 2020

@author: Alonso Pérez
"""

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDFillRoundFlatIconButton, MDIconButton
from kivymd.uix.textfield import MDTextField, MDTextFieldRound
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.card import MDCard
from kivymd.uix.spinner import MDSpinner

import spotipy
from spotipy.oauth2 import SpotifyOAuth 
import random
import webbrowser





class Playlist(object):
    def __init__(self):
        SPOTIPY_CLIENT_ID= '###'
        SPOTIPY_CLIENT_SECRET= '###'
        SPOTIPY_REDIRECT_URI='http://127.0.0.1:8080/'
        scope= 'playlist-modify-public'
       
        self.img='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'
        
        token = SpotifyOAuth(client_id= SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                                  redirect_uri= SPOTIPY_REDIRECT_URI,scope=scope )
                                  
        
        self.spotifyObject = spotipy.Spotify(auth_manager= token )
        self.username = self.spotifyObject.current_user()['uri'].split(':')[-1] #Es un dict, el user name se encuentra en uri y está rodeado de dos puntos (:)
            
        
    def get_playlist_info(self, playlist_name='Playlist.py'):
        """
        Looks for the Playlist.py, if it exists deletes all info inside it and 
        returns the plalist_id.
    
        If it doesn't exist, it creates it
        """
        prePlaylist= self.spotifyObject.user_playlists( user=self.username)
        
        for play_lists in range(len( prePlaylist['items'])): #Looks for playlist
            if prePlaylist['items'][play_lists]['name']==playlist_name:
                playlist_info = prePlaylist['items'][play_lists]['id']
            
            else: 
                playlist_info=self.create_playlist()
            
            return playlist_info
    
    def change_image_playlist(self, image, playlist_info):
        if image==None: image=self.img
        self.spotifyObject.playlist_upload_cover_image(playlist_id=playlist_info, image_b64=image)
        return None
    
    def create_playlist(self, playlist_name='Playlist.py',
                        playlist_description='Mix of your favourite artists '):
        
        prePlaylist= self.spotifyObject.user_playlists(user=self.username)
        
        self.spotifyObject.user_playlist_create(user=self.username, name=playlist_name, 
                                            public=False, description=playlist_description)
        
        playlist_info=prePlaylist['items'][0]['id']
        try:
            self.change_image_playlist(self.img, playlist_info)
        except:
            pass
        return playlist_info

    def get_playlist_image(self, playlist_info):
        return self.spotifyObject.playlist_cover_image(playlist_info)
    
    def playlist_resume(self, playlist_info):
        prePlaylist = self.spotifyObject.playlist_items(playlist_info)
        number_of_songs = prePlaylist['total']
        resume = {'Artists':{}, 'Duration':0 , 'Number of songs': number_of_songs, 'Songs name': []}
        
        for track in range(len(prePlaylist['items'])):
            resume['Duration'] += prePlaylist['items'][track]['track']['duration_ms']
            Song_info = prePlaylist['items'][track]['track']['name'] #+" by "+prePlaylist['items'][track]['track']['artists'][0]['name']
            resume['Songs name'].append(Song_info)
            
            for artist in range(len(prePlaylist['items'][track]['track']['artists'])):
                if prePlaylist['items'][track]['track']['artists'][artist]['name'] in resume['Artists']:
                    resume['Artists'][prePlaylist['items'][track]['track']['artists'][artist]['name']] +=1
                else:
                    resume['Artists'][prePlaylist['items'][track]['track']['artists'][artist]['name']] =1
        
        return resume
                
    
    def clear_playlist(self, playlist_info):
        tracks = self.spotifyObject.user_playlist_tracks(user=self.username, playlist_id=playlist_info)
        tracks_id=[]
        for songs in range(len(tracks['items'])):
            tracks_id.append(tracks['items'][songs]['track']['id'])
        
        self.spotifyObject.user_playlist_remove_all_occurrences_of_tracks(user=self.username, playlist_id=playlist_info, tracks=tracks_id)
        return None

    def get_songs(self, name, n_songs):
        search=self.spotifyObject.search(q=name, limit=50)
        list_of_songs = random.choices(search['tracks']['items'], k=int(n_songs))
        id_songs=[]
    
        print('\nThese are the songs that were found:')
        for track in list_of_songs:
            print(track['name'], " by " ,track['artists'][0]['name'])
            id_songs.append(track['uri'])
    
        return id_songs

    def add_songs_to_playlist(self, id_songs, playlist_info):
        self.spotifyObject.user_playlist_add_tracks(user=self.username, playlist_id=playlist_info, tracks=id_songs)
        return None
    
    
    def get_playlist_link(self, playlist_info):
        """
        Looks for the Playlist.py, if it exists deletes all info inside it and 
        returns the plalist_id.
    
        If it doesn't exist, it creates it
        """
        prePlaylist= self.spotifyObject.user_playlists(user=self.username)
        for play_lists in range(len( prePlaylist['items'])):
            if prePlaylist['items'][play_lists]['id']==playlist_info:
                playlist_link = prePlaylist['items'][play_lists]['external_urls']['spotify']
                return playlist_link
            


KV= '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Playlist.py'
        icon: 'git'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
        

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'My playlist'
            icon: 'music-circle-outline'
            
            MDFillRoundFlatIconButton:
                text: 'Playlist info'
                halign: 'right'
                pos_hint: {"center_x": .5, "center_y": .75}
                hint_size: "20sp"
                icon: 'information-variant'
                on_press: app.info()
            
            MDFillRoundFlatIconButton:
                text: 'Clear playlist'
                halign: 'left'
                hint_size: "20sp"
                icon: 'restart'
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: app.clean_playlist()
            
            MDFillRoundFlatIconButton:
                text: 'Go to playlist'
                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .25}
                hint_size: "20sp"
                icon: 'spotify'
                on_press: app.end()
            

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Modify'
            icon: 'headphones'

            MDFillRoundFlatIconButton:
                text: 'Add songs'
                halign: 'center'
                pos_hint: {"center_x": .5, "center_y": .5}
                hint_size: "20sp"
                line_color: 0, 0, 0, 1
                icon: 'music-note-plus'
                on_press: app.add_songs()
            
            MDIconButton:
                text: 'Hey'
                halign: 'center'
                pos_hint: {"center_x": .1, "center_y": .1}
                icon: 'ufo-outline'
                on_release: app.thanks()

<ThanksBox>
    orientation: "vertical"
    spacing: "10dp"
    size: "60dp", "60dp"
    

        
<AddSongsBox>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "240dp"

    MDTextField:
        hint_text: "Artist Name"
        icon_right: 'artist'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter an artist name"

    MDTextField:
        hint_text: "Album name (optional)"
        icon_right: 'album'
    
    MDTextField:
        hint_text: "Song name (optional)"
        icon_right: 'beats'
    
    MDTextField:
        hint_text: "How many songs (number)"
        icon_right: 'contrast'
        required: True
        helper_text_mode: "on_error"
        helper_text: "Enter a number"
'''


class ThanksBox(BoxLayout):
    pass

class AddSongsBox(BoxLayout):
    pass

class PlaylistApp(MDApp):
    
    def __init__(self):
        super().__init__()
        
        
        self.my_playlist = Playlist()
        self.playlist_info = self.my_playlist.get_playlist_info()
        self.add_songs_dialog = None
        try:
            self.my_playlist.change_image_playlist(None, self.playlist_info)
        except: 
            pass
    
    def build(self):
        self.diag_added = None
        self.thanks_dialog = None
        self.info_dialog = None
        self.theme_cls.primary_palette = "Green"
        return Builder.load_string(KV)
    
    
    def add_songs(self):
        if not self.add_songs_dialog:
            self.add_songs_dialog = MDDialog(
                title="Songs:",
                type="custom",
                content_cls= AddSongsBox(),
                buttons= [MDRaisedButton(
                            text="Add", text_color=[0,0,0,1], 
                            on_release= self.save_songs
                            )
                          ]
                        )
            
        self.add_songs_dialog.set_normal_height()
        self.add_songs_dialog.open()
    
    
    def thanks(self):
        if not self.thanks_dialog:
            self.thanks_dialog = MDDialog(
                title="THANKS FOR USING MY APP!",
                text='Contact info: calonso295@gmail.com\n Twitter: @alonso__95',
                content_cls=ThanksBox(),
                buttons=[MDIconButton(icon="alien-outline",
                                      text_color=[0,0,0,1], 
                                       on_press = self.close_thanks
                               ),
                         ]
                        )
            
        self.thanks_dialog.open()
    
    
    def clean_playlist(self):
        self.info_dialog=None
        self.playlist_info_text='Playlist name: Playlist.py\n\n'
        self.my_playlist.clear_playlist(self.playlist_info)
        Snackbar(text="Playlist empty!!",
                 size_hint_y=.5,
                 size_hint_x=.5).show()
    
    def close_info(self, inst):
        self.info_dialog.dismiss()
        self.info_dialog = None
    
    def close_thanks(self, inst):
        self.thanks_dialog.dismiss()
        self.thanks_dialog = None
            
    
    def info(self):
        self.playlist_info_text='Playlist name: Playlist.py\n\n'
        resume = self.my_playlist.playlist_resume(self.playlist_info)
        
        num_songs = 'Number of songs: '+ str(resume['Number of songs'])+'\n\n'
        self.playlist_info_text+= num_songs
        
        duration = 'Duration: '+str(int(round(resume['Duration']/1000/60/60,0)))+'hrs '+str(int(resume['Duration']/1000/60%60))+'min\n\n'
        self.playlist_info_text+= duration
        
        artists='Artists in this playlist: '
        for art in list(resume['Artists'].keys()):
            txt = art + ' ('+str(resume['Artists'][art])+'), '
            artists+=txt
        
        self.playlist_info_text+=artists
        #playlist_info_text+='\nSongs: '
        #playlist_info_text+= ' || '.join(resume['Songs name'])
        
        
        
        if not self.info_dialog:
            self.info_dialog = MDDialog(
                title="Playlist info",
                text=self.playlist_info_text,
                size= ["120dp", "120dp"],
                buttons=[MDIconButton(icon="donkey",
                                      text_color=[0,0,0,1], 
                                       on_press = self.close_info
                               )
                         ]
                        )
            
        self.info_dialog.open()
        
    
    def end(self):
        print('Done')
        spotify_playlist = self.my_playlist.get_playlist_link( self.playlist_info)
        webbrowser.open(spotify_playlist)
        self.stop()
            
    def save_songs(self, inst):
        self.info_dialog=None
        search = ''
        i=0
        order = ["", '#track:"',' album:"', ' artist:"']
        for obj in self.add_songs_dialog.content_cls.children:
            if isinstance(obj, MDTextField):
                print(obj.text)
                search+=order[i]+obj.text+'"'
                i+=1
                obj.text=''
        
        songs = search.split('"#')
        print(songs)
        
        try:
            id_songs=self.my_playlist.get_songs(songs[1], int(songs[0]))
            self.my_playlist.add_songs_to_playlist(id_songs, self.playlist_info)
            MDDialog(
                    title="Songs added!!",
                    size= ["60dp", "60dp"],
                    buttons=[MDIconButton(icon="hand-okay",
                                  text_color=[0,0,0,1]
                                  )
                             ]
                    ).open()
        
        
        except:
            MDDialog(
                    title="Something went wrong!!\nTry again!",
                    size= ["60dp", "60dp"],
                    buttons=[MDIconButton(icon="emoticon-sad-outline",
                                  text_color=[0,0,0,1]
                                  )
                             ]
                    ).open()

        self.add_songs_dialog.dismiss()







if __name__ == '__main__':
    PlaylistApp().run()
