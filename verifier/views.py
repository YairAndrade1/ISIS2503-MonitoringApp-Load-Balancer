from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import logging
from monitoring.utils import verificar_firma

logger = logging.getLogger(__name__)

@csrf_exempt
def verificar_hash_externo(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if not all(key in data for key in ['name', 'history', 'signature']):
                return JsonResponse({"status": "error", "message": "Missing required fields"}, status=400)
            
            contenido = f"{data['name']}|{data['history']}"
            firma = data['signature']
            
            if verificar_firma(contenido, firma):
                logger.info(f"Verification successful for patient: {data['name']}")
                return JsonResponse({"status": "ok", "message": "Verification successful"})
            else:
                logger.warning(f"Verification failed for patient: {data['name']}")
                return JsonResponse({"status": "alert", "message": "Verification failed"}, status=400)
        except json.JSONDecodeError:
            logger.error("Invalid JSON data received")
            return JsonResponse({"status": "error", "message": "Invalid JSON data"}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error during verification: {str(e)}")
            return JsonResponse({"status": "error", "message": "Internal server error"}, status=500)
    return JsonResponse({"status": "error", "message": "Method not allowed"}, status=405)
