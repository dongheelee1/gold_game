from django.shortcuts import render, HttpResponse, redirect
import random
import datetime

def index(request):
	request.session.clear
	if 'gold_count' not in request.session:
		request.session['gold_count'] = 0
	if 'gold_messages' not in request.session:
		request.session['gold_messages'] = []

	return render(request, 'gold/index.html')

def process_money(request):
	# print request.POST['building']

	if request.POST['building'] == 'farm':
		rand = random.randint(10, 20)
	elif request.POST['building'] == 'cave':
		rand = random.randint(5, 10)
	elif request.POST['building'] == 'house':
		rand = random.randint(2, 5)
	elif request.POST['building'] == 'casino':
		rand = random.randint(-50, 50)

	request.session['gold_count'] += rand
	date = datetime.datetime.now().strftime('%x %I:%M %p')

	if rand >= 0:
		string = "You won " + str(rand) + " golds. (" + str(date) + ")"
	else:
		string = "You lost " + str(abs(rand)) + " golds. (" + str(date) + ")"
	print string
	request.session['gold_messages'].insert(0, string)
	return redirect('/')
		
def reset(request):
	request.session.clear()
   	return redirect('/')


