import jqktrader.api


if __name__ == "__main__":
  user = jqktrader.use()

  user.connect(
    exe_path=r'D:\同花顺软件\同花顺\xiadan.exe',
    tesseract_cmd=r'D:\Program Files\Tesseract-OCR\tesseract.exe'
  )

  # 资金情况
  print(user.balance)
  # 持仓情况
  print(user.position)
  # 买入
  user.buy('162411', price=0.55, amount=100)
  #卖出
  user.sell('162411', price=3.55, amount=100)
