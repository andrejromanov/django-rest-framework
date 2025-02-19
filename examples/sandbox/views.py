"""The root view for the examples provided with Django REST framework"""

from django.core.urlresolvers import reverse
from djangorestframework.resource import Resource


class Sandbox(Resource):
    """This is the sandbox for the examples provided with [Django REST framework](http://django-rest-framework.org).

    These examples are provided to help you get a better idea of the some of the features of RESTful APIs created using the framework.

    All the example APIs allow anonymous access, and can be navigated either through the browser or from the command line...

        bash: curl -X GET http://api.django-rest-framework.org/                           # (Use default emitter)
        bash: curl -X GET http://api.django-rest-framework.org/ -H 'Accept: text/plain'   # (Use plaintext documentation emitter)

    The examples provided: 
   
    1. A basic example using the [Resource](http://django-rest-framework.org/library/resource.html) class.
    2. A basic example using the [ModelResource](http://django-rest-framework.org/library/modelresource.html) class.
    3. An basic example using Django 1.3's [class based views](http://docs.djangoproject.com/en/dev/topics/class-based-views/) and djangorestframework's [EmitterMixin](http://django-rest-framework.org/library/emitters.html).
    4. A generic object store API.
    5. A code highlighting API.
    6. A blog posts and comments API.

    Please feel free to browse, create, edit and delete the resources in these examples."""
    allowed_methods = anon_allowed_methods = ('GET',)

    def get(self, request, auth):
        return [{'name': 'Simple Resource example', 'url': reverse('example-resource')},
                {'name': 'Simple ModelResource example', 'url': reverse('my-model-root-resource')},
                {'name': 'Simple Mixin-only example', 'url': reverse('mixin-view')},
                {'name': 'Object store API', 'url': reverse('object-store-root')},
                {'name': 'Code highlighting API', 'url': reverse('pygments-root')},
                {'name': 'Blog posts API', 'url': reverse('blog-posts')}]
