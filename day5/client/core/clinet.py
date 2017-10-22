#!/usr/bin/env python
# _*_ encoding:utf-8 _*_
__author__='han'
import os,sys
import configparser,pika,random,threading,pickle,time
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,path)


class Rpc_Clinet(object):
    '''
    PRC客户端
    '''

    def __init__(self):

        #保存命令结果字典
        self.Rpc_dict = {}
        #保存任务ID列表
        self.Id_List = []
        self.Get_Conf()

    def Get_Conf(self):
        '''
        获取配置文件
        :return: 
        '''
        config = configparser.ConfigParser()
        config.read(os.path.join(path,'conf','config.ini'))
        self.Host = config['RabbitMQ']['host']
        self.Port = int(config['RabbitMQ']['port'])
        self.Time_Out = int(config['RabbitMQ']['timeout'])
        self.Credentials = pika.PlainCredentials(config['RabbitMQ']['user'],config['RabbitMQ']['pwd'])


    def Handler(self):
        '''
        链接RabbitMQ和信道
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

    def Command(self):
        '''
        交互输入命令
        :return: 
        '''
        while True:
            choice = input('\033[35m>>:\033[0m')
            choice_list = choice.split('"')
            if choice.startswith('run'):
                if len(choice_list) == 3:
                    cmd = choice[1]
                    host_str = choice_list[2].strip()
                    if '--host' not in host_str:
                        print('cmd Error!')
                    else:
                        host_group = host_str.split(' ')
                        host_list = []
                        task_id = self.Create_Id()
                        for i in range(1,len(host_group)):
                            host_list.append(host_group[i])
                        thread = threading.Thread(
                            target=self.Run,
                            args=(task_id,cmd,host_list)
                        )
                        thread.start()
                        continue
                else:
                    print('\033[31mCommand Error!\033[0m')
                    self.Help()
                continue
            elif choice.startswith('check_task'):
                choice_list = choice.split()
                if len(choice_list) ==2:
                    task_id = choice_list[1]
                    self.Result(task_id)
                else:
                    print('\033[1;31;1mCommand Error!\033[0m')
                    self.Help()
                continue
            elif choice == 'quit':
                break
            else:
                print('\033[1;31;1mCommand Error!\033[0m')
                self.Help()


    def Help(self):
        '''
        帮助
        :return: 
        '''
        print('\033[1;36;1mrun shell: run "command" [--host hostname]')
        print('you must add " at command start and end or it will be error')
        print('get result: check_task task_id')
        print('input quit to exit\033[0m')

    def Run(self,task_id,cmd,host_list):
        '''
        创建接收消费者返回结果，
        并且调用发送命令函数。
        :return: 
        '''
        self.Handler()
        self.Channel.queue_declare(queue=task_id)
        self.Channel.basic_consume(
            self.Response,
            queue=task_id
        )
        self.Send_Cmd(task_id,cmd,host_list)


    def Send_Cmd(self,task_id,cmd,host_list):
        '''
        发送函数
        :return: 
        '''
        for host in host_list:
            self.Rpc_dict[task_id][host] = ''
        data = {'cmd':cmd}
        self.Channel.exchange_declare(
            exchange='rpc',
            exchange_type='direct'
        )
        for host in host_list:
            self.Channel.basic_publish(
                exchange='rpc',
                routing_key=host,
                properties=pika.BasicProperties(
                    reply_to=task_id,
                ),
                body=pickle.dumps(data)
            )
        for host in host_list:
            count = 0
            while self.Rpc_dict[task_id][host] == '':
                self.Conn.process_data_events()
                time.sleep(0.1)
                count += 1
                if count > self.Time_Out*10:
                    print('host[%s] connection timeout'%host)
                    break

    def Response(self,ch,method,props,body):
        '''
        处理接收结果
        :return: 
        '''
        task_id = props.message_id
        res = pickle.loads(body)
        host = props.correlation_id
        self.Rpc_dict[task_id][host] = res

        #告知已收到
        self.Channel.basic_ack(delivery_tag=method.delivery_tag)


    def Create_Id(self):
        '''创建ID'''
        task_id = ''
        for i in range(5):
            current = random.randrange(0,9)
            task_id += str(current)
        if task_id in self.Rpc_dict:
            self.Create_Id()
        else:
            self.Rpc_dict[task_id] = {}
        print('task_id:',task_id)
        return task_id

    def Result(self,id):
        '''
        打印接收的结果，
        并清空保存命令字典
        :return: 
        '''
        for host in self.Rpc_dict[id]:
            print(('host %s')%host.center(50,'-'))
        del self.Rpc_dict[id]


