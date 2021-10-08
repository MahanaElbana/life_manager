
from django.urls import path
from sticknote.views import NoteList,StickNoteCreate ,UserList, StickNoteDetail ,UserDetail

app_name='sticknote'

urlpatterns = [
    path("list/", NoteList.as_view(), name="list"),
    path("create/", StickNoteCreate.as_view(), name="create"),
    path("userlist/", UserList, name="userlist"),
    path("detail/<int:pk>", StickNoteDetail.as_view(), name="detail"), # admin
    path("userdetail/<int:pk>", UserDetail, name="userdetail"),
]

