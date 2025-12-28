AUTHOR = 'Daniel Burke'
SITENAME = 'BargeHibernia'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Menu items
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (
    # ('Home', '/'),
    # ('About', '/pages/about.html'),
    # ('Latest News', '/pages/news.html'),
    # ('Publications & References', '/pages/publications.html'),
    # ('Vessels', '/category/vessels.html'),
    # ('Memories', '/pages/memories.html'),
    # ('Contact', '/pages/contact.html'),
    # ('Resources', '/pages/resources.html'),
    # ('Photos', '/pages/photos.html'),
    # ('Links', '/pages/links.html'),
)

FOOTERITEMS = (
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Vessels', '/category/vessels.html'),
    ('Publications & References', '/pages/publications.html'),
    ('Photos', '/pages/photos.html'),
    ('Tags', '/tags.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/simple'
