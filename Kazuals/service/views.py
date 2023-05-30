from django.shortcuts import render

from service.services.splash_quiz import easy_level, hard_level


def splash_quiz(request):
    data = hard_level()
    return render(request, 'service/splash_quiz.html', {"answer": data['answer'],
                                                        'splash': data['splash'],
                                                        'img_name': data['img_name']})
