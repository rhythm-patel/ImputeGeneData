from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import subprocess, os

# Create your views here.
nof = ""

def index(request):
	global nof
	if request.method == "POST":
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name,uploaded_file)
		nof = name
		# os.system("pwd")
		# os.chdir('test')
		# os.system("python3 test.py")

	# data = ''
	return render(request, 'impute/header.html')


def nmc(request):

	# print(os.getcwd())

	# os.chdir('test')
	# cmd = "python3 test.py "+nof
	# os.system(cmd)
	# os.chdir('..')
	# os.chdir('media')

	os.chdir('Impute-Gene_Data')
	os.chdir('NMC')	
	cmd = "python3 predict_missing.py --data_file ../../media/"+nof

	os.system(cmd)
	os.chdir('..')
	os.chdir('..')
	os.chdir('media')

	if os.path.exists(nof):
		os.remove(nof)
	os.chdir('..')

	nofL = nof.split('.')
	nofN = nofL[0]

	opfile = "NMC_Imputed_"+nofN+'.csv'
	oppath = "/media/"+opfile

	detfile = "NMC_Details_"+nofN+'.txt'
	detpath = "/media/"+detfile



	return render(request, 'impute/nmc.html', {'oppath':oppath, 'detpath':detpath})


def dapl(request):

	# print(os.getcwd())

	# os.chdir('test')
	# cmd = "python3 test.py "+nof
	# os.system(cmd)
	# os.chdir('..')
	# os.chdir('media')

	os.chdir('DAPL_scratch')
	cmd = "python3 predict_missing.py --input_file ../media/"+nof+" --output_filePath ../media --model_dir trained_model/best_model"

	os.system(cmd)
	os.chdir('..')
	os.chdir('media')

	if os.path.exists(nof):
		os.remove(nof)
	os.chdir('..')

	nofL = nof.split('.')
	nofN = nofL[0]

	opfile = "DAPL_Imputed_"+nofN+'.csv'
	oppath = "/media/"+opfile

	# detfile = "Details_"+nofN+'.txt'
	# detpath = "/media/"+detfile



	return render(request, 'impute/nmc.html', {'oppath':oppath})

# def index(request):
# 	context={}
# 	if request.method == "POST":
# 		uploaded_file = request.FILES['document']
# 		fs = FileSystemStorage()
# 		name = fs.save(uploaded_file.name,uploaded_file)
# 		context['url']=fs.url(name)
# 	data = ''
# 	return render(request, 'impute/header.html',context, {'data':data})


# def input_list(request):
# 	return render(request, 'input_list.html')