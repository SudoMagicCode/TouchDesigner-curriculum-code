import datetime
date = datetime.date.today()

project_name = f"{project.name.split('.')[0]}-{date}-review.toe"

all_ops = root.findChildren(type=COMP)

for each in all_ops:
	if each.par.externaltox != '':
		each.par.externaltox = ''

project.save(project_name)
project.quit(force=True)