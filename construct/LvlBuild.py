# coding=utf-8

import Parcer.readconfig as readconf
import Graphics.BaseObj
import Parcer.CreateTileMap
import Parcer.CreateSpritesOnMap

# Генератор Графики, данный класс читает конфиг и возвращает словари спрайтов и тайлов.
class GenerateGraphics (readconf.ParseLvlConf):

    def __init__(self, lvl_conf):
        super(GenerateGraphics, self).__init__(lvl_conf)

    def create_graphics_tiles(self, key, tile_size):
        tiles_lst = self.tiles_parce(key)
        tiles_variable_dict = {}
        for tileinatlas in tiles_lst.keys():
            tile_atlas = Graphics.BaseObj.ImgEditClass(tiles_lst[tileinatlas][0])
            for k in range(1, len (tiles_lst[tileinatlas]), 1):
                if type(tiles_lst[tileinatlas][k]) is str:
                    tiles_variable_dict [tiles_lst[tileinatlas][k]] = tile_atlas.convert_to_surface()
                elif type(tiles_lst[tileinatlas][k] is tuple):
                    if len(tiles_lst[tileinatlas][k]) == 3:
                        tiles_variable_dict [tiles_lst[tileinatlas][k][0]] = tile_atlas.cut_image(tiles_lst[tileinatlas][k][1], tiles_lst[tileinatlas][k][2], tile_size[0], tile_size[1])
                    else:
                        raise SyntaxError('value must have 2 coors x and y')
        self.tiles = tiles_variable_dict
        return self.tiles

    def create_graphics_sprites (self, key):
        sprites_lst = self.sprites_parce(key)
        sprite_variable_keys = {}
        for keys in sprites_lst.keys():
            spritePic = Graphics.BaseObj.ImgEditClass(sprites_lst[keys][0])
            for count in range(1, len(sprites_lst[keys]),1):
                if type (sprites_lst[keys][count]) is str:
                    sprite_variable_keys[sprites_lst[keys][count]] = spritePic.convert_to_surface()

                elif type (sprites_lst[keys][count]) is tuple:
                    try:
                        sprite_variable_keys [sprites_lst[keys][count][0]] = spritePic.cut_image(sprites_lst[keys][count][1],
                                                                                        sprites_lst[keys][count][2],
                                                                                        sprites_lst[keys][count][3],
                                                                                        sprites_lst[keys][count][4])
                    except:
                        raise SyntaxError ('Bad Description in segment : '+str (sprites_lst[keys][count]))
        self.sprites = sprite_variable_keys
        return self.sprites

# Делает тайловый уровнь, заполняя его объектами staticSprite
class JustDoMyTileLevel  (object):
    def __init__(self, mappath, tilespath):
        self.tiledMapa = Parcer.CreateTileMap.CreateTileMap(mappath).MapaTiles()
        self.generateTiles = GenerateGraphics(tilespath)
    # Заполнение словаря нужной формы
    def DictFillSurfaces(self, wheretiles, oprions_key, tileSize):
        self.generateTiles.tiles_parce(wheretiles)
        self.generateTiles.prepare_oprions(oprions_key)
        surfaces =  self.generateTiles.create_graphics_tiles('tiles', self.generateTiles.options[tileSize])
        mapa_construct = []
        for line in self.tiledMapa:
            line_container = []
            for element in line:
                line_container.append(surfaces[element])
            mapa_construct.append(line_container)
        return mapa_construct
    # Компановка и построение тайлового уровня
    def Build_lvl(self, wheretiles, oprions_key, tileSize):
        mapl = self.DictFillSurfaces(wheretiles, oprions_key, tileSize)
        united = Graphics.BaseObj.UniteSprite()
        heigth = 0
        for line in mapl:
            width = 0
            for item in line:
                sprite = Graphics.BaseObj.StaticSprite (0,0,10,10, '#000000')
                sprite.setSurface(item)
                sprite.rect.x = width
                sprite.rect.y = heigth
                united.add (sprite)
                width += self.generateTiles.options[tileSize][0]
            heigth += self.generateTiles.options[tileSize][1]
        return united

# Расстановка спрайтов. На тайловой карте.
class JustPlaceMySpritesOnLevel (GenerateGraphics):
    def __init__(self, spritepath, sprites ,options):
        super(JustPlaceMySpritesOnLevel, self).__init__(spritepath)
        self.prepare_oprions(options)
        self.sprites_parce(sprites)
        self.create_graphics_sprites(sprites)

    # Указание скоорсти по умолчанию 0, но если вы делаете активные объекты, то скорость необходимо указать
    def PlaceSptites (self, pathsprt, name, sprtClass, speedX=0, speedY=0):
        parced_sprt = Parcer.CreateSpritesOnMap.CreateSptitesOnMap(pathsprt, self.options['tile_size']).sptitedict[name]
        group = Graphics.BaseObj.UniteSprite ()
        for key in parced_sprt.keys():
            for item in parced_sprt[key]:

                created = sprtClass (0, 0, 0, 0, color = '#00FFAA')
                created.rect.x = item[0]
                created.rect.y = item[1]
                created.image = self.sprites[key]
                if hasattr(created, 'setSpeed'):
                    created.setSpeed(speedX, speedY)
                group.add(created)
                
        return group


#print Parcer.CreateSpritesOnMap.CreateSptitesOnMap ('../res/lvl/lvl1_sprt.gen', (50,50)).sptitedict
#staticsprt = Graphics.BaseObj.StaticSprite
#JustPlaceMySpritesOnLevel('../res/lvl/lvl_conf.gen', 'prepare').setStaticSprites('../res/lvl/lvl1_sprt.gen', 'sprites',staticsprt)
#JustDoMyTileDict ('../res/lvl/lvl1.gen', '../res/lvl/lvl_conf.gen').Build_lvl('tiles', 'prepare', 'tile_size')


