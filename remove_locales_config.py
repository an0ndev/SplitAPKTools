import pathlib, os
import bs4

base = pathlib.Path ("base")

bad_xml = base / "res" / "xml" / "locales_config.xml"
if bad_xml.exists(): os.remove (bad_xml)

values_xml_path = base / "res" / "values" / "public.xml"

with open (values_xml_path, "r") as values_file: values_xml_text = values_file.read ()
values_xml = bs4.BeautifulSoup (values_xml_text, "xml")
resources = values_xml.resources
for public_tag in resources.find_all ("public"):
    if public_tag ["name"] != "locales_config": continue
    public_tag.decompose ()
    break
# else: raise Exception ("locales_config key not found")
with open (values_xml_path, "w") as values_file_out: values_file_out.write (values_xml.prettify ())

android_manifest_xml_path = base / "AndroidManifest.xml"
with open (android_manifest_xml_path, "r") as android_manifest_file: android_manifest_xml_text = android_manifest_file.read ()
android_manifest_xml = bs4.BeautifulSoup (android_manifest_xml_text, "xml")
application = android_manifest_xml.manifest.application
if "android:localeConfig" in application: del application ["android:localeConfig"]
with open (android_manifest_xml_path, "w") as android_manifest_file_out: android_manifest_file_out.write (android_manifest_xml.prettify ())
