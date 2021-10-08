
from .services import *


@login_required
def dashboard_account(request):
	dashboard()
	

def user_login_account(request):
	user_login()					


@login_required
def user_logout_account(request):
	user_logout()

def register_account(request):
	register()

@login_required
def edit_profile(request):
	edit()
	

@login_required
def user_list_account(request):
	user_list()
				


@login_required
def user_detail_account(request, username):
	user_detail()



def user_follow_account(request):
	user_follow()

