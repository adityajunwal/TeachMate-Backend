from fastapi import APIRouter, HTTPException
from routes.AutoGrader.AutoGrade import get_grades
from routes.AutoGrader.Download import download_pdf

agRouter = APIRouter(
    prefix="/autograder",
    tags=["AutoGrader"]
)

@agRouter.get("/")
def grades(doc_url: str):
    document = download_pdf(doc_url)

    if document:
        try:
            grades = get_grades(file_path=document)
            return grades 
        except:
            raise HTTPException(status_code=500, detail="Inernal Server Error! Sorry for the inconvenience. Please Try again!")
    raise HTTPException(status_code=400,detail="Invalid File Link!")
    
