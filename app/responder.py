from app.responses import responses


def generate_response(category):
    return responses.get(category, responses["General"])