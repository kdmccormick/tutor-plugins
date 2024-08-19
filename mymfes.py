"""
whittle down list of mfes to save build time
"""
from tutormfe.hooks import MFE_APPS
@MFE_APPS.add()
def _remove_extra_mfes(apps: dict) -> dict:
    return {
        **{
            app_name: app
            for app_name, app in apps.items()
            if app_name in [
                "learning",
                "course-authoring",
                "authn",
            ]
        },
    }
if False:  # disabled for now
    @MFE_APPS.add()
    def _add_support_tools(apps: dict) -> dict:
        return {
            **apps,
            "support-tools": {
                "repository": "https://github.com/openedx/frontend-app-support-tools",
                "port": 2007,
                "version": "master",
            },
        }
