#python
import lx
import ntpath
import glob


def createQuad(sizeX, sizeY, name):
	lx.eval("layer.new")
	lx.eval("item.name {0}".format(name) )
	lx.eval("tool.set prim.cube on 0")
	lx.eval("tool.reset prim.cube")
	lx.eval("tool.setAttr prim.cube flip false")
	lx.eval("tool.setAttr prim.cube sizeX {0}".format(float(sizeX/100)) )
	lx.eval("tool.setAttr prim.cube sizeY {0}".format(float(sizeY/100)) )
	lx.eval("tool.setAttr prim.cube sizeZ 0.0")

	lx.eval("tool.setAttr prim.cube cenX 0")
	lx.eval("tool.setAttr prim.cube cenY 0")
	lx.eval("tool.setAttr prim.cube cenZ 0")
	lx.eval("tool.doApply") 
	lx.eval("tool.set prim.cube off")
	
	#hacks didn't check to see if I could rotate by a value
	lx.eval("uv.rotate")
	lx.eval("uv.rotate")
	lx.eval("uv.rotate")



lx.eval("dialog.setup dir");
lx.eval("dialog.title {Choose Folder}");
lx.eval("dialog.open");
file_path = lx.eval("dialog.result ?")

ims = lx.service.Image()
images = glob.glob("{0}/*.png".format(file_path))

for img in images:
	im = ims.Load(img);
	width, height = im.Size()
	createQuad(width, height, ntpath.basename(img) )


