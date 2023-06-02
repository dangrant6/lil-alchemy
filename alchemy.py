import pygame
import sys
sidebar_rect = pygame.Rect(900, 0, 200, 800)

class Element:
    def __init__(self, name, image_path, position, unlocked):
        self.name = name
        self.image_path = image_path
        self.image = pygame.image.load(image_path)
        self.position = position
        self.dragging = False
        self.unlocked = unlocked
        self.sidebar_position = None
        self.sidebar_rect = None
        #self.rect = pygame.Rect((0, 0), (element_size, element_size))
        #self.rect = pygame.Rect(position, self.image.get_size())

    def copy(self):
        mouse_position = pygame.mouse.get_pos()
        return Element(self.name, self.image_path, mouse_position, True)

    def draw(self, screen):
        '''
        screen.blit(self.image, self.position)
        self.rect = pygame.Rect(self.position, self.image.get_size())
        '''
        pygame.draw.rect(screen, self.color, self.rect)

    def draw_in_sidebar(self, screen, position):
        if self.unlocked:
            self.sidebar_rect = pygame.Rect(position, (60, 60))
            screen.blit(self.image, position)

    def handle_event(self, event, scroll_offset):
        if event.type == pygame.MOUSEBUTTONDOWN:
            new_elements = []
            print("Mouse button down event...")
            x, y = event.pos
            for ele in elements:
                print("Checking element: ", ele.name)
                if ele.unlocked and ele.sidebar_rect.collidepoint(x, y):
                    # Handle the sidebar click
                    ele.handle_sidebar_click()
                    break
                if ele.rect.collidepoint(x, y):
                    # Handle the grid click
                    ele.handle_click()
                    break
                elements.extend(new_elements)
            if event.button == 1:
                if self.image.get_rect(topleft=self.position).collidepoint(event.pos):
                    self.dragging = True
            elif event.button == 4:  # scroll up
                scroll_offset = min(scroll_offset + 20, 0)
            elif event.button == 5:  # scroll down
                scroll_offset = max(scroll_offset - 20, -len(elements) * 60 + sidebar_rect.height)

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.position = list(event.pos)

        return scroll_offset
    
    def handle_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.dragging = True

    # More methods for handling interactions with other elements...
class ScrollBar:
    def __init__(self, position, height):
        self.position = position
        self.height = height
        self.dragging = False
        self.handle_position = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), (*self.position, 20, self.height), 2)
        pygame.draw.rect(screen, (150, 150, 150), (self.position[0], self.position[1] + self.handle_position, 20, 60))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(self.position, (20, self.height)).collidepoint(event.pos):
                self.dragging = True

        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.handle_position = max(0, min(self.height - 60, event.pos[1] - self.position[1]))

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.dragging = False

    def get_offset(self):
        return self.handle_position / (self.height - 60) * (len(elements) * 60 - sidebar_rect.height)
