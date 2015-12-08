from collections import defaultdict
from dialog.schema.elements import Element


def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.iteritems():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.iteritems()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v) for k, v in t.attrib.iteritems())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

from xml.etree import cElementTree as ET
basestring = str

def dict_to_etree(d):
    def _to_etree(d, root):
        if not d:
            pass
        elif isinstance(d, basestring):
            root.text = d
        else:
            if isinstance(d, Element):
                d = d.create()

            if isinstance(d, dict):
                # sorted(d.items(), key=lambda t: t[1]["@order"] if "@order" in t[1] else 0)

                # for k, v in d.items():
                for key in list(sorted(d.keys(), key=lambda k: int(k[0]) if isinstance(k, tuple) else -1)):
                    key_string = key[1] if isinstance(key, tuple) else key
                    assert isinstance(key_string, basestring)
                    value = d[key]
                    if key_string.startswith('#'):
                        assert key_string == '#text' and isinstance(value, basestring)
                        root.text = value
                    elif key_string.startswith('@'):
                        assert isinstance(value, basestring)
                        root.set(key_string[1:], value)
                    elif isinstance(value, list):
                        for e in value:
                            _to_etree(e, ET.SubElement(root, key_string))
                    else:
                        _to_etree(value, ET.SubElement(root, key_string))
            else:
                assert d == 'invalid type', (type(d), str(d.create()))

    assert isinstance(d, dict) and len(d) == 1
    tag, body = next(iter(d.items()))
    node = ET.Element(tag)
    _to_etree(body, node)
    return node


