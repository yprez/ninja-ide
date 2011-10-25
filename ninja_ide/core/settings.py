# -*- coding: utf-8 -*-
import sys

from PyQt4.QtCore import QSettings

from ninja_ide.dependencies import pep8mod


###############################################################################
# OS DETECTOR
###############################################################################

OS_KEY = "Ctrl"

FONT_FAMILY = 'Monospace'
FONT_SIZE = 11
if sys.platform == "darwin":
    from PyQt4.QtGui import QKeySequence
    from PyQt4.QtCore import Qt

    FONT_FAMILY = 'Monaco'
    FONT_SIZE = 11
    OS_KEY = QKeySequence(Qt.CTRL).toString(QKeySequence.NativeText)
elif sys.platform == "win32":
    FONT_FAMILY = 'Lucida Console'
    FONT_SIZE = 10

###############################################################################
# IDE
###############################################################################

MAX_OPACITY = 1
MIN_OPACITY = 0.3

TOOLBAR_ORIENTATION = 1
#UI LAYOUT
#001 : Central Rotate
#010 : Panels Rotate
#100 : Central Orientation
UI_LAYOUT = 0

LANGUAGE = ""

SHOW_START_PAGE = True

CONFIRM_EXIT = True
NOTIFY_UPDATES = True
HIDE_TOOLBAR = False

PYTHON_PATH = "python"
EXECUTION_OPTIONS = ""

PROFILES = {}


###############################################################################
# EDITOR
###############################################################################

INDENT = 4
MARGIN_LINE = 80
SHOW_MARGIN_LINE = True
REMOVE_TRAILING_SPACES = True
SHOW_TABS_AND_SPACES = True

BRACES = {"'": "'",
    '"': '"',
    '{': '}',
    '[': ']',
    '(': ')'}

FONT_MAX_SIZE = 28
FONT_MIN_SIZE = 6
MAX_REMEMBER_TABS = 50
COPY_HISTORY_BUFFER = 20

HIGHLIGHT_VARIABLES = True    # Variables on Visible Area
HIGHLIGHT_ALL_VARIABLES = False    # Variables on the Document

FIND_ERRORS = True
ERRORS_HIGHLIGHT_LINE = False
CHECK_STYLE = True
CHECK_HIGHLIGHT_LINE = True
MAX_HIGHLIGHT_ERRORS = 5
CODE_COMPLETION = True
ENABLE_COMPLETION_IN_COMMENTS = True

CENTER_ON_SCROLL = True

SYNTAX = {}

EXTENSIONS = {}

BREAKPOINTS = {}
BOOKMARKS = {}


###############################################################################
# FILE MANAGER
###############################################################################

SUPPORTED_EXTENSIONS = [
    '.py',
    '.html',
    '.jpg',
    '.png',
    '.ui',
    '.css',
    '.json',
    '.ini']


###############################################################################
# PROJECTS DATA
###############################################################################

#PROJECT_TYPES = {'Python': None}
PROJECT_TYPES = {}

LANGS = []


###############################################################################
# EXPLORER
###############################################################################

SHOW_PROJECT_EXPLORER = True
SHOW_SYMBOLS_LIST = True
SHOW_WEB_INSPECTOR = False
SHOW_ERRORS_LIST = False

#Symbols handler per language (file extension)
SYMBOLS_HANDLER = {}

#Backward compatibility with older Qt versions
WEBINSPECTOR_SUPPORTED = True


###############################################################################
# WORKSPACE
###############################################################################

WORKSPACE = ""


###############################################################################
# FUNCTIONS
###############################################################################


def set_project_type_handler(project_type, project_type_handler):
    """
    Set a project type handler for the given project_type
    """
    global PROJECT_TYPES
    PROJECT_TYPES[project_type] = project_type_handler


def get_project_type_handler(project_type):
    """
    Returns the handler for the given project_type
    """
    global PROJECT_TYPES
    return PROJECT_TYPES.get(project_type)


def get_all_project_types():
    """
    Returns the availables project types
    """
    global PROJECT_TYPES
    return PROJECT_TYPES.keys()


def set_symbols_handler(file_extension, symbols_handler):
    """
    Set a symbol handler for the given file_extension
    """
    global SYMBOLS_HANDLER
    SYMBOLS_HANDLER[file_extension] = symbols_handler


def get_symbols_handler(file_extension):
    """
    Returns the symbol handler for the given file_extension
    """
    global SYMBOLS_HANDLER
    return SYMBOLS_HANDLER.get(file_extension)


###############################################################################
# LOAD SETTINGS
###############################################################################

