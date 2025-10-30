import os
import getpass

# 尝试使用 os.getlogin() 获取当前登录用户名，某些环境下可能失败，提供回退
try:
	username = os.getlogin()
except OSError:
	# Windows 下通常有 USERNAME 环境变量；再退一步使用 getpass.getuser()
	username = os.environ.get('USERNAME') or getpass.getuser() or 'unknown'

# 不使用 f-string，使用简单的字符串拼接打印问候语
print("你好！" + username)

