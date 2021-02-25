import logging
import logstash
import sys
import json
import socket
def test1():
    host = 'localhost'

    test_logger = logging.getLogger('python-logstash-logger')
    test_logger.setLevel(logging.INFO)
#    test_logger.addHandler(logstash.LogstashHandler(host, 5000, version=1))
    test_logger.addHandler(logstash.TCPLogstashHandler(host, 5000, version=1))

    extra = {
    "name":"taebin2",
    "age": 17,
    "value": 13
        }
    extra = json.dumps(extra)
    #test_logger.error(extra)
    test_logger.info(extra)
    #test_logger.warning(extra)

# add extra field to logstash message
def test2():
    #값을 보낼 서버 주소
    HOST = "0.0.0.0"
    # 서버에서 지정해 놓은 포트 번호입니다.
    PORT = 5000
    # 소켓 객체를 생성합니다.
    # 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
    client_socket.connect((HOST, PORT))
    # 메시지를 전송합니다.
    client_socket.sendall('hi'.encode())
    # 소켓을 닫습니다.
    client_socket.close()

if __name__ == '__main__':
    test2()
