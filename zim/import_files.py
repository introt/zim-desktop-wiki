
# Copyright 2020 Jaap Karssenberg <jaap.karssenberg@gmail.com>

# This module contains functions to import text files into a zim
# notebook

import logging


logger = logging.getLogger('zim')


def import_file(file, notebook, path, format='wiki'):
	'''Import a file into a zim notebook page

	:param file: a :class:`File` object to import from
	:param notebook: a :class:`Notebook` object to import into
	:param path: the :class:`Path` to import to within the notebook
	:returns: the :class:`Page` object for the imported page, this may be a different
		page than the one ``path`` is pointing - see :class:`notebook.get_new_page()`
	'''
	logging.debug('Import file "%s" to "%s" as %s', file, path, format)
	if file.ischild(notebook.folder):
		newfile = file.parent().new_file(file.basename + '~')
		file.moveto(newfile)
		file = newfile

	page = notebook.get_new_page(path)
	assert not page.exists()

	page.parse(format, file.readlines())
	notebook.store_page(page)
	return page


def import_folder(folder, notebook, path, filter=None, format='wiki'):
	'''Import a folder recursively

	:param folder: a :class:`Folder` object to import from
	:param notebook: a :class:`Notebook` object to import into
	:param path: the :class:`Path` to import to within the notebook
	:param filter: optional filter function to decide which files and folder
		to import when scanning ``folder``. Will be given each file or folder found
		when scanning ``folder`` and expected to return boolean whether to import
		yes or no.
	'''
	raise NotImplementedError
