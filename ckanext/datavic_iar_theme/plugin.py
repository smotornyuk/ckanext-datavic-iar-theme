import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import helpers


class DatavicIARThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'datavic_iar_theme')

    # ITemplateHelpers

    def get_helpers(self):
        ''' Return a dict of named helper functions (as defined in the ITemplateHelpers interface).
        These helpers will be available under the 'h' thread-local global object.
        '''
        return {
            'organization_list': helpers.organization_list,
            'group_list': helpers.group_list,
            'format_list': helpers.format_list,
            'get_parent_site_url': helpers.get_parent_site_url,
        }
