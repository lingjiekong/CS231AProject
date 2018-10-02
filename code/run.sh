# setup directory for temporary files
# mkdir temp

# Yolo Hand Detector
# python python/yolo.py $1 > temp/yolo.txt # HERE
# python bbox.py > bbox.txt

# Semantic Segmentation
# python grabcut.py bbox.txt
# python applymask.py ../data/egocentric/can-opener_3165831444_greg1/
# python applymask.py $1

# ORB-SLAM
# python timestamp.py $1
# python timestamp.py ../data/egocentric/can-opener_3165831444_greg1/
# python associate.py rgb.txt depth.txt > associations.txt
# ./ORB_SLAM2/Examples/RGB-D/ego ORB_SLAM2/Vocabulary/ORBvoc.txt ORB_SLAM2/Examples/RGB-D/ego.yaml ../data/egocentric/can-opener_3165831444_greg1/ associations.txt
# ./ORB_SLAM2/Examples/RGB-D/ego ORB_SLAM2/Vocabulary/ORBvoc.txt ORB_SLAM2/Examples/RGB-D/ego.yaml $1 associations.txt

# dense mapping
# ???