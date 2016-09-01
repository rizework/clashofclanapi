import requests
import urllib


class API(object):
    BASE_URL = 'https://api.clashofclans.com/v1/'

    def __init__(self, token):
        """ Api instance Constructor
        """

        self.token = token
        self.headers = {'authorization': 'Bearer %s' % self.token, 'Accept': 'application/json'}

    def fetch(self, url, params=None):
        print "requesting endpoint : " + self.BASE_URL + url
        print "---------------"
        result = requests.get(self.BASE_URL + url, headers=self.headers, params=params)
        """if result.status_code == 403:
        pass"""

        if result.status_code != 200:
            return [result.status_code, result.json()]
        return result.json()

    def search_clan(self, clanname=None, warfrequency=None, locationid=None, minmembers=None, maxmembers=None,
                    minclanpoints=None, minclanlevel=None, limit=10, after=None, before=None):
        params = dict(name=clanname,
                      warfrequency=warfrequency,
                      minmembers=minmembers,
                      maxmembers=maxmembers,
                      minclanpoints=minclanpoints,
                      minclanlevel=minclanlevel,
                      limit=limit,
                      after=after,
                      before=before)
        return self.fetch('clans', params=params)

    def get_clan_info(self, tag):
        return self.fetch('clans/' + urllib.quote_plus(tag))

    def get_clan_members(self, tag):
        return self.fetch('clans/' + urllib.quote_plus(tag) + '/members')

    def get_clan_warlog(self, tag):
        return self.fetch('clans/' + urllib.quote_plus(tag) + '/warlog')
