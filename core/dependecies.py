from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2AuthorizationCodeBearer
from backend.users.auth import verify_token
from backend.database.schema import TokenData 

oatuh2_scheme = OAuth2AuthorizationCodeBearer(tokenurl='token')

def get_current_user(token: str = oatuh2_scheme):
    payload = verify_token
    username: str = payload.get('sub')
    if username is None:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="please try again later"
        )
        return TokenData(username=username)
        
        
        