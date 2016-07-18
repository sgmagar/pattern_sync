# pattern_sync

Clone the repository and do the following to get it working

1. python manage.py migrate
2. python manage.py loaddata fixtures.json
3. python manage.py createsuperuser			//to create superuser
4. Go to localhost:8000/admin		//enter superuser credential
5. Add the codes

Then it is working:

	Initially to get the patterns:
		url: localhost:8000/
		In response: {'pattern': ''}
	To update pattern:
		url: localhost:8000/update/pattern/
		post with data: {'code':'', 'pattern': ''}
		In response: {'status':'success', 'pattern':''} or {'status':'failure', 'pattern':}


I have used the string for the pattern so, create the string from the form element for post and split the string for updating the form element.