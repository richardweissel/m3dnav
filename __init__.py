# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class Me3dNavbarPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin):
    def on_after_startup(self):
        self._logger.info("After Startup : Me3D Nav Bar Plugin")

__plugin_name__ = "Me3D NavBar"
__plugin_version__ = "1.0.0"
__plugin_description__ = "A Nav Bar plugin for Me3D"
__plugin_implementation__ = Me3dNavbarPlugin()


