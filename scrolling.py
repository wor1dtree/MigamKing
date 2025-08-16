import pygame
import collections
import os

"""
Scrolling: 스크롤링 배경을 구현합니다. 다양한 레이어의 구름 이미지가 화면을 가로지르며 배경을 구성합니다.
Cloud: 구름 객체를 생성하고, 속도에 따라 화면을 가로지르는 기능을 구현합니다.
"""

class Scrollers:
	def __init__(self):
		self.directory = "Scrolling"
		self.images = collections.defaultdict()
		self.scrollers = collections.defaultdict()
		self._load_images()
		self._load_scrollers()

	def _load_images(self):
		for file in os.listdir(self.directory):
			self.images[file] = pygame.image.load(f"{self.directory}\\{file}").convert_alpha()

	def _load_scrollers(self):
		""" 각 레이어에 맞는 구름 객체를 생성합니다.(스테이지 인덱스에 맞게 매칭시키면 될듯합니다.) """
		self.scrollers[3] = [Cloud(-40, 50, 0.05, self.images["4_clouds.png"], "bg")]
		self.scrollers[4] = [Cloud(-40, 70, 0.05, self.images["6_clouds.png"], "bg")]
		self.scrollers[5] = [Cloud(20, 200, 0.05, self.images["6_clouds.png"], "bg")]
		self.scrollers[13] = [Cloud(-30, 10, 0.05, self.images["14_clouds_bg.png"], "bg"), 
							Cloud(-30, 50, 0.10, self.images["14_clouds_mg.png"], "bg"), 
							Cloud(-30, 150, 0.25, self.images["14_clouds_fg.png"], "bg")]
		self.scrollers[14] = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), 
							Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg")]
		self.scrollers[15]  = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), 
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg")]
		self.scrollers[16] = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), 
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg")]
		self.scrollers[17]  = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"), 
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg")]
		self.scrollers[18]  = [Cloud(-30, 10, 0.25, self.images["mist_clouds1.png"], "fg"), Cloud(30, 100, 0.5, self.images["mist_clouds2.png"], "fg"),
							Cloud(70, 250, 0.4, self.images["mist_clouds3.png"], "fg")]
		self.scrollers[19] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn1.png"], "bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn2.png"], "bg")]
		self.scrollers[19] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn2.png"], "bg"), Cloud(-10, 200, 0.05, self.images["clouds_vakttorn1.png"], "bg")]
		self.scrollers[20] = [Cloud(-30, 100, 0.1,self.images["clouds_vakttorn2.png"], "bg"), Cloud(90, 160, 0.05, self.images["clouds_vakttorn1.png"], "bg")]
		self.scrollers[21] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn1.png"], "bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn2.png"], "bg")]
		self.scrollers[22] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn_dark2.png"],"bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn1.png"], "bg")]
		self.scrollers[23] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn_dark1.png"],"bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn_dark2.png"], "bg")]
		self.scrollers[24] = [Cloud(-30, 20, 0.1, self.images["clouds_vakttorn_dark1.png"],"bg"), Cloud(-10, 160, 0.05, self.images["clouds_vakttorn_dark2.png"], "bg")]
		self.scrollers[39] = [Cloud(0, 0, 0.1, self.images["40_clouds.png"],"bg")]
		self.scrollers[40] = [Cloud(0, 60, 0.1, self.images["41_clouds.png"],"bg")]
		self.scrollers[41] = [Cloud(0, 224, 0.1, self.images["42_clouds1.png"],"bg"), Cloud(0, 100, 0.1, self.images["42_clouds2.png"],"bg")]


class Cloud:
	def __init__(self, x = 0, y = 0, speed = None, image = None, layer = None):
		self.layer = layer
		self.speed = speed
		self.image = image
		self.x, self.y, self.width, self.height = x, y, self.image.get_width(), self.image.get_height()

	@property
	def rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)
	
	def blitme(self, screen, layer):
		if layer == self.layer:
			if self.rect.colliderect(screen.get_rect()):
				screen.blit(self.image, self.rect)
			if self.rect.move(-self.width, 0).colliderect(screen.get_rect()):
				screen.blit(self.image, self.rect.move(-self.width, 0))
			if self.rect.move(self.width, 0).colliderect(screen.get_rect()):
				screen.blit(self.image, self.rect.move(self.width, 0))
			self.x += self.speed
			if self.x > screen.get_width():
				self.x -= self.width
			if self.x < -self.width:
				self.x += self.width
