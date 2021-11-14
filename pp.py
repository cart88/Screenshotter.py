import paramiko

transport = paramiko.Transport(('10.100.24.221', 22))
transport.connect(username='root', password='880813')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('C:\\Users\\lpz-office\\Desktop\\Screenshotter.py\\pp.py', '/tmp/test.py')
# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')

transport.close()