import pathlib
import shutil
import re

base_dir = pathlib.Path("base")
xml_resources_dir = (base_dir / "res" / "xml")
src_network_security_config = pathlib.Path("network_security_config.xml")

if not xml_resources_dir.exists():
    xml_resources_dir.mkdir()

shutil.copy(src_network_security_config, xml_resources_dir / "network_security_config.xml")

manifest_dst = base_dir / "AndroidManifest.xml"

manifest_contents = manifest_dst.read_text()
if "networkSecurityConfig" not in manifest_contents:
    # very jank way to add ref to network security config in the <application> tag
    application_tag_re = r"" \
                         r"(?P<tag_start><application.*)" \
                         r"(?P<tag_end>>)"

    def inject_config(regex_match):
        return regex_match.group("tag_start") + \
            " android:networkSecurityConfig=\"@xml/network_security_config\"" + \
            regex_match.group("tag_end")

    updated_manifest = re.sub(application_tag_re, inject_config, manifest_contents)
    manifest_dst.write_text(manifest_contents)
