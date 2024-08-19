"""
run tasks asynchronously in dev mode (happens automatically in prod)
"""
from tutor import hooks
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-development-settings",
    "CELERY_ALWAYS_EAGER = False",
))

