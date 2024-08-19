"""
additional mappings for mountable packages
"""
from tutor import hooks
hooks.Filters.MOUNTED_DIRECTORIES.add_item(("openedx", "event-routing-backends"))

