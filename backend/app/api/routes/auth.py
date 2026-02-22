from fastapi import APIRouter, Depends, HTTPException, status

router = APIRouter()

@router.post("/signup", deprecated=True)
def signup_deprecated():
    raise HTTPException(
        status_code=status.HTTP_410_GONE,
        detail="Deprecated. Use Supabase OAuth login.",
    )


@router.post("/signin", deprecated=True)
def signin_deprecated():
    raise HTTPException(
        status_code=status.HTTP_410_GONE,
        detail="Deprecated. Use Supabase OAuth login.",
    )
