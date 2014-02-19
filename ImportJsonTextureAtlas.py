#python
import json
import lx
import os
import ntpath

lx.eval("dialog.setup fileOpen");
lx.eval("dialog.title {Select a JSON file}");
lx.eval("dialog.fileType text");
lx.eval("dialog.open");
file_path = lx.eval("dialog.result ?")
file_name, file_ext = os.path.splitext(os.path.basename(file_path))

def createQuad(rect, rotated, size):
	tmpw = float(rect['w'])/size['w'];
	tmph = float(rect['h'])/size['h'];

	px = float(rect['x'])/size['w'];
	py = 1 - (float(rect['y'])/size['h']);
	w =  tmph if rotated else tmpw;
	h =  tmpw if rotated else tmph;

	lx.eval("tool.setAttr prim.pen current 0");
	lx.eval("tool.setAttr prim.pen posX {0}".format(px));
	lx.eval("tool.setAttr prim.pen posY {0}".format(py));
	lx.eval("tool.setAttr prim.pen posZ {0}".format(0));	
	lx.eval("tool.setAttr prim.pen current 1");
	lx.eval("tool.setAttr prim.pen posX {0}".format(px+w));
	lx.eval("tool.setAttr prim.pen posY {0}".format(py));
	lx.eval("tool.setAttr prim.pen posZ {0}".format(0));
	lx.eval("tool.setAttr prim.pen current 2");
	lx.eval("tool.setAttr prim.pen posX {0}".format(px+w));
	lx.eval("tool.setAttr prim.pen posY {0}".format(py-h));
	lx.eval("tool.setAttr prim.pen posZ {0}".format(0));
	lx.eval("tool.setAttr prim.pen current 3");
	lx.eval("tool.setAttr prim.pen posX {0}".format(px));
	lx.eval("tool.setAttr prim.pen posY {0}".format(py-h));
	lx.eval("tool.setAttr prim.pen posZ {0}".format(0));


def path_leaf(path):
    head, tail = ntpath.split( path )
    return head

with open(file_path, 'r') as content_file:
    content = content_file.read();

framedata = json.loads(content);

lx.eval("select.itemType mesh");
lx.eval("delete");
lx.eval("layer.new");
lx.eval("select.typeFrom vertex;edge;polygon;item;pivot;center;ptag true");
lx.eval("select.type vertex");
lx.eval("tool.set prim.pen flush 0");

lx.eval("tool.set prim.pen type polygon");
lx.eval("tool.set prim.pen on 0");
lx.eval("tool.setAttr prim.pen current 0");
lx.eval("tool.setAttr prim.pen uvs true");
lx.eval("tool.setAttr prim.pen dist 0.0072");

for k in framedata['frames']:
	lx.eval("layer.new");
	lx.eval("item.name {0} mesh".format(k['filename']))
	createQuad( k['frame'], k['rotated'], framedata['meta']['size'])
	lx.eval("tool.doApply");

lx.eval("select.itemType mesh");
lx.eval("select.cut");
lx.eval("delete");
lx.eval("layer.new");
lx.eval("select.paste");
lx.eval("select.type polygon");
lx.eval("item.name {0} mesh".format(file_name));
lx.eval("select.all");
lx.eval("clip.addStill {0}/{1}".format(path_leaf(file_path),  framedata['meta']['image']));
