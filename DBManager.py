from tinydb import TinyDB
import os
if not os.path.exists('db'):
    os.makedirs('db')

admin_list = TinyDB('db/admin_list.json')
channels_list = TinyDB('db/channels_list.json')
assistants_list = TinyDB('db/assistants_list.json')
mozilla_projects_list = TinyDB('db/mozilla_projects_list.json')
mozilla_italia_projects_list = TinyDB('db/mozilla_italia_projects_list.json')
social_list = TinyDB('db/social_list.json')

def populate_db():
    # managing entries only if it is the first time / one of the dbs is empty
    if(len(admin_list) == 0):
        admin_list.insert({'id': 240188083, 'username': '@Sav22999'})
        admin_list.insert({'id': 69903837, 'username': '@Mte90'})
        admin_list.insert({'id': 75870906, 'username': '@mone27'})
        admin_list.insert({'id': 810740389, 'username': '@dag7d'})
        admin_list.insert({'id': 123150516, 'username': '@edovio'})
        admin_list.insert({'id': 161975186, 'username': '@astrastefania'})

    if(len(channels_list) == 0):
        channels_list.insert({'name': 'Mozilla Italia News', 'username': '@mozitanews'})

    if(len(assistants_list) == 0):
        assistants_list.insert({'handler': 'Damiano Gualandri', 'username': '@dag7dev'})
        assistants_list.insert({'handler': 'Daniele Scasciafratte', 'username': '@mte90'})
        assistants_list.insert({'handler': 'Martin Ligabue', 'username': '@MartinLigabue'})
        assistants_list.insert({'handler': 'Sara Todaro', 'username': '@sara_tod'})
        assistants_list.insert({'handler': 'Saverio Morelli', 'username': '@Sav22999'})
        assistants_list.insert({'handler': 'Simone Massaro', 'username': '@mone27'})

    if(len(mozilla_projects_list) == 0):
        mozilla_projects_list.insert({'name': 'Common Voice', 'link': 'https://commonvoice.mozilla.org/it'})
        mozilla_projects_list.insert({'name': 'Firefox Desktop', 'link': 'https://www.mozilla.org/it/firefox/new/'})
        mozilla_projects_list.insert({'name': 'Firefox Fire Tv', 'link': 'https://www.amazon.it/Mozilla-Firefox-for-Fire-TV/dp/B078B5YMPD'})
        mozilla_projects_list.insert({'name': 'Firefox Mobile', 'link': 'https://www.mozilla.org/it/firefox/mobile/'})
        mozilla_projects_list.insert({'name': 'Firefox Monitor', 'link': 'https://monitor.firefox.com/'})
        mozilla_projects_list.insert({'name': 'Firefox Lockwise', 'link': 'https://www.mozilla.org/it/firefox/lockwise/'})
        mozilla_projects_list.insert({'name': 'IHR (Internet Health Report)', 'link': 'https://internethealthreport.org/'})
        mozilla_projects_list.insert({'name': 'MDN Web Docs', 'link': 'https://developer.mozilla.org/it/'})

    if(len(mozilla_italia_projects_list) == 0):
        mozilla_italia_projects_list.insert({'name': 'Common Voice Tool', 'link': 'https://github.com/dag7dev/common-voice-tool'})
        mozilla_italia_projects_list.insert({'name': 'Mozilla Italia Hub Bot', 'link': 'https://github.com/Sav22999/mozitahub_bot'})
        mozilla_italia_projects_list.insert({'name': 'Mozilla Italia Antispam Bot', 'link': 'https://github.com/Sav22999/mozitaantispam_bot'})
        mozilla_italia_projects_list.insert({'name': 'Vademecum Generale, Tecnico e Common Voice', 'link': 'https://github.com/MozillaItalia/firefox-vademecum/'})

    if(len(social_list) == 0):
        social_list.insert({'name': 'Facebook', 'link': 'https://www.facebook.com/mozillaitalia'})
        social_list.insert({'name': 'Twitter', 'link': 'https://twitter.com/mozillaitalia'})
        social_list.insert({'name': 'Youtube', 'link': 'https://www.youtube.com/channel/UCsTquqVS0AJxCf4D3n9hQ1w'})
        social_list.insert({'name': 'Discourse', 'link': 'https://discourse.mozilla.org/c/community-portal/mozilla-italia'})
        social_list.insert({'name': 'Mozilla Community', 'link': 'https://community.mozilla.org/groups/mozilla-italia'})
        social_list.insert({'name': 'Matrix', 'link': 'https://chat.mozilla.org/#/room/#mozilla-italia:mozilla.org'})