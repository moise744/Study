1.When the user make the request that request is prepared by the browser and then send it to the wsgi server .and then server receives the request and then after receiving the request ,wsgi sends it to the django handler method and then this methods does its job where the middlewares also does it job like preparing the  request object .

and then  in the requesr we get:

request={
    POST:{},
    GET:{},
    FILES:{},
    COOKIES:{},
    META:{HTTP_AUTHORIZATION:'BEARER ERTYUJBVDFGHJ',HTTP_CONTENT_TYPE,HTTP_CONTENT_LENGTH}
}

THEN THE MIDDLEAWRES ADDS THINGS LIKE:
method,
user,
session,

so far we have ready request object to be used .

when we say path is the full url from the root urls.py:api/users/
messages.and remember we can store the sessions in the database or the cashe or somewhere else.
and at this point the session is the session based so from django.utils.translation import ugettext_lazy as _

and then other attributes that are put by the custom middleaware are set there and then we get the complete one
content type,content length,

as we know there is something you didnt know did you know that when the request is made then django urls handler finds the matching urlpatterns an dit does that so that it finds the method to call asssociated with it so that it can call that method  and then after find the match means the url pattern to typed and then one that is in the urls.py after finding it then it calls your method  nothing more than that.

so means we have to write the urls patterns because we must have them. that is the reason why when we do like from rest_framework import routers this is the file we are importing that is responsible for creating the urlspatterns for us so that when django is doing the search ,it finds the match pattersn.__path__
from rest_framework.routers import DefaultRouter
routers=DefaultRouter()