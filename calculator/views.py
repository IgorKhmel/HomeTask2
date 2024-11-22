from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 300,
        'сыр, г': 100,
    },
}

def recipe(request,dish:str):
    try:
        context = {}
        servings = int(request.GET.get('servings', 1))
        recep = DATA.get(dish)
        print(recep)
        final_dish = {}
        for dishs, count in recep.items():
            final_dish[dishs] = count * servings
            print(final_dish)
        context.setdefault('recipe', final_dish)
        return render(request,'calculator/index.html', context)
    except:
        context = {}
        return render(request, 'calculator/index.html', context)