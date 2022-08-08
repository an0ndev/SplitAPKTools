set -e

./pull.sh $1
./unpack.sh $2
python merge_resources.py
python remove_locales_config.py
./patch_network.sh
python remove_split_apk_attrib.py
