# coding=utf-8

import Parcer
import re

parced = Parcer.preInitLevel('..\\res\lvl\\lvl_conf.gen')

'''
!prepare!
bg_color = (255,255,255);
tile_size = (50, 50);
lvl_in_tiles = (20, 20);
tiles_src0 = 'tiles\terrain.jpg';
tiles_src1 = 'tiles\t.jpg';
tiles_in_atlas = (tiles_src1:1,tiles_src0:1);
sprites_src0 = 'sprites\trall.png';
sprites_src1 = 'sprites\trazz.png';
'''

print parced.preread_first().keys()




