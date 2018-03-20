# Ukulele
# 
# A simple multi-touch ukulele.

from scene import *
import sound
from itertools import chain

key_list=[
'C3','C3#','D3','D3#','E3','F3','F3#','G3','G3#','A3','A3#','B3',
'C4','C4#','D4','D4#','E4','F4','F4#','G4','G4#','A4','A4#','B4']
key_names_piano=['piano:'+key for key in key_list]
class Key (object):
    def __init__(self, frame):
        self.frame = frame
        self.name = None
        self.touch = None
        self.color = (1, 1, 1)
        self.highlight_color = (0.9, 0.9, 0.9)
        
    def hit_test(self, touch):
        return touch.location in self.frame


def set_string_key_names(start_pos,string_key_number):
	   
	   keys_in_string= key_names_piano[start_pos:start_pos+string_key_number]
	   return keys_in_string

class Ukulele (Scene):
    def setup(self):
        self.string_keys = [[],[],[],[]]
        self.string_buttom = [[],[],[],[]]
        self.string_base=[key_names_piano[9],
                          key_names_piano[4],
                          key_names_piano[0],
                          key_names_piano[7]]
        self.string_toplay=[key_names_piano[9],
                          key_names_piano[4],
                          key_names_piano[0],
                          key_names_piano[7]]
        
        # 此处可以修改成4根琴弦
        each_string_key_number= 8
        string4_key_names = set_string_key_names(7,each_string_key_number)                             
        string3_key_names = set_string_key_names(0,each_string_key_number)
        string2_key_names = set_string_key_names(4 ,each_string_key_number)
        string1_key_names = set_string_key_names(9,each_string_key_number)
        string_key_names=[string1_key_names,
                          string2_key_names,
                          string3_key_names,
                          string4_key_names]                     
        key_w = self.size.w/12
        key_h = self.size.h / (each_string_key_number+2)
        string_key_positions=range(each_string_key_number,0,-1)

        for i in range(4):
        	for j in range(each_string_key_number):
        		pos = string_key_positions[j]
        		key = Key(Rect(self.size.w-(i+1)*key_w,(pos+1) * key_h,key_w,key_h))
        		key.name = string_key_names[i][j]
        		self.string_keys[i].append(key)
        		sound.load_effect(key.name)
        		key_buttom=Key(Rect(self.size.w-(i+1)*key_w,0,key_w,key_h))
        		key_buttom.color = [0,0,1]
        		self.string_buttom[i].append(key_buttom)
        
    def draw(self):
        stroke_weight(1)
        stroke(0.5, 0.5, 0.5)

        for i in range(4):
          key_list = chain(self.string_keys[i],self.string_buttom[i])
          for key in key_list:
            if key.touch is not None:
                fill(*key.highlight_color)
            else:
                fill(*key.color)
            rect(*key.frame)

    def touch_began(self, touch):
        for i in range(4):
          for key in self.string_buttom[i]:
            if key.hit_test(touch):
                key.touch = touch
                # 在此处以按键触发了演奏声音
                sound.play_effect(self.string_toplay[i])
          #self.string_toplay[i]=self.string_base[i]
          for key in self.string_keys[i]:
            if key.hit_test(touch):
                key.touch = touch
                self.string_toplay[i]=key.name

    
    def touch_moved(self, touch):
        hit_key = None
        for i in range(4):
          #self.string_toplay[i]=self.string_base[i]  
          for key in self.string_keys[i]:
            hit = key.hit_test(touch)
            if hit and hit_key is None:
                hit_key = key
                if key.touch is None:
                    key.touch = touch
                    #sound.play_effect(key.name)
                    self.string_toplay[i]=key.name
            if key.touch == touch and key is not hit_key:
                key.touch = None
          for key in self.string_buttom[i]:
            hit = key.hit_test(touch)
            if hit and hit_key is None:
                hit_key = key
                if key.touch is None:
                    key.touch = touch
                    sound.play_effect(self.string_toplay[i])
            if key.touch == touch and key is not hit_key:
                key.touch = None
          #hit_key=None    
          
    def touch_ended(self, touch):
        for i in range(4):
          for key in self.string_buttom[i]:
            if key.touch == touch:
                key.touch = None
                
          
          for key in self.string_keys[i]:
            if key.touch == touch:
                key.touch = None
                self.string_toplay[i]=self.string_base[i]
run(Ukulele())
