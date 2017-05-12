import click

@click.command():
def cli():
    '''
    Welcome to Team b's calender app

    '''


	click.echo(" Calender 2017")



	name = click.prompt("Enter your name:")
	date = click.prompt("Enter your date :")
	task = click.prompt("enter your task : ")

