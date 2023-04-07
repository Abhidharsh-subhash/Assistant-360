from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index,name="index"),
    path('index', views.index,name="index"),
    path('userreg', views.userreg,name="userreg"),
    path('staffreg', views.staffreg,name="staffreg"),
    path('admin', views.admin,name="admin"),
    path('adminhome', views.adminhome,name="adminhome"),
    path('staffhome', views.staffhome,name="staffhome"),
    path('userhome', views.userhome,name="userhome"),
    path("Logout",views.Logout,name='Logout'),
    path("stafflogin",views.stafflogin,name="stafflogin"),
    path("getDistrict/",views.getDistrict,name="getDistrict"),
   
    path("Add_state/",views.Add_state,name="Add_state"),
    path("list_state/",views.list_state,name="list_state"),
    path("delete_state/",views.delete_state,name="delete_state"),
    path("edit_state/",views.edit_state,name="edit_state"),
   
    path("privacy/",views.privacy,name="privacy"),
    path("user_feed/",views.user_feed,name="user_feed"),
    path("staff_complaints/",views.staff_complaints,name="staff_complaints"),
    path("feedback/",views.feedback,name="feedback"),
    path("Feedback/",views.feedback,name="Feedback"),
    path("complaints/",views.complaints,name="complaints"),
path("find_labour/",views.find_labour,name="find_labour"),
path("book_labour/",views.book_labour,name="book_labour"),
path("staff_ongoing/",views.staff_ongoing,name="staff_ongoing"),
path("staff_rejected/",views.staff_rejected,name="staff_rejected"),
path("staff_completed/",views.staff_completed,name="staff_completed"),
path("request_payment/",views.request_payment,name="request_payment"),
path("waiting_payment/",views.waiting_payment,name="waiting_payment"),
path("payment_request",views.payment_request,name="payment_request"),
path("payment_completed/",views.payment_completed,name="payment_completed"),
path("payment_history/",views.payment_history,name="payment_history"),
path("reject_user/",views.reject_user,name="reject_user"),
path("ongoing/",views.ongoing,name="ongoing"),
path("approved_user/",views.approved_user,name="approved_user"),
path("reject_staff/",views.reject_staff,name="reject_staff"),
path("approved_staff/",views.approved_staff,name="approved_staff"),

path("schedule/",views.schedule,name="schedule"),
path("complete/",views.complete,name="complete"),
path("rejected/",views.rejected,name="rejected"),
path("delete_labour/",views.delete_labour,name="delete_labour"),
path("job_confirm/",views.job_confirm,name="job_confirm"),
path("confirm_labour/",views.confirm_labour,name="confirm_labour"),
path("reject_labour/",views.reject_labour,name="reject_labour"),


path("add_district/",views.add_district,name="add_district"),
    path("list_district/",views.list_district,name="list_district"),
    path("edit_district/",views.edit_district,name="edit_district"),
    path("delete_district/",views.delete_district,name="delete_district"),
    path("list_user/",views.list_user,name="list_user"),
    path("approve_user/",views.approve_user,name="approve-user"),
    path("delete_user/",views.delete_user,name="delete_user"),
    path("list_staff/",views.list_staff,name="list_staff"),
    path("approve_staff/",views.approve_staff,name="approve_staff"),
    path("delete_staff/",views.delete_staff,name="delete_staff"),
     path("approve_user/",views.approve_user,name="approve_user"),
     path("newjob",views.newjob,name="newjob"),
     path("newjob_approve",views.newjob_approve,name="newjob_approve"),
     path("task_complete/",views.task_complete,name="task_complete"),
     path("addmenu/",views.addmenu,name="addmenu"),
     path("menu/",views.menu,name="menu"),
     path("menudetails/",views.menudetails,name="menudetails"),
     path("neworders/",views.neworders,name="neworders"),
     path("delivered/",views.delivered,name="delivered")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
