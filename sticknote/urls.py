
from django.urls import path
from sticknote.views import NoteList,NoteCreate, NoteDetail, UserDetail,UserList

app_name='sticknote'

urlpatterns = [
    path("list/", NoteList.as_view(), name="list"),
    path("create/", NoteCreate.as_view(), name="create"),
    path("userlist/", UserList, name="userlist"),
    path("detail/<int:pk>", NoteDetail.as_view(), name="detail"),
    path("userdetail/<int:pk>", UserDetail, name="userdetail"),
]

