import click


@click.command()
def cli():

	click.echo(" Calender 2017")



	name = click.prompt("Enter your name:")
	date = click.prompt("Enter your date :")
	task = click.prompt("enter your task : ")

	calender = {}
	calender['date'] = date
	calender['events'] = task

	user = {}
	user['name'] = name
	user['calender'] =calender

	even_list = []
	even_list.append(calender)


	output ={user['name']:calender}

	for x in output:
		print(x)
		for y in output[x]:
			print(y,' : ', output[x][y])



if __name__ == '__main__':
	cli()