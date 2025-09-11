import sys
import pack.saying
from pack.saying import goodBye

if len(sys.argv) == 2:
    pack.saying.hello(sys.argv[1])
    goodBye(sys.argv[1])
