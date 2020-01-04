from django.shortcuts import render, redirect

from .models import Track


def index(request):
	music = Track.objects.all()
	return render(request, 'index.html', {'music': music, 'error': None})


def add_track(request):
	autor = request.POST['autor']
	name = request.POST['name']
	minutes = request.POST['min']
	seconds = request.POST['sec']

	if (len(autor.replace(" ", "")) != 0 
	and len(name.replace(" ", "")) != 0 
	and minutes.isdigit() 
	and seconds.isdigit() 
	and 0 <= int(minutes) <= 180 
	and 0 <= int(seconds) <= 59):

		if len("0" + seconds) == 2:
			seconds = "0" + seconds

		track = Track(autor = autor, name = name, length = minutes + ":" + seconds)
		track.save()
		return redirect('/music/')

	else:
	    music = Track.objects.all()
	    return render(request, 'index.html', {'music': music, 'error': True})


def delete_track(request):
	try:
		track = Track.objects.get( id = request.POST['track_id'] )
		track.delete()
	except Track.DoesNotExist:
		pass

	return redirect('/music/')