from django.shortcuts import render
from rest_framework import viewsets


# Create your views here.
class MultiSerializerViewSet(viewsets.ModelViewSet):
    serializers = {
        'default': None,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action,
                                    self.serializers['default'])

def root_page(request):
    return render(request, template_name='core/index.html')
