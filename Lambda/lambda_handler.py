# -*- coding: utf-8 -*-
import json

def lambda_handler(event, context):
    """
    Função de exemplo que é acionada pelo AWS Lambda.
    """
    
    data = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "Aluno": "Kauan",
            "Nota": "6.0"
            "Horas Estudadas": "4.0"
        })
    }
    # TEste
    return data