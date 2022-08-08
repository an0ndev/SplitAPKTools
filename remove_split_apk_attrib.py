import pathlib
import bs4

base = pathlib.Path ("base")

android_manifest_xml_path = base / "AndroidManifest.xml"
with open (android_manifest_xml_path, "r") as android_manifest_file: android_manifest_xml_text = android_manifest_file.read ()
android_manifest_xml = bs4.BeautifulSoup (android_manifest_xml_text, "xml")
application = android_manifest_xml.manifest.application
del application ["android:isSplitRequired"]
with open (android_manifest_xml_path, "w") as android_manifest_file_out: android_manifest_file_out.write (android_manifest_xml.prettify ())
