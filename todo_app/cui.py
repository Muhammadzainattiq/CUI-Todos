import requests

BASE_URL = "http://127.0.0.1:8000"
GET_URL = BASE_URL + "/read/"
ADD_URL = BASE_URL + "/add/"
DELETE_URL = BASE_URL + "/delete/" # id to be added
UPDATE_URL = BASE_URL + "/update/" # id to be added



def add_todo(title:str, description:str)->dict:
    data = {"title": title, "description": description}
    response = requests.post(ADD_URL, json=data)
    if response.status_code == 200:
        return {"message": "Todo Successfully added to your todo list"}
    else:
        return {"message": "Failed to add todo to your todo list"}


def read_todos()->dict:
    response = requests.get(GET_URL)
    if response.status_code == 200:
        todos = response.json()
        return todos
    else:
        return {"message": "Failed to fetch todos"}
    


def delete_todo(id:int)->dict:
    delete_url = DELETE_URL + str(id)
    response = requests.delete(delete_url)
    if response.status_code == 200:
        return {"message":"Todo deleted successfully"}
    else:
        return {"message":"Failed to delete todo"}
    

def update_todo(id:int, title:str, description:str)->dict:
    final_url = UPDATE_URL + str(id)
    data = {"title": title, "description": description}
    response = requests.put(final_url, json=data)
    if response.status_code == 200:
        {"message": "Todo updated successfully"}
    else:
        {"message": "Failed to update todo"}


# tools = [
#         {
#     "name": "add_todo",
#     "description": "Add a todo item to the todo list",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "title": {
#                 "type": "string",
#                 "description": "Title of the todo item"
#             },
#             "description": {
#                 "type": "string",
#                 "description": "Description of the todo item"
#             }
#         },
#         "required": ["title", "description"]
#     }
# },


# {
#     "name": "read_todos",
#     "description": "Read todos from the todo list",
#     "parameters": {
#         "type": "object",
#         "properties": {},
#         "required": []
#     }
# },


# {
#     "name": "delete_todo",
#     "description": "Delete a todo item from the todo list",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "id": {
#                 "type": "integer",
#                 "description": "ID of the todo item to delete"
#             }
#         },
#         "required": ["id"]
#     }
# },


# {
#     "name": "update_todo",
#     "description": "Update a todo item in the todo list",
#     "parameters": {
#         "type": "object",
#         "properties": {
#             "id": {
#                 "type": "integer",
#                 "description": "ID of the todo item to update"
#             },
#             "title": {
#                 "type": "string",
#                 "description": "New title for the todo item"
#             },
#             "description": {
#                 "type": "string",
#                 "description": "New description for the todo item"
#             }
#         },
#         "required": ["id", "title", "description"]
#     }
# }

#     ]