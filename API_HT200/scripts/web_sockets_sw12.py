import socket
import sys  
from scripts import tramas_sw12




class MySocketSW12:
    def __init__(self, ip_target):
        self.rx_var_formated = []
        self.__rx_var = bytearray(2048)
        self.__rx_num = 0
        self.__num = 11
        self.__ips_connected = []
        self.__port = 4001
        self.ip_target = ip_target
    def readPendingDatagrams(self,__frame):
        __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        __tcpSocket.settimeout(10)
        __tcpSocket.connect((self.ip_target,self.__port))
        __tcpSocket.sendall(__frame)
        reply = __tcpSocket.recv(1024)
        __tcpSocket.close()
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
                print(self.rx_var_formated)
                print("Fases Obtenidas")
                fases_data = []
                counter = 0
                for i in range(16):
                    fase = self.rx_var_formated[i]
                    counter +=1
                    fase = {'id':'fase-{}'.format(counter),'value':fase}
                    fases_data.append(fase)
                data_json = {'data':fases_data,'status':True}
                return data_json
            else:
                data_json = {'data':[],'status':False}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json
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
                    plan = {'id':'paso-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                data_json = {'data':plan_data,'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

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
                data_json = {'data':plan_data,'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json
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
                    plan = {'id':'paso-{}'.format(num),'fase':fase,'duracion':duracion}
                    plan_data.append(plan)
                data_json = {'data':plan_data,'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json

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
                data_json = {'data':plan_data,'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json

    def getPlan5(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan5_frame)):
                print("Plan5 Obtenido")
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
                data_json = {'data':plan_data,'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json


    def getPlan6(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan6_frame)):
                print("Plan6 Obtenido")
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
                data_json = {'data':plan_data,'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json

    def getPlan7(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan7_frame)):
                print("Plan7 Obtenido")
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
                data_json = {'data':plan_data,'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json

    def getPlan8(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.plan8_frame)):
                print("Plan8 Obtenido")
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
                data_json = { 'data':plan_data, 'status':True}
                return data_json
            else:
                data_json = {'data':plan_data,'status':True}
                return data_json
        except:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json

    def getOrdinarySchedule(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.horarios_frame)):
                print("Horario Obtenido")
                print(self.rx_var_formated)
                horarios_data = []
                counter = 1
                for i in range(16):
                    num = i
                    hora = self.rx_var_formated[counter]
                    counter +=1
                    minuto = self.rx_var_formated[counter]
                    counter +=1
                    mod = self.rx_var_formated[counter]
                    counter +=1
                    desfase = self.rx_var_formated[counter]
                    counter +=1
                    horario = {
                                'id':'horario-{}'.format(num),
                                'hora':hora,
                                'minuto':minuto,
                                'modo':mod,
                                'desfase':desfase,
                            }
                    horarios_data.append(horario)
                data_json = {'data':horarios_data,'status':True}
                return data_json
            else:
                data_json = {'data':[],'status':False}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

    def getWeekendSchedule(self):
                try:
                    if(self.readPendingDatagrams(tramas_sw12.semana_frame)):
                        print("Horario fin de semana obtenido")
                        print(self.rx_var_formated)
                        horarios_data = []
                        counter = 1
                        for i in range(16):
                            num = i
                            hora = self.rx_var_formated[counter]
                            counter +=1
                            minuto = self.rx_var_formated[counter]
                            counter +=1
                            mod = self.rx_var_formated[counter]
                            counter +=1
                            desfase = self.rx_var_formated[counter]
                            counter +=1
                            horario = {
                                        'id':'horario-{}'.format(num),
                                        'hora':hora,
                                        'minuto':minuto,
                                        'modo':mod,
                                        'desfase':desfase,
                                    }
                            horarios_data.append(horario)
                        data_json = {'data':horarios_data,'status':True }
                        return data_json
                    else:
                        data_json = {'data':[],'status':False}
                        return data_json
                except socket.timeout:
                    print('tiempo de espera sobrepasado')
                    data_json = {'data':[],'status':False}
                    return data_json
    def getFestivalSchedule(self):
            try:
                if(self.readPendingDatagrams(tramas_sw12.festivo_frame)):
                    print("Horario festivo obtenido")
                    horarios_data = []
                    counter = 1
                    for i in range(16):
                        num = i
                        hora = self.rx_var_formated[counter]
                        counter +=1
                        minuto = self.rx_var_formated[counter]
                        counter +=1
                        mod = self.rx_var_formated[counter]
                        counter +=1
                        desfase = self.rx_var_formated[counter]
                        counter +=1
                        horario = {
                                    'id':'horario-{}'.format(num),
                                    'hora':hora,
                                    'minuto':minuto,
                                    'modo':mod,
                                    'desfase':desfase,
                                }
                        horarios_data.append(horario)
                    data_json = {'data':horarios_data,'status':True}
                    return data_json
                else:
                    data_json = {'data':[],'status':False}
                    return data_json
            except socket.timeout:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json

    def getGrupos(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.grupos_frame)):
                print("Obteniendo Grupos")
                grupos = []
                print(self.rx_var_formated)
                counter = 1
                for i in range(4):
                    num = i
                    valor = self.rx_var_formated[counter]
                    counter +=1
                    horario = {'id':'grupo-{}'.format(num),'value':valor}
                    grupos.append(horario)
                data_json = {'data':grupos,'status':True}
                return data_json
            else:
                data_json = {'data':[],'status':False}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json
    def getGreenConflict(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.grenn_conflict)):
                print("Obteniendo conflictos verde")
                green_conflict = []
                print(self.rx_var_formated)
                counter = 0
                bin_format = f'{self.rx_var_formated[3]:08b}'
                g1_bin = f'{self.rx_var_formated[0]:04b}'
                g2_bin = f'{self.rx_var_formated[1]:04b}'
                g3_bin = f'{self.rx_var_formated[2]:04b}'
                green_conflict = {'fila-1':g1_bin,'fila-2':g2_bin,'fila-3':g3_bin,'ch3':bin_format[2],'ch2':bin_format[3],'ch1':bin_format[7]}
                data_json = {'data':green_conflict,'status':True}
                return data_json
            else:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json
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
                data_json = {'data':params,'status':True}
                return data_json
            else:
                data_json = {'data':[],'status':True}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

    def getTimeController(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.time_frame)):
                print("Obteniendo Tiempo del Controlador")
                print(self.rx_var_formated)
                dias_semana = self.rx_var_formated[3]
                dias = ['none','domingo','lunes','martes','miercoles','jueves','viernes','sabado']
                bin_format = f'{dias_semana:08b}'
                dia = ''
                index = 0
                #aqui podriamos tener problemas
                for i in bin_format:
                    if i == '1':
                        dia = dias[index]
                    index +=1
                time_data = {
                            'seconds':self.rx_var_formated[0],
                            'minutes': self.rx_var_formated[1],
                            'hours':self.rx_var_formated[2],
                            'day':dia,
                            'date':self.rx_var_formated[4],
                            'month':self.rx_var_formated[5],
                            'year':self.rx_var_formated[6],
                            'zone':self.rx_var_formated[7],

                }
                data_json = {'data':time_data,'status':True}
                return data_json
            else:
                data_json = {'data':[],'status':False}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json



    def getSpecialDays(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.especial_frame)):
                print("Obteniendo Dias especiales del Controlador")
                print(self.rx_var_formated)
                print(len(self.rx_var_formated))
                fecha_data = []
                counter = 1
                for i in range(16):
                    mes = self.rx_var_formated[counter]
                    dia = self.rx_var_formated[counter +1]
                    tipo = self.rx_var_formated[counter +2]
                    fecha = {'id':'date-{}'.format(i+1),'mes':mes,'dia':dia,'tipo':tipo}
                    counter +=3
                    if mes != 0 and dia != 0 and tipo != 0:
                        fecha_data.append(fecha)
                fines_semana = self.rx_var_formated.pop()
                bin_format = f'{fines_semana:08b}'
                print(bin_format)
                domingo = bool(int(bin_format[7]))
                lunes = bool(int(bin_format[6]))
                martes = bool(int(bin_format[5]))
                miercoles = bool(int(bin_format[4]))
                jueves = bool(int(bin_format[3]))
                viernes = bool(int(bin_format[2]))
                sabado = bool(int(bin_format[1]))
                fines_semana_formated = {
                    'lunes':lunes,
                    'martes':martes,
                    'miercoles':miercoles,
                    'jueves':jueves,
                    'viernes':viernes,
                    'sabado':sabado,
                    'domingo':domingo
                }
                data_json = {'data':{'dias':fecha_data,'fines_semana':fines_semana_formated},'status':True}
                return data_json
            else:
                data_json = {'data':[],'status':True}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

    def getEntradas(self):
            try:
                if(self.readPendingDatagrams(tramas_sw12.entradas_frame)):
                    print("Obteniendo Entradas")
                    print(self.rx_var_formated)
                    entradas_data = []
                    counter = 1
                    for i  in range(4):
                        value = f'{self.rx_var_formated[counter]:08b}'
                        print(value)
                        check_aux = bool(int(value[2]))
                        duracion = self.rx_var_formated[counter+1]
                        paso = value[4:8]
                        int_paso = int(paso, 2) + 1
                        counter +=2
                        entrada = {'id':'entrada-{}'.format(i+1),'check':check_aux,'duracion':duracion,'paso':int_paso}
                        entradas_data.append(entrada)
                    data_json = {'data':entradas_data,'status':True}
                    return data_json
                else:
                    data_json = {'data':[],'status':True}
                    return data_json
            except socket.timeout:
                print('tiempo de espera sobrepasado')
                data_json = {'data':[],'status':False}
                return data_json
    
    def getErrores(self):
        try:
            if(self.readPendingDatagrams(tramas_sw12.errores_frame)):
                print("Obteniendo Errores")
                errores_data = []
                aux = self.rx_var_formated
                longitud_trama = len(self.rx_var_formated) -2
                cantidad_logs = int(longitud_trama/16)
                counter = 2
                for i in range(cantidad_logs):
                    segundo = aux[counter]
                    minuto = aux[counter+1]
                    hora = aux[counter+2]
                    dia = aux[counter+3]
                    fecha = aux[counter+4]
                    month = aux[counter+5]
                    year = aux[counter+6]
                    mensaje = [aux[counter+7],aux[counter+8],aux[counter+9],aux[counter+10],aux[counter+11],aux[counter+12],aux[counter+13],aux[counter+14],aux[counter+15]]
                    error = {
                            'id':'error-{}'.format(i),
                            'seconds':segundo,
                            'minute':minuto,
                            'hour':hora,
                            'day':dia,
                            'date':fecha,
                            'month':month,
                            'year':year,
                            'message':mensaje
                            }
                    errores_data.append(error)
                    counter +=16
                data_json = {'data':errores_data,'status':True}
                return data_json
            else:
                data_json = {'data':[],'status':True}
                return data_json
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

    def setFases(self,__data):
        try:
            gbtx = bytearray(29)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=7
            gbtx[10]=16
            temp_var = []
            num = 11;
            temp_num = 16
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail

            # n = 0
            # for i in list(gbtx):
            #     print(" {} trama -> {}".format(i,n))
            #     n+=1
            # return True
            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(10)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json
    
    
    def setGrupos(self,__data):
        try:
            gbtx = bytearray(18)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=6
            gbtx[10]=5
            gbtx[11]=4
            temp_var = []
            num = 12;
            temp_num = 4
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail

            # n = 0
            # for i in list(gbtx):
            #     print(" {} trama -> {}".format(i,n))
            #     n+=1
            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(10)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

    def setGreenConflict(self,__data):
        try:
            gbtx = bytearray(20)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=17
            gbtx[10]=4
            temp_var = []
            num = 11;
            temp_num = 4
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail

            # n = 0
            # for i in list(gbtx):
            #     print(" {} trama -> {}".format(i,n))
            #     n+=1
            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(20)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json
    def setPlanes(self,__data):
        try:
            gbtx = bytearray(38)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=8
            gbtx[10]=25
            temp_var = []
            num = 11;
            temp_num = 25
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail

            # n = 0
            # for i in list(gbtx):
            #     print(" {} trama -> {}".format(i,n))
            #     n+=1
            # return True
            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(20)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json


    def setOtrosParametros(self,__data):
        try:
            gbtx = bytearray(23)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=8
            gbtx[10]=10
            gbtx[11]=16
            temp_var = []
            num = 12;
            temp_num = 9
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail

            # n = 0
            # for i in list(gbtx):
            #     print(" {} trama -> {}".format(i,n))
            #     n+=1
            # return True
            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(20)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

    def setHorarios(self,__data):
        try:
            gbtx = bytearray(78)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=9
            gbtx[10]=65
            temp_var = []
            num = 11;
            temp_num = 65
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail

            # n = 0
            # for i in list(gbtx):
            #     print(" {} trama -> {}".format(i,n))
            #     n+=1
            # return True
            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(20)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json


    def setDiasEspeciales(self,__data):
        try:
            gbtx = bytearray(63)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=9
            gbtx[10]=50
            temp_var = []
            num = 11;
            temp_num = 50
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail

            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(20)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

    def setEntradas(self,__data):
        try:
            gbtx = bytearray(22)
            gbtx[0]=192
            gbtx[1]=16
            gbtx[2]=32
            gbtx[3]=16
            gbtx[4]=3
            gbtx[5]=1
            gbtx[6]=1
            gbtx[7]=0
            gbtx[8]=129
            gbtx[9]=16
            gbtx[10]=9
            temp_var = []
            num = 11
            temp_num = 9
            for x in __data:
                temp_var.append(int(x))
            for i in range(temp_num):
                if temp_var[i] == 0xC0:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDC
                    num +=1
                elif temp_var[i] == 0xDB:
                    gbtx[num] = 0xDB
                    num +=1
                    gbtx[num] = 0xDD
                    num +=1
                else:
                    gbtx[num] = temp_var[i]
                    num +=1
            CheckSumCalc = 0
            for i in range(1,num):
                CheckSumCalc += gbtx[i]
            CheckSumCalc = (CheckSumCalc % 256)
     

            if CheckSumCalc == 0xC0:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDC
                num +=1
            elif CheckSumCalc == 0xDB:
                gbtx[num]= 0xDB
                num +=1
                gbtx[num]= 0xDD
                num +=1
            else:
                gbtx[num]= CheckSumCalc
                num +=1;
            gbtx[num]= 192 #frame tail
            #n = 0
            # for i in list(gbtx):
            #     print(" {} trama -> {}".format(i,n))
            #     n+=1
            # return True
            __tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            __tcpSocket.settimeout(20)
            __tcpSocket.connect((self.ip_target,self.__port))
            __tcpSocket.sendall(gbtx)
            reply = __tcpSocket.recv(1024)
            __tcpSocket.close()
            data= list(reply)
            if data[8]==132:
                return True
            else:
                return False
        except socket.timeout:
            print('tiempo de espera sobrepasado')
            data_json = {'data':[],'status':False}
            return data_json

















