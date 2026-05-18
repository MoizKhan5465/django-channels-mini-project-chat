from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render(request, 'Chat/lobby.html')

def room(request, room_name):
    return render(request, 'Chat/room.html', {
        'room_name': room_name
    })