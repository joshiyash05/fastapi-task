def individual_data(data):
    return {
        "id":str(data["_id"]),
        "Customer_id": data["Customer Id"],
        "Customer_Name":data["Customer Name"],
        "Days_overdue":str(data["Days Overdue"]),
        "Amount_outstanding":str(data["Amount Outstanding"]),
        "Recovery":str(data["Recovery"]),
    }

def list_data(datas):
    return [individual_data(x) for x in datas]