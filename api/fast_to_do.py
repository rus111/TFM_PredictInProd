from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def index(): 
    return {'greeting': 'Hello World'}

@app.get("/predict")
def predict(pickup_datetime,
            pickup_longitude,
            pickup_latitude,
            dropoff_longitude,
            dropoff_latitude,
            passenger_count
            ):
    dict = {"pickup_datetime": pickup_datetime,
            "pickup_longitude": pickup_longitude,
            "pickup_latitude": pickup_latitude,
            "dropoff_longitude": dropoff_longitude,
            "dropoff_latitude": dropoff_latitude,
            "passenger_count": passenger_count}

    return dict
    

if __name__ == '__main__': 
    print('done!')