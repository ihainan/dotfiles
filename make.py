#!/usr/bin/env python2.7
#coding:utf-8
# .dotfile 备份

import os
import shutil


def main():
	home_dir = os.getenv("HOME")
	bak_dir = home_dir + "/code/dotfiles"	# 备份目录
	old_dir = home_dir + "/code/old_dotfiles"	# 老文件目录
	files = "vimrc bashrc tmux.conf zshrc oh-my-zsh"

	# 创建 old_dir 目录
	print "Removing directory " + old_dir + "."
	shutil.rmtree(old_dir)
	print "Creating directory " + old_dir + "."
	os.mkdir(old_dir)

	# 对于 home 目录下的每一个文件
	for f in files.split(" "):
		if os.path.exists(home_dir + "/." + f):
			# 拷贝原文件（非 Symbol Link） 到 old_dir 目录
			print "Copying " + f + " in home to " + old_dir + "."
			# print "Move " + home_dir + "/." + f + " " + old_dir
			shutil.move(home_dir + "/." + f, old_dir)

		# 创建链接到 Home 目录
		print "Creating Symbol link of " + f + "."
		os.symlink(bak_dir + "/" + f, home_dir + "/." + f)
		# print "link -s " + bak_dir + "/" + f + " " + home_dir + "/." + f
	
	print ".....Done."

if __name__ == '__main__':
	main()
