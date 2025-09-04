from squareshape import SquareShape
from constants import *
import pygame
import json
import os

class Score(SquareShape):
    def __init__(self, x, y):
        super().__init__(x, y, SCORE_SIZE)
        pygame.sprite.Sprite.__init__(self)
        self.__current_score = 0

    def add_score(self, score):
        if score > 0:
            self.__current_score += score
        else:
            raise Exception('cannot add score below 1')

    def draw(self, screen):
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {self.__current_score}", True, (255, 255, 255))
        screen.blit(score_text, (self.position.x, self.position.y))

    def update(self, dt):
        # sub-classes must override
        pass


    def save_score(self, player, file_path):

        new_score = { "name": player.name, "score": self.__current_score}

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                try:
                    scores = json.load(f)
                    if not isinstance(scores, list):
                        scores = []
                except json.JSONDecodeError:
                    scores = []
        else:
            scores = []

        scores.append(new_score)

        with open(file_path, 'w') as f:
            json.dump(scores, f)