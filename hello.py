import os
import getpass

# 尝试使用 os.getlogin() 获取当前登录用户名，某些环境下可能失败，提供回退
try:
	username = os.getlogin()
except OSError:
	# Windows 下通常有 USERNAME 环境变量；再退一步使用 getpass.getuser()
	username = os.environ.get('USERNAME') or getpass.getuser() or 'unknown'

# 将打印改为使用 f-string 简洁表达
print(f"你好！{username}")
