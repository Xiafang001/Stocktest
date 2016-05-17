'''views.py to support views for the stockinfo of each user'''
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import TecStockUser, StockInfo
import urllib


@login_required
def stockinfo(request):
  ''' Returns the list of stocks for the current user'''
  user_id = request.user.id
  cur_user = TecStockUser.objects.filter(user=user_id)[0]
  stock_list = StockInfo.objects.filter(user=cur_user)
  spent = cur_user.spent
  earned = 0
  #Update to the lastest price
  for stock_sym in stock_list:
    url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=sl1' % stock_sym
    values = urllib.urlopen(url).read().strip().strip('"').split(',')
    StockInfo.update(user_id, values[0][0:-1],  values[1])
  #Get the total values
  total = StockInfo.count(user_id)
  earned = total - spent
  return render(request, 'stockinfo/stockinfo.html', {'user': user_id,'total':total, 'user_name': cur_user, 'spent':spent, 'earned':earned, 'cur_user': cur_user, 'stock_list': stock_list, })


@login_required
def getstock(request):
  '''Get the stock using Yahoo Finance API'''
  user_id = request.user.id
  cur_user = TecStockUser.objects.filter(user=user_id)[0]
  symbol = request.GET.get('stock_name','')
  url = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=soc1l1' % symbol
  values = urllib.urlopen(url).read().strip().strip('"').split(',')
  stock_info = []
  stock_info.append(values[0][0:-1])
  stock_info.append(values[1])
  stock_info.append(values[2])
  stock_info.append(values[3])
  sym_stock = stock_info[0]
  price_cur = stock_info[-1]
  return render (request, 'stockinfo/search/search.html', {'user': user_id, 'user_name': cur_user, 'stock_info': stock_info,'sym_stock': sym_stock, 'price_stock': price_cur, })

@login_required
def addstock(request):
  '''Add the stock to user's database'''
  user_id = request.user.id
  cur_user = TecStockUser.objects.filter(user=user_id)[0]
  stock_num = request.GET.get('stock_number','').strip()
  stock_price = request.GET.get('price_stock','').strip()
  stock_sym = request.GET.get('sym_stock','').strip()
  StockInfo.add(user_id, stock_sym, stock_price, stock_num)
  return render (request, 'stockinfo/add/addsuccess.html',{'user': user_id, 'user_name': cur_user, 'stock_sym': stock_sym, 'stock_num':stock_num})

    
