from fastapi import FastAPI, Path , Body
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated 
from pydantic import BaseModel , Field


class item_request(BaseModel):
    sample:str      | None = Field(default='مرحبا انا', max_length=100 , description='sample to start predicting based on it')
    max_tokens:int  | None = Field(default = 10 , gt=0 , lt= 50 , description='Max tokens to predict' )
    temp:float      | None = Field(default=1.0 , lt= 10.0 , gt = 0.0 , description="model temprature") 
    top_k:int       | None = Field(default=50 , gt=0 , lt=100, description="sample with multinomial probability with number K of probabilities")


from trained_models.models import Nagib_Mahfouz, Nagib_Mahfouz_All_In
def get_model(writer):
    if writer == 'nagib_mahfouz':
        return Nagib_Mahfouz()
    elif writer == 'nagib_mahfouz_all_in':
        return Nagib_Mahfouz_All_In()
    
    
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]  # allow all headers
)

@app.post("/test")
async def testing():
    return {"message": "Testing endpoint"}

@app.post('/generate_text/{writer}')
async def generate_text(
    writer: Annotated[str , Path()] ,
    body_data: Annotated[item_request , Body()] 
):
    model = get_model(writer.lower().strip())
    output = None
    output = model(**dict(body_data))
    return {'writer': writer , 'output': output}
    