def load_settings():
    qsettings = QSettings()
    #Globals
    global TOOLBAR_ORIENTATION
    global LANGUAGE
    global SHOW_START_PAGE
    global CONFIRM_EXIT
    global UI_LAYOUT
    global NOTIFY_UPDATES
    global PYTHON_PATH
    global PROFILES
    global EXECUTION_OPTIONS
    global SUPPORTED_EXTENSIONS
    global WORKSPACE
    global INDENT
    global MARGIN_LINE
    global REMOVE_TRAILING_SPACES
    global SHOW_TABS_AND_SPACES
    global ENABLE_COMPLETION_IN_COMMENTS
    global FONT_FAMILY
    global FONT_SIZE
    global HIGHLIGHT_VARIABLES
    global HIGHLIGHT_ALL_VARIABLES
    global SHOW_MARGIN_LINE
    global FIND_ERRORS
    global ERRORS_HIGHLIGHT_LINE
    global CHECK_STYLE
    global CHECK_HIGHLIGHT_LINE
    global CODE_COMPLETION
    global CENTER_ON_SCROLL
    global SHOW_PROJECT_EXPLORER
    global SHOW_SYMBOLS_LIST
    global SHOW_WEB_INSPECTOR
    global SHOW_ERRORS_LIST
    global BOOKMARKS
    global BREAKPOINTS
    global BRACES
    global HIDE_TOOLBAR
    #General
    HIDE_TOOLBAR = qsettings.value("window/hide_toolbar", False).toBool()
    TOOLBAR_ORIENTATION = qsettings.value(
        'preferences/general/toolbarOrientation', 1).toInt()[0]
    LANGUAGE = unicode(qsettings.value(
        'preferences/interface/language', '').toString())
    SHOW_START_PAGE = qsettings.value(
        'preferences/general/showStartPage', True).toBool()
    CONFIRM_EXIT = qsettings.value('preferences/general/confirmExit',
        True).toBool()
    UI_LAYOUT = qsettings.value('preferences/interface/uiLayout',
        0).toInt()[0]
    NOTIFY_UPDATES = qsettings.value(
        'preferences/general/notifyUpdates', True).toBool()
    PYTHON_PATH = unicode(
        qsettings.value('preferences/execution/pythonPath',
        'python').toString())
    profileDict = qsettings.value('ide/profiles', {}).toMap()
    for key in profileDict:
        PROFILES[unicode(key)] = [
            unicode(item.toString()) for item in profileDict[key].toList()]
    #EXECUTION OPTIONS
    EXECUTION_OPTIONS = unicode(
        qsettings.value('preferences/execution/executionOptions',
        '').toString())
    extensions = [unicode(item.toString()) for item in qsettings.value(
        'preferences/general/supportedExtensions', []).toList()]
    if extensions:
        SUPPORTED_EXTENSIONS = extensions
    WORKSPACE = unicode(qsettings.value(
        'preferences/general/workspace', "").toString())
    #Editor
    INDENT = qsettings.value('preferences/editor/indent',
        4).toInt()[0]
    MARGIN_LINE = qsettings.value('preferences/editor/marginLine',
        80).toInt()[0]
    pep8mod.MAX_LINE_LENGTH = MARGIN_LINE
    REMOVE_TRAILING_SPACES = qsettings.value(
        'preferences/editor/removeTrailingSpaces', True).toBool()
    SHOW_TABS_AND_SPACES = qsettings.value(
        'preferences/editor/showTabsAndSpaces', True).toBool()
    ENABLE_COMPLETION_IN_COMMENTS = qsettings.value(
        'preferences/editor/completeInComments', True).toBool()
    font_family = unicode(qsettings.value(
        'preferences/editor/fontFamily', "").toString())
    if font_family:
        FONT_FAMILY = font_family
    font_size = qsettings.value('preferences/editor/fontSize',
        0).toInt()[0]
    if font_size != 0:
        FONT_SIZE = font_size
    HIGHLIGHT_VARIABLES = qsettings.value(
        'preferences/editor/highlightVariables', True).toBool()
    HIGHLIGHT_ALL_VARIABLES = qsettings.value(
        'preferences/editor/highlightAllVariables', False).toBool()
    SHOW_MARGIN_LINE = qsettings.value(
        'preferences/editor/showMarginLine', True).toBool()
    FIND_ERRORS = qsettings.value('preferences/editor/errors',
        True).toBool()
    ERRORS_HIGHLIGHT_LINE = qsettings.value(
        'preferences/editor/errorsInLine', False).toBool()
    CHECK_STYLE = qsettings.value('preferences/editor/checkStyle',
        True).toBool()
    CHECK_HIGHLIGHT_LINE = qsettings.value(
        'preferences/editor/checkStyleInline', True).toBool()
    CODE_COMPLETION = qsettings.value(
        'preferences/editor/codeCompletion', True).toBool()
    CENTER_ON_SCROLL = qsettings.value(
        'preferences/editor/centerOnScroll', True).toBool()
    parentheses = qsettings.value('preferences/editor/parentheses',
        True).toBool()
    if not parentheses:
        del BRACES['(']
    brackets = qsettings.value('preferences/editor/brackets',
        True).toBool()
    if not brackets:
        del BRACES['[']
    keys = qsettings.value('preferences/editor/keys',
        True).toBool()
    if not keys:
        del BRACES['{']
    simpleQuotes = qsettings.value('preferences/editor/simpleQuotes',
        True).toBool()
    if not simpleQuotes:
        del BRACES["'"]
    doubleQuotes = qsettings.value('preferences/editor/doubleQuotes',
        True).toBool()
    if not doubleQuotes:
        del BRACES['"']
    #Projects
    SHOW_PROJECT_EXPLORER = qsettings.value(
        'preferences/interface/showProjectExplorer', True).toBool()
    SHOW_SYMBOLS_LIST = qsettings.value(
        'preferences/interface/showSymbolsList', True).toBool()
    SHOW_WEB_INSPECTOR = qsettings.value(
        'preferences/interface/showWebInspector', False).toBool()
    SHOW_ERRORS_LIST = qsettings.value(
        'preferences/interface/showErrorsList', False).toBool()
    #Bookmarks and Breakpoints
    bookmarks = qsettings.value('preferences/editor/bookmarks', {}).toMap()
    for key in bookmarks:
        BOOKMARKS[unicode(key)] = [
            i.toInt()[0] for i in bookmarks[key].toList()]
    breakpoints = qsettings.value('preferences/editor/breakpoints', {}).toMap()
    for key in breakpoints:
        BREAKPOINTS[unicode(key)] = [
            i.toInt()[0] for i in breakpoints[key].toList()]