import sys
import yaml, wrapt
import typing, pathlib, shutil

class Tagged (wrapt.ObjectProxy):
    tag = None
    
    def __init__ (self, tag, wrapped):
        super ().__init__ (wrapped)
        self.tag = tag

class Loader (yaml.SafeLoader): pass
class Dumper (yaml.Dumper): pass

def construct_undefined(self, node):
    if isinstance(node, yaml.nodes.ScalarNode):
        value = self.construct_scalar(node)
    elif isinstance(node, yaml.nodes.SequenceNode):
        value = self.construct_sequence(node)
    elif isinstance(node, yaml.nodes.MappingNode):
        value = self.construct_mapping(node)
    else:
        assert False, f"unexpected node: {node!r}"
    return Tagged(node.tag, value)

Loader.add_constructor(None, construct_undefined)

def represent_tagged(self, data):
    assert isinstance(data, Tagged), data
    node = self.represent_data(data.__wrapped__)
    node.tag = data.tag
    return node

Dumper.add_representer (Tagged, represent_tagged)

src_yml = "base/apktool.yml"
target = sys.argv [1]
print (f"adding dnc for {target}")
with open (src_yml, "r") as yml_file:
    yml = yaml.load (yml_file, Loader = Loader)

print (f"{len (yml ['doNotCompress'])} entries in dnc list")

base = pathlib.Path (__file__).parent / "base"
target_dir = pathlib.Path (__file__).parent / target
for _file in [*list (target_dir.glob ("**/**")), *list (target_dir.glob ("**/*.*"))]:
    file_relpath = _file.relative_to (target_dir)
    file_path_in_base = base / file_relpath
    if not file_path_in_base.exists ():
        if _file.is_dir ():
            print (f"creating {file_relpath}")
            file_path_in_base.mkdir ()
        else:
           print (f"copying {file_relpath}")
           shutil.copy (_file, file_path_in_base)
           yml ["doNotCompress"].append (str (file_relpath))

print (f"{len (yml ['doNotCompress'])} entries in dnc list")

with open (src_yml, "w") as yml_file_out:
    yml_file_out.write (yaml.dump (yml, Dumper = Dumper))
