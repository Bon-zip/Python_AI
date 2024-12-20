import pyttsx3
import PyPDF2

sach = open("sachover.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(sach)
pages = pdfReader.numPages
bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voice', voices[1].id)
for num in range(711, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    bot.say("Văn bản là một loại hình phương tiện để ghi nhận, lưu giữ và truyền đạt các thông tin từ chủ thể này sang chủ thể khác bằng ký hiệu gọi là chữ viết. Nó gồm tập hợp các câu có tính trọn vẹn về nội dung, hoàn chỉnh về hình thức, có tính liên kết chặt chẽ và hướng tới một mục tiêu giao tiếp nhất định.[1][2][3][4] Hay nói khác đi, văn bản là một dạng sản phẩm của hoạt động giao tiếp bằng ngôn ngữ được thể hiện ở dạng viết trên một chất liệu nào đó (giấy, bia đá,...). Văn bản bao gồm các tài liệu, tư liệu, giấy tờ có giá trị pháp lý nhất định, được sử dụng trong hoạt động của các cơ quan Nhà nước, các tổ chức chính trị, chính trị - xã hội, các tổ chức kinh tế... như: các văn bản pháp luật, các công văn, tài liệu, giấy tờ.")
    bot.runAndWait()

