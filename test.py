from api import API

api = API('<APIKey>')
print api.search_clan('ozaki league')
print api.get_clan_info('#QU9R8P09')
print api.get_clan_members('#QU9R8P09')
print api.get_clan_warlog('#QU9R8P09')  # 403 in case of private war log