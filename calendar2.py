import click

@click.command()
def cli():

	click.echo(" Calender 2017")



	name = click.prompt("Enter your name:")
	#print name
	date = click.prompt("Enter your date :")
	#print date
	task = click.prompt("enter your task : ")
	#print task

	calender = {}
	calender['date'] = date
	calender['events'] = task
	#print calender

	user = {}
	user['name'] = name
	user['calender'] =calender
	#print user

	even_list = []
	even_list.append(calender)


	output ={user['name']:calender}
