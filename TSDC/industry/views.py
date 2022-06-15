from django.shortcuts import render
from django.http import HttpResponse
#表格用
import pandas as pd
import json
import datetime as dt
import os

#關於我們aboutus
def aboutus1(request):
    return render(request, 'industry/aboutus1.html')
def aboutus2(request):
    return render(request, 'industry/aboutus2.html')
def aboutus3(request):
    return render(request, 'industry/aboutus3.html')


#強制更改pythonanywhere讀取statistic位置
os.chdir("/home/kaihsin/TSDC_Project0501/TSDC")
#散戶的50道難題
def question1(request):
    return render(request, 'industry/question1.html')
def question2(request):
    return render(request, 'industry/question2.html')
def question3(request):
    return render(request, 'industry/question3.html')
def question4(request):
    return render(request, 'industry/question4.html')
def question5(request):
    return render(request, 'industry/question5.html')

#company公司
def company_2324(request):
    return render(request, 'industry/company_2324.html')
def company_2357(request):
    return render(request, 'industry/company_2357.html')
def company_2365(request):
    return render(request, 'industry/company_2365.html')
def company_2382(request):
    return render(request, 'industry/company_2382.html')
def company_2809(request):
    return render(request, 'industry/company_2809.html')
def company_2832(request):
    return render(request, 'industry/company_2832.html')
def company_2849(request):
    return render(request, 'industry/company_2849.html')
def company_2886(request):
    return render(request, 'industry/company_2886.html')
def company_2891(request):
    return render(request, 'industry/company_2891.html')
def company_3231(request):
    return render(request, 'industry/company_3231.html')

#chip籌碼
def chip_2324(request):
    return render(request, 'industry/chip_2324.html')
def chip_2357(request):
    return render(request, 'industry/chip_2357.html')
def chip_2365(request):
    return render(request, 'industry/chip_2365.html')
def chip_2382(request):
    return render(request, 'industry/chip_2382.html')
def chip_2809(request):
    return render(request, 'industry/chip_2809.html')
def chip_2832(request):
    return render(request, 'industry/chip_2832.html')
def chip_2849(request):
    return render(request, 'industry/chip_2849.html')
def chip_2886(request):
    return render(request, 'industry/chip_2886.html')
def chip_2891(request):
    return render(request, 'industry/chip_2891.html')
def chip_3231(request):
    return render(request, 'industry/chip_3231.html')

#index指標
def index_2324(request):
    return render(request, 'industry/index_2324.html')
def index_2357(request):
    return render(request, 'industry/index_2357.html')
def index_2365(request):
    return render(request, 'industry/index_2365.html')
def index_2382(request):
    return render(request, 'industry/index_2382.html')
def index_2809(request):
    return render(request, 'industry/index_2809.html')
def index_2832(request):
    return render(request, 'industry/index_2832.html')
def index_2849(request):
    return render(request, 'industry/index_2849.html')
def index_2886(request):
    return render(request, 'industry/index_2886.html')
def index_2891(request):
    return render(request, 'industry/index_2891.html')
def index_3231(request):
    return render(request, 'industry/index_3231.html')

#month月資料
def month_2324(request):
    return render(request, 'industry/month_2324.html')
def month_2357(request):
    return render(request, 'industry/month_2357.html')
def month_2365(request):
    return render(request, 'industry/month_2365.html')
def month_2382(request):
    return render(request, 'industry/month_2382.html')
def month_2809(request):
    return render(request, 'industry/month_2809.html')
def month_2832(request):
    return render(request, 'industry/month_2832.html')
def month_2849(request):
    return render(request, 'industry/month_2849.html')
def month_2886(request):
    return render(request, 'industry/month_2886.html')
def month_2891(request):
    return render(request, 'industry/month_2891.html')
def month_3231(request):
    return render(request, 'industry/month_3231.html')

#report財報
def report_2324(request):
    return render(request, 'industry/report_2324.html')
def report_2357(request):
    return render(request, 'industry/report_2357.html')
def report_2365(request):
    return render(request, 'industry/report_2365.html')
def report_2382(request):
    return render(request, 'industry/report_2382.html')
def report_2809(request):
    return render(request, 'industry/report_2809.html')
def report_2832(request):
    return render(request, 'industry/report_2832.html')
def report_2849(request):
    return render(request, 'industry/report_2849.html')
def report_2886(request):
    return render(request, 'industry/report_2886.html')
def report_2891(request):
    return render(request, 'industry/report_2891.html')
def report_3231(request):
    return render(request, 'industry/report_3231.html')

######################下面是複雜的#################################################

