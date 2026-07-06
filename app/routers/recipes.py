from fastapi import APIRouter, HTTPException
from app.schemas.recipe import Recipe ,CreateRecipe

router = APIRouter(
    prefix = "/recipes",
    tags = ["Recipes"]
)
recipes : list[dict] = []
next_id: int = 1

@router.get("/" , response_model=list[Recipe])
def list_all():
    return recipes

@router.get("/{recipe_id}" , response_model = Recipe)
def list_recipe(recipe_id:int):
    for recipe in recipes:
        if recipe["id"] == recipe_id:
            # recipes.append(recipe)
            return recipe
    raise HTTPException(status_code=404, detail="Recipe not found")

@router.post("/" ,  response_model = Recipe , status_code=201)
def creat_recipe(recipe : CreateRecipe):
    global next_id
    new_recipe = {"id": next_id, **recipe.model_dump()}
    recipes.append(new_recipe)
    next_id += 1
    return new_recipe
