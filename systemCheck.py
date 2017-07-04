import os
import platform

print(
	"Operating System: %s  %s  %s"
	% (os.name,platform.system(),platform.release())
	)