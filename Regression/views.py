from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from Regression.forms import FileForm
from Regression.functions import process_files, csvdownload
import csv

# Create your views here.
def index(request):
	global ans_list
	if request.method == 'POST':
		classroom = FileForm(request.POST, request.FILES)
		#classroomにデータがある場合
		if classroom.is_valid():
			test_x = request.FILES['test_x']
			#implement process_files
			ans_list = process_files(test_x)
			
			return render(request,"download.html",{'ans_list':ans_list})

	else:
	    classroom = FileForm()
	    return render(request,"index.html",{'form':classroom})


def csvdownload_page(request):
	if request.method == 'POST':
		if 'button_1' in request.POST:
			response = HttpResponse(content_type='text/csv')
			response['Content-Disposition'] = 'attachment; filename="ans.csv"'
			writer = csv.writer(response)
			writer.writerow(['お仕事No.', '応募数 合計'])
			writer.writerows(ans_list)

			return response
