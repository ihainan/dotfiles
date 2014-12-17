#!/usr/bin/env python2.7
#coding:utf-8
# Author : ihainan
# Created Date : 2014/10/11
# Description : .dotfile 备份

import os
import shutil


def main():
	# 路径 / 文件名初始化
	home_dir = os.getenv("HOME")
	bak_dir = os.getcwd()
	old_dir = bak_dir + "/../old_dotfiles"
	files = "vimrc bashrc tmux.conf zshrc oh-my-zsh"

	# 创建 old_dir 目录，如果存在则删除
	if os.path.exists(old_dir):
		print "Removing directory : " + old_dir + "."
		shutil.rmtree(old_dir)
	print "Creating directory : " + old_dir + "."
	os.mkdir(old_dir)

	# 对于 home 目录下的每一个文件
	for f in files.split(" "):
		# 如果是 symlink，直接删除
		if os.path.islink(home_dir + "/." + f):
			print home_dir + "/." + f + " is a symlink file, remove it."
			os.remove(home_dir + "/." + f)
			print "remove successfully."

		# 拷贝原文件（非 Symbol Link） 到 old_dir 目录
		if os.path.exists(home_dir + "/." + f):
			print "Copying " + f + " in home to " + old_dir + "."
			# print "Move " + home_dir + "/." + f + " " + old_dir
			shutil.move(home_dir + "/." + f, old_dir)

		# 创建链接到 Home 目录
		print "Creating Symbol link of " + f + "."
		os.symlink(bak_dir + "/" + f, home_dir + "/." + f)
	
	print ".........Done."

if __name__ == '__main__':
	main()
