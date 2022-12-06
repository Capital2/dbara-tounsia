% This is the main rule that suggests a recipe based on the available ingredients

suggest_recipe :-
	% read ingredients from user
	read_ingredients,(
	findall(Recipe, recipe(Recipe), Recipes),
	write('Based on the available ingredients, you can make the following recipes: '),
	write(Recipes)).

read_ingredients :-
    % input example "flour sugar" .
    write('Enter the ingredients you have available: '),
    read(String),
    % input broken down
    split_string(String, " ", "", Ingredients),
    assert_ingredients(Ingredients).

% assert ingredients finished needs validation with empty list
assert_ingredients([]).
% breaking down ingredients
assert_ingredients([Ingredient|Ingredients]) :-
    % converting ingredients from strings to atoms
    atom_string(Out, Ingredient),
    % adding the ingredient to the knowledge base
    assertz(ingredient(Out)),
    assert_ingredients(Ingredients).

% This database defines the ingredients and recipes available

recipe(cake) :-
  ingredient(flour),
  ingredient(sugar),
  ingredient(butter),
  ingredient(eggs),
  ingredient(vanilla).

recipe(cookies) :-
  ingredient(flour),
  ingredient(sugar),
  ingredient(butter).

recipe(pancakes) :-
  ingredient(flour),
  ingredient(sugar),
  ingredient(eggs).
