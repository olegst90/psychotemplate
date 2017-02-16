#!/usr/bin/env python

import sys
import os
import MySQLdb
from shutil import copytree

import pushconfig

print "Copying files..."
dst = pushconfig.site_root + "/public/themes/" + pushconfig.in_name
os.makedirs(dst)
print "copying to " + dst
copytree("fonts", dst + "/fonts")
copytree("css", dst + "/css")
copytree("images", dst + "/images")
print "Copying layout to db..."
db=MySQLdb.connect(host=pushconfig.db_host,user=pushconfig.db_user, passwd=pushconfig.db_pass,db=pushconfig.db_name)

st = "update layout set content = %s where name = %s"

file = file(pushconfig.in_file, "r")

content = file.read()
file.close()
db.cursor().execute(st,[content, pushconfig.in_name])
