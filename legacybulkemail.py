"""
enables the legacy bulk email tool
"""
from tutor import hooks
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-lms-common-settings",
    "FEATURES['ENABLE_NEW_BULK_EMAIL_EXPERIENCE'] = False"
), priority=90)
