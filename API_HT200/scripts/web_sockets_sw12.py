import socket
import sys  
import tramas_sw12 




class MySocketSW12:
    def __init__(self, ip_target):
        self.rx_var_formated = []
        self.__rx_var = bytearray(2048)
        self.__rx_num = 0
        self.__num = 11
        self.__ips_connected = []
        self.__port = 4001
        self.ip_target = ip_target
        self.__tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__connect()
    def __connect(self):
        try:
            self.__tcpSocket.connect((self.ip_target,self.__port))
        except socket.error:
            sys.exit()
    def readPendingDatagrams(self,__frame):
        self.__tcpSocket.sendto(__frame,(self.ip_target,self.__port))
        reply = self.__tcpSocket.recv(1024)
        self.rx_var_formated = []
        data = list(reply)
        if (data[8]== 131):
            for i in range(11,len(data)-2):
                self.rx_var_formated.append(data[i])
            return True
        else:
            print("trama incorrecta")
            return False
    def getFases(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.fases_frame)):
                print("Fases Obtenidas")
                fases_data = []
                counter = 0
                for i in self.rx_var_formated:
                    counter +=1
                    fase = {'id':'fase-{}'.format(counter),'value':i}
                    fases_data.append(fase)
                return fases_data
        except socket.error:
            sys.exit()
    def getPlan1(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan1_frame)):
                print("Plan1 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
            sys.exit()
    def getPlan2(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan2_frame)):
                print("Plan2 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
                sys.exit()
    def getPlan3(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan3_frame)):
                print("Plan3 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
            sys.exit()

    def getPlan4(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan4_frame)):
                print("Plan4 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
            sys.exit()

    def getPlan5(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan4_frame)):
                print("Plan4 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
            sys.exit()


    def getPlan6(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan4_frame)):
                print("Plan4 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
            sys.exit()

    def getPlan7(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan4_frame)):
                print("Plan4 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
            sys.exit()

    def getPlan8(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan4_frame)):
                print("Plan4 Obtenido")
                plan_data = []
                counter = 1
                for i in range(12):
                    num = i
                    fase = self.rx_var_formated[counter]
                    counter +=1
                    duracion = self.rx_var_formated[counter]
                    counter +=1
                    plan = {'id':'plan-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                return plan_data
        except socket.error:
            sys.exit()


    def getOrdinarySchedule(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.horarios_frame)):
                print("Horario Obtenido")
                horarios_data = []
                counter = 1
                for i in range(16):
                    num = i
                    tiempo = self.rx_var_formated[counter]
                    counter +=1
                    modo = self.rx_var_formated[counter]
                    counter +=1
                    plan = self.rx_var_formated[counter]
                    counter +=1
                    desfase = self.rx_var_formated[counter]
                    counter +=1
                    horario = {
                                'id':'horario-{}'.format(num),
                                'tiempo':tiempo,
                                'modo':modo,
                                'plan':plan,
                                'desfase':desfase,
                            }
                    horarios_data.append(horario)
                return horarios_data
        except socket.error:
            sys.exit()
    def getWeekendSchedule(self):
                try:
                    if(self.readPendingDatagrams(tramas_sw12.semana_frame)):
                        print("Horario fin de semana obtenido")
                        horarios_data = []
                        counter = 1
                        for i in range(16):
                            num = i
                            tiempo = self.rx_var_formated[counter]
                            counter +=1
                            modo = self.rx_var_formated[counter]
                            counter +=1
                            plan = self.rx_var_formated[counter]
                            counter +=1
                            desfase = self.rx_var_formated[counter]
                            counter +=1
                            horario = {
                                        'id':'horario-{}'.format(num),
                                        'tiempo':tiempo,
                                        'modo':modo,
                                        'plan':plan,
                                        'desfase':desfase,
                                    }
                            horarios_data.append(horario)
                        return horarios_data
                except socket.error:
                    sys.exit()
    def getFestivalSchedule(self):
            try:
                if(self.readPendingDatagrams(tramas_sw12.festivo_frame)):
                    print("Horario festivo obtenido")
                    horarios_data = []
                    counter = 1
                    for i in range(16):
                        num = i
                        tiempo = self.rx_var_formated[counter]
                        counter +=1
                        modo = self.rx_var_formated[counter]
                        counter +=1
                        plan = self.rx_var_formated[counter]
                        counter +=1
                        desfase = self.rx_var_formated[counter]
                        counter +=1
                        horario = {
                                    'id':'horario-{}'.format(num),
                                    'tiempo':tiempo,
                                    'modo':modo,
                                    'plan':plan,
                                    'desfase':desfase,
                                }
                        horarios_data.append(horario)
                    return horarios_data
            except socket.error:
                sys.exit()

    def getGrupos(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.grupos_frame)):
                print("Obteniendo Grupos")
                horarios_data = []
                print(self.rx_var_formated)
                counter = 1
                for i in range(4):
                    num = i
                    valor = self.rx_var_formated[counter]
                    counter +=1
                    horario = {
                                'id':'grupo-{}'.format(num),
                                'value':valor
                                }
                    horarios_data.append(horario)
                return horarios_data
        except socket.error:
            sys.exit()

    def getGreenConflict(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.grenn_conflict)):
                print("Obteniendo Grupos")
                horarios_data = []
                print(self.rx_var_formated)
                counter = 0
                for i in range(4):
                    num = i
                    valor = self.rx_var_formated[counter]
                    counter +=1
                    horario = {
                                'id':'grupo-{}'.format(num+1),
                                'value':valor
                                }
                    horarios_data.append(horario)
                    return horarios_data
        except socket.error:
            sys.exit()

    def getOperativeParams(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.operative_frame)):
                print("Obteniendo parametros Operativos")

                params ={
                            'destello_al_encender':self.rx_var_formated[1],
                            'tiempo_en_rojo_al_encender':self.rx_var_formated[2],
                            'destello_verde_peatonal':self.rx_var_formated[3],
                            'destello_verde_vehicular':self.rx_var_formated[4],
                            'tiempo_amarillo_vehicular':self.rx_var_formated[5],
                            'tiempo_todo_rojo':self.rx_var_formated[6],
                            'min_verde':self.rx_var_formated[7],
                        }
                return params
        except socket.error:
            sys.exit()

    def getTimeController(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.time_frame)):
                print("Obteniendo Tiempo del Controlador")
                print(self.rx_var_formated)
                        # params ={
                        #     'destello_al_encender':self.rx_var_formated[1],
                        #     'tiempo_en_rojo_al_encender':self.rx_var_formated[2],
                        #     'destello_verde_peatonal':self.rx_var_formated[3],
                        #     'destello_verde_vehicular':self.rx_var_formated[4],
                        #     'tiempo_amarillo_vehicular':self.rx_var_formated[5],
                        #     'tiempo_todo_rojo':self.rx_var_formated[6],
                        #     'min_verde':self.rx_var_formated[7],
                        # }
                        # return params
        except socket.error:
            sys.exit()


    def getSpecialDays(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.especial_frame)):
                print("Obteniendo Tiempo del Controlador")
                print(self.rx_var_formated)
                        # params ={
                        #     'destello_al_encender':self.rx_var_formated[1],
                        #     'tiempo_en_rojo_al_encender':self.rx_var_formated[2],
                        #     'destello_verde_peatonal':self.rx_var_formated[3],
                        #     'destello_verde_vehicular':self.rx_var_formated[4],
                        #     'tiempo_amarillo_vehicular':self.rx_var_formated[5],
                        #     'tiempo_todo_rojo':self.rx_var_formated[6],
                        #     'min_verde':self.rx_var_formated[7],
                        # }
                        # return params
        except socket.error:
            sys.exit()
    def getEntradas(self):
            try:
                if(self.readPendingDatagrams(tramas_sw12.entradas_frame)):
                    print("Obteniendo Entradas")
                    print(self.rx_var_formated)
                            # params ={
                            #     'destello_al_encender':self.rx_var_formated[1],
                            #     'tiempo_en_rojo_al_encender':self.rx_var_formated[2],
                            #     'destello_verde_peatonal':self.rx_var_formated[3],
                            #     'destello_verde_vehicular':self.rx_var_formated[4],
                            #     'tiempo_amarillo_vehicular':self.rx_var_formated[5],
                            #     'tiempo_todo_rojo':self.rx_var_formated[6],
                            #     'min_verde':self.rx_var_formated[7],
                            # }
                            # return params
            except socket.error:
                sys.exit()
    def disconnect(self):
        self.__tcpSocket.close()


# tcp_client = MySocketSW12('192.168.2.97')
# datos = tcp_client.getEntradas()
# print(datos)
# tcp_client.disconnect()