'''
elements = [
    'Earth', 'Air', 'Fire', 'Water', 'Acid', 'Airplane', 'AlarmClock', 'Alcohol', 
    'Algae', 'Alien', 'Allergy', 'Alpaca', 'Ambulance', 'Angel', 'Ant', 'Antarctica', 
    'Aquarium', 'Archipelago', 'Armadillo', 'Armor', 'Astronaut', 'Atmosphere', 'Aurora', 
    'Axe', 'Bacon', 'Bacteria', 'Baker', 'Bakery', 'Banana', 'BananaBread', 'Bank', 
    'Barn', 'Basilisk', 'Bat', 'Batter', 'Battery', 'Beach', 'Bear', 'Beaver', 
    'Bee', 'Beehive', 'Beer', 'Bicycle', 'Bird', 'Birdhouse', 'BlackHole', 'Blade', 
    'Blender', 'Blizzard', 'Boat', 'Boiler', 'Bone', 'BonsaiTree', 'Book', 'Bread', 
    'Brick', 'Bridge', 'Broom', 'Bucket', 'Butterfly', 'Cactus', 'Cake', 'Camel', 
    'Candle', 'CandyCane', 'Cannon', 'Car', 'Caramel', 'CarbonDioxide', 'Carrot', 'Castle', 
    'Cat', 'Cauldron', 'Caviar', 'Cement', 'Centaur', 'Ceramics', 'Chainsaw', 'Chair', 
    'Chameleon', 'Charcoal', 'Cheese', 'Chicken', 'ChickenSoup', 'Chimney', 'ChristmasStocking', 'ChristmasTree', 
    'Cigarette', 'City', 'Clay', 'Clock', 'Cloud', 'Coal', 'Coconut', 'Coffee', 
    'Comet', 'Computer', 'Confetti', 'Cookie', 'CookieDough', 'CookingOil', 'Corpse', 'Cotton', 
    'Cow', 'Crab', 'Crocodile', 'Crow', 'Crown', 'CrystalBall', 'Cuckoo', 'Cup', 
    'Cupcake', 'Cyclops', 'Daisy', 'Dam', 'Desert', 'Dew', 'Diamond', 'Dinosaur', 
    'Dog', 'Dolphin', 'Donkey', 'Dough', 'Dragon', 'Drone', 'Duck', 'Dune', 
    'Dust', 'Dynamite', 'Eagle', 'Earthquake', 'Eclipse', 'Egg', 'ElectricEel', 'Electricity', 
    'Elephant', 'Elf', 'Energy', 'Engineer', 'Eruption', 'Explosion', 'Extinguisher', 'Fabric', 
    'Fairy', 'FairyTale', 'Family', 'Farm', 'Farmer', 'Fence', 'Ferret', 'FerrisWheel', 
    'FiberOptics', 'Field', 'FireExtinguisher', 'Firefighter', 'Fireplace', 'Firework', 'Fish', 'FishAndChips', 
    'FishTank', 'FishingRod', 'Flamethrower', 'Flamingo', 'Flashlight', 'Flood', 'Flour', 'Flower', 
    'Flute', 'Fly', 'FlyingFish', 'FlyingSquirrel', 'Fog', 'Forest', 'Fossil', 'Fountain', 
    'Fox', 'Frog', 'Fruit', 'FruitTree', 'Furnace', 'Galaxy', 'Garden', 'Gardener', 
    'Geyser', 'Ghost', 'Gift', 'GingerbreadHouse', 'GingerbreadMan', 'Giraffe', 'Glass', 'Glasses', 
    'Gnome', 'Goat', 'Godzilla', 'Gold', 'Goldfish', 'Golem', 'Gondola', 'Gopher', 
    'Gorgon', 'Graffiti', 'Grain', 'Granite', 'Grape', 'Grass', 'Grave', 'Greenhouse', 
    'Grenade', 'GrilledCheese', 'GrimReaper', 'Gun', 'Gym', 'Hail', 'Ham', 'Hamburger', 
    'Hammer', 'Hamster', 'Harmonica', 'Harp', 'Hay', 'Hedge', 'Helicopter', 'Hercules', 
    'Hippo', 'Hive', 'Honey', 'Horse', 'Horseshoe', 'Hospital', 'HotDog', 'Hotel', 
    'House', 'Human', 'Hummingbird', 'Hurricane', 'Hydrogen', 'Ice', 'IceCream', 'IceCreamTruck', 
    'Iceberg', 'IcedTea', 'Icicle', 'Icing', 'Igloo', 'Indigo', 'Ink', 'Internet', 
    'Island', 'Ivy', 'JackOLantern', 'Jam', 'Jedi', 'Jelly', 'Jellyfish', 'Jerky', 
    'Juice', 'Jupiter', 'Kaiju', 'Kaleidoscope', 'Kangaroo', 'Kebab', 'Key', 'KeyboardCat', 
    'Kite', 'Knight', 'Ladybug', 'Lake', 'Lamp', 'Land', 'Lasso', 'Lava', 
    'LavaLamp', 'LawnMower', 'Leaf', 'Leather', 'Lemon', 'Lemonade', 'Letter', 'Library', 
    'Lichen', 'Life', 'Light', 'LightBulb', 'Lighthouse', 'Lightning', 'Lion', 'Liquid', 
    'Lizard', 'Llama', 'Log', 'LogCabin', 'Love', 'Machete', 'Machine', 'Mackerel', 
    'Mailbox', 'Mammoth', 'Manatee', 'Map', 'MapleSyrup', 'Marshmallows', 'Mars', 'Marsh', 
    'Mask', 'Mastodon', 'Mayonnaise', 'Meat', 'Medusa', 'Mermaid', 'Metal', 'Meteor', 
    'Meteorologist', 'Milk', 'MilkyWay', 'Minotaur', 'Mirror', 'Mist', 'Mold', 'Monarch', 
    'Money', 'Monkey', 'Monster', 'Moon', 'Mop', 'Moss', 'Moth', 'Motorcycle', 
    'Mountain', 'Mouse', 'Mousetrap', 'Mud', 'Mummy', 'Music', 'Musketeer', 'Myth', 
    'Narwhal', 'Nest', 'Net', 'Newt', 'Night', 'Ninja', 'NinjaTurtle', 'Nitrogen', 
    'Ocean', 'Octopus', 'Oil', 'OilLamp', 'Omelette', 'Orange', 'Orchard', 'Origami', 
    'Ostrich', 'Otter', 'Owl', 'Oxygen', 'Oyster', 'Pacifier', 'Paint', 'Painting', 
    'Palm', 'Pancake', 'Panda', 'Paper', 'Parachute', 'Parrot', 'Pasta', 'Pegasus', 
    'Pelican', 'Pencil', 'Penguin', 'Pepper', 'Perfume', 'Petroleum', 'Phoenix', 'Picnic', 
    'Pig', 'Pigeon', 'Pillow', 'Pilot', 'Pinocchio', 'Pipe', 'Piranha', 'Pirate', 
    'PirateShip', 'Pitchfork', 'Pizza', 'Planet', 'Plankton', 'Plant', 'Platypus', 'Playground', 
    'Plesiosaurus', 'Pliers', 'PolarBear', 'Pollution', 'Pond', 'Popcorn', 'Popsicle', 'Postage', 
    'Potato', 'Potter', 'Pressure', 'Printer', 'Prism', 'Pterodactyl', 'Pudding', 'Pumpkin', 
    'Puppy', 'Pyramid', 'Quicksand', 'Rabbit', 'Rain', 'Rainbow', 'Rat', 'Recipe', 
    'Reindeer', 'Ring', 'River', 'Robot', 'Rock', 'Rocket', 'Roomba', 'Rose', 
    'Roulette', 'Rowboat', 'Ruler', 'Rust', 'RV', 'Saddle', 'Safe', 'SafetyGlasses', 
    'Sailboat', 'Sailor', 'Salad', 'Salmon', 'Salt', 'Sand', 'SandCastle', 'SandPaper', 
    'Sandstone', 'Sandwich', 'Santa', 'Saturn', 'Sausage', 'Saw', 'Scalpel', 'Scarecrow', 
    'Scarf', 'Scientist', 'Scissors', 'Scorpion', 'Scythe', 'Sea', 'Seagull', 'Seahorse', 
    'Seal', 'Seaplane', 'Seasickness', 'Seaweed', 'SewingMachine', 'Shadow', 'Shark', 'Sheep', 
    'SheetMusic', 'Shell', 'Ship', 'Shoe', 'Shuriken', 'Sick', 'Silo', 'Silver', 
    'Siren', 'Skateboard', 'Skeleton', 'SkiGoggles', 'Skull', 'Sky', 'Sledge', 'Sloth', 
    'Smog', 'Smoke', 'SmokingPipe', 'Snail', 'Snake', 'Snow', 'Snowball', 'Snowboard', 
    'SnowGlobe', 'Snowman', 'Soap', 'SolarCell', 'SolarSystem', 'Sound', 'Space', 'SpaceStation', 
    'Spaceship', 'Sphinx', 'Spider', 'Spoon', 'Spring', 'Squirrel', 'Stable', 'StainedGlass', 
    'Star', 'Starfish', 'Statue', 'Steam', 'Steamboat', 'SteamEngine', 'Steel', 'Steelwool', 
    'Stethoscope', 'StickyNote', 'Stone', 'Storm', 'Story', 'Sugar', 'Sun', 'Sundial', 
    'Sunflower', 'Sunglasses', 'SuperNova', 'Surfer', 'Sushi', 'Swamp', 'Sweater', 'SwimGoggles', 
    'Sword', 'Swordfish', 'Syringe', 'Tank', 'Tape', 'Tarzan', 'Tea', 'Telescope', 
    'Tent', 'TheOneRing', 'Thread', 'Tide', 'Tiger', 'Time', 'Tin', 'Tire', 
    'Toad', 'Toast', 'Tobacco', 'Toolbox', 'Tornado', 'Toucan', 'Tower', 'Tractor', 
    'TrafficLight', 'Treasure', 'TreasureMap', 'Tree', 'Treehouse', 'TrojanHorse', 'Tsunami', 'Turtle', 
    'UFO', 'Umbrella', 'Unicorn', 'VacuumCleaner', 'Vampire', 'Van', 'Vegetable', 'Venus', 
    'Vinegar', 'Vulture', 'Waffle', 'Wall', 'Walrus', 'Wand', 'Warrior', 'Watch', 
    'WaterGun', 'WaterLily', 'Waterfall', 'Wax', 'Web', 'Werewolf', 'Whale', 'Wheel', 
    'Wheelbarrow', 'WildBoar', 'Wind', 'Windmill', 'Window', 'Wine', 'Wire', 'Witch', 
    'Wolf', 'Wolverine', 'Wood', 'Woodpecker', 'Wool', 'Wrench', 'Yeti', 'Yoda', 
    'Yogurt', 'Zebra', 'Zombie'
]
'''
combinations = {
    ('Earth', 'Air'): 'Dust',
    ('Earth', 'Fire'): 'Lava',
    ('Earth', 'Water'): 'Mud',
    ('Air', 'Fire'): 'Energy',
    ('Air', 'Water'): 'Rain',
    ('Fire', 'Water'): 'Steam',
    ('Energy', 'Water'): 'Electricity',
    ('Lava', 'Air'): 'Stone',
    ('Stone', 'Air'): 'Sand',
    ('Sand', 'Fire'): 'Glass', 
    ('Glass', 'Sand'): 'Time',
    ('Water', 'Water'): 'Puddle',
    ('Water', 'Puddle'): 'Pond',
    ('Water', 'Pond'): 'Lake',
    ('Water', 'Lake'): 'Sea',
    ('Water', 'Sea'): 'Ocean',
    ('Lava', 'Sea'): 'Primordialsoup',
    ('Volcano', 'Primordialsoup'): 'Life',
    ('Earth', 'Life'): 'Soil',
    ('Soil', 'Life'): 'Plant',
    ('Time', 'Life'): 'Human',
    ('Human', 'Stone'): 'Tool',
    ('Human', 'Metal'): 'Armor',
    ('Human', 'Human'): 'Love',
    ('Human', 'Earth'): 'Farmer',
    ('Farmer', 'Plant'): 'Wheat',
    ('Wheat', 'Stone'): 'Flour',
    ('Flour', 'Water'): 'Dough',
    ('Dough', 'Fire'): 'Bread',
    ('Bread', 'Human'): 'Baker',
    ('Human', 'Tool'): 'Engineer',
    ('Engineer', 'Metal'): 'Machine',
    ('Machine', 'Bread'): 'Toaster',
    ('Love', 'Time'): 'Life',
    ('Life', 'Stone'): 'Egg',
    ('Egg', 'Sand'): 'Turtle',
    ('Turtle', 'Earth'): 'Beach',
    ('Beach', 'Water'): 'Ocean',
    ('Ocean', 'Volcano'): 'Island',
    ('Island', 'Ocean'): 'Archipelago',
    ('Island', 'Animal'): 'WildAnimal',
    ('WildAnimal', 'Water'): 'Shark',
    ('Shark', 'Human'): 'Blood',
    ('Blood', 'Human'): 'Vampire',
    ('Vampire', 'Human'): 'Corpse',
    ('Corpse', 'Life'): 'Zombie',
    ('Zombie', 'Human'): 'Zombie',
    ('Zombie', 'Corpse'): 'Ghost',
    ('Ghost', 'Time'): 'History',
    ('History', 'Time'): 'Century',
    ('Century', 'Century'): 'Millennium',
    ('Millennium', 'Time'): 'Eternity',
    ('Continent', 'Continent'): 'Planet',
    ('Planet', 'Planet'): 'Solarsystem',
    ('Solarsystem', 'Solarsystem'): 'Galaxy',
    ('Galaxy', 'Galaxy'): 'Galaxycluster',
    ('Galaxycluster', 'Galaxycluster'): 'Universe',
    ('Eternity', 'Universe'): 'Infinity',
    ('Fire', 'Planet'): 'Sun',
    ('Air', 'Planet'): 'Atmosphere',
    ('Sun', 'Atmosphere'): 'Sky',
    ('Sun', 'Atmosphere'): 'Aurora',
    ('Sky', 'Solarsystem'): 'Space', 
    ('Infinity', 'Space'): 'BlackHole',
    ('BlackHole', 'Sun'): 'Supernova',
    ('Supernova', 'Supernova'): 'Hypernova',
    ('Hypernova', 'Time'): 'Bigbang',
    ('Atmosphere', 'Water'): 'Cloud',
    ('Sky', 'Cloud'): 'Storm',
    ('Storm', 'Energy'): 'Thunder',
    ('Thunder', 'Metal'): 'Electricity',
    ('Electricity', 'Wire'): 'Circuit',
    ('Circuit', 'Metal'): 'Computer',
    ('Computer', 'Human'): 'Cyborg',
    ('Cyborg', 'Time'): 'Android',
    ('Android', 'Space'): 'Astronaut',
    ('Stone', 'Planet'): 'Moon',
    ('Astronaut', 'Moon'): 'Spacestation',
    ('Atmosphere', 'Metal'): 'Rocket',
    ('Spacestation', 'Rocket'): 'Spaceship',
    ('Spaceship', 'Planet'): 'Solarsystem',
    ('Galaxycluster', 'Universe'): 'Multiverse',
    ('Multiverse', 'Time'): 'Timetravel',
    ('Life', 'Fire'): 'Phoenix',
    ('Phoenix', 'Phoenix'): 'Egg',
    ('Wall', 'Wall'): 'House',
    ('Metal', 'Earth'): 'Plow',
    ('Plow', 'Earth'): 'Field',
    ('Field', 'House'): 'Barn',
    ('Barn', 'Egg'): 'Chicken',
    ('Chicken', 'Egg'): 'Philosophy',
    ('Philosophy', 'Planet'): 'Big',
    ('Life', 'Land'): 'Animal',
    ('Animal', 'Stone'): 'Lizard',
    ('Big', 'Lizard'): 'Dinosaur',
    ('Dinosaur', 'Air'): 'Pterodactyl',
    ('Dinosaur', 'Blood'): 'Tyrannosaurusrex',
    ('Dinosaur', 'Earth'): 'Fossil',
    ('Fossil', 'Human'): 'Paleontologist',
    ('Timetravel', 'Dinosaur'): 'Jurassicpark',
    ('Jurassicpark', 'Volcano'): 'Idea',
    ('Life', 'Fire'): 'Phoenix',
    ('Plant', 'Big'): 'Tree',
    ('Tool', 'Tree'): 'Wood',
    ('Fire', 'Wood'): 'Campfire',
    ('Human', 'Campfire'): 'Story',
    ('Idea', 'Story'): 'Detective',
    ('Detective', 'Murder'): 'Investigation',
    ('Human', 'Universe'): 'Science',
    ('Investigation', 'Science'): 'Research',
    ('Research', 'Life'): 'Biology',
    ('Biology', 'Earth'): 'Evolution',
    ('Evolution', 'Egg'): 'Bird',
    ('Bird', 'Beach'): 'Seagull',
    ('Animal', 'Ocean'): 'Fish',
    ('Seagull', 'Fish'): 'Hunting',
    ('Hunting', 'Human'): 'Hunter',
    ('Gunpowder', 'Metal'): 'Bullet',
    ('Bullet', 'Metal'): 'Gun',
    ('Hunter', 'Gun'): 'Shooting',
    ('Sky', 'Moon'): 'Night',
    ('Sky', 'Night'): 'Star',
    ('Shooting', 'Star'): 'Meteor',
    ('Meteor', 'Atmosphere'): 'Meteoroid',
    ('Meteoroid', 'Earth'): 'Meteorite',
    ('Life', 'Mud'): 'Bacteria',
    ('Meteorite', 'Bacteria'): 'Alien',
    ('Alien', 'Planet'): 'ExtraterrestrialLife',
    ('ExtraterrestrialLife', 'Space'): 'UFO',
    ('Animal', 'Field'): 'Livestock',
    ('Field', 'Livestock'): 'Cow',
    ('UFO', 'Cow'): 'Abduction',
    ('Abduction', 'Idea'): 'X-Files',
    ('X-Files', 'Story'): 'Conspiracy',
    ('Glass', 'Glass'): 'Glasses',
    ('Glasses', 'Human'): 'Hacker',
    ('Hacker', 'Tool'): 'Computer',
    ('Conspiracy', 'Computer'): 'Darkweb',
    ('Hacker', 'Bank'): 'Cybercrime',
    ('Air', 'Air'): 'Pressure',
    ('Air', 'Pressure'): 'Wind',
    ('Wind', 'Science'): 'Motion',
    ('Tool', 'Motion'): 'Wheel',
    ('Metal', 'Wheel'): 'Car',
    ('Big', 'Car'): 'Bus',
}

