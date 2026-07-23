from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Welcome to ResumeRoast API 🚀"
    }


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "ResumeRoast API is running smoothly!"
    }