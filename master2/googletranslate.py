import googletrans
from googletrans import Translator

t = Translator()
a = t.translate("toi yeu em", src="vi", dest="en")
print(a.text)
