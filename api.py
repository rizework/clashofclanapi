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


'self test'

if __name__ == '__main__':
    print 'test'
    api = API('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImMwZjhiNWVkLWUwNzktNDYyMC05ODYyLTcwY2Y1NDY5MTQ4ZiIsImlhdCI6MTQ3MjMwMTMzNywic3ViIjoiZGV2ZWxvcGVyLzQzNDNjMDY5LTBlZGEtZjNkOS04MmE5LWU0YmY5YWVmZjZlOCIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjExOC4xMDcuMTMwLjE2MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.kkWBKYgY3sPFW8pzD_TW2AO20tE1Y4sRk89Y4y8_3Q9cB-j2mynn89aEufz-MtQoTBQDUZUY--vFRek2PzJ71w')
    print api.search_clan('ozaki league')
    print api.get_clan_info('#QU9R8P09')
    print api.get_clan_members('#QU9R8P09')
    print api.get_clan_warlog('#QU9R8P09')  # 403 in case of private war log
