# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started.

import octoprint.plugin

class MacrosPlugin(octoprint.plugin.StartupPlugin,
		octoprint.plugin.TemplatePlugin,
		octoprint.plugin.SettingsPlugin,
		octoprint.plugin.AssetPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! %s" %__plugin_description__)
    def get_settings_defaults(self):
        return dict(macro1="G28; Home XYZ",
			macro1Name = "Home All Axis",
			macro2="G28\nG90 \nG1 X100 F3000\nG1 Y100 F3000\nG1 Z100 F200",
			macro2Name = "Macro 2",
			macro3="",
			macro3Name = "Macro 3",)
    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]
    def get_assets(self):
        return dict(
            js=["js/macrosplugin.js"],
            css=["css/macrosplugin.css"]
        )

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "Macros Plugin"
__plugin_description__ = "This ia an awesome plugin to create user customised macros"
__plugin_implementation__ = MacrosPlugin()
