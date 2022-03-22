def set_annotate_width(width):
	print("set annotate width")
	annotate_comps = parent().findChildren(type=annotateCOMP)
	for each_op in annotate_comps:
		if 'id' not in each_op.tags:
			each_op.par.Bodylimitwidth = True
			each_op.par.Bodymaxwidth = width
			print(each_op)

def set_external_path():
	print("set external path")
	targets = parent().findChildren(depth=1, tags=['curriculum'])
	for each_op in targets:
		if each_op.par.externaltox == '':
			ext_path = f"working/{each_op.name}.tox"
			each_op.par.externaltox = ext_path
			each_op.par.savebackup = False
			print(f"Setting External path for {each_op}")
		else:
			print(f"-->Skipping {each_op}")

set_annotate_width(400)
set_external_path()