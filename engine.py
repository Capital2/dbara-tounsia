from experta import *

class RecipeSystem(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.ingredients = None
        self.recipe = None

    @DefFacts()
    def _initial_action(self):
        print("Welcome to the recipe expert system!")
        yield Fact(action="get_ingredients")


    # the user inputs the ingredients he has
    @Rule(Fact(action='get_ingredients'))
    def input_ingredients(self):
        self.declare(Fact(ingredients=self.ingredients))
        self.declare(Fact(action="suggest_recipe"))
        self.run()



    # the system suggests a recipe based on the ingredients given
    @Rule(Fact(action='suggest_recipe'), Fact(ingredients=MATCH.ing))
    def suggest_recipe(self, ing):
        print("Suggesting a recipe based on the ingredients you have...")
        for i in ing:
            self.declare(Fact(i))
        self.declare(Fact(action="end"))
        self.run()
        

    @Rule(Fact(action='suggest_recipe'), Fact("oeuf"), Fact("tomate"), Fact("piment"), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()))
    def ojja_recipe(self):
        self.declare(Fact(recipe="ojja"))


    @Rule(Fact(action='suggest_recipe'), Fact("viande"), Fact("tomate"), Fact("poivron"), Fact("oignon"), Fact("patata"), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()))
    def couscous_recipe(self):
        self.declare(Fact(recipe="Couscous"))


    @Rule(Fact(action='suggest_recipe'), Fact("viande"), Fact("poivron"), Fact("oeuf"), Fact("patata"), Fact("oignon"), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()))
    def tajine_recipe(self):
        self.declare(Fact(recipe="Tajine"))

    @Rule(Fact(action='suggest_recipe'), Fact("viande"), Fact("tomate"), Fact("poivron"), Fact("citrouille"), Fact("oignon"), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()))
    def marka_citrouille(self):
        self.declare(Fact(recipe="Mar9et 9ar3a"))    

    @Rule(Fact(action='suggest_recipe'), Fact("viande"), Fact("tomate"), Fact("poivron"), Fact("patata"), Fact("oignon"), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()))
    def marka_patata(self):
        self.declare(Fact(recipe="Mar9et patata"))

    @Rule(Fact(action='suggest_recipe'), Fact("viande"), Fact("poivron"), Fact("patata"), Fact("oignon"), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()))
    def marka_patata_zaara(self):
        self.declare(Fact(recipe="Mar9et patata zaara"))


    @Rule(Fact(action='suggest_recipe'), Fact("thon"), Fact("poivron"), Fact("tomate"), Fact("fromage"), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()), Fact(W()))
    def pizza_thon(self):
        self.declare(Fact(recipe="Pizza Thon"))
    

    @Rule(Fact(action='end'), Fact(recipe=MATCH.recipe))
    def display_recipe(self, recipe):
        print("The suggested recipe is: " + recipe)
        self.recipe = "The suggested recipe is: " + recipe

if __name__ == '__main__':
    expert = RecipeSystem()
    expert.reset()
    expert.run()
