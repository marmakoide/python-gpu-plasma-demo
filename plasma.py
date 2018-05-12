import math
import pyglet
from pyglet.gl import *
from shader import Shader



class PlasmaWindow(pyglet.window.Window):
	def __init__(self):
		super(PlasmaWindow, self).__init__(caption = 'plasma', width = 512, height = 512)

		self.C1 = ( .0,   .0)
		self.C2 = ( .2,  .2)
		self.C3 = (-.2, -.2)

		shader_path = 'plasma'
		self.shader = Shader(''.join(open('%s.v.glsl' % shader_path)),
		                     ''.join(open('%s.f.glsl' % shader_path)))

	def on_mouse_motion(self, x, y, dx, dy):
		self.C1 = ((float(x) / window.width) - .5, (float(y) / window.height) - .5)

	def on_draw(self):
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		glOrtho(-1., 1., 1., -1., 0., 1.)

		glMatrixMode(GL_MODELVIEW)
		glLoadIdentity()

		self.shader.bind()
		self.shader.uniformf('C1', *self.C1)
		self.shader.uniformf('C2', *self.C2)
		self.shader.uniformf('C3', *self.C3)

		glBegin(GL_QUADS)
		glVertex2i(-1, -1)
		glTexCoord2f(-.5, -.5)
		glVertex2i(1, -1)
		glTexCoord2f(.5, -.5)
		glVertex2i(1,  1)
		glTexCoord2f(.5, .5)
		glVertex2i(-1,  1)
		glTexCoord2f(-.5, .5)
		glEnd()
		self.shader.unbind()


window = PlasmaWindow()
pyglet.app.run()
