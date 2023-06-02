from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts import web_sockets,web_sockets_sw12

import json

'''
funciones de lectura del controlador ht200

'''

controlador_ht200 = web_sockets.MySocket('192.168.2.122')
controlador_sw12 = web_sockets_sw12.MySocketSW12('192.168.2.97')
class homeView(APIView):
    ''' Vista de Inicio'''
    def get(self, request, *args, **kwargs):
        result = {"para obtener tiempos": "/getTimeHT200",
                  "para obtener fases": "/getFasesHT200",
                  "para obtener secuencias": "/getSecuenciaHT200",
                  "para obtener spllit": "/getSplitHT200",
                  "para obtener patrones": "/getPatternHT200",
                  "para obtener acciones": "/getAccionHT200",
                  "para obtener planes": "/getPlanesHT200",
                  "para obtener horarios": "/getScneduleHT200",
                  "para obtener info1": "/getDeviceInfoHT200",
                  "para obtener info2": "/getBasicInfoHT200",
                  "para obtener unidades": "/getUnitHT200",
                  "para obtener canales": "/getChannelHT200",
                  "para obtener cordenadas": "/getCoordlHT200",
                  "para obtener superposicion": "/getOverlapHT200",
                  "fases sw12":"getFasesSW12"
                  }
        print(result)
        return Response(result,status=status.HTTP_200_OK)
    
class readTimeH200(APIView):
    ''' Lectura del Controlador HT200 '''
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getTime()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
    

class readFasesHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getFases()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        
class readSecuenciasHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getSecuencia()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readSplitHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getSplit()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readPatternHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getPattern()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readAccionHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getAccion()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readPlanesHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getPlanes()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readScneduleHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getScnedule()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readDeviceInfoHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getDeviceInfo()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        

class readBasicInfoHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getBasicInfo()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readUnitHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getUnit()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        
class readChannelHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getChannel()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readCoordHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getCoord()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readOverlapHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador_ht200.getOverlap()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador_ht200.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


'''
funciones de escritura del controlador ht200
'''

class setUnitHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        print(json_data)
        try:
            result = controlador_ht200.setUnit(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 



class setFasesHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setFases(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class setSecuenciasHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setSecuencias(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 
    
class setSplitHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setSplit(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class setPatternHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setPattern(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class setActionHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setAction(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 
        
class setPlanHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setPlan(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class setHorariosHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setHorarios(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class setChannelHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setChannel(json_data['trama'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class setIpTarget(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            result = controlador_ht200.setIpTarget(json_data['ip'])
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            controlador_ht200.disconnect()
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 



class getFasesSW12(APIView):
    ''' Lectura del Controlador HT200 '''
    def get(self, request, *args, **kwargs):
        try:
           
            result = controlador_sw12.getFases()
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)

'''
funciones de lectura del controlador sw12
'''



