from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts import web_sockets_ht200,web_sockets_sw12

import json

'''
funciones de lectura del controlador ht200
'''

controlador_ht200 = web_sockets_ht200.MySocketHT200()
controlador_sw12 = web_sockets_sw12.MySocketSW12()
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
                  "fases sw12":"/getFasesSW12"
                  }
        print(result)
        return Response(result,status=status.HTTP_200_OK)
    
class readTimeH200(APIView):
    ''' Lectura del Controlador HT200 '''
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getTime(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
    

class readFasesHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getFases(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        
class readSecuenciasHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getSecuencia(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readSplitHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getSplit(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readPatternHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getPattern(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readAccionHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getAccion(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readPlanesHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getPlanes(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readScneduleHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getScnedule(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readDeviceInfoHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getDeviceInfo(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        

class readBasicInfoHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getBasicInfo(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readUnitHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getUnit(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        
class readChannelHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getChannel(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readCoordHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getCoord(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readOverlapHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getOverlap(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        
class readRegistroErroresHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getErroresControlador(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readWorkStateHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.getWorkState(ip)
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
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
            ip=request.GET.get('ip')
            result = controlador_ht200.setUnit(json_data['trama'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class setFasesHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setFases(json_data['trama'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class setSecuenciasHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setSecuencias(json_data['trama'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 
    
class setSplitHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setSplit(json_data['trama'],ip)
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
            ip=request.GET.get('ip')
            result = controlador_ht200.setPattern(json_data['trama'],ip)
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
            ip=request.GET.get('ip')
            result = controlador_ht200.setAction(json_data['trama'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 
        
class setPlanHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setPlan(json_data['trama'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class setHorariosHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setHorarios(json_data['trama'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class setChannelHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setChannel(json_data['trama'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class setIpTarget(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setIpTarget(json_data['ip'],ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class setTimeHT200(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setTime(ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class setBasicPlan(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_ht200.setBasicPlan(json_data,ip)
            if result:
                print('envio correcto')
                return Response(result,status=status.HTTP_200_OK)
            else:
                print('envio incorrecto')
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 
'''
funciones de lectura del controlador sw12
'''

class getFasesSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getFases(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getOrdinaryScheduleSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getOrdinarySchedule(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getWeekendScheduleSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getWeekendSchedule(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)




class getFestivalScheduleSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getFestivalSchedule(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getGruposSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getGrupos(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)
        


class getGreenConflictSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getGreenConflict(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
            
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getOperativeParamsSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getOperativeParams(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getPlan1SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan1(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)



class getPlan2SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan2(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getPlan3SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan3(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)

class getPlan4SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan4(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)
        

class getPlan5SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan5(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getPlan6SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan6(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)



class getPlan7SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan7(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getPlan8SW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getPlan8(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)
        

class getTimeControllerSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getTimeController(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getSpecialDaysSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getSpecialDays(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)

class getEntradasSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getEntradas(ip)
            if result['status']:
                return Response(result['data'],status=status.HTTP_200_OK)
            else:
                return Response({"error": "problema en el controlador"},status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            return Response(result,status=status.HTTP_503_SERVICE_UNAVAILABLE)


class getErroresSW12(APIView):
    def get(self, request, *args, **kwargs):
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.getErrores(ip)
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
    Funciones de Escritura del controlador SW12
'''


class postFasesSW12(APIView):
    def post(self, request):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setFases(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 
        
class postGruposSW12(APIView):
    def post(self, request):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setGrupos(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class postGreenConflictSW12(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setGreenConflict(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class postPlanesSW12(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setPlanes(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class postOtrosParametrosSW12(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setOtrosParametros(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 



class postHorariosSW12(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setHorarios(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class postDiasEspecialesSW12(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setDiasEspeciales(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 


class postEntradasSW12(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        json_data = json.loads(request.body)
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setEntradas(json_data['trama'],ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 

class postTimeSW12(APIView):
    def post(self, request, *args, **kwargs):
        if len(request.body) == 0 :
            raise Exception('Datos de entrada invalidos: se requiere pasar la ip')
        try:
            ip=request.GET.get('ip')
            result = controlador_sw12.setTime(ip)
            if result:
                return Response(result,status=status.HTTP_200_OK)
            else:
                return Response(result,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            return Response({"mal":"data"},status=status.HTTP_408_REQUEST_TIMEOUT) 