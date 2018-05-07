# -*- coding: utf-8 -*-

# Gdax
# https://api.gdax.com/
# By Sander Van de Moortel <sander.vandemoortel@gmail.com>

from exchange import Exchange, CURRENCY


class Gdax(Exchange):
    CONFIG = {
        'name': 'Gdax',
        'ticker': 'https://api.gdax.com/products/',
        'asset_pairs': [
            {
                'isocode': 'XXBTZUSD',
                'pair': 'BTC-USD',
                'name': 'BTC to USD',
                'currency': CURRENCY['usd']
            },
            {
                'isocode': 'XXBTZEUR',
                'pair': 'BTC-EUR',
                'name': 'BTC to EUR',
                'currency': CURRENCY['eur']
            },
            {
                'isocode': 'XXBTZGBP',
                'pair': 'BTC-GBP',
                'name': 'BTC to GBP',
                'currency': CURRENCY['gbp']
            },
            {
                'isocode': 'XXETZUSD',
                'pair': 'ETH-USD',
                'name': 'ETH to USD',
                'currency': CURRENCY['usd']
            },
            {
                'isocode': 'XXETZEUR',
                'pair': 'ETH-EUR',
                'name': 'ETH to EUR',
                'currency': CURRENCY['eur']
            },
            {
                'isocode': 'XXLTZUSD',
                'pair': 'LTC-USD',
                'name': 'LTC to USD',
                'currency': CURRENCY['usd']
            },
            {
                'isocode': 'XXLTZEUR',
                'pair': 'LTC-EUR',
                'name': 'LTC to EUR',
                'currency': CURRENCY['eur']
            },
            {
                'isocode': 'XXBCZEUR',
                'pair': 'BCH-EUR',
                'name': 'BCH to EUR',
                'currency': CURRENCY['eur']
            },
            {
                'isocode': 'XXBCZUSD',
                'pair': 'BCH-USD',
                'name': 'BCH to USD',
                'currency': CURRENCY['usd']
            },
        ]
    }

    def get_discovery_url(self):
        return self.config.get('ticker')

    def _parse_discovery(self, result):
        asset_pairs = []
        for asset in result:
            base = asset.get('base_currency')
            quote = asset.get('quote_currency')

            asset_pair = {
                'pair': asset.get('id'),
                'base': base,
                'quote': quote,
                'name': base + ' to ' + quote,
                'currency': quote.lower(),
                'volumecurrency': base
            }

            asset_pairs.append(asset_pair)

        return asset_pairs

    def _get_ticker_url(self):
        return self.config.get('ticker') + self.pair + '/ticker'

    def _parse_ticker(self, asset):
        cur = asset.get('price')
        bid = asset.get('bid')
        ask = asset.get('ask')
        vol = asset.get('volume')

        return {
            'cur': cur,
            'bid': bid,
            'high': None,
            'low': None,
            'ask': ask,
            'vol': vol
        }
