from pydantic import BaseModel

class CreateRecipe(BaseModel):
    title : str
    cuisine : str
    prep_time_minutes : str
    servings : str

class Recipe(BaseModel):
    id : int
    title : str
    cuisine : str
    prep_time_minutes : str
    servings : str
