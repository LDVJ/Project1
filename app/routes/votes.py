from fastapi import APIRouter, Depends,  HTTPException, status
from sqlalchemy.orm import Session
from ..db import  get_db
from .. import schemas, models, oauth2

router = APIRouter(
    prefix="/vote",
    tags=['Vote']
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(payload: schemas.Vote, db: Session = Depends(get_db), current_user : models.Users = Depends(oauth2.get_user_with_token)):
    check_post = db.get(models.Posts, payload.post_id)
    if check_post:
        vote_query = db.query(models.Votes).filter(models.Votes.post_id == payload.post_id, models.Votes.user_id == current_user.id)
        check_vote =  vote_query.first()
        if (payload.vote_dir == 1):
            if check_vote:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Vote is already given")
            new_vote = models.Votes(post_id = payload.post_id, user_id = current_user.id)
            db.add(new_vote)
            db.commit()
            return {"message":"Vote given successfully"}
        else:
            if not check_vote:
                raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="No Vote Found")
            db.delete(check_vote)
            db.commit()
            return {"message":"Vote Removed"}
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Post Not found")
    