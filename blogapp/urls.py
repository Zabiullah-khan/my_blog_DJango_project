from django.urls import path
from blogapp import views

urlpatterns=[
	path('signup',views.signupform,name='signup'),
	path('login',views.loginform,name='login'),
	path('dash',views.dashboard,name='dash'),
	path('logzout',views.logzout,name='logzout'),
	path('addpost',views.addpost,name='addpost'),
	path('editfeed/<int:id>/',views.editfeed,name='editfeed'),
	path('delz/<int:id>/',views.deletez,name='delz'),
	path('members',views.memberz,name='members'),
	path('membersedit/<int:id>/',views.editmember,name='membersedit'),
	path('deletememeber/<int:id>/',views.deletemember,name='deletemember'),
	path('commonuser',views.commonuser,name='commonuser'),
	path('editpass',views.editpassword,name='editpass'),
	path('editprof',views.profileedit,name='editprof'),
]

