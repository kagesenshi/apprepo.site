from five import grok
from Products.CMFCore.utils import getToolByName
from zope.interface import Interface
from plone.app.layout.viewlets.interfaces import IPortalTop
from zope.component.hooks import getSite

from plone.app.users.userdataschema import IUserDataSchema
IUserDataSchema.get('fullname').required = True
IUserDataSchema.get('fullname').title = u'Display Name'
IUserDataSchema.get('fullname').description = u'Enter your desired display name'

class OIDProfileRedirect(grok.Viewlet):
    grok.viewletmanager(IPortalTop)
    grok.context(Interface)

    def render(self):
        membership = getToolByName(self.context, 'portal_membership')
        if membership.isAnonymousUser():
            return ''
        path = self.request.physicalPathFromURL(self.request.getURL())
        if path[-1] == '@@personal-information':
            return ''
        if not self.request.get('openid_provider'):
            return ''

        member = membership.getAuthenticatedMember()

        if member.fullname and member.email:
            return ''

        memberid = str(member.getId())

        if (memberid.startswith('http://') or
            memberid.startswith('https://')):
            site = getSite()
            self.request.response.redirect(
                '%s/@@personal-information' % site.absolute_url()
            )
        return ''
