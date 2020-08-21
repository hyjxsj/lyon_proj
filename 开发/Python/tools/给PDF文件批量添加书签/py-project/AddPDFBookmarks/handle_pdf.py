# coding:utf-8
# 添加PDF书签
from pdf_utils import MyPDFHandler,PDFHandleMode as mode
import configparser
import sys
from imp import reload

reload(sys)
# sys.setdefaultencoding('utf-8')

def main():
    # 从配置文件中读取配置信息
    cf = configparser.SafeConfigParser()
    cf.read('./info.conf',encoding="utf-8")
    pdf_path = cf.get('info','pdf_path')
    bookmark_file_path = cf.get('info','bookmark_file_path')
    page_offset = cf.getint('info','page_offset')
    new_pdf_file_name = cf.get('info','new_pdf_file_name')

    # pdf_handler = MyPDFHandler(pdf_path,mode = mode.NEWLY)
    pdf_handler = MyPDFHandler(pdf_path,mode = mode.COPY)
    pdf_handler.add_bookmarks_by_read_txt(bookmark_file_path,page_offset = page_offset)
    pdf_handler.save2file(new_pdf_file_name)

if __name__ == '__main__':
    main()