from django.urls import path
from myapp.views import(Register, LoginView, ProfileDetail, UserUpdateView,
                        logout_view, UsersList, addFriend, removeRequest, confrimRequest,
                        deletefriendship, UserRequerstsDetails, PostCreateView, PostUpdateView, deletepost,
                        PostsList, addcomment, CommetDetail)
from django.conf.urls.static import static
from django.conf import settings

app_name = "myapp"
urlpatterns = [
    path("register/", Register.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/<int:pk>", ProfileDetail.as_view(), name="profile"),
    path("profile/editprofile/<int:pk>",
         UserUpdateView.as_view(), name="editprofile"),
    path("profile/userrequestsdetails/<int:pk>",
         UserRequerstsDetails.as_view(), name="requestsdetails"),
    path("logout/", logout_view, name="logout"),
    path("people/", UsersList.as_view(), name="people"),
    path("people/add/<int:pk>", addFriend, name="addfriend"),
    path("people/removerequest/<int:pk>", removeRequest, name="removerequest"),
    path("people/confirmfriendship/<int:pk>",
         confrimRequest, name="confirmfriendship"),
    path("people/deletefriendship/<int:pk>",
         deletefriendship, name='deletefriendship'),
    path("posts/", PostsList.as_view(), name="posts"),
    path("posts/create", PostCreateView.as_view(), name="createpost"),
    path("posts/<int:userid>/edit/<int:pk>",
         PostUpdateView.as_view(), name="editpost"),
    path("posts/<int:userid>/delete/<int:pk>", deletepost, name="deletepost"),
    path("posts/<int:postid>/comments/add/user/<int:userid>",
         addcomment, name='addcomment'),
    path("posts/<int:pk>/comments/", CommetDetail.as_view(), name='postcomments'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
