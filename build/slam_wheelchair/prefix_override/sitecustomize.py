import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/gesepulveda/tfm-robot-wheelchair/install/slam_wheelchair'
