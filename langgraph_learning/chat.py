from typing_extensions import TypedDict, Annotated
class State(TypedDict):
    message:Annotated[list,add_message]
    
    