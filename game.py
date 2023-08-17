import pygame
import sys
import random

pygame.init()

size = (1200, 800)
screen = pygame.display.set_mode(size)

original_positions = [[10, 10], [10, 110], [10, 210], [10, 310]]

playlist = ['mus/track1.mp3', 'mus/track2.mp3', 'mus/track3.mp3']
pygame.mixer.init()



elements = [
    {"name": "earth", "image": pygame.image.load('elements/earth.png'), "pos": [50, 50], "dragging": False, "origin": True},
    {"name": "water", "image": pygame.image.load('elements/water.png'), "pos": [200, 50], "dragging": False, "origin": True},
    {"name": "air", "image": pygame.image.load('elements/air.png'), "pos": [50, 200], "dragging": False, "origin": True},
    {"name": "fire", "image": pygame.image.load('elements/fire.png'), "pos": [200, 200], "dragging": False, "origin": True},
]

combinations = {
    ('earth', 'air'): 'dust',
    ('earth', 'fire'): 'lava',
    ('earth', 'water'): 'mud',
    ('air', 'fire'): 'energy',
    ('air', 'water'): 'rain',
    ('fire', 'water'): 'steam',
    ('energy', 'water'): 'electricity',
    ('lava', 'air'): 'stone',
    ('stone', 'air'): 'sand',
    ('sand', 'fire'): 'glass', 
    ('glass', 'sand'): 'time',
    ('water', 'water'): 'puddle',
    ('water', 'puddle'): 'pond',
    ('water', 'pond'): 'lake',
    ('water', 'lake'): 'sea',
    ('water', 'sea'): 'ocean',
    ('lava', 'sea'): 'primordialsoup',
    ('lava', 'earth'): 'volcano',
    ('volcano', 'primordialsoup'): 'life',
    ('earth', 'life'): 'soil',
    ('soil', 'life'): 'plant',
    ('time', 'life'): 'human',
    ('human', 'stone'): 'tool',
    ('human', 'metal'): 'armor',
    ('human', 'human'): 'love',
    ('human', 'earth'): 'farmer',
    ('farmer', 'plant'): 'wheat',
    ('wheat', 'stone'): 'flour',
    ('flour', 'water'): 'dough',
    ('dough', 'fire'): 'bread',
    ('bread', 'human'): 'baker',
    ('human', 'tool'): 'engineer',
    ('engineer', 'metal'): 'machine',
    ('machine', 'bread'): 'toaster',
    ('love', 'time'): 'life',
    ('life', 'stone'): 'egg',
    ('egg', 'sand'): 'turtle',
    ('turtle', 'earth'): 'beach',
    ('beach', 'water'): 'ocean',
    ('ocean', 'volcano'): 'island',
    ('island', 'ocean'): 'archipelago',
    ('island', 'animal'): 'wildanimal',
    ('wildanimal', 'water'): 'shark',
    ('shark', 'human'): 'blood',
    ('blood', 'human'): 'vampire',
    ('vampire', 'human'): 'corpse',
    ('corpse', 'life'): 'zombie',
    ('zombie', 'human'): 'zombie',
    ('zombie', 'corpse'): 'ghost',
    ('ghost', 'time'): 'history',
    ('history', 'time'): 'century',
    ('century', 'century'): 'millennium',
    ('millennium', 'time'): 'eternity',
    ('continent', 'continent'): 'planet',
    ('planet', 'planet'): 'solarsystem',
    ('solarsystem', 'solarsystem'): 'galaxy',
    ('galaxy', 'galaxy'): 'galaxycluster',
    ('galaxycluster', 'galaxycluster'): 'universe',
    ('eternity', 'universe'): 'infinity',
    ('fire', 'planet'): 'sun',
    ('air', 'planet'): 'atmosphere',
    ('sun', 'atmosphere'): 'sky',
    ('sun', 'atmosphere'): 'aurora',
    ('sky', 'solarsystem'): 'space', 
    ('infinity', 'space'): 'blackhole',
    ('blackhole', 'sun'): 'supernova',
    ('supernova', 'supernova'): 'hypernova',
    ('hypernova', 'time'): 'bigbang',
    ('atmosphere', 'water'): 'cloud',
    ('sky', 'cloud'): 'storm',
    ('storm', 'energy'): 'thunder',
    ('thunder', 'metal'): 'electricity',
    ('electricity', 'wire'): 'circuit',
    ('circuit', 'metal'): 'computer',
    ('computer', 'human'): 'cyborg',
    ('cyborg', 'time'): 'android',
    ('android', 'space'): 'astronaut',
    ('stone', 'planet'): 'moon',
    ('astronaut', 'moon'): 'spacestation',
    ('atmosphere', 'metal'): 'rocket',
    ('spacestation', 'rocket'): 'spaceship',
    ('spaceship', 'planet'): 'solarsystem',
    ('galaxycluster', 'universe'): 'multiverse',
    ('multiverse', 'time'): 'timetravel',
    ('life', 'fire'): 'phoenix',
    ('phoenix', 'phoenix'): 'egg',
    ('wall', 'wall'): 'house',
    ('metal', 'earth'): 'plow',
    ('plow', 'earth'): 'field',
    ('field', 'house'): 'barn',
    ('barn', 'egg'): 'chicken',
    ('chicken', 'egg'): 'philosophy',
    ('philosophy', 'planet'): 'big',
    ('life', 'land'): 'animal',
    ('animal', 'stone'): 'lizard',
    ('big', 'lizard'): 'dinosaur',
    ('dinosaur', 'air'): 'pterodactyl',
    ('dinosaur', 'blood'): 'tyrannosaurusrex',
    ('dinosaur', 'earth'): 'fossil',
    ('fossil', 'human'): 'paleontologist',
    ('timetravel', 'dinosaur'): 'jurassicpark',
    ('jurassicpark', 'volcano'): 'idea',
    ('life', 'fire'): 'phoenix',
    ('plant', 'big'): 'tree',
    ('tool', 'tree'): 'wood',
    ('fire', 'wood'): 'campfire',
    ('human', 'campfire'): 'story',
    ('idea', 'story'): 'detective',
    ('detective', 'murder'): 'investigation',
    ('human', 'universe'): 'science',
    ('investigation', 'science'): 'research',
    ('research', 'life'): 'biology',
    ('biology', 'earth'): 'evolution',
    ('evolution', 'egg'): 'bird',
    ('bird', 'beach'): 'seagull',
    ('animal', 'ocean'): 'fish',
    ('seagull', 'fish'): 'hunting',
    ('hunting', 'human'): 'hunter',
    ('gunpowder', 'metal'): 'bullet',
    ('bullet', 'metal'): 'gun',
    ('hunter', 'gun'): 'shooting',
    ('sky', 'moon'): 'night',
    ('sky', 'night'): 'star',
    ('shooting', 'star'): 'meteor',
    ('meteor', 'atmosphere'): 'meteoroid',
    ('meteoroid', 'earth'): 'meteorite',
    ('life', 'mud'): 'bacteria',
    ('meteorite', 'bacteria'): 'alien',
    ('alien', 'planet'): 'extraterrestriallife',
    ('extraterrestriallife', 'space'): 'ufo',
    ('animal', 'field'): 'livestock',
    ('field', 'livestock'): 'cow',
    ('ufo', 'cow'): 'abduction',
    ('abduction', 'idea'): 'x-files',
    ('x-files', 'story'): 'conspiracy',
    ('glass', 'glass'): 'glasses',
    ('glasses', 'human'): 'hacker',
    ('hacker', 'tool'): 'computer',
    ('conspiracy', 'computer'): 'darkweb',
    ('hacker', 'bank'): 'cybercrime',
    ('air', 'air'): 'pressure',
    ('air', 'pressure'): 'wind',
    ('wind', 'science'): 'motion',
    ('tool', 'motion'): 'wheel',
    ('metal', 'wheel'): 'car',
    ('big', 'car'): 'bus',
}

