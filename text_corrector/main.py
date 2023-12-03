from CorrectorProcess import *

emailhelper = EmailHelper()

mail = input("請輸入您的email內容：")
mail = emailhelper.tra2sim(mail)
mail = emailhelper.correct_batch(mail)
mail = emailhelper.get_target(mail)
mail = emailhelper.sim2tra(mail)
print(mail)