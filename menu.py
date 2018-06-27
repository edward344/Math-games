#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Menu(object):
    state = -1
    def __init__(self,items,font_color=(0,0,0),select_color=(255,0,0),ttf_font=None,font_size=25):
        self.font_color = font_color
        self.select_color = select_color
        self.items = items
        self.font = pygame.font.Font(ttf_font,font_size)
        # Generate a list that will contain the rect for each item
        self.rect_list = self.get_rect_list(items)

    def get_rect_list(self,items):
        rect_list = []
        for index, item in enumerate(items):
            # determine the amount of space needed to render text
            size = self.font.size(item)
            # Get the width and height of the text
            width = size[0]
            height = size[1]

            posX = (SCREEN_WIDTH / 2) - (width /2)
            # t_h: total heigth of the text block
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            # Create rects
            rect = pygame.Rect(posX,posY,width,height)
            # Add rect to the list
            rect_list.append(rect)

        return rect_list

    def collide_points(self):
        index = -1
        mouse_pos = pygame.mouse.get_pos()
        for i,rect in enumerate(self.rect_list):
            if rect.collidepoint(mouse_pos):
                index = i

        return index

    def update(self):
        # assign collide_points to state
        self.state = self.collide_points()
        
    def display_frame(self,screen):
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item,True,self.select_color)
            else:
                label = self.font.render(item,True,self.font_color)
            
            width = label.get_width()
            height = label.get_height()
            
            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(self.items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)
            
            screen.blit(label,(posX,posY))
