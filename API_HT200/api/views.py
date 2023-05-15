from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scripts import web_sockets
import json

'''
funciones de lectura del controlador

'''

controlador = web_sockets.MySocket('192.168.1.122')
class homeView(APIView):
    ''' Vista de Inicio'''
    def get(self, request, *args, **kwargs):
        result = {"message": "Hello, world!"}
        print(result)
        return Response(result,status=status.HTTP_200_OK)
    
class readTimeH200(APIView):
    ''' Lectura del Controlador HT200 '''
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getTime()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
    

class readFasesHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getFases()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        
class readSecuenciasHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getSecuencia()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readSplitHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getSplit()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readPatternHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getPattern()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readAccionHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getAccion()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readPlanesHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getPlanes()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readScneduleHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getScnedule()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readDeviceInfoHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getDeviceInfo()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        

class readBasicInfoHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getBasicInfo()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readUnitHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getUnit()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)
        
class readChannelHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getChannel()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)


class readCoordHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getCoord()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)

class readOverlapHT200(APIView):
    def get(self, request, *args, **kwargs):
        try:
            result = controlador.getOverlap()
            return Response(result,status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            print("algo ocurrio mal")
            result = {"error": "problema en el controlador"}
            controlador.disconnect()
            return Response(result,status=status.HTTP_408_REQUEST_TIMEOUT)










