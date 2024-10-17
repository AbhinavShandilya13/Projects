import unittest
import pygame
from flappy_bird import *

class TestFlappyBird(unittest.TestCase):
    def setUp(self):
        # Initialize the game variables
        self.FPS = 32
        self.SCREENWIDTH = 289
        self.SCREENHEIGHT = 511
        self.SCREEN = None
        self.GROUNDY = self.SCREENHEIGHT * 0.8
        self.GAME_SPRITES = {}
        self.GAME_SOUNDS = {}
        self.PLAYER = 'gallery/sprites/bird.png'
        self.BACKGROUND = 'gallery/sprites/background.png'
        self.PIPE = 'gallery/sprites/pipe.png'

        # Initialize Pygame
        pygame.init()
        self.FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Flappy Bird')

        # Load game sprites and sounds
        self.load_sprites()
        self.load_sounds()

    def load_sprites(self):
        # Load game sprites
        self.GAME_SPRITES['numbers'] = (
            pygame.image.load('gallery/sprites/0.png').convert_alpha(),
            pygame.image.load('gallery/sprites/1.png').convert_alpha(),
            pygame.image.load('gallery/sprites/2.png').convert_alpha(),
            pygame.image.load('gallery/sprites/3.png').convert_alpha(),
            pygame.image.load('gallery/sprites/4.png').convert_alpha(),
            pygame.image.load('gallery/sprites/5.png').convert_alpha(),
            pygame.image.load('gallery/sprites/6.png').convert_alpha(),
            pygame.image.load('gallery/sprites/7.png').convert_alpha(),
            pygame.image.load('gallery/sprites/8.png').convert_alpha(),
            pygame.image.load('gallery/sprites/9.png').convert_alpha(),
        )

        self.GAME_SPRITES['message'] =pygame.image.load('gallery/sprites/message2.png').convert_alpha()
        self.GAME_SPRITES['base'] =pygame.image.load('gallery/sprites/base.png').convert_alpha()
        self.GAME_SPRITES['pipe'] =(pygame.transform.rotate(pygame.image.load(self.PIPE).convert_alpha(), 180),
                                     pygame.image.load(self.PIPE).convert_alpha()
                                     )

    def load_sounds(self):
        # Game sounds
        self.GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
        self.GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
        self.GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
        self.GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
        self.GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    def test_load_sprites(self):
        # Test if sprites load correctly
        self.assertIsNotNone(self.GAME_SPRITES['numbers'][0])
        self.assertIsNotNone(self.GAME_SPRITES['message'])
        self.assertIsNotNone(self.GAME_SPRITES['base'])
        self.assertIsNotNone(self.GAME_SPRITES['pipe'][0])

    def test_load_sounds(self):
    # Test if sounds load correctly
        self.assertIsNotNone(self.GAME_SOUNDS['die'])
        self.assertIsNotNone(self.GAME_SOUNDS['hit'])
        self.assertIsNotNone(self.GAME_SOUNDS['point'])
        self.assertIsNotNone(self.GAME_SOUNDS['swoosh'])
        self.assertIsNotNone(self.GAME_SOUNDS['wing'])