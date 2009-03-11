# -*- coding: utf8 -*-

# Copyright 2008 Jaap Karssenberg <pardus@cpan.org>

'''FIXME'''

import gtk

from zim._lib import xdot
from zim.gui import Dialog
from zim.gui.widgets import IconButton

from zim.plugins.linkmap import LinkMap

ui_xml = '''
<ui>
	<menubar name='menubar'>
		<menu action='view_menu'>
			<placeholder name='plugin_items'>
				<menuitem action='show_linkmap'/>
			</placeholder>
		</menu>
	</menubar>
</ui>
'''

ui_actions = (
	# name, stock id, label, accelerator, tooltip
	('show_linkmap', None, 'Show Link Map', None, 'Show Link Map'),
)


class GtkLinkMap():

	def __init__(self, ui):
		self.ui = ui
		self.ui.add_actions(ui_actions, self)
		self.ui.add_ui(ui_xml, self)

	def show_linkmap(self):
		linkmap = LinkMap(self.ui.notebook)
		dialog = LinkMapDialog(self.ui, linkmap)
		dialog.show_all()


class LinkMapDialog(Dialog):
	'''FIXME'''

	def __init__(self, ui, linkmap):
		Dialog.__init__(self, ui, 'LinkMap', buttons=gtk.BUTTONS_CLOSE)
		self.set_default_size(400, 400)
		self.linkmap = linkmap

		hbox = gtk.HBox(spacing=5)
		self.vbox.add(hbox)

		self.xdotview = xdot.DotWidget()
		#~ self.xdotview.set_filter('neato')
		self.xdotview.set_dotcode(linkmap.get_dotcode())
		hbox.add(self.xdotview)

		vbox = gtk.VBox()
		hbox.pack_start(vbox, False)
		for stock, method in (
			(gtk.STOCK_ZOOM_IN,  self.xdotview.on_zoom_in ),
			(gtk.STOCK_ZOOM_OUT, self.xdotview.on_zoom_out),
			(gtk.STOCK_ZOOM_FIT, self.xdotview.on_zoom_fit),
			(gtk.STOCK_ZOOM_100, self.xdotview.on_zoom_100),
		):
			button = IconButton(stock)
			button.connect('clicked', method)
			vbox.pack_start(button, False)
