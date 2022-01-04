import platform
import pulp

print("Platform   :", platform.platform())
print("Python ver.:", platform.python_version())
print("PuLP ver.  :", pulp.__version__)
pulp.pulpTestAll()

# $ python environment_check.py > log.txt
