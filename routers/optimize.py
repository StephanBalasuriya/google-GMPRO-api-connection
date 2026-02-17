from fastapi import APIRouter, HTTPException
from schemas.request_schema import OptimizeRequest
from mappers.mapper_in import map_to_gmpro
from mappers.mapper_out import map_from_gmpro
from services.gmpro_client import call_gmpro

router = APIRouter()

@router.post("/request")
def optimize_routes(request: OptimizeRequest):
    try:
        gmpro_body = map_to_gmpro(request)
        gmpro_response = call_gmpro(gmpro_body)
        return map_from_gmpro(gmpro_response)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
