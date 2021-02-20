from django.urls import path
from myapp.views import(Register, LoginView, ProfileDetail, UserUpdateView,
                        logout_view, UsersList, addFriend, removeRequest, confrimRequest,
                        deletefriendship)
from django.conf.urls.static import static
from django.conf import settings

app_name = "myapp"
urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/<int:pk>", ProfileDetail.as_view(), name="profile"),
    path("profile/editprofile/<int:pk>",
         UserUpdateView.as_view(), name="editprofile"),
    path("logout/", logout_view, name="logout"),
    path("people/", UsersList.as_view(), name="people"),
    path("people/add/<int:pk>", addFriend, name="addfriend"),
    path("people/removerequest/<int:pk>", removeRequest, name="removerequest"),
    path("people/confirmfriendship/<int:pk>",
         confrimRequest, name="confirmfriendship"),
    path("people/deletefriendship/<int:pk>",
         deletefriendship, name='deletefriendship')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
