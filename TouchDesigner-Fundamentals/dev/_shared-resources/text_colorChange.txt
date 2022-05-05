labels = parent().findChildren(name="annotate_networkLabel")

for each in labels:
	if each.parent().name == 'base_sweet16':
		pass
	else:
		each.par.Backcolorr = 0.189477
		each.par.Backcolorg = 0.21593
		each.par.Backcolorb = 0.333