from django.conf import settings

DEFAULT_PARSERS = [
    ('netdiff.OlsrParser', 'OLSRd (txtinfo/jsoninfo)'),
    ('netdiff.BatmanParser', 'batman-advanced (jsondoc/txtinfo)'),
    ('netdiff.BmxParser', 'BMX6 (q6m)'),
    ('netdiff.NetJsonParser', 'NetJSON NetworkGraph'),
    ('netdiff.CnmlParser', 'CNML 1.0'),
    ('netdiff.OpenvpnParser', 'OpenVPN')
]

PARSERS = DEFAULT_PARSERS + getattr(settings, 'NETJSONGRAPH_PARSERS', [])
SIGNALS = getattr(settings, 'NETJSONGRAPH_SIGNALS', None)
TIMEOUT = getattr(settings, 'NETJSONGRAPH_TIMEOUT', 8)
LINK_EXPIRATION = getattr(settings, 'NETJSONGRAPH_LINK_EXPIRATION', 60)
VISUALIZER_CSS = getattr(settings, 'NETJSONGRAPH_VISUALIZER_CSS', 'netjsongraph/css/style.css')
