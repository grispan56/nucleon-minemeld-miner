import logging
import json

import requests

from minemeld.ft.basepoller import BasePollerFT

LOG = logging.getLogger(__name__)


class Miner(BasePollerFT):
    def configure(self):
        super(Miner, self).configure()

        self.polling_timeout = self.config.get('polling_timeout', 30)
        self.verify_cert = self.config.get('verify_cert', True)
        self.url = 'http://api.nucleoncyber.com/feed/ActiveThreats'

        # The basic authentication details
        self.auth_user = self.config.get('auth_user')
        self.auth_pass = self.config.get('auth_pass')
        self.usrn = self.config.get('usrn')
        self.client_id = self.config.get('client_id')
        self.limit = 1

    def _build_iterator(self, item):
        # builds the request and retrieves the page
        # Make the request to the API
        r = requests.post(endpoint_url, data = {'usrn':self.usrn,'clientID':self.client_id,'limit':self.limit}, auth=(self.auth_user, self.auth_pass))

        try:
            r.raise_for_status()
        except:
            LOG.debug('%s - exception in request: %s %s',
                      self.name, r.status_code, r.content)
            raise

        all_ips = list()
        counter = 0

        # build list of ip addresses
        # for doc in data['data']:
        #     all_ips.append(doc['ip'])
        #     counter = counter + 1
        result = r[data][0]['ip']
        return result

    def _process_item(self, item):

        #ndicator = item
        value = {
            'type': 'IPv4',
            'confidence': 100
        }

        return [[item, value]]