#chip籌碼表格
def chip_2324(request):
    df = pd.read_csv("static/csv/chip2324.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2324': data}
  
    return render(request, 'industry/chip_2324.html', context)
def chip_2357(request):
    df = pd.read_csv("static/csv/chip2357.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2357': data}
  
    return render(request, 'industry/chip_2357.html', context)
def chip_2365(request):
    df = pd.read_csv("static/csv/chip2365.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2365': data}
  
    return render(request, 'industry/chip_2365.html', context)
def chip_2382(request):
    df = pd.read_csv("static/csv/chip2382.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2382': data}
  
    return render(request, 'industry/chip_2382.html', context)
def chip_2809(request):
    df = pd.read_csv("static/csv/chip2809.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2809': data}
  
    return render(request, 'industry/chip_2809.html', context)
def chip_2832(request):
    df = pd.read_csv("static/csv/chip2832.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2832': data}
  
    return render(request, 'industry/chip_2832.html', context)
def chip_2849(request):
    df = pd.read_csv("static/csv/chip2849.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2849': data}
  
    return render(request, 'industry/chip_2849.html', context)
def chip_2886(request):
    df = pd.read_csv("static/csv/chip2886.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2886': data}
  
    return render(request, 'industry/chip_2886.html', context)
def chip_2891(request):
    df = pd.read_csv("static/csv/chip2891.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip2891': data}
  
    return render(request, 'industry/chip_2891.html', context)
def chip_3231(request):
    df = pd.read_csv("static/csv/chip3231.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'chip3231': data}
  
    return render(request, 'industry/chip_3231.html', context)

#index指標報表
def index_2324(request):
    df = pd.read_csv('static/csv/index2324.csv')
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2324': data}
  
    return render(request, 'industry/index_2324.html', context)
def index_2357(request):
    df = pd.read_csv("static/csv/index2357.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2357': data}
  
    return render(request, 'industry/index_2357.html', context)
def index_2365(request):
    df = pd.read_csv("static/csv/index2365.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2365': data}
  
    return render(request, 'industry/index_2365.html', context)
def index_2382(request):
    df = pd.read_csv("static/csv/index2382.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2382': data}
  
    return render(request, 'industry/index_2382.html', context)
def index_2809(request):
    df = pd.read_csv("static/csv/index2809.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2809': data}
  
    return render(request, 'industry/index_2809.html', context)
def index_2832(request):
    df = pd.read_csv("static/csv/index2832.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2832': data}
  
    return render(request, 'industry/index_2832.html', context)
def index_2849(request):
    df = pd.read_csv("static/csv/index2849.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2849': data}
  
    return render(request, 'industry/index_2849.html', context)
def index_2886(request):
    df = pd.read_csv("static/csv/index2886.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2886': data}
  
    return render(request, 'industry/index_2886.html', context)
def index_2891(request):
    df = pd.read_csv("static/csv/index2891.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index2891': data}
  
    return render(request, 'industry/index_2891.html', context)
def index_3231(request):
    df = pd.read_csv("static/csv/index3231.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'index3231': data}
  
    return render(request, 'industry/index_3231.html', context)

#month月資料表格
def month_2324(request):
    df = pd.read_csv("static/csv/month2324.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2324': data}
  
    return render(request, 'industry/month_2324.html', context)
def month_2357(request):
    df = pd.read_csv("static/csv/month2324.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2357': data}
  
    return render(request, 'industry/month_2357.html', context)
def month_2365(request):
    df = pd.read_csv("static/csv/month2365.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2365': data}
  
    return render(request, 'industry/month_2365.html', context)
def month_2382(request):
    df = pd.read_csv("static/csv/month2382.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2382': data}
  
    return render(request, 'industry/month_2382.html', context)
def month_2809(request):
    df = pd.read_csv("static/csv/month2809.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2809': data}
  
    return render(request, 'industry/month_2809.html', context)
def month_2832(request):
    df = pd.read_csv("static/csv/month2832.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2832': data}
  
    return render(request, 'industry/month_2832.html', context)
def month_2849(request):
    df = pd.read_csv("static/csv/month2849.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2849': data}
  
    return render(request, 'industry/month_2849.html', context)
def month_2886(request):
    df = pd.read_csv("static/csv/month2886.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2886': data}
  
    return render(request, 'industry/month_2886.html', context)
def month_2891(request):
    df = pd.read_csv("static/csv/month2891.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month2891': data}
  
    return render(request, 'industry/month_2891.html', context)
def month_3231(request):
    df = pd.read_csv("static/csv/month3231.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'month3231': data}
  
    return render(request, 'industry/month_3231.html', context)

#report財報表格
def report_2324(request):
    df = pd.read_csv("static/csv/report2324.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2324': data}
  
    return render(request, 'industry/report_2324.html', context)
def report_2357(request):
    df = pd.read_csv("static/csv/report2357.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2357': data}
  
    return render(request, 'industry/report_2357.html', context)
def report_2365(request):
    df = pd.read_csv("static/csv/report2365.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2365': data}
  
    return render(request, 'industry/report_2365.html', context)
def report_2382(request):
    df = pd.read_csv("static/csv/report2382.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2382': data}
  
    return render(request, 'industry/report_2382.html', context)
def report_2809(request):
    df = pd.read_csv("static/csv/report2809.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2809': data}
  
    return render(request, 'industry/report_2809.html', context)
def report_2832(request):
    df = pd.read_csv("static/csv/report2832.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2832': data}
  
    return render(request, 'industry/report_2832.html', context)
def report_2849(request):
    df = pd.read_csv("static/csv/report2849.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2849': data}
  
    return render(request, 'industry/report_2849.html', context)
def report_2886(request):
    df = pd.read_csv("static/csv/report2886.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2886': data}
  
    return render(request, 'industry/report_2886.html', context)
def report_2891(request):
    df = pd.read_csv("static/csv/report2891.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report2891': data}
  
    return render(request, 'industry/report_2891.html', context)
def report_3231(request):
    df = pd.read_csv("static/csv/report3231.csv")
  
    # parsing the DataFrame in json format.
    #json_records = df.reset_index().to_json(orient ='records')
    json_records = df.to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    context = {'report3231': data}
  
    return render(request, 'industry/report_3231.html', context)