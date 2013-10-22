#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
	#This is for live settings:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmarks.settings")
	
	#This is for test settings:
	#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bookmarks.TESTsettings")
	
	
	from django.core.management import execute_from_command_line
	execute_from_command_line(sys.argv)
