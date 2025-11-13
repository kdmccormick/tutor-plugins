"""
enables the lti_consumer block in v2 libs
"""
from tutor import hooks
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-cms-common-settings",
    "LIBRARY_ENABLED_BLOCKS.append('lti_consumer')"
), priority=90)
