from five import grok
from plone.app.layout.viewlets.interfaces import IPortalHeader
from zope.interface import Interface
from zope.component.hooks import getSite

def _patch_personalbar_openid():
    from plone.app.layout.viewlets.common import PersonalBarViewlet
    import urlparse

    if getattr(PersonalBarViewlet, '__openid_patched', False):
        return

    _orig_update = PersonalBarViewlet.update
    def update(self):
        result = _orig_update(self)
        if getattr(self, 'user_name', None) is None:
            return result

        if 'http://' in self.user_name or 'https://' in self.user_name:
            self.user_name = 'openid:%s' % urlparse.urlparse(self.user_name).netloc

        return result

    PersonalBarViewlet.update = update
    PersonalBarViewlet.__openid_patched = True

_patch_personalbar_openid()
