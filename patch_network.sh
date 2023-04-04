#!/bin/bash
set -e

base_dir="base"

if [ ! -d "$base_dir/res/xml" ]; then
	mkdir "$base_dir/res/xml"
fi

cp network_security_config.xml "$base_dir/res/xml/."
if ! grep -q "networkSecurityConfig" "$base_dir/AndroidManifest.xml"; then
  sed -E "s/(<application.*)(>)/\1 android\:networkSecurityConfig=\"@xml\/network_security_config\" \2 /" "$base_dir/AndroidManifest.xml" > "$base_dir/AndroidManifest.xml.new"
  mv "$base_dir/AndroidManifest.xml.new" "$base_dir/AndroidManifest.xml"
fi

