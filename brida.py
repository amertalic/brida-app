from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, StringProperty, NumericProperty
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image
from time import *
import threading
import random
import os
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen

#define our differnet screens
class WelcomeWindow(Screen):
    pass
class InpPlayerWindow(Screen):

    def store_palyers(self):
        #self.ids.input_pl1.text = 'test'
        pl1 = self.ids.input_pl1.text
        pl2 = self.ids.input_pl2.text
        pl3 = self.ids.input_pl3.text
        pl4 = self.ids.input_pl4.text
        pl5 = self.ids.input_pl5.text
        pl6 = self.ids.input_pl6.text
        pl7 = self.ids.input_pl7.text
        pl8 = self.ids.input_pl8.text
        pl9 = self.ids.input_pl9.text
        pl10 = self.ids.input_pl10.text

    def check_and_submit_players(self):
        self.four_players_list()
        if self.four_player_status == True:
            self.six_player_list()
            if self.six_player_status == True:
                self.eight_player_list()
                if self.eight_player_status == True:
                    self.ten_player_list()
        try:
            self.merge_teams_and_players_into_list()
        except:
            pass

    def automate_palyer_input(self):
        #self.ids.input_pl1.text = 'test'
        self.ids.input_pl1.text = 'Sam'
        self.ids.input_pl2.text = 'Ahmed'
        self.ids.input_pl3.text = 'Alex'
        self.ids.input_pl4.text = 'Ivan'
        self.ids.input_pl5.text = 'Hana'
        self.ids.input_pl6.text = 'Daniel'
        self.ids.input_pl7.text = ''
        self.ids.input_pl8.text = ''
        self.ids.input_pl9.text = ''
        self.ids.input_pl10.text = ''

    def four_players_list(self):
        if (self.ids.input_pl1.text and self.ids.input_pl2.text and self.ids.input_pl3.text and self.ids.input_pl4.text) != '':
            self.inp_player_list = [self.ids.input_pl1.text, self.ids.input_pl2.text, self.ids.input_pl3.text, self.ids.input_pl4.text]
            self.four_player_status = True
            self.ids.pl_inp_error_lbl.text = ' 4 players ready\nPress palay to start playing'
        else:
            self.four_player_status = False
            self.ids.pl_inp_error_lbl.text = 'Minimal 4 players required!'

    def six_player_list(self):
        if (self.ids.input_pl5.text and self.ids.input_pl6.text) != '':
            self.inp_player_list.append (self.ids.input_pl5.text)
            self.inp_player_list.append (self.ids.input_pl6.text)
            self.six_player_status = True
        elif (self.ids.input_pl5.text or self.ids.input_pl6.text) != '':
            self.ids.pl_inp_error_lbl.text = 'Player number must be an evan number!\nDelete player 5 or enter player 6'
            self.six_player_status = False
        else:
            self.six_player_status = False
            self.ids.pl_inp_error_lbl.text = ' 4 players ready\nPress play to start playing'

    def eight_player_list(self):
        if (self.ids.input_pl7.text and self.ids.input_pl8.text) != '':
            self.inp_player_list.append (self.ids.input_pl7.text)
            self.inp_player_list.append (self.ids.input_pl8.text)
            self.eight_player_status = True
        elif (self.ids.input_pl7.text or self.ids.input_pl8.text) != '':
            self.ids.pl_inp_error_lbl.text = 'Player number must be an evan number!\nDelete player 7 or enter palyer 8'
            self.eight_player_status = False
        else:
            self.eight_player_status = False
            self.ids.pl_inp_error_lbl.text = '6 players ready\nPress play to start playing'

    def ten_player_list(self):
        if (self.ids.input_pl9.text and self.ids.input_pl10.text) != '':
            self.inp_player_list.append (self.ids.input_pl9.text)
            self.inp_player_list.append (self.ids.input_pl10.text)
            self.ten_player_status = True
        elif (self.ids.input_pl9.text or self.ids.input_pl10.text) != '':
            self.ids.pl_inp_error_lbl.text = 'Player number must be an evan number!\nDelete player 9 or enter palyer 10'
            self.ten_player_status = False
        else:
            self.ten_player_status = False
            self.ids.pl_inp_error_lbl.text = '8 players ready\nPress play to start playing'

    def randomize_players(self):
        try:
            int_list =[]
            list_2 = self.inp_player_list
            while len(list_2) > 0:
                player = random.choice(list_2)
                int_list.append(player)
                list_2.remove(player)
            self.inp_player_list = int_list

            self.ids.input_pl1.text = self.inp_player_list[0]
            self.ids.input_pl2.text = self.inp_player_list[1]
            self.ids.input_pl3.text = self.inp_player_list[2]
            self.ids.input_pl5.text = self.inp_player_list[3]
            try:
                self.ids.input_pl4.text = self.inp_player_list[4]
                self.ids.input_pl6.text = self.inp_player_list[5]
            except:
                pass
            try:
                self.ids.input_pl8.text = self.inp_player_list[6]
                self.ids.input_pl7.text = self.inp_player_list[7]
            except:
                pass
            try:
                self.ids.input_pl9.text = self.inp_player_list[8]
                self.ids.input_pl10.text = self.inp_player_list[9]
            except:
                pass
        except: self.ids.pl_inp_error_lbl.text = 'Error: number of players must be evan\nand in sequential order!'

    def merge_teams_and_players_into_list(self):
        self.team_player_list = []
        list_teams = ['TEAM 1','TEAM 2', 'TEAM 3','TEAM 4','TEAM 5']
        for i in range(int((len(self.inp_player_list))/2)):
            self.team_player_list.append(list_teams[i])
            self.team_player_list.append([self.inp_player_list[i*2], self.inp_player_list[i*2+1]])
        print(self.team_player_list)

