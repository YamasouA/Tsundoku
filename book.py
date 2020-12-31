import json
import getpass

bookmark_path = 'C:/Users/{username}/AppData/Local/Google/Chrome/User Data/Default/bookmarks'.format(username=getpass.getuser())


# Get the json of user's Chrome bookmark.
with open(bookmark_path, encoding='utf-8') as f:
    bookmark_data = json.load(f)



print(type(bookmark_data))

print(bookmark_data.keys())

print(bookmark_data['checksum'])
print(bookmark_data['version'])

print(bookmark_data['roots'].keys())

bookmark_bar = bookmark_data['roots']['bookmark_bar']
print(bookmark_bar.keys())
print(bookmark_bar['name'])
for entry in bookmark_bar['children']:
    if entry['type'] == 'folder':
        print('{type}: {name}'.format(**entry))
    else:
        print('{type}: {name} - {url}'.format(**entry))