new_elements = []
created_elements = set()
menu_elements = []

def play_next_song(playlist):
    pygame.mixer.music.load(playlist.pop(0))  # Load the first song
    pygame.mixer.music.play(0)  # Play the song

    # When the song ends, call play_next_song with the rest of the playlist
    pygame.mixer.music.set_endevent(pygame.USEREVENT)


def draw_element(element):
    screen.blit(element["image"], element["pos"])

def is_position_valid(pos, elements):
    for element in elements:
        if pygame.Rect(*pos, 64, 64).colliderect(pygame.Rect(*element['pos'], 64, 64)):
            return False
    return True

def generate_valid_position(elements):
    for _ in range(1000):
        new_pos = [random.randint(0, size[0]-64), random.randint(0, size[1]-64)]
        if is_position_valid(new_pos, elements):
            return new_pos
    print("No valid position found for new element!")
    return None

held_element = None
delete_mode = False
font = pygame.font.Font(None, 36)
total_elements = 145
found_elements = 4
play_next_song(playlist)

while True:
    screen.fill((48, 25, 52))
    text = font.render('Press D for delete mode', True, (255, 255, 255))  # Create a text surface
    text_rect = text.get_rect()
    text_rect.bottomright = (size[0] - 10, size[1] - 10)  # Set the position of the text
    screen.blit(text, text_rect)  # Blit the text onto the screen
    
    counter_text = f"Elements Found: {found_elements}/{total_elements}"
    counter_surface = font.render(counter_text, True, (255, 255, 255))  # RGB color for white
    counter_rect = counter_surface.get_rect()
    counter_rect.bottomright = (size[0] - 10, size[1] - 50)  # Set the position of the counter
    screen.blit(counter_surface, counter_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            if len(playlist) > 0:  # If there are more songs in the playlist
                play_next_song(playlist)
            else:
                pygame.mixer.music.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:  # if "d" key is pressed
                delete_mode = not delete_mode 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button.
                for i, element in enumerate(menu_elements):
                    menu_pos = (10 + i * 70, 10)
                    if pygame.Rect(menu_pos, (64, 64)).collidepoint(event.pos):
                        new_element = element.copy()
                        new_element["dragging"] = True
                        new_element["pos"] = list(event.pos)
                        new_elements.append(new_element)
                        held_element = new_element
                        break
                else:
                    for element in elements + new_elements:
                        if element["image"].get_rect(topleft=element["pos"]).collidepoint(event.pos):
                            if delete_mode:  # if we're in delete mode, remove the element and break the loop
                                if element in elements:
                                    elements.remove(element)
                                else:
                                    new_elements.remove(element)
                                break
                            if "origin" in element and element["origin"]:
                                held_element = element.copy()
                                held_element["origin"] = False
                                held_element["dragging"] = True
                                new_elements.append(held_element)
                            else:
                                held_element = element
                                held_element["dragging"] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button.
                if held_element:
                    held_element["dragging"] = False
                for i, element1 in enumerate(elements + new_elements):
                    if element1 is held_element:
                        for j, element2 in enumerate(elements + new_elements):
                            if i != j:
                                if element1["image"].get_rect(topleft=element1["pos"]).colliderect(element2["image"].get_rect(topleft=element2["pos"])):
                                    combination = combinations.get((element1["name"], element2["name"])) or combinations.get((element2["name"], element1["name"]))
                                    if combination and combination not in created_elements:
                                        new_pos = generate_valid_position(elements + new_elements)
                                        found_elements += 1
                                        if new_pos is None:
                                            continue
                                        new_element = {"name": combination, "image": pygame.image.load(f'elements/{combination}.png'), "pos": new_pos, "dragging": False}
                                        new_elements.append(new_element)
                                        menu_elements.append(new_element.copy())
                                        created_elements.add(combination)
                                        print(f"New element created: {combination}")
                                        if element1["dragging"]:
                                            new_elements.remove(element1)
                                        if element2["dragging"]:
                                            new_elements.remove(element2)
                                    elif not combination:
                                        print(f"Not a valid combination: {element1['name']}, {element2['name']}")
                                        if element1["dragging"]:
                                            new_elements.remove(element1)
                                        if element2["dragging"]:
                                            new_elements.remove(element2)
                held_element = None
        elif event.type == pygame.MOUSEMOTION:
            if held_element:
                held_element["pos"] = list(event.pos)
    
    for element in elements + new_elements:
        draw_element(element)
    for i, element in enumerate(menu_elements):
        menu_pos = (10 + i * 70, 10)
        screen.blit(element["image"], menu_pos)
    pygame.display.flip()