class ManualWindow(Screen):
    pass
class GameplayWindow(Screen):
    w_list = ['cresol', 'twelvemonths', 'shedule', 'locution', 'milk-caps', 'microcopy', 'henry fonda', 'Wanderwort', 'synovia', 'leprechaun', 'magnetized', 'clothe', 'undercard', 'pacifications', 'fitty', 'soliform', 'toilet-roll', 'separateth', 'plazas', 'ministery', 'distancers', 'anonymises', 'uncommonness', 'intransigent', 'steam-brake', '2Kinda', 'split-phase', 'slapdash', 'apicoplast', 'grepped', 'sausagefests', 'gynecocratic', 'Digha', 'goldenly', 'slash', 'Canyonlands', 'nongasoline', 'caddish', 'semis', 'Aachen', 'cirripedia', 'comptometers', 'maxim', 'churningly', 'gunny-cloth', 'projection', 'mixin', 'Schiller', 'shriving', 'leidger']
    #izbrisati listu i staviti: player_list = []
    player_list = []
    team_points = {'TEAM 1':0, 'TEAM 2':0, 'TEAM 3':0, 'TEAM 4':0, 'TEAM 5':0}
    team_jokers = {'TEAM 1':3, 'TEAM 2':3, 'TEAM 3':3, 'TEAM 4':3, 'TEAM 5':3}
    circle_counter = 0
    r_counter = 1

    def reset_values(self):
        self.team_jokers = {'TEAM 1':3, 'TEAM 2':3, 'TEAM 3':3, 'TEAM 4':3, 'TEAM 5':3}
        self.team_points = {'TEAM 1':0, 'TEAM 2':0, 'TEAM 3':0, 'TEAM 4':0, 'TEAM 5':0}
        self.grab_player_list()
        self.r_counter = 1


    #grabs the player list from the InpPlayerWindow screen
    #https://stackoverflow.com/questions/41337656/how-to-transfer-a-list-of-element-from-a-screen-to-another-using-kivy
    def grab_player_list(self):
        self.player_list = self.manager.get_screen('input_player').team_player_list
        print(self.player_list)

    def check_winner(self):
        highest = max(self.team_points.values())
        winner_list = [k for k, v in self.team_points.items() if v == highest]
        if highest >= 3:
            if len(winner_list) >1:
                winner_txt = "It's a draw! We have {} winners!!!".format(len(winner_list))
                for i in range(len(winner_list)):
                    winner_txt += '\n{}: {} & {}'.format(winner_list[i], self.player_list[self.player_list.index(winner_list[i])+1][0], self.player_list[self.player_list.index(winner_list[i])+1][1])
                self.ids.label_points.text = winner_txt
                self.reset_values()
            else:
                self.ids.label_points.text = ('WINNEEERR!!!\n{}\n{} & {}'.format(winner_list[0], self.player_list[self.player_list.index(winner_list[0])+1][0], self.player_list[self.player_list.index(winner_list[0])+1][1]))
                self.reset_values()
        else:
            self.r_counter += 1
            print(self.r_counter)
    def full_circle_counter(self):
        if self.circle_counter == len(self.player_list)/2:
            self.check_winner()
            self.circle_counter = 0
            print('loop')
        else:
            self.circle_counter +=1
    def some_func(self):
        script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = "word_lst_en.txt"
        abs_file_path = os.path.join(script_dir, rel_path)

        with open(abs_file_path, 'r') as txt_file:
            list_words = []
            for item in txt_file:
                list_words.append(item.strip())
        self.w_list = list_words

