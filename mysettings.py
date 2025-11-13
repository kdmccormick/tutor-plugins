"""
enables some settings
"""
from tutor import hooks
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-common-settings",
    """# mysettings
ENABLE_SPECIAL_EXAMS = True
PROCTORING_BACKENDS['mockprock'] = {
    'client_id': 'abcd',
    'client_secret': 'abcdsecret',
}
MFE_CONFIG.setdefault('authoring', {})['ENABLE_ACCESSIBILITY_PAGE'] = True
""",
))
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-lms-common-settings",
    """# mysettings
FEATURES['ENABLE_NEW_BULK_EMAIL_EXPERIENCE'] = False
""",
))
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-cms-common-settings",
    """# mysettings
""",
))

hooks.Filters.ENV_PATCHES.add_item((
    "openedx-production-settings",
    """# mysettings
""",
))
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-lms-production-settings",
    """# mysettings
""",
))
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-cms-production-settings",
    """# mysettings
""",
))

hooks.Filters.ENV_PATCHES.add_item((
    "openedx-development-settings",
    """# mysettings
""",
))
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-lms-development-settings",
    """# mysettings
""",
))
hooks.Filters.ENV_PATCHES.add_item((
    "openedx-cms-development-settings",
    """# mysettings
""",
))
