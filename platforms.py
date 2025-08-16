import pygame
import collections
import os

class Rectangles:

	def __init__(self):

		self.levels = collections.defaultdict()

		self.levels[0]	=	[(352, 185, 128, 175, 0, 0, False, False),
							(185, 40, 110, 50, 0, 0, False, False),
							(128, 330, 224, 30, 0, 0, False, False),
							(8, 184, 120, 107, 0, 0, False, False),
							(8, 291, 65, 69, 0, 0, False, False),
							(73, 330, 55, 30, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[1]	=	[(296, 296, 95, 38, 0, 0, False, False),
							(409, 197, 71, 35, 0, 0, False, False),
							(255, 199, 74, 33, 0, 0, False, False),
							(119, 103, 74, 65, 0, 0, False, False),
							(0, 80, 81, 86, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[2]	=	[(137, 0, 70, 14, 0, 0, False, False),
							(0, 98, 63, 12, 0, 0, False, False),
							(161, 120, 55, 47, 0, 0, False, False),
							(290, 209, 46, 46, 0, 0, False, False),
							(193, 224, 98, 31, 0, 0, False, False),
							(426, 259, 54, 12, 0, 0, False, False),
							(208, 305, 48, 13, 0, 0, False, False),
							(321, 306, 56, 14, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[3]	=	[(137, 89, 40, 79, 0, 0, False, False),
							(137, -4, 15, 93, 0, 0, False, False),
							(-5, 216, 69, 16, 0, 0, False, False),
							(137, 217, 71, 16, 0, 0, False, False),
							(329, 0, 17, 16, 0, 0, False, False),
							(329, 73, 17, 88, 0, 0, False, False),
							(297, 161, 49, 71, 0, 0, False, False),
							(345, 73, 55, 16, 0, 0, False, False),
							(434, 129, 46, 15, 0, 0, False, False),
							(137, 321, 71, 39, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[4]	=	[(40, 88, 31, 15, 0, 0, False, False),
							(160, 57, 32, 14, 0, 0, False, False),
							(225, 72, 31, 15, 0, 0, False, False),
							(152, 0, 176, 14, 0, 0, False, False),
							(288, 88, 31, 15, 0, 0, False, False),
							(441, 161, 39, 14, 0, 0, False, False),
							(0, 241, 39, 14, 0, 0, False, False),
							(329, 241, 38, 14, 0, 0, False, False),
							(112, 313, 40, 15, 0, 0, False, False),
							(137, 327, 15, 33, 0, 0, False, False),
							(328, 312, 40, 16, 0, 0, False, False),
							(328, 328, 16, 32, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[5]	=	[(153, 329, 173, 30, 0, 0, False, False),
							(0, 184, 55, 15, 0, 0, False, False),
							(57, 72, 39, 16, 0, 0, False, False),
							(80, 88, 16, 39, 0, 0, False, False),
							(96, 112, 95, 16, 0, 0, False, False),
							(0, 0, 136, 15, 0, 0, False, False),
							(136, 0, 54, 55, 0, 0, False, False),
							(129, 241, 47, 15, 0, 0, False, False),
							(289, 80, 191, 175, 0, 0, False, False),
							(290, 0, 39, 24, 0, 0, False, False),
							(329, 0, 94, 39, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False)]

		self.levels[6]	=	[(0, 0, 88, 17, 0, 0, False, False),
							(0, 168, 33, 15, 0, 0, False, False),
							(0, 239, 104, 120, 0, 0, True, False),
							(0, 183, 33, 56, 0, 0, False, False),
							(129, 48, 39, 24, 0, 0, False, False),
							(153, 0, 15, 48, 0, 0, False, False),
							(104, 72, 126, 31, 0, 0, False, False),
							(152, 103, 78, 56, 0, 0, False, False),
							(152, 159, 39, 34, 0, 0, False, False),
							(136, 239, 72, 8, 0, 0, False, False),
							(184, 248, 7, 47, 0, 0, False, False),
							(191, 248, 17, 7, 0, 0, False, False),
							(209, 0, 56, 23, 0, 0, False, False),
							(265, 0, 31, 17, 0, 0, False, False),
							(290, 153, 94, 7, 0, 0, False, False),
							(368, 95, 16, 59, 0, 0, True, False),
							(384, 113, 40, 23, 0, 0, False, False),
							(457, 113, 23, 23, 0, 0, False, False),
							(290, 208, 134, 15, 0, 0, False, False),
							(290, 223, 14, 136, 0, 0, False, False),
							(304, 305, 64, 40, 0, 0, False, False),
							(304, 345, 120, 15, 0, 0, False, False),
							(353, 223, 15, 24, 0, 0, False, False),
							(290, 110, 46, 10, 0, 0, True, False),
							(385, 0, 95, 48, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(33, 168, 71, 71, (-1, 1), 0, False, False),
							(136, 247, 48, 48, (-1, -1), 0, False, False),
							(290, 64, 46, 46, (1, 1), 0, False, False),
							(336, 48, 17, 16, (1, 1), 0, False, False),
							(336, 64, 17, 15, (1, -1), 0, False, False),
							(353, 33, 15, 15, (1, 1), 0, False, False),
							(368, 16, 17, 17, (1, 1), 0, False, False),
							(368, 33, 17, 15, (1, 1), 0, False, False),
							(353, 48, 15, 16, (1, -1), 0, False, False),
							(104, 269, 87, 90, (-1, 1), 0, False, False),
							(265, 17, 31, 29, (1, -1), 0, False, False),
							(368, 80, 16, 15, (1, 1), 0, False, False),
							(104, 48, 25, 24, (1, 1), 0, False, False)]

		self.levels[7]	=	[(0, 144, 248, 40, 0, 0, False, False),
							(0, 184, 72, 72, 0, 0, False, False),
							(0, 256, 24, 104, 0, 0, False, False),
							(0, 64, 32, 80, 0, 0, False, False),
							(24, 344, 64, 15, 0, 0, False, False),
							(223, 24, 24, 63, 0, 0, True, False),
							(88, 0, 135, 87, 0, 0, False, False),
							(152, 328, 16, 32, 0, 0, False, False),
							(249, 353, 47, 7, 0, 0, False, False),
							(208, 344, 41, 15, 0, 0, False, False),
							(434, 0, 46, 87, 0, 0, False, False),
							(434, 225, 46, 135, 0, 0, False, False),
							(384, 320, 50, 40, 0, 0, True, False),
							(153, 241, 94, 31, 0, 0, False, False),
							(153, 272, 94, 7, 0, 0, False, False),
							(240, 279, 7, 25, 0, 0, False, False),
							(247, 287, 16, 18, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(223, 0, 24, 24, (-1, 1), 0, False, False),
							(249, 344, 9, 9, (-1, 1), 0, False, False),
							(384, 270, 50, 50, (1, 1), 0, False, False),
							(247, 272, 16, 15, (-1, 1), 0, False, False),
							(216, 279, 24, 25, (-1, -1), 0, False, False),
							(262, 287, 18, 17, (-1, 1), 0, False, False),
							(279, 304, 18, 16, (-1, 1), 0, False, False),
							(262, 304, 18, 16, (-1, -1), 0, False, False)]

		self.levels[8]	=	[(0, 0, 102, 17, 0, 0, False, False),
							(154, 0, 70, 17, 0, 0, False, False),
							(208, 17, 16, 143, 0, 0, False, False),
							(0, 167, 31, 24, 0, 0, False, False),
							(176, 136, 32, 24, 0, 0, False, False),
							(88, 89, 16, 119, 0, 0, False, False),
							(88, 208, 47, 152, 0, 0, False, False),
							(65, 296, 23, 24, 0, 0, False, False),
							(224, 96, 31, 64, 0, 0, False, False),
							(393, 97, 30, 31, 0, 0, False, False),
							(393, 0, 87, 17, 0, 0, False, False),
							(199, 207, 33, 66, 0, 0, False, False),
							(296, 207, 31, 66, 0, 0, False, False),
							(391, 207, 33, 66, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(135, 272, 89, 88, (-1, 1), 0, False, False),
							(431, 312, 49, 48, (1, 1), 0, False, False)]

		self.levels[9]	=	[(0, 185, 56, 175, 0, 0, False, False),
							(56, 328, 48, 32, 0, 0, False, False),
							(154, 233, 68, 127, 0, 0, False, False),
							(393, 329, 87, 31, 0, 0, False, False),
							(152, 104, 47, 32, 0, 0, False, False),
							(199, 120, 281, 16, 0, 0, False, False),
							(152, 0, 47, 47, 0, 0, False, False),
							(248, 89, 48, 31, 0, 0, False, False),
							(344, 97, 49, 23, 0, 0, False, False),
							(248, 0, 48, 48, 0, 0, False, False),
							(344, 0, 49, 49, 0, 0, False, False),
							(440, 88, 40, 32, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(56, 279, 48, 49, (-1, 1), 0, False, False)]

		self.levels[10]	=	[(120, 0, 33, 9, 0, 0, False, False),
							(153, 0, 47, 40, 0, 0, False, False),
							(153, 40, 23, 40, 0, 0, False, False),
							(153, 80, 47, 24, 0, 0, False, False),
							(153, 168, 47, 32, 0, 0, False, False),
							(8, 120, 24, 25, 0, 0, False, False),
							(8, 209, 32, 15, 0, 0, False, False),
							(153, 240, 47, 120, 0, 0, False, False),
							(248, 0, 47, 8, 0, 0, False, False),
							(248, 48, 47, 15, 0, 0, False, False),
							(248, 113, 47, 63, 0, 0, False, False),
							(273, 63, 22, 50, 0, 0, False, False),
							(249, 240, 46, 32, 0, 0, False, False),
							(249, 320, 46, 40, 0, 0, False, False),
							(344, 0, 48, 63, 0, 0, False, False),
							(344, 128, 48, 32, 0, 0, False, False),
							(344, 224, 48, 32, 0, 0, False, False),
							(344, 344, 48, 15, 0, 0, False, False),
							(441, 48, 39, 15, 0, 0, False, False),
							(440, 128, 40, 34, 0, 0, False, False),
							(0, 0, 8, 360, 0, 0, False, False),
							(472, 0, 8, 360, 0, 0, False, False),
							(32, 120, 24, 25, (-1, 1), 0, False, False)]


class Platform():

	def __init__(self, x, y, width, height, slope = False, slip = False, support = False, snow = False):

		self.x, self.y, self.width, self.height = x, y, width, height

		self.type = "Land"

		if slope:

			self.slope = (slope[0] * self.height/self.width, slope[1])

		else:

			self.slope = 0

		if slip:

			self.slip = 0.95
			self.type = "Ice"

		else:
			self.slip = 0

		self.support = support

		self.snow = snow

		if snow:

			self.type = "Snow"

	@property
	def rect(self):
		return pygame.Rect(self.x, self.y, self.width, self.height)
	

class Platforms():

	def __init__(self):

		self.rectangles = Rectangles()

	def platforms(self, level):

		try:

			return [Platform(*rectangle) for rectangle in self.rectangles.levels[level]]

		except:

			return []


if __name__ == "__main__":
	pygame.init()
	shit = Platforms()

	for level in range(43):

		platform = shit.platforms(level)

		print(f"self.levels[{level}]\t=\t", end = "")
		print('[', end = "")
		print(*sorted([(rect.x, rect.y, rect.width, rect.height, rect.slope, rect.slip, rect.support, rect.snow) for rect in platform], key = lambda l : type(l[4]) == tuple), sep = ",\n\t\t\t\t\t", end = "")
		print(']\n')