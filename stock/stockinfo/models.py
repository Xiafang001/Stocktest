'''Creating database for TecStock users'''
from django.db import models
from django.contrib.auth.models import User

class TecStockUser(models.Model):
  '''Add Stockinfo data to User'''
  first_name = models.CharField(default='', max_length=10)
  last_name = models.CharField(default='', max_length=10)
  user = models.OneToOneField(User)
  email = models.CharField(default='', max_length=30)
  
  def __str__(self):
      return self.first_name +' '+ self.last_name

class StockInfo(models.Model):
  '''Stock Table to maintain the stock bought'''
  user = models.ForeignKey(TecStockUser)
  stock = models.CharField(max_length=5)
  numbers = models.PositiveIntegerField(default=0)
  current_price = models.FloatField(default=0)

  def __str__(self):
      return self.stock

  class Meta:
    '''The ForeignKey i.e. user and a stock symbol must be unique'''
    unique_together = ('user', 'stock')

  @staticmethod
  def add(user_id, stock_symbol, stock_price, stock_num):
    '''Create stock row or add num of shares'''
    stock_user = TecStockUser.objects.get(user=user_id)
    stock_user.save()
    result = StockInfo.objects.get_or_create(stock=stock_symbol, user=stock_user)[0]
    result.current_price = stock_price
    result.numbers += int(stock_num)
    result.save()
  
  @staticmethod
  def update(user_id, stock_symbol, stock_price):
    '''Update the lastest price into database'''
    stock_user = TecStockUser.objects.get(user=user_id)
    result = StockInfo.objects.get_or_create(stock=stock_symbol, user=stock_user)[0]
    result.current_price = stock_price
    result.save()
  
  @staticmethod
  def count(user_id):
    '''Get the total values of the current user'''
    stock_user = TecStockUser.objects.filter(user=user_id)[0]
    stock_list = StockInfo.objects.filter(user=stock_user)
    total = 0.0
    for stock in stock_list:
      total += stock.current_price * stock.numbers
    return total

