#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author_ ='han'
import os,sys
import configparser,pika,pickle
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)


class RPC_Server(object):
    '''
    RPC服务端
    '''

    def __init__(self):
        self.Get_Conf()
        self.Handler()


    def Get_Conf(self):
        '''
        换取配置文件
        :return: 
        '''
        config = configparser.ConfigParser()
        config.read(os.path.join(path,"conf","config.ini"))
        self.Host = config['RabbitMQ']['host']
        self.Port = int(config['RabbitMQ']['port'])
        self.MyHost = config['LOCAL']['host']
        self.Credentials = pika.PlainCredentials(config['RabbitMQ']['user'],config['RabbitMQ']['pwd'])

    def Handler(self):
        '''
        创建链接RabbitMQ信道和接收
        :return: 
        '''
        self.Conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.Host,
                port=self.Port,
                credentials=self.Credentials
            )
        )
        self.Channel = self.Conn.channel()
        self.Channel.exchange_declare(
            exchange='rpc',
            exchange_type='direct'
        )
        result = self.Channel.queue_declare(exclusive=True)
        queue_name = result.method.queue
        self.Channel.queue_bind(
            exchange='rpc',
            queue = queue_name,
            routing_key=self.MyHost
        )
        self.Channel.basic_consume(
            self.Response,
            queue=queue_name,
            no_ack=True
        )
        self.Channel.start_consuming()

    def Response(self,ch,method,props,body):
        '''
        处理接收到的命令，
        再发命令执行结果
        :return: 
        '''
        cmd = pickle.loads(body)['cmd']
        print('command[%s]'%cmd)
        res = self.Command(cmd)
        data = {'res':res}
        self.Channel.basic_publish(
            exchange='',
            routing_key=props.reply_to,
            properties=pika.BasicProperties(
                message_id=props.reply_to,
                correlation_id=self.MyHost
            ),
            body=pickle.dumps(data)
        )

    def Command(self,cmd):
        '''
        执行命令
        :return: 
        '''
        res = os.popen(cmd).read()
        return res
