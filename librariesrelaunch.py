"""
all config needed to test the libraries relaunch project
"""
from tutor.hooks import Filters
Filters.ENV_PATCHES.add_item((
    "openedx-lms-common-settings",
    """\
MFE_CONFIG_OVERRIDES.setdefault('course-authoring', {})['LIBRARY_MODE'] = 'mixed'
"""
))
Filters.CLI_DO_INIT_TASKS.add_item((
    "cms",
    """\
(./manage.py cms waffle_flag --list | grep contentstore.new_studio_mfe.use_new_unit_page) || \\
./manage.py cms waffle_flag contentstore.new_studio_mfe.use_new_unit_page --create --everyone
"""
))
