#!/usr/bin/env python2.7
#coding:utf-8
# Filename : ssh_key_setup.py
# Author : ihainan
# Created Date : 2014/12/17
# Description : ssh 配置脚本


import os
import sys
import subprocess


def main():
	# 基本路径信息
	home_dir = os.getenv("HOME")

	# 主机名与用户名
	hosts = ["vps2.ihainan.me", "lab.ihainan.me"]
	usernames = ["ihainan", "ihainan"]

	# 如果 ssh-key 不存在，生成
	if not os.path.exists(home_dir + "/.ssh/id_rsa.pub"):
		print "id_rsa.pub file is not existed, use rsa_keygen command to generate one."
		os.system("ssh-keygen -t rsa")	
		print "generate rsa_keygen successfully."	
	else:
		print "id_rsa.pub file is existed."
	
	# 逐一配置主机
	for i in range(len(hosts)):
		# 创建 ~/.ssh 目录
		command = "ssh " + usernames[i] + "@" + hosts[i] + " mkdir -p ~/.ssh"
		os.system(command)
		print command
		
		# 将 id_rsa.pub 拷贝到主机上
		command = "cat ~/.ssh/id_rsa.pub | ssh " + usernames[i] + "@" + hosts[i] + " 'cat >> ~/.ssh/authorized_keys'" 
		os.system(command)
		print command

if __name__ == '__main__':
	main()
