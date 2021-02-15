from rest_framework import generics
from form.models import Post
#For easy Rendering of Json to python
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status

# UsingDjango's generic class and overriding create method.
class List_Create_FormData(generics.ListCreateAPIView):
    queryset = Post.objects.all().distinct()
    serializer_class = PostSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # Checking if data format is correct.
        try: 
            serializer.is_valid(raise_exception=True)
        except:
            content = {"Bad Request : Data not valid!"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # Checking if duplicate data exists
        try:
            self.perform_create(serializer)
        except:
            content = {"Conflict : Data Already exists!"}
            return Response(content,status=status.HTTP_409_CONFLICT)
        return Response(serializer.data["id"], status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()

# UsingDjango's generic class and overriding edit method.
class Edit_Retrieve_FormData(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        # Checking if data format is correct.
        try: 
            serializer.is_valid(raise_exception=True)
        except:
            content = {"Bad Request : Data not valid!"}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # Checking if duplicate data exists
        try:
            self.perform_update(serializer)
        except:
            content = {"Conflict : Data Already exists!"}
            return Response(content,status=status.HTTP_409_CONFLICT)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