elements = list(set([element for combo in combinations.keys() for element in combo] 
+ [result for result in combinations.values()]))
print(elements)


def generate_elements(element_names):
    elements = []
    for name in element_names:
        image_path = f'elements/{name.lower()}.png'
        position = [100, 100]  # You'll want to change these to your desired default positions
        elements.append(Element(name, image_path, position, True))
    return elements

elements = generate_elements(elements)

'''
elements = [
    Element('Earth', 'elements/earth.png', [100, 100], True),
    Element('Air', 'elements/air.png', [200, 200], True),
    Element('Fire', 'elements/fire.png', [300, 300], True),
    Element('Water', 'elements/water.png', [400, 400], True),
    # etc...
]
'''
#generate_elements(elements)

unique_elements_in_combinations = set()
for element_pair, result in combinations.items():
    unique_elements_in_combinations.add(element_pair[0])
    unique_elements_in_combinations.add(element_pair[1])
    unique_elements_in_combinations.add(result)

# Filter original elements list
filtered_elements = [ele for ele in elements if ele in unique_elements_in_combinations]

print(filtered_elements)
def combine(element1, element2):
    result = combinations.get((element1, element2))
    if result is None:
        result = combinations.get((element2, element1))
    # Check if the result is a new element
    if result is not None and not any(ele.name == result for ele in elements):
        # Add the new element to your list
        elements.append(Element(result, f'elements/{result.lower()}.png', [100, 100], True)) 
    return result
