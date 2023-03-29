import jqktrader.api
from jqktrader.utils.stock import get_today_ipo_data


if __name__ == "__main__":
  user = jqktrader.use()

  user.connect(
    exe_path=r'D:\同花顺软件\同花顺\xiadan.exe',
    tesseract_cmd=r'D:\Program Files\Tesseract-OCR\tesseract.exe'
  )

  # 资金情况
  print(user.balance)
  # # 持仓情况
  print(user.position)
  # 买入
  buymessage = user.buy('162411', price=0.7, amount=100)
#   # #卖出
#   # sellmessage = user.sell('162411', price=3.55, amount=100)
# #   一键打新
#   user.auto_ipo()
#   user.cancel_entrust(buymessage['entrust_no'])
#   # 查询当日成交
#   # user.today_trades
#   # 查询当日委托
#   entrusts = user.today_entrusts
#   print(entrusts)
#   # 查询当日可打新股
#   ipo_data = get_today_ipo_data()
#   print(ipo_data)
#   # 刷新数据
#   user.refresh()
#   # 退出客户端
#   user.exit()