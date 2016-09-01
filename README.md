This module is used to call official clan of clan api.


Get your api key from https://developer.clashofclans.com


```sh
from api import API

api = API('<APIKEY>')
api.search_clan('ozaki league')
api.get_clan_info('#QU9R8P09')
api.get_clan_members('#QU9R8P09')
api.get_clan_warlog('#QU9R8P09')  # returns 403 in case of private war log
'''