#moves first two positions of the list to the end and the reverses the players
    def move_players(self):
	    self.player_list[1].append(self.player_list[1].pop(0))
	    self.player_list[1].insert(-1, self.player_list[1].pop(0))
	    self.player_list.append(self.player_list.pop(0))
	    self.player_list.append(self.player_list.pop(0))
#chooses a random word from a list and removes it from the list
    def random_word(self):
        self.gues_word = random.choice(self.w_list)
        self.w_list.remove(self.gues_word)
        return self.gues_word
#if correct  calls 2 func:  new word and +1 point.
    def correct(self):
        self.func_link = 'cw'
        self.ids.label_3.text = self.random_word()
        self.point_counter()
        self.display_points()

    def next_word(self):
        self.func_link = 'nw'
        print('labels updatet: gues word')
        self.ids.label_3.text = self.random_word()
        self.point_counter()
        self.display_points()

# if joker used next word appears but no point changes
    def joker(self):
        self.func_link = 'joker'
        if self.team_jokers[self.player_list[0]] > 0:
            self.team_jokers[self.player_list[0]] -= 1
            self.display_points()
        else:
            print('no more jokers left')

    def joker_button(self):
        if self.team_jokers[self.player_list[0]] == 0:
            self.ids.but_1.background_color = 1.0, 0.0, 0.0, 1.0
            self.ids.but_1.text = 'No Jokers\nLEFT'

#resets all values to 0
    def point_counter(self):
        if self.func_link == 'nw':
            self.team_points[self.player_list[0]] -= 1
        else:
            self.team_points[self.player_list[0]] += 1
    #dispalys points, jokers and round
    def display_points(self):
        self.ids.label_points.text = ('Round: '+str(self.r_counter)+'\n'+self.player_list[0]+':\nPoints: ' + str(self.team_points[self.player_list[0]])+'\nJokers: '+str(self.team_jokers[self.player_list[0]]))
        #str(self.team_points[self.player_list[0]])

#Update players on label display
    def display_players(self):
        self.ids.label_1.text = (self.player_list[1][0])
        self.ids.label_2.text = (self.player_list[1][1])

#Button
    def st_round(self):
        if self.circle_counter > 0:
            self.move_players()
        if self.player_list == []:
            self.grab_player_list()
        self.display_players()
        self.ids.label_3.text = 'press start to start\ntimer & get word'
        self.display_points()
        self.full_circle_counter()
        self.some_func()

    def st_play_round(self):
        self.ids.label_3.text = self.random_word()
        self.display_points()
        self.start_timer()

    sec60 = 10
    number = NumericProperty(10)

    # To increase the time / count
    def increment_time(self, interval):
        self.number += -1

    # To start the count
    def start_timer(self):
        Clock.unschedule(self.increment_time)
        Clock.schedule_interval(self.increment_time, 1)
        # To stop the count / time

    def stop_timer(self):
        Clock.unschedule(self.increment_time)

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('brida.kv')

class BridaApp(App):
    def build(self):
        Window.clearcolor =(1,1,1,1)
        Window.size = (280,580)
        return kv

if __name__ == "__main__":
    BridaApp().run()
