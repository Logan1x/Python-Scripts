## bobomailrc:
import os
from defaults import *

## main settings:

# please activate when sending bug reports
DEBUG = false

# main directory
app_dir = "/usr/local/bobomail"

# Choose here your pop3 server
pop3_host = "localhost"

# This enables IMAP-support. Otherwise POP3 is used
use_imap = false

# Place here the domain for the from-header
domain = "localdomain"

# For support of multiple domains
multi_domain = {"localhost": "localdomain"}

# You can change this to the hostname of a tcp/ip smtp server,
# or you can change the string to the path to your sendmail.
# On many systems the server will not relay even from localhost
# over tcp/ip, but will via the sendmail program
# smtp_host = "/usr/bin/env sendmail -bs"
smtp_host = "localhost"

# Enable/Disable support for multiple hosts/domains
multihosts = 1

# Here you can specify which hosts are allowed.
# If you leave it empty, every host is allowd
allowed_hosts = []

# "en_EN": English, "pt_BR": Brazilian Portuguese, "de_DE": German,
# "fi_FI": Finish, "es_ES": Spanish
language = "en_EN"

# Move the images directory somewhere to your document root
# or make an alias in your httpd.conf 
# like this:  
#  Alias /bobomail/ "/usr/local/bobomail/images/"
image_dir = "/bobomail/images" # relative to document root

# Only important if you use persistent cgi
pcgi_password = "secret123" 

# localisation
DateStrFormat = "%a, %d. %b %Y\n %H:%M"
DateShortStrFormat = "%D %T"

## the rest should be okay
# the following directories normally depend on the app_dir
var_dir = pathjoin(app_dir, "var")
log_dir =  pathjoin(app_dir, "var")
template_dir = pathjoin(app_dir, "dtml")   
locale_dir = pathjoin(app_dir, "locale")

# message-templates
mime_template = pathjoin(template_dir, "mimepart.html")
message_template = pathjoin(template_dir, "messagepart.html")
text_template = pathjoin(template_dir, "textpart.html")
html_template = pathjoin(template_dir, "htmlpart.html")
image_template = pathjoin(template_dir, "imagepart.html")
vcard_template = pathjoin(template_dir, "vcardpart.html")

# page-templates
template_template = pathjoin(template_dir, "template.html")
about_template = pathjoin(template_dir, "about.html")
addrs_template = pathjoin(template_dir, "addrs.html")
bounce_template = pathjoin(template_dir, "bounce.html")
login_template = pathjoin(template_dir, "login.html")
error_template = pathjoin(template_dir, "error.html")
compose_template = pathjoin(template_dir, "compose.html")
list_template = pathjoin(template_dir, "list.html")
mail_template = pathjoin(template_dir, "mail.html")
sent_template = pathjoin(template_dir, "sent.html")
prefs_template = pathjoin(template_dir, "prefs.html")
frames_template = pathjoin(template_dir, "frames.html")

# other files
pcgi_infofile = pathjoin(app_dir, "pcgibobomail.cgi")
log_filename = pathjoin(log_dir, "bobomail.log")
profile_stats = pathjoin(var_dir, "bobomail.profile")
bm_mimetypes = pathjoin(app_dir, "mime.types")
session_db_filename = pathjoin(var_dir, "bobomail_session.db")
user_db_filename = pathjoin(var_dir, "bobomail_user.db")
access_log = pathjoin(log_dir, "access.log")
error_log = pathjoin(log_dir, "error.log")


## please do not change below ##
auth_host = imap4_host = pop3_host
