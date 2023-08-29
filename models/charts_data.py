from pydantic import BaseModel
from datetime import datetime

class CsvData(BaseModel):
    Date: datetime
    Chart_Type: str
    Customer_Id: int
    Customer_Name: str
    Days_Overdue: float
    Amount_Outstanding: int
    Recovery: float