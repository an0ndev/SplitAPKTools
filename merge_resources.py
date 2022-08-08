import pathlib
import bs4

base = pathlib.Path ("base")

for target in [x for x in pathlib.Path (__file__).parent.glob ("split_config*/res/values*/*.xml") if x.is_file ()]:
    rel_path = target.relative_to (target.parent.parent.parent)
    # if str (rel_path) != "res/values/public.xml": continue
    if not (base / rel_path).exists (): continue
    og_p = base / rel_path
    other_p = target
    print (f"source {og_p} other {other_p}")
    with open (og_p, "r") as og_f: og_t = og_f.read ()
    with open (other_p, "r") as other_f: other_t = other_f.read ()
    print (f"boi {len (og_t)} {len (other_t)}")
    og_s = bs4.BeautifulSoup (og_t, "xml")
    old_len = len (og_s.prettify ())
    other_s = bs4.BeautifulSoup (other_t, "xml")
    og_r = og_s.resources
    og_r_pretty = og_r.prettify ()
    other_r = other_s.resources
    # print (og_r)
    # print (other_r)
    print (len (list (other_r.children)))
    existing_names = [item ["name"] for item in filter (lambda _i: not isinstance (_i, str), og_r.contents)]
    # print (other_r.contents)
    for i, child in enumerate (other_r.contents):
        str_repr_child = str (repr (child))
        # print (f"STR_REPR_CHILD is >>{str_repr_child}<<")
        if isinstance (child, str): continue
        print (f"{i} {repr (child)}")
        if child ["name"] in existing_names:
            print (f"duplicate value")
            continue
        og_r.append (child)
    print (f"new len {len (og_s.prettify ())} vs old {old_len}")
    with open (og_p, "w") as og_f_o: og_f_o.write (og_s.prettify ())
